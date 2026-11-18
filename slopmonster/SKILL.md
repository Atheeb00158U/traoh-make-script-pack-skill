---
name: "slopmonster"
description: "Review writing for its intended reader, check common AI writing patterns, revise, optionally get a second pass from a different model family, and check again. Trigger on /slopmonster, \"humanize this\", \"de-slop this\", \"does this sound like AI\", \"fix this copy\"."
---

# SlopMonster

Edit the supplied draft for its audience and purpose (READMEs, landing pages, blogs,
emails, ad copy, scripts). Use the checker to locate known patterns, then review the
writing in context. A score of 5/5 means no scored patterns matched; it does not
establish that the copy is clear or accurate. Source: github.com/ItsssssJack/SlopMonster (MIT).

## Step 0: Install the checker

The checker is embedded at the bottom of this file (Python 3, standard library only).
Before first use in a session, write it verbatim to `deslop.py` in the scratchpad (or
working directory) and run it from there. Do not paraphrase or "improve" the code.

## Step 1: Establish the context and run the checker

Identify the reader, the format and what the reader needs from the text. Use the
user's brief and the draft itself. Ask a focused question only when missing context
would materially change the edit.

A README should explain what the project does, how to use it and its limitations.
A sales page may need an opening that establishes a problem. An email may need to
start with the request. Choose an approach that fits the document.

```bash
python3 deslop.py draft.md
python3 deslop.py page.html
python3 deslop.py page.html --view view-site
python3 deslop.py --text "paste a draft"
python3 deslop.py --text "paste markdown" --markdown
```

The checker scores five categories: vocabulary, sentence patterns, punctuation,
three-item lists and possible unsupported proof. Each category with a match costs
one point. Below 5/5 it exits with status 1. Empty input also fails.

For Markdown, use a `.md` file path (or `--markdown`) so code blocks, inline code,
images and `~~struck~~` specimens are skipped. HTML is stripped of tags, scripts and
styles. The rules are English only.

## Step 2: Review and rewrite

Work through the draft in this order:

1. **Purpose and structure.** Answer the reader's first question early. Remove
   duplicate hooks and curiosity gaps that delay an explanation. Keep each
   paragraph focused on a useful point, with enough context to understand it.
2. **Meaning and evidence.** Check that each sentence adds information and follows
   from what came before. Explain conditions on claims. Remove empty contrasts,
   repeated metaphors and comparisons that do not help the reader. Preserve
   facts, technical behavior and the author's position.
3. **Wording and rhythm.** Review the checker findings and replace vague language
   with direct wording. Read adjacent sentences together for repetitive shapes.
   Let sentence length follow the thought. Keep useful lists and punctuation.

Do not manufacture personality by adding an opinion, a mistake, a fragment or a
fixed quota of short sentences. Do not add a number to every claim. Use only facts
supplied by the author or verified from an appropriate source.

The checker can flag valid language. Review the actual match before editing it.
Never hide ordinary prose in code formatting to raise the score. If a necessary
phrase still triggers a rule, explain the remaining finding to the user.

### Pattern catalogue (from Wikipedia's "Signs of AI writing" and related projects)

These patterns can also appear in human writing; read findings in context.

**1 · Vocabulary.** Review for vague or promotional use; keep literal and technical
meanings: delve, tapestry, testament to, underscores, seamless, robust, navigate the
landscape, in today's fast-paced world, it's important/worth noting, that being said,
at the end of the day, unlock, supercharge, elevate, game-changing, revolutionise,
harness the power of, dive deep, myriad, plethora, realm, ever-evolving, cutting-edge,
transformative, paradigm shift, synergy, holistic, embark. Also in context: leverage,
foster, crucial, pivotal, streamline, empower, showcase, curated, meticulous,
compelling, innovative, comprehensive, journey, solution, effortless, intuitive,
world-class, best-in-class, unleash, boost. Often a plain word such as "use" is enough.

**2 · Constructions.**

