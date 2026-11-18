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
