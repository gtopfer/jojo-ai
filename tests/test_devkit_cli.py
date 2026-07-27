#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testes da CLI DevKit-AI (subprocess + diretório temporário)."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVKIT = ROOT / "devkit"


def run_devkit(cwd: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(DEVKIT), *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=check,
    )


def strip_ansi(s: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


class DevkitCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="devkit_test_"))
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))
        # init from kit root
        r = subprocess.run(
            [sys.executable, str(DEVKIT), "init", str(self.tmp)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        # local copy of CLI
        self.cli = self.tmp / "devkit"
        self.assertTrue(self.cli.is_file())

    def _run(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(self.cli), *args],
            cwd=str(self.tmp),
            capture_output=True,
            text=True,
            check=check,
        )

    def test_help_lists_new_commands(self) -> None:
        r = self._run("help")
        out = strip_ansi(r.stdout)
        for cmd in ("doctor", "log", "activate", "hotfix", "sync", "reject", "propose"):
            self.assertIn(cmd, out)

    def test_doctor_ok_after_init(self) -> None:
        r = self._run("doctor")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("APROVADO", strip_ansi(r.stdout))

    def test_propose_flags_and_approve_chain_includes_ux(self) -> None:
        r = self._run(
            "propose",
            "--title",
            "Lista",
            "--persona",
            "user",
            "--want",
            "ver itens",
            "--so-that",
            "trabalhar",
            "--req",
            "paginar",
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(any(self.tmp.joinpath(".ai/specs").glob("001_*.md")))

        # draft -> spec_approved (ux)
        r = self._run("approve")
        self.assertIn("spec_approved", strip_ansi(r.stdout))
        self.assertIn("`ux`", strip_ansi(r.stdout))

        # -> ux_approved (architect)
        r = self._run("approve")
        self.assertIn("ux_approved", strip_ansi(r.stdout))
        self.assertIn("architect", strip_ansi(r.stdout))

        # -> tech_approved
        r = self._run("approve")
        self.assertIn("tech_approved", strip_ansi(r.stdout))

    def test_reject_from_ux_approved(self) -> None:
        self._run(
            "propose",
            "--title",
            "X",
            "--persona",
            "p",
            "--want",
            "w",
            "--so-that",
            "s",
        )
        self._run("approve")  # spec_approved
        self._run("approve")  # ux_approved
        r = self._run("reject")
        out = strip_ansi(r.stdout)
        self.assertIn("spec_approved", out)
        self.assertIn("`ux`", out)

    def test_activate_reorders_queue(self) -> None:
        self._run("propose", "--title", "A", "--persona", "p", "--want", "w", "--so-that", "s")
        self._run("propose", "--title", "B", "--persona", "p", "--want", "w", "--so-that", "s")
        # Without activate, first non-done after 000 is SPEC-001
        r = self._run("activate", "SPEC-002")
        self.assertEqual(r.returncode, 0, r.stderr)
        r = self._run("approve")
        self.assertIn("SPEC-002", strip_ansi(r.stdout))

    def test_hotfix_starts_at_tech_approved(self) -> None:
        r = self._run("hotfix", "--title", "corrige 500", "--reason", "prod down")
        self.assertEqual(r.returncode, 0, r.stderr)
        state = (self.tmp / ".ai/state.md").read_text(encoding="utf-8")
        self.assertIn("tech_approved", state)
        self.assertIn("qa_tdd", state)
        self.assertIn("HOTFIX", state)

    def test_sync_migrate_lifecycle(self) -> None:
        # craft legacy row: spec_approved + architect
        state_path = self.tmp / ".ai/state.md"
        text = state_path.read_text(encoding="utf-8")
        legacy = (
            "| SPEC-009 | Legacy | `.ai/specs/009_legacy.md` | "
            "`spec_approved` | `architect` | 2026-01-01 |"
        )
        text = text.replace(
            "| SPEC-000 |",
            legacy + "\n| SPEC-000 |",
            1,
        )
        state_path.write_text(text, encoding="utf-8")
        (self.tmp / ".ai/specs/009_legacy.md").write_text("# Legacy\n", encoding="utf-8")
        r = self._run("sync", "--migrate-lifecycle")
        self.assertEqual(r.returncode, 0, r.stderr)
        state = state_path.read_text(encoding="utf-8")
        self.assertRegex(state, r"SPEC-009.*`spec_approved`\s*\|\s*`ux`")

    def test_state_transitions_constant_order(self) -> None:
        # Import transitions by exec portion of file is heavy; assert via approve count from draft
        self._run("propose", "--title", "Full", "--persona", "p", "--want", "w", "--so-that", "s")
        statuses = []
        for _ in range(7):
            r = self._run("approve")
            m = re.search(r"`(\w+)` ➔ `(\w+)`", strip_ansi(r.stdout))
            self.assertIsNotNone(m, r.stdout)
            statuses.append((m.group(1), m.group(2)))
        self.assertEqual(
            statuses,
            [
                ("draft", "spec_approved"),
                ("spec_approved", "ux_approved"),
                ("ux_approved", "tech_approved"),
                ("tech_approved", "test_red"),
                ("test_red", "code_review"),
                ("code_review", "tested"),
                ("tested", "done"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
