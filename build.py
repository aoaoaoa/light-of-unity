import html, json, sys
sys.path.insert(0, "/home/claude/unity")
from data import *

def esc(s): return html.escape(s) if s else ""
ITEMS = items()
SIDES = '<meta name="claude:viewport-fit-sides" content="cover">'
GUT = "padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));"

# ---------------------------------------------------------------- A: TWO VOICES
def build_a():
    secs = []
    for si, (name, dark, light, its) in enumerate(SECTIONS):
        rows = []
        for it in [i for i in ITEMS if i["si"] == si]:
            echo = ""
            if it["echo"]:
                echo = f'''<div class="echo"><p>{esc(it["echo"])}</p><cite>{esc(it["source"])}{(" · " + it["year"]) if it["year"] else ""}</cite></div>'''
            rows.append(f'''<article class="pair" id="p{it["n"]}">
  <div class="num">{it["n"]:02d}</div>
  <p class="letter">{esc(it["letter"])}</p>
  {echo}
</article>''')
        secs.append(f'''<section class="band" style="--d:{dark};--l:{light}">
  <div class="inner">
    <header class="sec"><span class="label">{esc(name)}</span><span class="label">{si+1} / {len(SECTIONS)}</span></header>
    {"".join(rows)}
  </div>
</section>''')
    return f'''<title>Two Voices</title>
{SIDES}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..600&display=swap">
<style>
/* Layout: full-bleed color bands, one per theme of the letter; inside each, the letter speaks in a condensed grotesque and the literature answers in an italic serif, set as a two-column spread that stacks on phones. */
:root{{
  --paper:#f4f6f3; --ink:#15201a; --mute:#5c6a62; --rule:#c9d2cc;
  --band-bg:var(--l); --band-fg:#15201a; --band-mute:rgba(21,32,26,.62); --band-rule:rgba(21,32,26,.22);
  --display:"Archivo",Impact,"Arial Narrow",sans-serif; --serif:"Newsreader",Georgia,"Times New Roman",serif;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--paper:#0e1411;--ink:#eef1ec;--mute:#9aa79f;--rule:#2a3630;--band-bg:var(--d);--band-fg:#f3f1ea;--band-mute:rgba(243,241,234,.62);--band-rule:rgba(243,241,234,.22);color-scheme:dark}}}}
:root[data-theme="dark"]{{--paper:#0e1411;--ink:#eef1ec;--mute:#9aa79f;--rule:#2a3630;--band-bg:var(--d);--band-fg:#f3f1ea;--band-mute:rgba(243,241,234,.62);--band-rule:rgba(243,241,234,.22);color-scheme:dark}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--serif);font-size:18px;line-height:1.45}}
.inner{{max-width:1440px;margin:0 auto;{GUT}}}
.label{{font-family:var(--display);font-stretch:85%;font-weight:600;font-size:12px;letter-spacing:.14em;text-transform:uppercase}}
/* cover */
.cover{{padding-block:clamp(48px,9vw,120px) clamp(40px,6vw,80px);border-bottom:1px solid var(--rule)}}
.cover h1{{font-family:var(--display);font-stretch:70%;font-weight:900;font-size:clamp(64px,13vw,180px);line-height:.86;letter-spacing:-.02em;margin:0 0 .35em;text-transform:uppercase;text-wrap:balance;max-width:9ch}}
.cover .meta{{display:grid;grid-template-columns:1fr 1fr;gap:32px;max-width:860px;align-items:start}}
.cover .meta p{{margin:0;font-size:17px;line-height:1.5;color:var(--mute)}}
.cover .meta p b{{color:var(--ink);font-weight:500}}
.key{{display:flex;gap:6px;margin-top:28px;flex-wrap:wrap}}
.key a{{display:block;height:10px;flex:1 1 60px;min-width:40px;background:var(--sw);border-radius:2px;text-decoration:none}}
/* bands */
.band{{background:var(--band-bg);color:var(--band-fg);padding-block:clamp(40px,6vw,88px)}}
.sec{{display:flex;justify-content:space-between;border-bottom:1px solid var(--band-rule);padding-bottom:12px;margin-bottom:clamp(28px,4vw,56px);color:var(--band-mute)}}
.pair{{display:grid;grid-template-columns:3.2rem minmax(0,1.1fr) minmax(0,.9fr);gap:0 clamp(24px,4vw,64px);padding-block:clamp(28px,4vw,56px);border-top:1px solid var(--band-rule)}}
.pair:first-of-type{{border-top:0;padding-top:0}}
.num{{font-family:var(--display);font-stretch:75%;font-weight:700;font-size:15px;color:var(--band-mute);padding-top:.6em;font-variant-numeric:tabular-nums}}
.letter{{margin:0;font-family:var(--display);font-stretch:78%;font-weight:700;font-size:clamp(26px,3.3vw,44px);line-height:1.04;letter-spacing:-.012em;text-wrap:pretty;min-width:0}}
.echo{{min-width:0;border-left:1px solid var(--band-rule);padding-left:clamp(16px,2vw,28px)}}
.echo p{{margin:0;font-style:italic;font-size:clamp(17px,1.5vw,21px);line-height:1.42;font-weight:300;font-variation-settings:"opsz" 20}}
.echo cite{{display:block;margin-top:14px;font-style:normal;font-family:var(--display);font-stretch:85%;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--band-mute)}}
.pair:not(:has(.echo)) .letter{{grid-column:2/4;max-width:24ch}}
.close{{padding-block:clamp(48px,8vw,100px);text-align:left}}
.close p{{max-width:38ch;font-size:20px;margin:0 0 20px}}
.close a{{font-family:var(--display);font-stretch:80%;font-weight:700;color:var(--ink);text-decoration:underline;text-underline-offset:.2em}}
a:focus-visible{{outline:2px solid currentColor;outline-offset:3px}}
@media (max-width:760px){{
  .pair{{grid-template-columns:2.2rem minmax(0,1fr)}}
  .echo{{grid-column:2;margin-top:22px;border-left:0;padding-left:0;border-top:1px solid var(--band-rule);padding-top:18px}}
  .pair:not(:has(.echo)) .letter{{grid-column:2}}
  .cover .meta{{grid-template-columns:1fr}}
}}
</style>
<main>
<header class="cover inner">
  <span class="label" style="color:var(--mute)">Bahá'ís of the United States · Juneteenth 2020</span>
  <h1>{esc(TITLE)}</h1>
  <div class="meta">
    <p><b>Twenty-three sentences</b> from a letter of the National Spiritual Assembly of the Bahá'ís of the United States, dated June 19, 2020, read in sequence.</p>
    <p>Beside each, an echo from Bahá'í literature.</p>
  </div>
  <nav class="key" aria-label="Sections">{"".join(f'<a href="#p{[i for i in ITEMS if i["si"]==si][0]["n"]}" title="{esc(s[0])}" style="--sw:var(--sw{si})"></a>' for si,s in enumerate(SECTIONS))}</nav>
</header>
{"".join(secs)}
<footer class="close inner">
  <p>{esc(CLOSE_TEXT.replace(" at link.bahai.us/juneteenth","."))}</p>
  <a href="{CLOSE_URL}">link.bahai.us/juneteenth</a>
</footer>
</main>
<style>:root{{{";".join(f"--sw{si}:{s[1]}" for si,s in enumerate(SECTIONS))}}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{{";".join(f"--sw{si}:{s[2]}" for si,s in enumerate(SECTIONS))}}}}}
:root[data-theme="dark"]{{{";".join(f"--sw{si}:{s[2]}" for si,s in enumerate(SECTIONS))}}}</style>
'''

