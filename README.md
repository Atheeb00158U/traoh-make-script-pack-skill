# make-script-pack (TRAOH)

A Claude skill that turns a client-approved UGC script doc into TRAOH **script packs**: one branded PDF per script, with everything an international creator needs to shoot without back-and-forth.

Each pack has a cover with the project overview, key filming notes, framing & angles with "before you shoot", an optional B-roll checklist (only when approved), and the script in one continuous box with a filming note under every line.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill: what to ask, how to write the content, the design spec, and a self-contained setup block that writes the builder and assets. |
| `sample-script-pack.pdf` | The approved reference output. Packs built with this skill should look exactly like it. |
| `build_panels.py` | The PDF builder (pack.json to US Letter PDF). Same code as embedded in `SKILL.md`. |
| `logo.svg`, `film.svg`, `camera.svg` | TRAOH! logo (watermark and cover) and the faint film-strip and camera silhouettes. |

## Install

Add `SKILL.md` to Claude as a skill. Everything it needs is inside that one file; the setup block fetches the fonts (Bricolage Grotesque + DM Sans) from npm.

## Build a pack by hand

Needs Python 3, Node with `playwright`, and the fonts in `fonts/` (see the setup block in `SKILL.md`).

```bash
python3 build_panels.py pack.json "out/Jane Doe - Script Pack 1 - Eskimo.pdf" --assets . --png-preview out/preview
```

Questions: collabs@traoh.com
