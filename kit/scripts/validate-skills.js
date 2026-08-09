#!/usr/bin/env node
/**
 * Validates kit/docs/skills/<id>/SKILL.md
 */

const fs = require("fs");
const path = require("path");
const { parseFrontmatter } = require("./lib/frontmatter");
const { listSkills, isValidSkillName } = require("./lib/skills-fs");

const KIT_ROOT = path.join(__dirname, "..");
const ROOT = KIT_ROOT;
const SKILLS_DIR = path.join(KIT_ROOT, "docs", "skills");

const REQUIRED_META = ["name", "type", "category", "description"];
const RECOMMENDED_META = ["usedFor", "appliesTo", "requiredKnowledge"];
const ALLOWED_TYPES = [
  "development",
  "documentation",
  "design",
  "knowledge",
  "refinement",
  "architecture",
  "process",
];
const ALLOWED_CATEGORIES = [
  "quality",
  "design",
  "organization",
  "documentation",
  "knowledge",
  "infra",
  "process",
];

function hasSection(body, titles) {
  const lower = body.toLowerCase();
  return titles.some((t) => lower.includes(t.toLowerCase()));
}

function validateFile(fullPath, expectedId) {
  const rel = path.relative(ROOT, fullPath);
  const content = fs.readFileSync(fullPath, "utf8");
  const { data, body, hasFrontmatter } = parseFrontmatter(content);
  const errors = [];
  const warnings = [];

  if (!hasFrontmatter) {
    errors.push("missing YAML frontmatter");
    return { rel, errors, warnings };
  }
  for (const key of REQUIRED_META) {
    if (data[key] === undefined || data[key] === null || data[key] === "") {
      errors.push(`missing required frontmatter: ${key}`);
    }
  }
  const name = data.name != null ? String(data.name) : "";
  if (name && !isValidSkillName(name)) {
    errors.push(`name "${name}" must be lowercase a-z0-9 and hyphens`);
  }
  if (expectedId && name && name !== expectedId) {
    errors.push(`name "${name}" must equal directory id "${expectedId}"`);
  }
  if (data.description) {
    const d = String(data.description);
    if (d.length > 1024) errors.push("description must be ≤ 1024 characters");
    if (d.length < 40) warnings.push("description short — include what + when");
  }
  if (data.type && !ALLOWED_TYPES.includes(data.type)) {
    warnings.push(`type "${data.type}" not in standard set`);
  }
  if (data.category && !ALLOWED_CATEGORIES.includes(data.category)) {
    warnings.push(`category "${data.category}" not in standard set`);
  }
  for (const key of RECOMMENDED_META) {
    if (data[key] === undefined) warnings.push(`recommended missing: ${key}`);
  }
  if (!hasSection(body, ["## quando usar", "## when to use"])) {
    errors.push('missing "## Quando usar"');
  }
  if (!hasSection(body, ["## quando não usar", "## when not to use", "## do not use"])) {
    errors.push('missing "## Quando NÃO usar"');
  }
  const lines = body.split(/\r?\n/).length;
  if (lines > 500) {
    warnings.push(`body ${lines} lines (>500) — prefer references/ (L3)`);
  }
  if (!hasSection(body, ["exemplo", "checklist", "anti-padr", "anti-pattern"])) {
    warnings.push("consider examples, checklist, or anti-patterns");
  }
  return { rel, errors, warnings };
}

function main() {
  const arg = process.argv[2];
  const files = arg
    ? [{ skillPath: path.resolve(arg), id: path.basename(path.dirname(path.resolve(arg))) }]
    : listSkills(SKILLS_DIR);

  let failed = 0;
  let warnCount = 0;
  for (const item of files) {
    const file = item.skillPath;
    if (!fs.existsSync(file)) {
      console.error(`FAIL ${file}: not found`);
      failed++;
      continue;
    }
    const { rel, errors, warnings } = validateFile(file, item.id);
    if (errors.length) {
      failed++;
      console.error(`FAIL ${rel}`);
      errors.forEach((e) => console.error(`  ✗ ${e}`));
    } else {
      console.log(`OK   ${rel}`);
    }
    warnings.forEach((w) => {
      warnCount++;
      console.warn(`  ⚠ ${w}`);
    });
  }
  console.log(
    `\nValidated ${files.length} skill(s): ${files.length - failed} ok, ${failed} failed, ${warnCount} warning(s)`
  );
  process.exit(failed ? 1 : 0);
}

main();
