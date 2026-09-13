"""Construit le comparatif autonome depuis les sources conservées. Python standard."""
from pathlib import Path
import base64, csv, hashlib, io, json, re, subprocess
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
paths = subprocess.check_output(['git','ls-files','projet-fable-ultibro','projet-astra-ultibro','comparaison-ultibro'],cwd=ROOT,text=True).splitlines()
docs=[]
for name in paths:
    p=ROOT/name
    if '/html/' in name or p.name=='COMPARATIF_TROIS_METHODES.html' or p.suffix not in ('.md','.csv','.json','.py','.html','.pdf'): continue
    raw=p.read_bytes()
    docs.append(dict(path=name,size=len(raw),sha256=hashlib.sha256(raw).hexdigest(),kind=p.suffix[1:],data=base64.b64encode(raw).decode(),text='' if p.suffix=='.pdf' else raw.decode('utf-8')))
def rows(name,skip=0):
    text=(ROOT/name).read_text(encoding='utf-8')
    return list(csv.DictReader(io.StringIO('\n'.join(text.splitlines()[skip:])),delimiter=';'))
astra=rows('projet-astra-ultibro/source-originale/outputs/plan-experiences-19-lots.csv',3)
astra=[r for r in astra if r['Ordre_propose'].isdigit()]
fable=[r for r in rows('projet-fable-ultibro/outputs/plan_dsd_15_lots.csv') if r['ordre'].isdigit()]
assert len(astra)==19 and len(fable)==15
protocol=(ROOT/'projet-fable-ultibro/protocole/PROTOCOLE_FB2.md').read_text()
experiments=[]
for m in re.finditer(r'^### EXP-(\d+) — (.*)$',protocol,re.M):
    experiments.append(dict(number=int(m[1]),title=m[2],start=m.start()))
for e in experiments:
    e.pop('start')
assert len(experiments)==16
payload=dict(docs=docs,astra=astra,fable=fable,experiments=experiments,
    mcda=rows('projet-fable-ultibro/outputs/selection_mcda.csv'),power=rows('projet-fable-ultibro/outputs/puissance_equivalence_in_vitro.csv'),
    checks=json.loads((ROOT/'comparaison-ultibro/VERIFICATIONS.json').read_text()),
    source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),date='13 septembre 2026')
# Escaping '<' makes embedded user documents inert inside the JSON script element.
data=json.dumps(payload,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
html=(HERE/'modele.html').read_text().replace('/*__DATA__*/',data)
out=ROOT/'comparaison-ultibro/COMPARATIF_TROIS_METHODES.html'
out.write_text(html,encoding='utf-8')
print(json.dumps(dict(output=str(out),bytes=out.stat().st_size,documents=len(docs),astra_rows=len(astra),fable_rows=len(fable),simulations=len(payload['power'])),ensure_ascii=False))
