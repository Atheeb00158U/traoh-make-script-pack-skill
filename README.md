# make-script-pack (TRAOH)

A Claude skill that turns a client-approved UGC script doc into TRAOH **script packs**: one branded PDF per script, with everything an international creator needs to shoot without back-and-forth.

Each pack has a cover with the project overview, key filming notes, framing & angles with "before you shoot", an optional B-roll checklist (only when approved), and the script in one continuous box with a filming note under every line.

## How the copy gets written

The client's script lines are never changed. Everything TRAOH adds (tone, objective, filming notes, visual directions) goes through this pipeline:

1. **Draft.** If the user has the Cowork browser (Cmd+Shift+B) or the Claude in Chrome extension and is signed in to ChatGPT, ChatGPT writes the first draft. Otherwise Claude writes it.
2. **De-slop.** The draft is checked and edited with **SlopMonster** (AI-pattern checker plus editing steps) and **Fluent Prose** (sentence flow), with the second pass done by a different model from the one that drafted.
3. **Build.** The final copy goes into `pack.json` and the builder renders the PDF.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill: what to ask, how to write the content, the design spec, and a self-contained setup block that writes the builder and assets. |
| `slopmonster/SKILL.md` | SlopMonster, packaged so the skill works even if it isn't installed. Based on [ItsssssJack/SlopMonster](https://github.com/ItsssssJack/SlopMonster) (MIT, see `slopmonster/LICENSE`). |
| `fluent-prose/SKILL.md` | Fluent Prose, packaged the same way. |
| `sample-script-pack.pdf` | The approved reference output. Packs built with this skill should look exactly like it. |
| `build_panels.py` | The PDF builder (pack.json to US Letter PDF). Same code as embedded in `SKILL.md`. |
| `logo.svg`, `film.svg`, `camera.svg` | TRAOH! logo (watermark and cover) and the faint film-strip and camera silhouettes. |

## Install

Add `SKILL.md` to Claude as a skill. For the best results also add `slopmonster/SKILL.md` and `fluent-prose/SKILL.md` as skills; if they're missing, the skill downloads them from this repo when it needs them. The setup block fetches the fonts (Bricolage Grotesque + DM Sans) from npm.

## Build a pack by hand

Needs Python 3, Node with `playwright`, and the fonts in `fonts/` (see the setup block in `SKILL.md`).

```bash
python3 build_panels.py pack.json "out/Jane Doe - Script Pack 1 - Eskimo.pdf" --assets . --png-preview out/preview
```

Questions: collabs@traoh.com