| Shape | Example | Fix |
|---|---|---|
| not just X, but Y | It's not just a course, it's a journey | Cut the first clause, keep the claim |
| more than just | More than just another app | Same |
| whether you're X or Y | Whether you're a beginner or a pro… | Name the one reader you mean |
| that's where X comes in | That's where Acme comes in | State what X does |
| say goodbye to | Say goodbye to guesswork | Name what replaces it |
| imagine a… | Imagine a world where… | Show it instead |
| hedged benefit | helps you to, can help you | State the benefit at the certainty the evidence supports |
| stacked hedging | may potentially, could possibly | Remove redundant hedges, keep real uncertainty |
| self-answering question | The result? Faster shipping. | A sentence |

Also review adjacent sentences that repeat a metaphor, manufacture a contrast between
audiences, or introduce a second hook before explaining the first. Remove process
commentary and repeated summaries.

**3 · Punctuation cadence.** Two or more em dashes in one sentence (220-char windows);
four stacked hyphenated compounds in one sentence; semicolon density that scales with
length. Punctuation can be appropriate even when it triggers; judge readability.

**4 · Rhythm.** Three-item lists like "faster, smarter, and better". Check each item
contributes information; keep a useful list at its natural length.

**5 · Invented proof.** Numbers near nouns like users, customers, teams, companies,
clients, projects. The checker cannot judge truth. Verify dates and specs too.

### Editing principles

1. **Give the reader what they need.** README: explain function before optional
   integrations. Email: state the reason early. Sales page: may establish the
   customer problem first (Krug's *Don't Make Me Think*; Priestley/Hormozi
   problem-first pitch order, for sales copy only).
2. **Make the opening lead into an explanation.** A hook establishes a reason to
   read; then answer it. Read the first few paragraphs together; cut openings that
   could introduce almost any product. Avoid unsupported comparisons with others.
3. **Check the relationship between sentences.** Each sentence adds information,
   explains a consequence or gives a needed example. Mirrored structures and
   repeated metaphors create rhythm without developing the point. Use a contrast
   only when the distinction matters.
4. **Keep claims within the evidence.** Don't add a number or testimonial merely to
   feel concrete. If evidence is missing, mark the gap. Keep limitations attached
   to the claims they qualify.
5. **Preserve a voice that suits the document.** Keep the author's formality. Lists
   can have three items when there are three useful items. An em dash can be fine.
   No quota of fragments or contractions; no invented opinions or deliberate errors.

## Step 3: Request a second editing pass (optional)

Use a different model family from the one that wrote the draft, with the cleanse
prompt below, and inspect its suggestions before accepting them.

- If a rival CLI is installed and authenticated (e.g. `codex` for a Claude-written
  draft), run it with the prompt plus the draft, read-only, with a timeout.
- Otherwise give the user the prompt plus draft to paste into the other family's
  chat (ChatGPT, Gemini). Do not run the same model family on its own draft and
  call it a second pass.
- If no second model is reachable, say the pass was not completed and continue.

The reply puts the copy first, then a line `<<<SLOPMONSTER-NOTES>>>`, then notes.
If the marker is missing, notes may be mixed into the copy; inspect it.

<cleanse_prompt>
Edit the draft below for its intended reader and purpose. Infer the format and
audience from the supplied context. Preserve the author's position and level of
formality. A README needs a clear explanation and usable instructions. A sales
page or script may need a different opening.

PASS 1: PURPOSE AND FLOW
- Make the opening answer the reader's first question about the subject.
- Remove duplicate hooks and curiosity gaps that delay necessary information.
- Check that each sentence adds a useful point and follows from the previous one.
- Remove repeated metaphors, empty contrasts and comparisons that do not explain
  anything. Describe the relevant behavior directly.
- Explain jargon where the reader needs it. Keep conditions attached to claims.
- Keep a closing summary only if it serves this document's reader.

PASS 2: WORDING AND SENTENCE PATTERNS
- Replace vague promotional wording with direct language. Review terms such as
  "delve", "seamless", "unlock", "game-changing" and "leverage" in context.
- Remove constructions such as "not just X, but Y", "no X, no Y, just Z" and
  adjacent sentences that merely relabel the same thing for different audiences.
  Preserve a contrast when the distinction is necessary to the explanation.
- Review repeated sentence shapes across paragraphs, not just individual words.
- Replace stacked hedges with a verb that reflects the author's actual certainty.
- Review self-answering questions and decorative lists. Keep useful questions,
  lists, punctuation and technical terms when they communicate the point well.

