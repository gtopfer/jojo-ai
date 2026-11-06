"""Testes da CLI `jojo` (init | detect | run | sync | version).

Estratégia: caixa-preta via subprocess, rodando o script real do repositório
contra diretórios temporários. Sem dependências externas (stdlib unittest).
O teste de `sync` exige npm e é pulado quando npm não está disponível.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JOJO = REPO_ROOT / "jojo"

HAS_NPM = shutil.which("npm") is not None


def run_jojo(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(JOJO), *args],
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
        timeout=120,
    )


def read_version() -> str:
    m = re.search(
        r'^VERSION\s*=\s*["\']([^"\']+)["\']',
        JOJO.read_text(encoding="utf-8"),
        re.M,
    )
    assert m, "VERSION não encontrada no script jojo"
    return m.group(1)


FEATURES_MD = """# AGENTS.MD

## SEÇÃO 1

### Features

**Backlog:**

- [x] setup do projeto
- [ ] primeira pendente
- [ ] segunda pendente
"""

FEATURES_COM_CERCA = """# AGENTS.MD

### Features

```markdown
- [ ] feature falsa dentro de bloco de código
```

- [ ] feature real fora do bloco
"""

FEATURES_SO_TEMPLATE = """# AGENTS.MD

### Features

- [ ] [exemplo] título curto da feature
- [ ] A IA marca [x] quando concluir
- [ ] feature de verdade
"""

FEATURES_TUDO_FEITO = """# AGENTS.MD

### Features