# ---------------------------------------------------------------- B: THE LETTER, GLOSSED
def build_b():
    paras = []
    refs = []
    for it in ITEMS:
        note = ""
        if it["echo"]:
            k = len(refs) + 1
            refs.append(it)
            note = f'''<aside class="gloss" id="g{k}" style="--c:{it["dark"]};--cl:{it["light"]}">
  <p>{esc(it["echo"])}</p>
  <cite>{esc(it["source"])}{(", " + it["year"]) if it["year"] else ""}</cite>
</aside>'''
        paras.append(f'''<div class="row" id="r{it["n"]}" style="--c:{it["dark"]};--cl:{it["light"]}">
  <p class="line">{esc(it["letter"])}{note}</p>
</div>''')
    biblio = "".join(f'<li><span class="bk">{i+1}</span><span>{esc(r["source"])}{(", " + r["year"]) if r["year"] else ""}</span></li>' for i, r in enumerate(refs))
    return f'''<title>The Letter, Glossed</title>
{SIDES}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0;1,9..144,300..700,0&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap">
<style>
/* Layout: the letter read as a letter, one measure, book scale, in a soft serif; each echo sits in the right margin as a numbered gloss in a quiet sans, with the section color as a hairline beside it. On phones the gloss follows its sentence. */
:root{{
  --paper:#f6f7f4; --ink:#161b17; --mute:#66706a; --rule:#d8ddd8; --tint:var(--c);
  --text:"Fraunces",Georgia,"Times New Roman",serif; --sans:"Instrument Sans","Helvetica Neue",Arial,sans-serif;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--paper:#101412;--ink:#ecefe9;--mute:#98a39c;--rule:#2b332e;--tint:var(--cl);color-scheme:dark}}}}
:root[data-theme="dark"]{{--paper:#101412;--ink:#ecefe9;--mute:#98a39c;--rule:#2b332e;--tint:var(--cl);color-scheme:dark}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--text);font-size:19px;line-height:1.5}}
.wrap{{max-width:1360px;margin:0 auto;{GUT}padding-block:clamp(40px,7vw,96px) clamp(48px,8vw,110px)}}
.head{{display:grid;grid-template-columns:minmax(0,62ch) minmax(0,40ch);grid-template-rows:auto auto;gap:0 40px;align-items:end;border-bottom:1px solid var(--rule);padding-bottom:28px;margin-bottom:clamp(36px,5vw,72px)}}
.eyebrow{{font-family:var(--sans);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);margin:0;grid-column:1/-1;line-height:1.7;padding-bottom:clamp(28px,4vw,44px)}}
h1{{font-weight:300;font-size:clamp(50px,8.4vw,108px);line-height:1;grid-column:1;letter-spacing:-.025em;margin:0;text-wrap:balance;font-variation-settings:"opsz" 144}}
h1 em{{font-style:italic;font-weight:400}}
.head .desc{{grid-column:2;font-family:var(--sans);font-size:14px;line-height:1.55;color:var(--mute);margin:0;max-width:34ch}}
.row{{display:grid;grid-template-columns:minmax(0,62ch) minmax(0,40ch);gap:0 clamp(48px,8vw,128px);position:relative}}
.row+.row{{margin-top:clamp(20px,2.6vw,34px)}}
.line{{margin:0;font-size:clamp(20px,1.9vw,26px);line-height:1.42;font-weight:300;font-variation-settings:"opsz" 30;text-wrap:pretty;position:relative}}
.line::before{{content:"";position:absolute;left:-14px;top:.5em;bottom:.3em;width:3px;background:var(--tint);border-radius:2px}}
.mark{{font-family:var(--sans);font-size:11px;font-weight:600;color:var(--tint);margin-left:.25em;vertical-align:top}}
.gloss{{grid-column:2;font-family:var(--sans);font-size:13.5px;line-height:1.5;color:var(--mute);align-self:start;padding-top:.45em;display:grid;gap:6px;min-width:0}}
.gloss .gk{{font-weight:600;color:var(--tint);font-size:11px;padding-top:.25em}}
.gloss p{{margin:0;font-style:italic}}
.gloss cite{{font-style:normal;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);margin-top:2px}}
.gloss cite::before{{content:"";display:inline-block;width:10px;height:2px;background:var(--tint);vertical-align:middle;margin-right:8px}}
.coda{{border-top:1px solid var(--rule);margin-top:clamp(40px,6vw,80px);padding-top:32px;display:grid;grid-template-columns:minmax(0,62ch);gap:32px clamp(28px,5vw,80px)}}
.coda h2{{font-family:var(--sans);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);margin:0 0 14px;font-weight:600}}
.coda ol{{list-style:none;margin:0;padding:0;font-family:var(--sans);font-size:13.5px;line-height:1.5;display:grid;gap:6px}}
.coda li{{display:grid;grid-template-columns:1.6em 1fr;gap:8px}}
.bk{{color:var(--mute);font-variant-numeric:tabular-nums}}
.coda .note{{font-size:17px;font-weight:300;margin:0 0 14px}}
.coda a{{font-family:var(--sans);color:var(--ink);text-decoration:underline;text-underline-offset:.2em;font-size:14px}}
a:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}
@media (max-width:820px){{
  .head,.row,.coda{{grid-template-columns:minmax(0,1fr)}}
  .gloss{{grid-column:1;padding-top:12px}}
  .head .desc{{grid-column:1;margin-top:20px}}
}}
</style>
<main class="wrap">
<header class="head">
  <p class="eyebrow">National Spiritual Assembly of the Bahá'ís of the United States<br>June 19, 2020</p>
  <h1>How powerful is the <em>light of unity?</em></h1>
  <p class="desc">Passages from the letter, with echoes from Bahá'í literature set in the margin.</p>
</header>
{"".join(paras)}
<footer class="coda">
  <div>
    <p class="note">{esc(CLOSE_TEXT.replace(" at link.bahai.us/juneteenth","."))}</p>
    <a href="{CLOSE_URL}">link.bahai.us/juneteenth</a>
  </div>
</footer>
</main>
'''

