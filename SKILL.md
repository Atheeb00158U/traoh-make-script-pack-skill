---
name: make-script-pack
description: Turn a TRAOH UGC script doc (docx/text with one or more scripts and hooks) into branded TRAOH script pack PDFs for international creators, one pack per script.
---

# make-script-pack (TRAOH)

Turns a client-approved UGC script document (usually a .docx with one or more scripts and hook variations) into TRAOH **script packs**: one branded PDF per script that gives an international creator everything they need to shoot in one go, with no back-and-forth across time zones.

One script = one pack. A doc with 4 scripts produces 4 PDFs.

## Before you build: ask, don't guess

Use AskUserQuestion (one round, all questions together) for anything below that the doc or the user hasn't already given you:

1. **Creator name.** Never invent it. If it isn't in the doc or the message, ask. (If the user says it's a test run, use "Jane Doe".)
2. **B-roll checklist page.** Ask explicitly whether this pack needs a B-roll checklist page (unboxing, before/after, product close-ups). Do NOT add one unless the user approves. If approved, add it via `extra_pages` (one row per shot: label = shot name, value = what to film and for how long) and make the Product Shots row point to it.
3. **Brand website / product link** for the Additional Resource section, if it isn't in the doc. You may look it up on the web, but confirm the URL with the user if you're not certain.
4. **Deliverable length** only if the doc implies something other than the default ("1 Raw UGC Video (Up to 60 seconds)").
5. **Who drafts the copy:** ChatGPT through their browser, or Claude. See "Writing the copy" below.

Brand and product usually come from the script itself. The product name in the script is often a model name of a brand (e.g. "Gordon" is a towel rail by Eskimo), so check before filling Brand vs Product.

## Pack structure (every pack, in this order)

| Page | Content | Static or dynamic |
|---|---|---|
| 1. Cover + Project overview | Big centred TRAOH! logo with "SCRIPT PACK" under it, then Creator / Brand / Product boxes, then Project overview: Deliverable, Format, Tone, Objective | Creator, Brand, Product, Tone, Objective are dynamic. Deliverable + Format are standard unless the brief says otherwise. Never repeat Creator/Brand/Product in the overview. |
| 2. Key filming notes | Location, Props, Lighting, Framing, Voice, Editing, Product shots | Location, Props, Framing, Product shots are dynamic (depend on product + script). Lighting, Voice, Editing are standard (Lighting may be lightly adapted). |
| (2b. B-roll checklist) | Only if the user approved it (`extra_pages` in pack.json) | Dynamic |
| 3. Framing & angles + Before you shoot | Intro line, Scene / Angle and framing / Why rows, Angle tips, Before you shoot | Intro + tips are standard. Rows are dynamic and must match this pack's script scenes 1:1, in order, with the same names. Before you shoot is standard plus 1-2 product-specific bullets. |
| 4+. Script | One continuous box holding every scene (lines + filming notes), then Get to know {Brand} and End of script pack + contact | Scenes are dynamic. The script starts on the Framing page if there's room. The resource line uses the brand/product URL. End block is static. |

Every page carries the small TRAOH! logo as a watermark, bottom centre. There is no running header and no creator/product text repeated on every page. Page 1 has a very faint film-strip silhouette bottom right and the last page a very faint camera silhouette.

## Writing the content

**Creator lines are client-approved copy. Keep them word-for-word.** Only fix obvious typos/formatting (stray quotes, "Hook 2 - -", double spaces). Never rewrite, shorten, or "improve" a line. Keep the offer exactly as written (e.g. "up to 37% off").