- [x] única feature concluída
"""


class JojoCLITest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="jojo-test-"))
        self.target = self.tmp / "app"

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def init_target(self, *extra: str) -> subprocess.CompletedProcess:
        return run_jojo("init", str(self.target), "--skip-sync", *extra)

    # ── init ────────────────────────────────────────────────────────────

    def test_init_fresh_installs_managed_and_human_files(self) -> None:
        r = self.init_target()
        self.assertEqual(r.returncode, 0, r.stderr)
        for rel in (
            "jojo",
            "LICENSE",
            "agents.md",
            "system-design.md",
            "CHANGELOG.md",
            "kit",
            ".ai/jojo-install.json",
            ".ai/state.md",
        ):
            self.assertTrue((self.target / rel).exists(), f"faltou {rel}")
        meta = json.loads((self.target / ".ai/jojo-install.json").read_text())
        self.assertEqual(meta["jojo_version"], read_version())
        self.assertEqual(meta["mode"], "install")
        self.assertIn("### Features", (self.target / "agents.md").read_text())

    def test_init_update_preserves_human_files(self) -> None:
        self.assertEqual(self.init_target().returncode, 0)
        agents = self.target / "agents.md"
        changelog = self.target / "CHANGELOG.md"
        agents.write_text(agents.read_text() + "\nMARCA-HUMANA-AGENTS\n")
        changelog.write_text(changelog.read_text() + "\nMARCA-HUMANA-CHANGELOG\n")

        r = self.init_target()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("MARCA-HUMANA-AGENTS", agents.read_text())
        self.assertIn("MARCA-HUMANA-CHANGELOG", changelog.read_text())

    def test_init_force_overwrites_human_files(self) -> None:
        self.assertEqual(self.init_target().returncode, 0)
        agents = self.target / "agents.md"
        agents.write_text(agents.read_text() + "\nMARCA-HUMANA-AGENTS\n")

        r = run_jojo("init", str(self.target), "--skip-sync", "--force")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("MARCA-HUMANA-AGENTS", agents.read_text())

    # ── metadado de instalação (privacidade do campo source) ────────────

    ABSOLUTE_PATH_RE = r"^(/|[A-Za-z]:[\\/]|~)"  # posix, windows ou ~

    def test_init_writes_public_source_not_local_path(self) -> None:
        self.assertEqual(self.init_target().returncode, 0)
        meta = json.loads((self.target / ".ai/jojo-install.json").read_text())
        source = meta["source"]
        self.assertNotRegex(source, self.ABSOLUTE_PATH_RE)
        self.assertNotIn(str(REPO_ROOT), source)
        self.assertIn("jojo-ai", source)

    def test_update_replaces_legacy_local_path_in_source(self) -> None:
        self.assertEqual(self.init_target().returncode, 0)
        meta_path = self.target / ".ai/jojo-install.json"
        meta = json.loads(meta_path.read_text())
        # metadado legado (<=0.3.0): caminho absoluto da máquina no source
        meta["source"] = str(self.tmp / "projetos" / "jojo-ai")
        meta["installed_at"] = "2020-01-01T00:00:00Z"
        meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

        r = self.init_target()  # modo update
        self.assertEqual(r.returncode, 0, r.stderr)
        new_meta = json.loads(meta_path.read_text())
        self.assertNotRegex(new_meta["source"], self.ABSOLUTE_PATH_RE)
        self.assertNotIn(str(self.tmp), new_meta["source"])
        self.assertEqual(new_meta["mode"], "update")
        # compatibilidade: metadado legado continua legível e demais campos preservados
        self.assertEqual(new_meta["installed_at"], "2020-01-01T00:00:00Z")

    # ── detect ──────────────────────────────────────────────────────────

    def test_detect_empty_dir_reports_absent(self) -> None:
        r = run_jojo("detect", str(self.target))
        self.assertEqual(r.returncode, 1)
        self.assertIn("jojo installed: no", r.stdout)

    def test_detect_after_init_reports_present(self) -> None:
        self.assertEqual(self.init_target().returncode, 0)
        r = run_jojo("detect", str(self.target))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("jojo installed: yes", r.stdout)
        self.assertIn(read_version(), r.stdout)

    # ── run ─────────────────────────────────────────────────────────────

    def prepare_agents(self, content: str) -> None:
        self.target.mkdir(parents=True, exist_ok=True)
        (self.target / "agents.md").write_text(content, encoding="utf-8")

    def test_run_selects_first_pending_feature(self) -> None:
        self.prepare_agents(FEATURES_MD)
        r = run_jojo("run", str(self.target))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("PRÓXIMA FEATURE", r.stdout)
        self.assertIn("primeira pendente", r.stdout)
        state = json.loads((self.target / ".ai/jojo-run.json").read_text())
        self.assertEqual(state["next_feature"], "primeira pendente")
        self.assertEqual(state["pending"], ["primeira pendente", "segunda pendente"])
        self.assertEqual(state["done"], ["setup do projeto"])

    def test_run_ignores_fenced_code_blocks(self) -> None:
        self.prepare_agents(FEATURES_COM_CERCA)
        r = run_jojo("run", str(self.target))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("feature real fora do bloco", r.stdout)
        self.assertNotIn("feature falsa dentro de bloco de código", r.stdout)

    def test_run_ignores_template_example_lines(self) -> None:
        self.prepare_agents(FEATURES_SO_TEMPLATE)
        r = run_jojo("run", str(self.target))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("feature de verdade", r.stdout)
        state = json.loads((self.target / ".ai/jojo-run.json").read_text())
        self.assertEqual(state["next_feature"], "feature de verdade")
        self.assertEqual(state["pending"], ["feature de verdade"])

    def test_run_without_agents_md_fails(self) -> None:
        self.target.mkdir(parents=True, exist_ok=True)
        r = run_jojo("run", str(self.target))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("agents.md", r.stderr)

    def test_run_with_all_done_reports_no_pending(self) -> None:
        self.prepare_agents(FEATURES_TUDO_FEITO)
        r = run_jojo("run", str(self.target))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Nenhuma feature pendente", r.stdout)

    def test_run_json_flag_emits_json(self) -> None:
        self.prepare_agents(FEATURES_MD)
        r = run_jojo("run", str(self.target), "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        start = r.stdout.find("{")
        self.assertGreaterEqual(start, 0, r.stdout)
        payload = json.loads(r.stdout[start:])
        self.assertEqual(payload["next"], "primeira pendente")

    # ── version ─────────────────────────────────────────────────────────

    def test_version_command_and_flag(self) -> None:
        for args in (("version",), ("--version",)):
            r = run_jojo(*args)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn(f"jojo {read_version()}", r.stdout)

    # ── sync ────────────────────────────────────────────────────────────

    @unittest.skipUnless(HAS_NPM, "npm não disponível neste ambiente")
    def test_sync_runs_kit_scripts(self) -> None:
        self.assertEqual(self.init_target().returncode, 0)
        r = run_jojo("sync", str(self.target))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("sync OK", r.stdout)


if __name__ == "__main__":
    unittest.main()
