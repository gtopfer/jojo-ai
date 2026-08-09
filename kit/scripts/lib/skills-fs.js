/**
 * Discover Agent Skills layout: kit/docs/skills/<id>/SKILL.md
 */

const fs = require("fs");
const path = require("path");

/**
 * @param {string} skillsDir
 * @returns {{ id: string, skillPath: string, relFromRepo: string }[]}
 */
function listSkills(skillsDir) {
  if (!fs.existsSync(skillsDir)) return [];
  const out = [];
  for (const entry of fs.readdirSync(skillsDir, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name.startsWith(".")) continue;
    const skillPath = path.join(skillsDir, entry.name, "SKILL.md");
    if (!fs.existsSync(skillPath)) continue;
    out.push({
      id: entry.name,
      skillPath,
      relFromRepo: path
        .join("kit", "docs", "skills", entry.name, "SKILL.md")
        .replace(/\\/g, "/"),
    });
  }
  return out.sort((a, b) => a.id.localeCompare(b.id));
}

/** agentskills.io name: lowercase a-z0-9 and hyphens */
function isValidSkillName(name) {
  if (typeof name !== "string" || !name || name.length > 64) return false;
  return /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name);
}

module.exports = { listSkills, isValidSkillName };