PASS 3: CONTEXT AND ACCURACY
- Read the result as a complete document. Does it suit the reader and the format?
- Let sentence length follow the meaning. Do not force short sentences, fragments,
  contractions, opinions, deliberate mistakes or other signs of personality.
- Use concrete details already in the source where they help. Do not add a number
  to each claim or turn every document into sales copy.
- Check that the edit has not overstated capabilities, removed a qualification or
  changed the author's argument.

ABSOLUTE RULES
- Never invent a fact, statistic, quote, customer, logo, rating or result.
- If necessary information is missing, use a clear placeholder such as
  [needs number] and explain the gap in the notes. Do not guess.
- Preserve factual meaning and technical behavior. Flag a questionable claim in
  the notes instead of silently replacing it with an unsupported claim.
- Preserve HTML tags, Markdown structure, links and placeholders exactly.
- Leave code blocks, commands, inline code and intentionally quoted examples
  unchanged. They may document the very patterns being discussed.
- Keep the author's register. Do not add an opinion the author did not express.

OUTPUT
Return the rewritten copy in full, and nothing before it. Then a line containing
exactly
<<<SLOPMONSTER-NOTES>>>
and nothing else, then at most five bullets describing the substantive edits or
unresolved concerns. No preamble or restatement of these instructions.

The marker is parsed by a script. Emit it exactly once, alone on its line, with no
bullet, quotes or backticks around it, even when you changed nothing. Everything
above it is returned as copy; everything below it is shown to the author as notes.

TEXT TO EDIT:
[draft goes here]
</cleanse_prompt>

## Step 4: Compare the edit and check again

Compare the result with the source. Check facts and commands for changes, confirm
links and placeholders survived, and read the opening in context. Review notes for
deletions that removed necessary information. Re-run `python3 deslop.py` on the
result. Resolve findings while preserving meaning; report justified exceptions. The
final editorial review is required even at 5/5.

## Factual claims

Never invent evidence: customer counts, testimonials, ratings, results. If the draft
needs missing information, flag it with a placeholder such as `[needs number]`. Do
not publish an unresolved placeholder as a verified claim. Use `--allow-proof` only
after checking the evidence; it keeps the warning but removes the score penalty.

## Output

Return the rewritten copy or save the edited artifact as requested. Then give up to
five short notes on substantive changes and the check results (before/after score).
State whether the second model pass completed. Keep unresolved claims and remaining
checker findings visible. Do not claim the edit proves human authorship.

## Embedded checker: deslop.py

