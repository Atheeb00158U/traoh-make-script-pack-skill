# make-script-pack (TRAOH)

A Claude skill that turns a client-approved UGC script doc into TRAOH **script packs**: one branded PDF per script, with everything an international creator needs to shoot without back-and-forth.

Each pack has a cover, project overview, key filming notes, framing & angles, an optional B-roll checklist (only when approved) and the script. In the script, every line the creator says sits in its own card with its filming direction.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill: rules for asking, writing the content, the design spec, and a self-contained setup block that writes the builder and logo. |
| `build_panels.py` | The PDF builder (pack.json → US Letter PDF, "Soft panels" design). Same code as embedded in `SKILL.md`. |
| `logo.svg` | TRAOH! logo used in the header and on the cover. |
| `example-pack.json` | A filled-in pack (Eskimo / Gordon heated towel rail, skincare angle). |

## Install

Add `SKILL.md` to Claude as a skill, or drop this folder into your skills directory.

## Build a pack by hand

Needs Python 3, Node with `playwright`, and the fonts (Bricolage Grotesque + DM Sans, fetched from npm by the setup block in `SKILL.md`).

```bash
python3 build_panels.py example-pack.json "out/Jane Doe - Script Pack 2 - Eskimo.pdf" --assets . --png-preview out/preview
```

Questions: collabs@traoh.com
