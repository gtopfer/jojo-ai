#!/usr/bin/env node
/**
 * Scans kit/docs/skills/<id>/SKILL.md → kit/generated/skills-registry.json
 * Progressive disclosure: L1 registry, L2 SKILL body, L3 references/
 */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { parseFrontmatter } = require("./lib/frontmatter");
const { listSkills, isValidSkillName } = require("./lib/skills-fs");

const KIT_ROOT = path.join(__dirname, "..");
const SKILLS_DIR = path.join(KIT_ROOT, "docs", "skills");
const OUT = path.join(KIT_ROOT, "generated", "skills-registry.json");
const REQUIRED = ["name", "type", "category", "description"];

function loadSkills() {
  if (!fs.existsSync(SKILLS_DIR)) {
    console.error(`Missing skills dir: ${SKILLS_DIR}`);
    process.exit(1);
  }
  fs.mkdirSync(path.dirname(OUT), { recursive: true });

  const skills = [];
  const errors = [];

  for (const { id, skillPath, relFromRepo } of listSkills(SKILLS_DIR)) {
    const content = fs.readFileSync(skillPath, "utf8");
    const { data, hasFrontmatter } = parseFrontmatter(content);
    const hash = crypto.createHash("sha256").update(content).digest("hex").slice(0, 12);

    if (!hasFrontmatter) {
      errors.push(`${relFromRepo}: missing YAML frontmatter`);
      continue;
    }
    for (const key of REQUIRED) {
      if (data[key] === undefined || data[key] === null || data[key] === "") {
        errors.push(`${relFromRepo}: missing frontmatter field "${key}"`);
      }
    }
    const name = data.name != null ? String(data.name) : "";
    if (name && !isValidSkillName(name)) {
      errors.push(`${relFromRepo}: name "${name}" must be lowercase alphanumeric + hyphens`);
    }
    if (name && name !== id) {
      errors.push(`${relFromRepo}: name "${name}" must match directory "${id}"`);
    }

    const skillDir = path.dirname(skillPath);
    skills.push({
      id,
      name: name || id,
      type: data.type,
      category: data.category,
      description: data.description,
      usedFor: data.usedFor || [],
      appliesTo: data.appliesTo || [],
      requiredKnowledge: data.requiredKnowledge || [],
      conflicts: data.conflicts || [],
      mandatory: Boolean(data.mandatory),
      path: relFromRepo,
      layers: {
        l1: "registry",
        l2: relFromRepo,
        l3: {
          references: fs.existsSync(path.join(skillDir, "references")),
          scripts: fs.existsSync(path.join(skillDir, "scripts")),
          assets: fs.existsSync(path.join(skillDir, "assets")),
        },
      },
      hash: `sha256:${hash}`,
    });
  }
  return { skills, errors };
}

function main() {
  const { skills, errors } = loadSkills();
  if (errors.length) {
    console.error("Registry generation failed:\n" + errors.map((e) => `  - ${e}`).join("\n"));
    process.exit(1);
  }
  const registry = {
    version: "2.0",
    generated: new Date().toISOString(),
    sourceOfTruth:
      "kit/docs/skills/<id>/SKILL.md (agents only; humans use CLI + 3 root MDs)",
    progressiveDisclosure: {
      l1: "name + description in this registry",
      l2: "full SKILL.md when activated",
      l3: "references/, scripts/, assets/ on demand",
    },
    skills,
  };
  fs.writeFileSync(OUT, JSON.stringify(registry, null, 2) + "\n", "utf8");
  console.log(`Wrote kit/generated/skills-registry.json (${skills.length} skills)`);
}

main();