```python
#!/usr/bin/env python3
"""deslop.py: score copy for common AI writing patterns.
  python3 deslop.py file.md|file.html [--view ID] [--allow-proof]
  python3 deslop.py --text "copy" [--markdown]"""
import html as _html
import re
import sys
VOCAB = ['delve', 'leverage', 'seamless', 'elevate', 'robust', 'unlock', 'unleash', 'empower', 'streamline', 'cutting-edge', 'state-of-the-art', 'game-changer', 'game-changing', 'revolutionize', 'revolutionise', 'transformative', 'transformation', 'innovate', 'holistic', 'synergy', 'synergies', 'paradigm', 'bespoke', 'meticulous', 'tapestry', 'testament', 'beacon', 'unparalleled', 'supercharge', 'turbocharge', 'effortless', 'next-level', 'pivotal', 'foster', 'showcase', 'compelling', 'intuitive', 'world-class', 'best-in-class']
VOCAB_EXACT = ['crafted', 'curated', 'harnessing', 'harness the power', 'journey', 'realm', 'landscape', 'navigate the', 'in the world of', "in today's", 'ever-evolving', 'fast-paced', 'look no further', 'dive in', "let's dive", 'deep dive', 'embark', 'unlock the power', 'buckle up', 'the secret sauce', 'level up']

def _root_pattern(word):
    root = re.sub('(ed|ing|ly|e)$', '', word)
    if len(root) < 4:
        return f'(?<!\\w){re.escape(word)}(?!\\w)'
    return f'(?<!\\w){re.escape(root)}(?:e|es|ed|ing|ion|ions|ional|ive|al|ally|s|ly|ness)?(?!\\w)'
_NEG_JUST = "(?:\\bnot|n['’]t)\\s+(?:just|only|merely|simply)\\b"
_XY_TAIL = '[^!?]{0,80}?[,.]\\s*(?:it|this|that|they|we|you|he|she|i)\\b'
PHRASES = [(_NEG_JUST + '[^.!?]{0,80}\\bbut\\b', "the 'not just X, but Y' construction"), (_NEG_JUST + _XY_TAIL, "the 'not just X, it's Y' construction"), ("\\bwhether you(?:'?re| are)\\b[^.!?]{0,40}\\bor\\b", "the 'whether you're X or Y' opener"), ('\\bmore than just\\b', "'more than just'"), ("\\b(that|this)(?:'?s| is) where\\b[^.!?]{0,30}\\bcomes? in\\b", "'that's where X comes in'"), ('\\bsay goodbye to\\b', "'say goodbye to'"), ('\\bimagine (a|an|the)\\b', "the 'imagine a…' opener"), ('\\bin conclusion\\b|\\bto sum up\\b', 'essay-summary phrasing'), ('\\bwhen it comes to\\b', "'when it comes to' filler"), ('\\bat the end of the day\\b', "'at the end of the day'"), ('\\bthe key is\\b|\\bthe truth is\\b', 'throat-clearing opener'), ('\\bhelps? you to\\b|\\bcan help you\\b', "hedged benefit ('helps you to…')"), ('\\bmay potentially\\b|\\bcould potentially\\b|\\bmight possibly\\b', 'stacked hedging'), ('\\bvery unique\\b|\\bquite literally\\b', 'intensifier padding'), ("\\bhere'?s the thing\\b|\\blet'?s break (it|this) down\\b|\\bthe best part\\b", 'throat-clearing opener'), ("\\bready to get started\\b|\\blet'?s get started\\b", 'boilerplate CTA'), ('\\bthe (result|answer|catch|kicker|upshot)\\?\\s', 'self-answering question')]
COMPOUND = re.compile('\\b[a-z]{2,}-[a-z]{2,}(?:-[a-z]{2,})*\\b', re.I)
COMPOUND_FLOOR = 4
PROOF = re.compile('([\\d][\\d,]*(?:\\.\\d+)?)\\s*\\+?\\s*((?:happy|early|active|satisfied|verified|trusted|delighted)\\s+)?(?:\\w+\\s+){0,1}(users?|customers?|learners?|students?|teams?|members?|companies|businesses|homeowners?|subscribers?|clients?|patients?|readers?|sites?|projects?)(?!\\w)', re.I)

def normalise(t):
    t = t.replace('‑', '-').replace('\xa0', ' ').replace('’', "'")
    return re.sub('\\s+', ' ', t).strip()

def visible_text(html):
    t = re.sub('<(script|style)\\b.*?</\\1>', ' ', html, flags=re.S | re.I)
    t = re.sub('<!--.*?-->', ' ', t, flags=re.S)
    t = re.sub('<[^>]+>', ' ', t)
    t = _html.unescape(t)
    return normalise(t)

def read_utf8(path):
    return open(path, encoding='utf-8', errors='replace').read()

def markdown_prose(md):
    md = re.sub('```.*?```', ' ', md, flags=re.S)
    md = re.sub('!\\[[^\\]]*\\]\\([^)]*\\)', ' . ', md)
    md = re.sub('\\[([^\\]]*)\\]\\([^)]*\\)', '\\1', md)
    md = re.sub('`[^`]*`', ' it ', md)
    md = re.sub('~~.*?~~', ' it ', md, flags=re.S)
    md = re.sub('^\\s{0,3}#{1,6}\\s*(.*)$', ' . \\1 . ', md, flags=re.M)
    md = re.sub('\\|', ' . ', md)
    md = re.sub('^\\s*(?:[-*+]|\\d+\\.)\\s+', ' . ', md, flags=re.M)
    md = re.sub('^\\s*>\\s?', ' . ', md, flags=re.M)
    md = re.sub('[*_>]', ' ', md)
    return normalise(md)

def audit(text):
    hits = {'vocab': [], 'phrases': [], 'punctuation': [], 'rhythm': [], 'proof': []}
    low = text.lower()
    for w in VOCAB:
        n = len(re.findall(_root_pattern(w), low))
        if n:
            hits['vocab'].append((w, n))
    for w in VOCAB_EXACT:
        n = len(re.findall(f'(?<!\\w){re.escape(w)}(?!\\w)', low))
        if n:
            hits['vocab'].append((w, n))
    for pat, label in PHRASES:
        found = re.findall(pat, low)
        if found:
            hits['phrases'].append((label, len(found)))
    for s in re.split('(?<=[.!?])\\s+', text):
        for i in range(0, max(1, len(s)), 220):
            window = s[i:i + 220]
            if window.count('—') >= 2:
                hits['punctuation'].append(('two or more em-dashes in one sentence', window[:70].strip()))
                break
    for s in re.split('(?<=[.!?])\\s+', text):
        for i in range(0, max(1, len(s)), 220):
            window = s[i:i + 220]
            found = COMPOUND.findall(window)
            if len(found) >= COMPOUND_FLOOR:
                hits['punctuation'].append((f'{len(found)} hyphenated compounds stacked in one sentence', ', '.join(found[:4])))
                break
    if text.count(';') > max(3, len(text) // 1200):
        hits['punctuation'].append(('semicolon-heavy for web copy', f"{text.count(';')} found"))
    for pat in ('\\b(\\w{4,}),\\s+(\\w{4,}),\\s+and\\s+(\\w{4,})\\b', '\\b(\\w{4,}),\\s+(\\w{4,})\\s+and\\s+((?:\\w+\\s+){1,2}\\w+)\\s*[.!?,;:]'):
        for m in re.finditer(pat, text):
            hits['rhythm'].append(('rule-of-three list', m.group(0)[:60]))
    for m in PROOF.finditer(text):
        hits['proof'].append(m.group(0).strip())
    return hits

def report(hits, label='', allow_proof=False):
    weights = {'vocab': 1, 'phrases': 1, 'punctuation': 1, 'rhythm': 1, 'proof': 1}
    if allow_proof:
        weights['proof'] = 0
    failed = [k for k, v in hits.items() if v]
    score = 5 - sum((weights[k] for k in failed))
    score = max(0, score)
    titles = {'vocab': 'AI vocabulary', 'phrases': 'AI constructions', 'punctuation': 'punctuation cadence', 'rhythm': 'rule-of-three rhythm', 'proof': 'possible invented proof'}
    if label:
        print(f'── {label}')
    for k in ('proof', 'phrases', 'vocab', 'punctuation', 'rhythm'):
        if not hits[k]:
            continue
        print(f'  {titles[k]}:')
        for item in hits[k][:8]:
            print(f'    · {(item[0] if isinstance(item, tuple) else item)}' + (f'  ({item[1]})' if isinstance(item, tuple) and len(item) > 1 else ''))
        if len(hits[k]) > 8:
            print(f'    · …and {len(hits[k]) - 8} more')
    print(f'\n  score {score}/5', end='  ')
    print('CLEAN' if score == 5 else 'needs a cleanse')
    return score
if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(errors='replace')
    except (AttributeError, ValueError):
        pass
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    allow_proof = '--allow-proof' in args
    args = [a for a in args if a != '--allow-proof']
    as_md = '--markdown' in args
    args = [a for a in args if a != '--markdown']
    if args[0] == '--text':
        text = ' '.join(args[1:])
        if as_md:
            text = markdown_prose(text)
    elif args[0].endswith('.md') or as_md:
        try:
            text = markdown_prose(read_utf8(args[0]))
        except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
            sys.exit(f'deslop: cannot read {args[0]}: {e.strerror}')
    else:
        try:
            html = read_utf8(args[0])
        except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
            sys.exit(f'deslop: cannot read {args[0]}: {e.strerror}')
        if '--view' in args:
            vid = args[args.index('--view') + 1]
            start = html.find(f'id="{vid}"')
            if start < 0:
                sys.exit(f'no element with id "{vid}"')
            nxt = html.find('id="view-', start + 1)
            html = html[start:nxt if nxt > 0 else len(html)]
        text = visible_text(html)
    if not text.split():
        sys.exit('deslop: no visible copy to score — empty input')
    print(f'{len(text.split())} words of visible copy\n')
    sys.exit(0 if report(audit(text), allow_proof=allow_proof) == 5 else 1)
```