**No em dashes anywhere in the pack**, including creator lines (TRAOH's rule). Swap an em dash for a comma or full stop without changing the words. The builder also converts any that slip through (`—` becomes `, `, `–` becomes `-`).

Split each script into numbered scenes (Scene 1, 2, 3… with no gaps in numbering). Typical shapes:
- Hook (Intro): all hook variants from the doc as Hook 1, Hook 2, Hook 3… each with its own Visual Direction. If the hooks are seasonal variants of the same line (e.g. Black Friday vs Holiday Season), say so in the scene note so the creator knows which edit each one is for.
- Then whatever the script naturally contains: Problem, Product Intro / Solution (The Reveal), Benefits / Product Demo, Experience, Personal Verdict, Offer & CTA. Name scenes after what the lines actually do.
- If a scene has two or more benefit lines, consider "Record these lines using two different camera angles to create a clean visual cut in the edit." with Angle 1 / Angle 2 visual directions.
- The CTA scene includes the offer line and the "link below" line.

**Visual Directions** are TRAOH's value-add. Write one for every hook and every line group. Make them concrete and shootable by one person with a phone: camera height and position, what's in frame, what the creator does with their hands/the product, and when. Mention when the product must NOT be visible (problem scenes). For bathroom/shower products, put the creator in a robe or towel-wrapped and keep it tasteful.

**Tone** (one line) and **Objective** (one or two sentences: what the video must make the viewer believe + the action) come from the script's angle.

**Props**: a short bullet list of what the creator must have on set, including script-specific items (e.g. "skincare bottle (for Hook 3)").

**Product Shots**: describe 3–4 short extra clips (5 seconds each) of the product, unless a B-roll page was approved (then point to it).

## Writing the copy: ChatGPT + SlopMonster + Fluent Prose

This covers every piece of text TRAOH writes for the pack: Tone, Objective, Location, Props, Framing, Product shots, scene names and notes, Visual directions, the framing rows and the product-specific "Before you shoot" bullets. It never touches the creator's lines, which stay exactly as the client wrote them.

**1. Pick who drafts.** Check which browser tools this session has:
- The Cowork built-in browser (tools named `Claude_Browser`): ask the user to press **Cmd+Shift+B** (Ctrl+Shift+B on Windows) to open the browser pane in the Claude desktop app and sign in to chatgpt.com there.
- The Claude in Chrome extension (tools named `claude-in-chrome`): ask the user to sign in to chatgpt.com in that Chrome.
- Ask this together with the other questions above, and say once that the client's script will be sent to their ChatGPT account. The user signs in themselves; never type a password. Wait until they confirm they're signed in.
- If neither browser exists, or the user can't or doesn't want to sign in, skip ChatGPT and let Claude write the draft. Don't ask again.

**2. Draft.** With ChatGPT: open chatgpt.com in a new tab, start a new chat, paste the prompt below with the script and product details, wait for the full answer, then read it with the page-text tool. If ChatGPT fails twice (not signed in, error, limit reached), fall back to Claude. Without ChatGPT, Claude writes the same draft itself.

```text
You're writing the production notes for a TRAOH UGC script pack. A creator will film one vertical video on their phone, alone, from these notes. Brand: {brand}. Product: {product}. Script (client-approved, do not change a word of it):
{script}

Return JSON only, with these keys: tone (one line), objective (one or two sentences), location, props (list), framing, product_shots, scenes (list of {name, note, visuals: one direction per line or hook}), framing_rows (list of {scene, angle, purpose}, one per scene), prep_bullets (one or two product-specific prep tips).

Rules: write plain, specific directions a creator can shoot (camera height and position, what's in frame, what their hands do, and when). No em dashes. No hype words (seamless, elevate, unlock, game-changing and the like). Don't invent product claims, numbers or results. Don't repeat or rewrite the script lines.
```

**3. De-slop, every time.** Load the `slopmonster` and `fluent-prose` skills with the Skill tool. If they aren't installed, download the copies packaged with this skill and read them before editing:
`mkdir -p ~/script-pack && curl -fsSL https://raw.githubusercontent.com/Atheeb00158U/traoh-make-script-pack-skill/main/slopmonster/SKILL.md -o ~/script-pack/slopmonster.md` (and the same for `fluent-prose/SKILL.md`).
- Put all the TRAOH-written copy in one markdown file, one field per paragraph or bullet, and run SlopMonster's checker (`deslop.py`) on it. Leave the creator's lines out of the file.
- Edit with SlopMonster steps 2 and 4. Apply Fluent Prose to the longer prose fields (Objective, Framing, Visual directions) so they read as connected sentences; short labels and prop lists stay as short lists.
- The second pass (SlopMonster step 3) must come from a different model family from the drafter. If ChatGPT drafted, Claude's edit is that second pass. If Claude drafted and ChatGPT is available, send SlopMonster's cleanse prompt plus the copy to ChatGPT and check its changes before accepting them.
- Re-run the checker until it scores 5/5, or note any finding you kept on purpose. Then fill pack.json and build.

### Standard copy (use as-is unless the user asks to change it)

- Deliverable: `1 Raw UGC Video (Up to 60 seconds)`
- Format: `9:16 Vertical Video, clear audio, no filters or transitions`
- Lighting: `Bright, natural light. No yellow lights or harsh shadows. Use extra lights if needed, but make sure the product is clearly visible.`
- Voice: `Talk like you are speaking to a friend. Be natural, avoid “salesy” tone.`
- Editing: `Deliver **raw footage** only. Do not add filters, text, transitions, or background music.`
- Framing & Angles intro: `To make the video more engaging, please vary your framing and angle slightly for each section. This keeps the content visually dynamic while staying authentic.`
- Angle Tips: `Record one-two takes per section (one static, one handheld) for editor flexibility.` / `Each take should run 5–10 seconds.` / `Keep lighting consistent and avoid background distractions (cars, crowds, harsh shadows).`
- Before you shoot: `Record each hook as its own clip. One or two clean takes per hook is plenty.` / `Stable audio - avoid fans, AC noise, and cars.` / (1-2 product-specific prep bullets, e.g. clean product, no smudges or water spots) / `No filters, no music, no transitions. Raw only.`
  - Never write "Deliver each hook separately (3-4 takes)". Asking for many takes of one line makes creators anxious.
- Resource (auto): `Get to know {Brand}` / `If you’d like more inspiration for your delivery, visit {URL} before you shoot.`
- End (auto): `End of script pack` + `Questions? collabs@traoh.com`

## Design spec ("Soft panels", approved by TRAOH)

Calm, light and minimal. Don't add colour blocks, heavy rules or big display type.

- US Letter (816×1056 px), Creator Cream background `#FDF9F3` (same as the old template), ink `#151515`, warm panels `#F3ECE1` with 14px rounded corners.
- Page 1: the logo is the hero (big, centred), with a grey rule and "SCRIPT PACK" in bold grey caps under it. No other title font next to the logo.
- Fonts: **Bricolage Grotesque** for section titles and scene names, **DM Sans** for everything else (TRAOH's brand fonts).
- Field labels (Creator, Location, Angle and framing...) are small but **bold and in full ink**, so they hold their own against the values.
- Red `#FF3131` (Ohhhh Red) is only a small accent: the logo, hook label pills, bullet dots and "End of script pack".
- Boxes sit in a two-column grid that packs tightly; long values span the full width. Short pages are spread out so they don't end in a big empty gap.
- Script: one continuous box. Inside it, "Scene N" + scene name in Bricolage, **every line the creator says in italics**, the filming note in smaller grey text under it, and thin dividers between scenes. Hook labels are small red pills.
- Packs normally land at 5 pages. If a page still overflows after tightening, the builder logs `OVERFLOW`.
- Reference: `sample-script-pack.pdf` in the skill's GitHub repo (github.com/Atheeb00158U/traoh-make-script-pack-skill) is the approved output. Packs built with the builder below should look the same.

Brand palette for reference (TRAOH Playbook): Ohhhh Red `#FF3131`, Scroll Black `#0F0F0F`, Algorithm Blue `#3386FF`, Creator Cream `#FDF9F3`, Viral Grey `#A1A1A1`, Impact Green `#00D79A`.

The builder below implements all of this. Don't hand-build the PDF.

## How to build

1. Read the script doc (`pandoc -t plain file.docx`) and split it into scripts.
2. Ask the questions above, including who drafts the copy (ChatGPT or Claude).
3. Write the copy with the ChatGPT + SlopMonster + Fluent Prose steps above.
4. Run the setup block once per session (writes the builder, logo and silhouettes to `~/script-pack/` and fetches the fonts from npm).
5. For each script, write `packN.json` (schema below), then run:
   `python3 ~/script-pack/build_panels.py packN.json "out/{Creator} - Script Pack {N} - {Brand}.pdf" --assets ~/script-pack --png-preview out/previewN`
6. Look at every preview PNG yourself (Read tool). Check: nothing overlaps the bottom watermark, framing rows match the script scenes, creator lines are verbatim (apart from em dashes), no empty fields, scene numbers have no gaps, no big empty areas. If the builder logs `OVERFLOW`, shorten the dynamic text on that page (never the creator lines).
7. Deliver the PDFs with SendUserFile (PDF only, no PNGs unless asked). If a folder is connected, also save them there.

### pack.json schema

Text fields accept `**bold**` and `*italic*`. A field given as a list renders as bullets.

```json
{
 "overview": {"creator": "", "brand": "", "product": "", "deliverable": "", "format": "", "tone": "", "objective": ""},
 "filming_notes": {"location": "", "props": ["", ""], "lighting": "", "framing": "", "voice": "", "editing": "", "product_shots": ""},
 "framing_angles": {"intro": "", "rows": [{"scene": "Hook (Intro)", "angle": "", "purpose": ""}], "tips": ["", "", ""]},
 "extra_pages": [{"title": "B-roll checklist", "intro": "", "rows": [{"label": "Unboxing", "value": ""}]}],
 "script": [
  {"title": "Scene 1: Hook (Intro)", "note": "Perform all hooks in separate takes:",
   "items": [{"label": "Hook 1", "line": "exact hook text", "visual": "direction"}]},
  {"title": "Scene 2: Problem", "note": "(optional)",
   "items": [{"line": ["paragraph 1", "paragraph 2"], "visual": "direction"}]}
 ],
 "before_you_shoot": ["", ""],
 "resource": {"brand": "", "url": ""},
 "contact": "collabs@traoh.com"
}
```

- `extra_pages` is optional. Leave it out unless the user approved a B-roll page.
- Script titles must be `Scene N: Name`. Items with a `label` get a red hook pill. Don't put quote marks in the lines.
- Framing `rows` must mirror the scene names, in order.

### Setup block (run once per session)

Needs Python 3, Node with `playwright` (pre-installed in the sandbox), and npm access for the fonts.

```bash
mkdir -p ~/script-pack/fonts && cd ~/script-pack
for p in @fontsource-variable/bricolage-grotesque @fontsource-variable/dm-sans; do npm pack $p --silent >/dev/null; done
for f in fontsource-variable-*.tgz; do tar xzf $f && cp package/files/*-latin-standard-*.woff2 fonts/ && rm -rf package $f; done
ls fonts   # expect bricolage-grotesque-latin-standard-normal + dm-sans-latin-standard-normal/italic
```

```bash
cat > ~/script-pack/logo.svg <<'SVG_EOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 142"><path fill="#2D2E2D" d="M44 86L44 38L26 37L8 37L8 25L8 12L59 12L110 12L110 25L110 37L92 37L74 38L74 86L74 135L59 135L44 135L44 86ZM122 74L122 12L156 13C187 13 189 13 196 15C207 18 213 21 218 26C224 33 228 42 227 51C225 66 216 74 200 78C193 80 192 81 199 83C211 86 217 91 222 103C225 111 231 132 231 134C231 135 226 135 215 135L198 135L196 125C192 106 190 101 184 97C181 95 179 94 166 94L152 94L152 114L152 134L137 135L122 135L122 74ZM237 134C237 134 246 108 256 77C267 46 276 19 276 16L278 12L299 12C321 12 321 12 322 15C323 16 324 19 325 21C325 23 334 48 343 76C360 124 363 134 363 135C363 135 356 135 347 135L331 134L329 130C329 128 327 123 326 119L324 112L300 112L276 112L272 124L269 134L253 135C244 135 237 135 237 134ZM317 91C318 91 316 87 315 81C311 70 309 63 305 48C301 34 299 33 297 41C296 44 292 57 289 69C285 81 282 91 282 92C282 92 317 92 317 91ZM183 70C193 67 198 58 195 48C192 38 186 35 165 35L152 35L152 54L152 72L166 72C173 71 181 71 183 70Z"/><path fill="#FF2B2B" d="M416 137C402 136 390 130 380 121C373 114 369 107 365 96C363 89 363 87 363 72C363 57 363 56 365 48C370 32 380 21 393 14C403 9 411 7 426 7C446 7 459 11 472 24C484 36 489 51 489 72C489 109 470 133 435 137C431 138 426 138 425 138C424 138 420 137 416 137ZM495 135C494 135 494 106 494 71L495 8L511 8L528 8L528 33L528 57L554 57L580 57L580 33L580 8L596 8L612 8L613 72L613 136L597 136L580 136L580 111L580 86L554 86L528 86L528 111L528 136L511 136C502 136 495 136 495 135ZM630 135C629 135 629 128 629 120L629 105L649 105L668 105L668 120L668 136L649 136C639 136 630 136 630 135ZM443 102C449 99 452 93 453 81C454 74 454 70 453 63C451 45 446 40 429 39C405 38 398 46 398 72C398 91 402 100 412 103C414 105 419 105 427 105C437 105 439 104 443 102ZM632 92C631 90 628 55 627 29C626 19 626 11 626 10C627 8 629 8 648 8C659 8 669 8 670 9C670 9 671 11 671 12C671 16 666 87 665 91C665 93 665 93 648 93C636 93 632 93 632 92Z"/></svg>
SVG_EOF
cat > ~/script-pack/film.svg <<'SVG_EOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 208 177"><path fill="currentColor" d="M4 176C4 174 11 157 14 149C35 96 62 67 100 60C110 58 126 57 145 59C167 60 178 59 186 55C198 49 205 35 206 10C206 6 207 4 207 4C207 4 207 6 207 19C207 34 207 35 207 35C206 34 205 35 206 36C206 37 206 37 207 36C207 36 207 38 207 61L207 87L205 87C199 86 197 86 185 83C163 78 153 78 143 83C124 93 110 121 99 170C99 173 98 175 98 175C98 176 98 176 51 176C25 176 4 176 4 176ZM12 172C12 172 13 170 13 168C14 166 16 162 17 159C19 154 19 154 18 153C16 151 16 151 11 165C9 171 9 171 9 172C10 173 11 173 12 172ZM94 171C95 169 96 164 95 164C94 163 92 162 91 163C90 164 89 170 90 170C91 171 93 172 94 171ZM97 157C97 157 98 155 99 153C100 149 100 149 97 148C95 147 95 148 94 152C92 157 93 157 96 158C96 158 97 158 97 157ZM24 142C25 140 25 140 24 139C22 137 21 138 20 142C19 144 19 144 19 145C21 147 22 146 24 142ZM102 141C103 139 104 134 104 134C101 131 100 132 98 136C97 140 98 141 101 142C101 142 101 141 102 141ZM28 132C28 132 29 130 30 129L32 126L31 125C29 123 28 124 26 128C25 131 25 132 27 132C27 133 27 133 28 132ZM107 125C109 124 110 119 109 119C108 117 106 117 105 118C105 119 103 123 103 124C103 125 104 126 106 126C106 126 107 126 107 125ZM38 115C39 113 39 113 39 112C37 110 36 111 33 115C32 118 32 118 32 118C34 120 35 120 38 115ZM113 112C116 109 116 106 113 105C111 105 111 106 109 109C108 111 108 112 110 112C112 113 112 113 113 112ZM44 105C47 102 47 101 45 100C43 100 43 100 41 103C40 104 40 105 42 106C43 106 43 106 44 105ZM120 99C122 97 121 97 119 96C117 96 117 96 115 98C114 100 114 101 117 102C119 102 119 102 120 99ZM54 94C56 91 56 91 56 90C54 89 53 89 50 92C47 95 47 96 51 97C51 97 52 95 54 94ZM127 91C129 89 128 88 125 87C124 87 120 90 122 91C122 91 124 92 125 92C125 92 126 92 127 91ZM64 84C67 82 67 82 66 81C65 79 62 80 59 84C58 84 60 86 62 86C62 86 63 85 64 84ZM136 83C137 82 137 82 136 81C134 79 132 80 130 82C130 82 131 83 132 84C134 84 134 84 136 83ZM135 76C136 75 135 74 132 74C132 74 131 73 130 73C130 73 126 73 122 72C114 70 114 70 113 71C112 72 112 72 113 73C114 73 130 76 130 76C131 76 131 76 132 77C133 78 133 78 135 76ZM149 77C149 76 149 76 149 75C147 74 143 75 144 77C145 78 147 78 149 77ZM74 77C77 75 77 75 76 74C75 73 72 73 70 75C69 76 71 77 73 77C73 77 74 77 74 77ZM169 72C170 71 170 70 166 69C162 68 162 68 164 67C165 66 165 66 164 65C163 64 163 64 161 65C160 66 160 67 159 66C159 66 159 66 159 66C158 67 158 69 159 68C160 68 161 69 160 69C159 70 159 70 159 69C158 69 156 69 155 69C154 71 157 72 159 71C159 70 159 71 160 71C160 71 164 72 168 73C169 73 169 72 169 72ZM89 69C91 68 88 66 86 67C85 68 85 68 85 69C87 70 88 70 89 69ZM140 65C141 64 141 64 139 63C137 62 136 63 137 64C137 64 137 64 137 64C137 64 137 65 137 65C138 66 139 66 140 65ZM120 63C121 63 121 63 120 62C118 60 111 61 113 63C114 64 119 64 120 63ZM186 62C187 62 187 62 187 61C188 61 188 61 187 60C187 60 187 60 186 60C186 60 186 60 186 60C184 58 182 60 183 61C184 62 185 62 186 62C186 62 186 62 186 62ZM197 55L198 53L197 52L196 51L194 53C193 54 193 54 194 55C195 56 196 56 197 55ZM203 46C204 45 204 45 203 44C202 43 200 45 201 46C202 47 202 47 203 46Z"/></svg>
SVG_EOF
cat > ~/script-pack/camera.svg <<'SVG_EOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 159 270"><path fill="currentColor" d="M34 268C34 268 38 252 42 232C49 196 49 195 48 195C47 194 48 188 49 188C50 188 51 187 53 174C56 161 56 161 57 161C58 160 58 160 59 161C60 161 60 161 57 174C55 187 55 187 55 188C57 189 57 188 61 174C64 164 64 161 65 161C66 160 66 160 65 160C65 159 66 156 67 157C68 158 68 159 67 160C67 160 67 160 68 161C68 162 68 162 65 175C61 187 61 188 62 189C62 189 62 190 62 192C62 194 62 195 61 195C59 195 59 195 49 231C44 250 40 267 40 267C39 268 39 268 37 268C35 268 34 268 34 268ZM81 267C81 266 79 242 78 214C74 162 74 162 75 161C76 161 76 161 75 160C74 159 74 158 75 157C75 156 75 156 75 156C74 155 74 155 74 153C74 149 72 149 71 153C70 156 70 156 69 155C68 154 68 154 67 155C66 157 66 156 67 152C68 149 68 148 69 148C69 148 70 148 70 148C70 148 70 148 71 149C72 150 72 150 73 149C74 147 72 143 71 144C69 145 69 144 71 138C73 129 73 127 69 127C67 127 66 127 65 136C64 142 63 143 63 144C62 144 62 144 62 145C63 145 63 147 62 148C61 148 61 149 62 149C63 150 61 157 59 156C59 156 59 156 58 156C56 158 57 150 59 147C61 145 61 145 60 144C59 143 59 143 61 136L62 129L61 127C60 126 60 126 60 122C60 118 60 117 61 117C61 116 61 116 61 116C60 115 60 115 54 115C47 115 47 115 47 120C46 122 46 124 46 124C45 124 41 125 35 126L25 128L23 130L21 132L14 134C8 135 6 135 6 135C5 134 4 127 5 127C5 126 9 126 13 125L20 123L22 125L24 126L33 124C44 122 44 122 44 119C45 115 44 115 40 115C38 115 37 115 37 115C36 114 36 94 37 93C38 92 38 92 37 92C37 91 37 91 37 88C37 84 36 83 34 83C32 83 32 83 31 84C29 86 28 86 28 85C27 84 21 73 22 72C22 72 25 72 29 73C32 75 35 75 36 74C37 72 36 72 33 70C23 67 16 56 17 45C19 22 47 13 62 31C66 35 68 34 69 30C70 24 78 14 80 14C80 14 81 14 81 15C82 15 84 13 84 13C83 13 84 12 84 12C85 11 85 11 85 12C86 12 86 12 87 11C88 10 88 10 89 11C90 12 92 10 91 10C90 9 93 7 94 8C95 9 95 9 95 8C97 7 107 8 105 9C105 10 106 12 107 11C107 10 108 10 109 11C109 12 109 12 110 11C111 10 112 11 112 12C112 13 113 14 114 14C114 13 114 13 115 14C115 14 116 15 117 15C118 15 118 15 120 16C132 28 132 46 121 59C119 61 119 62 122 62C125 62 125 62 125 65C125 67 126 69 126 68C127 68 129 68 132 68L138 68L146 64C151 60 153 59 153 59C154 60 154 100 153 100C153 101 151 99 146 96L138 92L132 92C129 92 127 92 126 91C126 91 126 91 126 92C125 93 125 93 125 103C125 111 125 114 124 115C124 115 122 115 117 115C110 115 110 115 109 116C109 116 109 116 109 117C110 118 110 126 109 128L108 129L109 136C110 140 111 143 111 143C110 143 111 144 111 144C111 145 111 147 111 147C110 148 110 148 111 149C113 151 113 155 111 156C110 158 107 150 108 147C109 146 109 146 108 145C107 144 107 144 105 136C104 127 104 127 100 127C96 127 96 127 99 136C101 143 101 144 99 143C99 143 98 144 98 144C97 144 97 144 97 143C96 143 96 143 95 144C95 145 94 146 94 146L93 147L94 148C95 149 95 149 95 153C94 156 94 157 93 156C92 156 92 156 91 156C90 156 90 155 90 152C90 150 90 149 91 149C91 149 91 148 91 147C91 147 91 146 92 145C92 145 92 145 92 144C91 143 91 143 91 135C91 127 92 127 84 127C76 127 77 127 77 138C78 143 78 143 77 144C76 145 76 147 77 148C78 150 78 150 78 152C78 153 78 154 78 155C79 156 79 156 78 157C77 158 77 158 77 159C78 160 78 160 79 161C79 161 79 166 80 174C81 190 80 189 84 189C88 189 88 190 89 175C90 161 90 160 91 161C92 161 92 161 93 161C94 160 94 160 94 172C93 178 93 186 93 190C92 199 89 266 89 268C88 268 88 268 85 268L81 268L81 267ZM131 268C131 268 126 252 121 232C111 197 111 197 110 195C109 194 109 194 109 191C109 188 109 188 105 175C102 162 102 162 102 161C103 160 103 160 102 160C102 159 102 158 102 157C103 157 103 157 102 156C101 155 101 155 101 155C100 155 98 150 99 149C100 148 102 148 102 149C102 149 103 151 103 152C104 155 104 155 103 155C103 156 103 156 104 157C105 158 105 159 104 159C104 160 104 160 105 160C105 161 106 163 109 174C113 189 113 189 115 188C116 187 116 187 113 174C111 163 110 161 111 160C111 160 111 159 111 159C110 158 112 159 113 160C114 161 114 161 117 174C120 188 120 188 122 188C123 188 123 189 123 192C123 194 123 194 122 195C121 196 121 192 129 233C133 252 136 268 136 268C136 269 131 268 131 268ZM87 214C88 194 88 196 84 196C81 196 81 194 82 215C83 234 83 235 85 233C86 232 86 232 87 214ZM46 58C55 55 58 43 51 37C44 29 31 34 30 45C30 54 38 60 46 58ZM38 52C37 51 38 49 40 49C41 49 42 51 41 52C40 53 39 53 38 52ZM102 53C110 51 115 43 113 35C111 22 96 18 87 27C76 38 87 56 102 53ZM45 51C44 50 45 48 47 48C49 48 50 50 48 51C48 52 46 52 45 51ZM92 46C91 44 92 42 94 42C95 42 97 43 97 44C97 46 94 47 92 46ZM35 45C34 44 36 41 38 43C38 43 38 44 38 44C38 46 36 47 35 45ZM102 44C100 43 101 40 103 40C104 40 106 42 106 43C106 45 103 46 102 44ZM47 44C45 44 46 41 48 41C49 41 50 43 49 44C48 45 48 45 47 44ZM40 40C39 39 39 39 40 38C41 36 43 37 43 39C43 41 41 41 40 40ZM89 37C88 36 88 34 90 33C93 33 94 36 92 37C91 38 90 38 89 37ZM103 36C101 34 102 32 104 32C106 32 107 34 106 35C105 36 104 36 103 36ZM95 31C93 29 94 27 97 27C98 27 99 28 99 29C99 31 96 32 95 31Z"/></svg>
SVG_EOF
cat > ~/script-pack/build_panels.py <<'PY_EOF'
#!/usr/bin/env python3
"""TRAOH script pack builder, "panels" design: pack.json -> PDF.
Usage: python3 build_panels.py pack.json out.pdf [--assets DIR] [--png-preview DIR]
DIR needs logo.svg, film.svg, camera.svg and fonts/{bricolage-grotesque-latin-standard-normal,dm-sans-latin-standard-normal,dm-sans-latin-standard-italic}.woff2
"""
import json, base64, html, pathlib, argparse, subprocess, re

ap = argparse.ArgumentParser()
ap.add_argument("pack"); ap.add_argument("out")
ap.add_argument("--assets", default=str(pathlib.Path(__file__).parent))
ap.add_argument("--png-preview")
a = ap.parse_args()
A = pathlib.Path(a.assets); P = json.loads(pathlib.Path(a.pack).read_text())

def clean(s):  # house rule: no em dashes anywhere; ranges use a plain hyphen
    s = re.sub(r"\s*—\s*", ", ", str(s or "")); return s.replace("–", "-")
e = lambda s: html.escape(clean(s))
def rich(s):
    s = e(s); s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s); return re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
def val(v): return "<ul>" + "".join(f"<li>{rich(i)}</li>" for i in v) + "</ul>" if isinstance(v, list) else f"<p>{rich(v)}</p>"
def font(n): return base64.b64encode((A / "fonts" / n).read_bytes()).decode()
def svg(n): return (A / f"{n}.svg").read_text()

ov, fn, fa = P["overview"], P["filming_notes"], P["framing_angles"]
FOOT = f'<footer class="wm">{svg("logo")}</footer>'
def page(inner, cls=""): return f'<section class="page {cls}">{inner}{FOOT}</section>'
def h1(title, sub=""): return f'<div class="ph"><h1>{e(title)}</h1>{f"<p class=sub>{rich(sub)}</p>" if sub else ""}</div>'
def spec(rows, cls=""):
    return f'<dl class="spec {cls}">' + "".join(f'<div class="row{" wide" if w else ""}"><dt>{e(k)}</dt><dd>{val(v)}</dd></div>' for k, v, w in rows if v) + "</dl>"

# 1. first page: big centred logo + SCRIPT PACK, Creator / Brand / Product boxes, then the project overview
p1 = f'''<section class="page cover"><div class="cv"><div class="cvlogo">{svg("logo")}</div><div class="cvrule"></div><div class="cvsub">SCRIPT PACK</div></div>
<dl class="cmeta"><div><dt>Creator</dt><dd>{e(ov["creator"])}</dd></div><div><dt>Brand</dt><dd>{e(ov["brand"])}</dd></div><div><dt>Product</dt><dd>{e(ov["product"])}</dd></div></dl>
{h1("Project overview")}{spec([("Deliverable", ov["deliverable"], False), ("Format", ov["format"], False), ("Tone", ov["tone"], True), ("Objective", ov["objective"], True)])}
<div class="film">{svg("film")}</div></section>'''

# 2. key filming notes
L = lambda v: isinstance(v, list) or len(clean(v)) > 150
p2 = page(h1("Key filming notes") + spec([(k, fn.get(key), L(fn.get(key))) for k, key in
              [("Location", "location"), ("Props", "props"), ("Lighting", "lighting"), ("Framing", "framing"),
               ("Voice", "voice"), ("Editing", "editing"), ("Product shots", "product_shots")]], "notes"), "fill")

# 3. framing & angles + before you shoot; the script starts in the space left on this page
rows = "".join(f'<tr><th>{e(r["scene"])}</th><td>{rich(r["angle"])}</td><td>{rich(r["purpose"])}</td></tr>' for r in fa["rows"])
extra = "".join(page(h1(x["title"], x.get("intro", "")) + spec([(r["label"], r["value"], True) for r in x["rows"]])) for x in P.get("extra_pages", []))
p3 = f'''<section class="page shared">{h1("Framing & angles", fa["intro"])}
<table class="fa"><thead><tr><th>Scene</th><th>Angle and framing</th><th>Why</th></tr></thead><tbody>{rows}</tbody></table>
<div class="box tips"><h2>Angle tips</h2>{val(fa["tips"])}</div><div class="box tips"><h2>Before you shoot</h2>{val(P["before_you_shoot"])}</div><div class="content"><div class="box script"></div></div>{FOOT}</section>'''

# script: one continuous box; blocks marked in (inside the box) or out (after it)
blocks = ['<div class="blk out first">' + h1("Script", "Say the lines in italics word for word. The note under each one tells you what to film.") + '</div>']
for sc in P["script"]:
    m = re.match(r"Scene (\d+):\s*(.*)", sc["title"]); num, name = (m.group(1), m.group(2)) if m else ("", sc["title"])
    h = f'<div class="sh"><span class="sn">Scene {num}</span><h2>{e(name)}</h2>{f"<p class=note>{rich(sc.get("note"))}</p>" if sc.get("note") else ""}</div>'
    for k, it in enumerate(sc["items"]):
        lines = it["line"] if isinstance(it["line"], list) else [it["line"]]
        say = (f'<span class="lab">{e(it["label"])}</span>' if it.get("label") else "") + "".join(f'<p class="say">{e(l)}</p>' for l in lines)
        do = f'<p class="vd">{rich(it["visual"])}</p>' if it.get("visual") else ""
        blocks.append(f'<div class="blk in{" scene" if k == 0 else ""}">{h if k == 0 else ""}<div class="item">{say}{do}</div></div>')
r = P["resource"]
blocks.append(f'<div class="blk out end"><h2>Get to know {e(r["brand"])}</h2><p>If you’d like more inspiration for your delivery, visit <a href="{e(r["url"])}">{e(re.sub(r"^https?://", "", r["url"]).rstrip("/"))}</a> before you shoot.</p></div>')
c = e(P.get("contact", "collabs@traoh.com"))
blocks.append(f'<div class="blk out fin"><p class="eosp">End of script pack</p><p>Questions? <a href="mailto:{c}">{c}</a></p></div>')
src = f'<div id="src" style="display:none">{"".join(blocks)}</div>'

CSS = f"""
@font-face{{font-family:B;font-weight:200 800;src:url(data:font/woff2;base64,{font('bricolage-grotesque-latin-standard-normal.woff2')}) format('woff2')}}
@font-face{{font-family:D;font-weight:100 1000;font-style:normal;src:url(data:font/woff2;base64,{font('dm-sans-latin-standard-normal.woff2')}) format('woff2')}}
@font-face{{font-family:D;font-weight:100 1000;font-style:italic;src:url(data:font/woff2;base64,{font('dm-sans-latin-standard-italic.woff2')}) format('woff2')}}
@page{{size:816px 1056px;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#FDF9F3;--ink:#151515;--soft:#8A847B;--acc:#FF3131;--panel:#F3ECE1;--line:#E6DCCD}}
body{{-webkit-print-color-adjust:exact;font-family:D;background:var(--bg);color:var(--ink)}}
.page{{width:816px;height:1056px;position:relative;overflow:hidden;page-break-after:always;background:var(--bg);padding:58px 64px 0}}
ul{{list-style:none}} li{{position:relative;padding-left:14px}}
li::before{{content:"";position:absolute;left:0;top:.66em;width:5px;height:5px;border-radius:50%;background:var(--acc)}}
a{{color:inherit;text-decoration-thickness:1px;text-underline-offset:3px}}
.wm{{position:absolute;left:0;right:0;bottom:34px;display:flex;justify-content:center;z-index:2}} .wm svg{{width:84px;display:block}}
.ph{{margin:0 0 18px}}
.ph h1{{font-family:B;font-weight:600;font-size:30px;letter-spacing:-.02em}}
.ph .sub{{font-size:15px;line-height:1.55;margin-top:8px;max-width:600px;color:#5A554E}}
.spec{{display:grid;grid-template-columns:1fr 1fr;gap:10px;grid-auto-flow:row dense}}
.spec .row{{background:var(--panel);border-radius:14px;padding:var(--pv,16px) 20px}}
.spec .row.wide{{grid-column:span 2}}
.spec dt{{font-size:13px;font-weight:600;color:var(--ink);margin-bottom:4px}} .spec dd{{font-size:15px;line-height:1.55;color:#3A3631}}
.fa{{width:100%;border-collapse:separate;border-spacing:0 8px;font-size:14.5px;line-height:1.5;margin-top:-4px}}
.fa th,.fa td{{text-align:left;vertical-align:top;padding:var(--pv,15px) 16px;background:var(--panel)}}
.fa tbody th{{border-radius:14px 0 0 14px;font-weight:600;width:160px}} .fa tbody td:last-child{{border-radius:0 14px 14px 0}}
.fa thead th{{background:none;font-weight:600;font-size:13px;color:var(--ink);padding:0 16px}}
.box{{background:var(--panel);border-radius:14px;padding:18px 20px;margin-top:10px}}
.tips h2{{font-family:B;font-weight:600;font-size:17px;margin-bottom:8px}} .tips li{{font-size:14.5px;line-height:1.6;margin-bottom:3px}}
/* cover */
.cover{{padding-top:110px}} .cover .cv{{display:flex;flex-direction:column;align-items:center;margin-bottom:64px}}
.cvlogo svg{{width:400px;display:block}}
.cvrule{{width:396px;height:3px;background:#545454;margin-top:16px}}
.cvsub{{font-weight:700;font-size:28px;letter-spacing:.06em;color:#545454;margin-top:8px}}
.cmeta{{width:100%;display:grid;grid-template-columns:1fr 1fr 1.4fr;gap:10px;position:relative;z-index:1;margin-bottom:44px}}
.cmeta div{{background:var(--panel);border-radius:14px;padding:18px 20px}}
.cmeta dt{{font-size:13px;font-weight:600;color:var(--ink);margin-bottom:4px}} .cmeta dd{{font-size:16px;line-height:1.4;color:#3A3631}}
.cover .spec{{position:relative;z-index:1}} .film{{position:absolute;right:0;bottom:0;width:330px;color:var(--ink);opacity:.06}} .film svg{{display:block;width:100%;height:auto}}
/* script */
.content{{position:relative;z-index:1}}
.shared .content{{margin-top:34px}} .box.script{{margin-top:0;padding:6px 26px 14px}} .box.script:empty{{display:none}}
.box.script .blk.scene:not(:first-child){{border-top:1px solid var(--line);margin-top:10px}}
.sh{{padding-top:16px;margin-bottom:4px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}}
.sh .sn{{font-size:12.5px;font-weight:500;color:#615B53}} .sh h2{{font-family:B;font-weight:600;font-size:18px}}
.sh .note{{flex-basis:100%;font-size:13.5px;color:#615B53}}
.item{{padding:8px 0}}
.lab{{display:inline-block;font-size:12px;font-weight:600;color:var(--acc);background:var(--bg);border-radius:99px;padding:2px 10px;margin-bottom:5px}}
.say{{font-style:italic;font-size:16px;line-height:1.55;margin-bottom:3px}}
.vd{{font-size:13.5px;line-height:1.55;color:#615B53;margin-top:4px}}
.end{{margin-top:26px}} .end h2{{font-family:B;font-weight:600;font-size:18px;margin-bottom:6px}} .end p{{font-size:14.5px;line-height:1.6}}
.fin{{margin-top:22px}} .fin .eosp{{font-family:B;font-weight:600;font-size:18px;color:var(--acc)}} .fin p{{font-size:14px;color:#615B53}}
.cam{{position:absolute;right:56px;bottom:0;width:230px;color:var(--ink);opacity:.05;z-index:0}} .cam svg{{display:block;width:100%;height:auto}}
"""

JS = r"""document.fonts.ready.then(()=>{
const LIM=975, bottom=pg=>Math.max(...[...pg.children].filter(c=>!c.matches('.wm,.film,.cam')).map(k=>k.getBoundingClientRect().bottom))-pg.getBoundingClientRect().top;
for(const pg of document.querySelectorAll('section.page:not(.cover)')){   // tighten panels until the page clears the watermark
 let pv=16; while(bottom(pg)>LIM&&pv>7){pv--;pg.style.setProperty('--pv',pv+'px');}
 if(bottom(pg)>LIM)console.log('OVERFLOW',pg.querySelector('h1')?.textContent);}
for(const pg of document.querySelectorAll('section.fill')){  // spread a short page so it doesn't end in a big gap
 let pv=16; while(bottom(pg)<LIM-30&&pv<28){pv++;pg.style.setProperty('--pv',pv+'px');} if(bottom(pg)>LIM){pv--;pg.style.setProperty('--pv',pv+'px');}}
const items=[...document.getElementById('src').children];
let pg=document.querySelector('section.shared'),content=pg.querySelector('.content'),box=content.querySelector('.box.script'),placed=0,shared=true;
const mk=()=>{pg=document.createElement('section');pg.className='page sp';pg.innerHTML='<div class="content"><div class="box script"></div></div>'+FOOT;
 document.body.appendChild(pg);content=pg.querySelector('.content');box=pg.querySelector('.box.script');placed=0;shared=false;};
const put=it=>{ if(it.classList.contains('first'))content.insertBefore(it,box);
 else if(it.classList.contains('in')&&!content.querySelector(':scope>.blk.out:not(.first)'))box.appendChild(it); else content.appendChild(it); placed++; };
for(const it of items){ put(it);
 if(bottom(pg)>LIM && (placed>1||shared)){ it.remove(); const prevFirst=(placed===2&&content.querySelector(':scope>.blk.first'));
  mk(); if(prevFirst){content.insertBefore(prevFirst,box);placed++;} put(it); } }
document.querySelectorAll('.box.script').forEach(b=>{if(!b.children.length)b.remove()});
const cam=document.createElement('div');cam.className='cam';cam.innerHTML=CAM;pg.appendChild(cam);
document.getElementById('src').remove(); document.body.dataset.ready='1';});
"""
doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
{p1}{p2}{extra}{p3}{src}
<script>const FOOT={json.dumps(FOOT)};const CAM={json.dumps(svg("camera"))};{JS}</script></body></html>"""

out = pathlib.Path(a.out); out.parent.mkdir(parents=True, exist_ok=True); hp = out.with_suffix(".html"); hp.write_text(doc)
node = f"""const {{chromium}}=require('playwright');
(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:816,height:1056}}}});
p.on('console',m=>console.log('[page]',m.text()));
await p.goto('file://{hp.resolve()}');await p.waitForSelector('body[data-ready="1"]');
await p.pdf({{path:'{out.resolve()}',width:'816px',height:'1056px',printBackground:true,preferCSSPageSize:true}});
const prev={json.dumps(a.png_preview)};
if(prev){{const els=await p.$$('section.page');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:prev+'/p'+(i+1)+'.png'}});}}
await b.close();}})();"""
if a.png_preview: pathlib.Path(a.png_preview).mkdir(parents=True, exist_ok=True)
subprocess.run(["node", "-e", node], check=True)
print("wrote", out)
PY_EOF
```
