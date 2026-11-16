# Changelog

## 3.4.1 (2026-11-16): first public release

**Contents**
- 10,087 device and system parameter records in 19 classes from 1,133 published papers. Each gives the value, number and unit, status (measured, simulated or predicted), material, device, conditions, page and section. No text from the papers is included.
- Tables computed from the records by fixed rules (`references/derived/`): a device parameter atlas, a materials atlas, coverage counts and a benchmark accuracy ledger.
- SOTA ledgers for 11 platforms × 7 metrics, with measured and projected values kept apart.
- Rules for writing, figures, journal choice, reviewer concerns and responses, materials, novelty positioning and idea generation (`SKILL.md` and `references/`).
- A 13-command toolkit that needs only Python 3.8 or later and its standard library.

**Fixed before release**
- The `description` in `SKILL.md` no longer contains an unquoted ": ", so agents that read the frontmatter with a standard YAML parser can load the skill. §0 now says that paths are relative to the skill folder.
- `lit-search --author` / `--group` and the exclusion lists of `reviewer-finder` ignore accents (`Ozcan` finds `Özcan`).
- The SOTA ledger parser no longer splits a cell at an escaped pipe (`\|`).
- `reviewer-finder` lists the leading groups for a platform from `references/global_groups.md`.

**Checks**
- Frontmatter parsed by PyYAML, js-yaml and Ruby, and checked against the Agent Skills specification.
- The 11 toolkit outputs pasted in the documentation match the program.
- Toolkit output is identical under Python 3.8 and 3.13, apart from the layout of `--help`.