# ---------------------------------------------------------------- C: LANTERN
def build_c():
    panels = []
    for it in ITEMS:
        echo = f'''<div class="echo"><p>{esc(it["echo"])}</p><cite>{esc(it["source"])}{(" · " + it["year"]) if it["year"] else ""}</cite></div>''' if it["echo"] else ""
        panels.append(f'''<section class="panel" data-d="{it["dark"]}" data-l="{it["light"]}" id="s{it["n"]}">
  <div class="in">
    <h2>{esc(it["letter"])}</h2>
    {echo}
  </div>
</section>''')
    spine = "".join(f'<a href="#s{it["n"]}" style="--l:{it["light"]}" title="{it["n"]:02d} {esc(it["section"])}"></a>' for it in ITEMS)
    return f'''<title>Lantern</title>
{SIDES}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&display=swap">
<style>
/* Layout: a single dark room. Each sentence of the letter fills a screen in a tall condensed display face, lit in that section's tint; the echo glows beneath in an italic garamond. The background hue shifts as you scroll; a spine of lights on the left marks where you are. Deliberately one theme. */
:root{{
  --bg:#0b0d10; --room:#1f3a0f; --glow:#8fb996; --fg:#f2efe6; --dim:rgba(242,239,230,.6); --rule:rgba(242,239,230,.18);
  --display:"Big Shoulders Display",Impact,"Arial Narrow",sans-serif; --serif:"Cormorant Garamond",Garamond,Georgia,serif;
  color-scheme:dark;
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--fg);font-family:var(--serif);font-size:18px}}
body::after{{content:"";position:fixed;inset:0;z-index:-1;background:radial-gradient(120% 90% at 20% 10%,var(--room) 0%,var(--bg) 70%);transition:background 1.2s ease}}
.spine{{position:fixed;left:max(10px,env(safe-area-inset-left,0px));top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:6px;z-index:5}}
.spine a{{width:4px;height:12px;background:var(--l);opacity:.3;border-radius:2px;transition:opacity .4s,height .4s}}
.spine a.on{{opacity:1;height:22px}}
.cover,.panel,.close{{min-height:100svh;display:grid;align-items:center;{GUT}}}
.in{{max-width:1240px;margin:0 auto;width:100%;padding-left:28px;padding-block:72px}}
.top{{display:flex;justify-content:space-between;font-family:var(--display);font-weight:700;font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--dim);border-bottom:1px solid var(--rule);padding-bottom:10px;margin-bottom:clamp(20px,4vh,44px)}}
h1{{font-family:var(--display);font-weight:900;font-size:clamp(84px,19vw,300px);line-height:.82;margin:0;text-transform:uppercase;color:var(--glow);text-wrap:balance;max-width:7ch;letter-spacing:.005em;text-shadow:0 0 60px color-mix(in oklab,var(--glow) 35%,transparent)}}
.lede{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:32px;max-width:900px;margin-top:40px;font-size:20px;line-height:1.4;color:var(--dim)}}
.lede p{{margin:0}} .lede b{{color:var(--fg);font-weight:500}}
h2{{font-family:var(--display);font-weight:500;font-size:clamp(34px,5.6vw,84px);line-height:1.12;margin:0;color:var(--glow);letter-spacing:.004em;text-wrap:pretty;max-width:22ch;text-shadow:0 0 50px color-mix(in oklab,var(--glow) 28%,transparent);transition:color 1.2s}}
.echo{{margin-top:clamp(28px,5vh,56px);max-width:62ch;border-top:1px solid var(--rule);padding-top:20px}}
.echo p{{margin:0;font-style:italic;font-size:clamp(20px,2.1vw,27px);line-height:1.35;color:var(--fg)}}
.echo cite{{display:block;margin-top:14px;font-style:normal;font-family:var(--display);font-size:13px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim)}}
.close .in p{{font-size:22px;max-width:40ch;color:var(--dim);margin:0 0 18px}}
.close a{{font-family:var(--display);font-weight:700;font-size:28px;letter-spacing:.06em;text-transform:uppercase;color:var(--glow);text-decoration:none;border-bottom:2px solid var(--glow)}}
a:focus-visible{{outline:2px solid var(--fg);outline-offset:4px}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}} body::after,h2,.spine a{{transition:none}}}}
@media (max-width:600px){{.in{{padding-left:18px}} .spine{{gap:4px}} .spine a{{height:8px}} .spine a.on{{height:16px}}}}
</style>
<nav class="spine" aria-label="Sections">{spine}</nav>
<main>
<header class="cover" data-d="#1f3a0f" data-l="#8fb996">
  <div class="in">
    <div class="top"><span>Bahá'ís of the United States</span><span>Juneteenth 2020</span></div>
    <h1>{esc(TITLE)}</h1>
    <div class="lede">
      <p><b>Twenty-three sentences</b> from a letter of the National Spiritual Assembly of the Bahá'ís of the United States, dated June 19, 2020, one to a screen.</p>
      <p>Beneath each, an echo from Bahá'í literature. Scroll.</p>
    </div>
  </div>
</header>
{"".join(panels)}
<footer class="close" data-d="#8a3f12" data-l="#f1b28a">
  <div class="in">
    <div class="top"><span>Source</span><span>·</span></div>
    <p>{esc(CLOSE_TEXT.replace(" at link.bahai.us/juneteenth","."))}</p>
    <a href="{CLOSE_URL}">link.bahai.us/juneteenth</a>
  </div>
</footer>
</main>
<script>
(function(){{
  var root=document.documentElement, links=[].slice.call(document.querySelectorAll('.spine a'));
  var secs=[].slice.call(document.querySelectorAll('[data-d]'));
  if(!('IntersectionObserver' in window))return;
  var io=new IntersectionObserver(function(es){{
    es.forEach(function(e){{ if(!e.isIntersecting)return;
      root.style.setProperty('--room',e.target.dataset.d); root.style.setProperty('--glow',e.target.dataset.l);
      links.forEach(function(a){{a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id)}});
    }});
  }},{{threshold:.55}});
  secs.forEach(function(s){{io.observe(s)}});
}})();
</script>
'''

import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

def standalone(body):
    body = body.replace(SIDES, "")
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}</style>\n'
            + __import__("re").sub(r"<main\b", "</head>\n<body>\n<main", body, count=1) + "\n</body>\n</html>\n")

LANDING = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>How powerful is the light of unity?</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..500;1,9..144,300..500&family=Instrument+Sans:wght@400;600&display=swap">
<style>
:root{--paper:#f6f7f4;--ink:#161b17;--mute:#66706a;--rule:#d8ddd8;--tint:#1b6b4e}
@media (prefers-color-scheme:dark){:root{--paper:#101412;--ink:#ecefe9;--mute:#98a39c;--rule:#2b332e;--tint:#8fcdb0;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"Fraunces",Georgia,serif;font-size:19px;line-height:1.5}
main{max-width:720px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:clamp(48px,10vw,120px)}
p.eyebrow{font-family:"Instrument Sans",Arial,sans-serif;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);line-height:1.7;margin:0 0 32px}
h1{font-weight:300;font-size:clamp(44px,8vw,84px);line-height:1;letter-spacing:-.025em;margin:0 0 48px;text-wrap:balance;font-variation-settings:"opsz" 144}
h1 em{font-style:italic;font-weight:400}
ol{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}
li{border-bottom:1px solid var(--rule)}
li a{display:block;padding:22px 0;color:inherit;text-decoration:none}
li a:hover h2,li a:focus-visible h2{color:var(--tint)}
li a:focus-visible{outline:2px solid var(--ink);outline-offset:4px}
.v{font-family:"Instrument Sans",Arial,sans-serif;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);padding-top:.5em}
h2{margin:0 0 6px;font-weight:400;font-size:28px;line-height:1.1}
li p{margin:0;font-family:"Instrument Sans",Arial,sans-serif;font-size:14px;color:var(--mute);max-width:46ch}
footer{margin-top:48px;font-family:"Instrument Sans",Arial,sans-serif;font-size:14px;color:var(--mute)}
footer a{color:var(--ink)}
</style>
</head>
<body>
<main>
<p class="eyebrow">National Spiritual Assembly of the Bahá'ís of the United States<br>June 19, 2020</p>
<h1>How powerful is the <em>light of unity?</em></h1>
<ol>
<li><a href="v1/"><div><h2>Version one</h2><p>The letter and its echoes as a two-column spread, in eight color bands.</p></div></a></li>
<li><a href="v2/"><div><h2>Version two</h2><p>The passages read in one measure, with echoes as numbered margin glosses and the sources at the foot.</p></div></a></li>
</ol>
<footer>The original letter: <a href="https://link.bahai.us/juneteenth">link.bahai.us/juneteenth</a></footer>
</main>
</body>
</html>
"""

for name, fn in [("two-voices", build_a), ("letter-glossed", build_b)]:
    with open(os.path.join(OUT, f"{name}.html"), "w") as f: f.write(fn())
SITE = os.path.join(os.path.dirname(OUT), "site")
for d, fn in [("v1", build_a), ("v2", build_b)]:
    os.makedirs(os.path.join(SITE, d), exist_ok=True)
    with open(os.path.join(SITE, d, "index.html"), "w") as f: f.write(standalone(fn()))
with open(os.path.join(SITE, "index.html"), "w") as f: f.write(LANDING)
open(os.path.join(SITE, ".nojekyll"), "w").close()
print("ok")
