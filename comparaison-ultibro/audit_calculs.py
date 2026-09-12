"""Contrôles ciblés, sans écriture dans les sources. Python standard uniquement.

Afficher le rapport JSON : python -B comparaison-ultibro/audit_calculs.py
Les anomalies historiques détectées sont attendues ; les contrôles M3 doivent passer.
"""
import csv
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import random
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / 'projet-fable-ultibro/tools'))
from calculateur_m3 import calculate, examples


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def rank(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        div = a[r][c]
        a[r] = [v / div for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                mult = a[i][c]
                a[i] = [x - mult * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def main():
    manifest = json.loads((HERE / 'INVENTAIRE_SOURCES.json').read_text())
    records = manifest['originaux_fable'] + manifest['originaux_astra'] + [manifest['revue_fournie']]
    for rec in records:
        assert hashlib.sha256((ROOT / rec['path']).read_bytes()).hexdigest() == rec['sha256'], rec['path']
    tracked_changes = subprocess.check_output(
        ['git', 'diff', '--name-only', manifest['base_fable_commit'], '--',
         *[r['path'] for r in manifest['originaux_fable']]], cwd=ROOT, text=True)
    assert not tracked_changes, tracked_changes

    # 19 lots : lecture du CSV historique, sans exécuter son générateur.
    lines = list(csv.reader((ROOT / 'projet-astra-ultibro/source-originale/outputs/plan-experiences-19-lots.csv').open(), delimiter=';'))
    h = next(i for i, row in enumerate(lines) if row and row[0] == 'Ordre_propose')
    rows = [dict(zip(lines[h], row)) for row in lines[h+1:] if row and row[0].isdigit()]
    factors = ['Lactose_fin_pct', 'MgSt_total_pct', 'Precoating_min_2500rpm', 'Melange_actifs_min_1500rpm']
    centres = [r for r in rows if r['Essai'].startswith('C')]
    corners = [r for r in rows if r['Essai'].startswith('F')]
    settings = {tuple(float(r[f]) for f in factors) for r in corners}
    assert len(rows) == 19 and len(centres) == 3 and len(settings) == 16
    for f in factors:
        levels = sorted({float(r[f]) for r in corners})
        assert len(levels) == 2 and all(sum(float(r[f]) == v for r in corners) == 8 for v in levels)
    for r in rows:
        assert math.isclose(sum(float(r[k]) for k in ['IND_sel_g', 'GLY_sel_total_g', 'MgSt_total_g', 'Lactose_fin_g', 'Lactose_porteur_g']), 300, abs_tol=1e-7)
        assert math.isclose(float(r['MgSt_dans_PI_g_si_F0_PI']) + float(r['MgSt_externe_g_si_F0_PI']), float(r['MgSt_total_g']), abs_tol=1e-7)
    x4 = list(itertools.product([-1, 1], repeat=4)) + [(0,) * 4] * 3
    x4full = [[1, *x, *[v*v for v in x], *[x[i]*x[j] for i in range(4) for j in range(i+1,4)]] for x in x4]
    assert rank(x4full) == 12

    doe = module('historical_doe', ROOT / 'projet-fable-ultibro/tools/doe.py')
    doe.check_conference(doe.C6)
    dsd = doe.dsd_runs()
    x = [[r[f + '_code'] for f in doe.FACTORS] for r in dsd]
    main_sq = [[1, *r, *[v*v for v in r]] for r in x]
    full = [a + [r[i]*r[j] for i in range(6) for j in range(i+1,6)] for a,r in zip(main_sq,x)]
    assert len(dsd) == 15 and len(set(map(tuple,x))) == 13
    assert rank(main_sq) == 13 and len(full[0]) == 28 and rank(full) == 13

    select = module('historical_select', ROOT / 'projet-fable-ultibro/tools/select_candidate.py')
    scores = {n: select.score(v, select.WEIGHTS) for n,v in select.CANDIDATES.items()}
    c1 = next(n for n in scores if n.startswith('C1 '))
    c2 = next(n for n in scores if n.startswith('C2 '))
    notes = list(select.CANDIDATES[c2]); notes[1] -= 1; notes[2] -= 1
    changed = select.score(notes, select.WEIGHTS)
    assert math.isclose(scores[c1],3.64) and math.isclose(scores[c2],3.94) and math.isclose(changed,3.59)
    freqs = select.sensitivity()
    score_errors = []
    with (ROOT / 'projet-fable-ultibro/lactose/candidats_lactose.csv').open() as f:
        for r in csv.DictReader(f, delimiter=';'):
            if r['Score_pondere_max14'].isdigit():
                expected = sum(int(r[k])*w for k,w in [('S1_princeps',2),('S2_fines_intrinseques',2),('S3_dry_coating',1),('S4_contraste',1),('S5_disponibilite',1)])
                if expected != int(r['Score_pondere_max14']):
                    score_errors.append({'grade':r['Grade'],'historique':int(r['Score_pondere_max14']),'recalcule':expected})
    assert len(score_errors) == 2
    old = module('historical_batch', ROOT / 'projet-fable-ultibro/tools/batch_record.py')
    old_rows, _ = old.batch_record('invalid',300,.986,.1,.9,1)
    negative = next(r[1] for r in old_rows if r[0].startswith('MgSt externe'))
    assert negative < -6

    # Recalcul indépendant des masses molaires à partir des formules atomiques.
    c,h,n,o,br = 12.011,1.008,14.007,15.999,79.904
    ind = 24*c+28*h+2*n+3*o
    gly = 19*c+28*h+n+3*o
    fi = (ind+4*c+4*h+4*o)/ind
    fg = (gly+br)/gly
    base = dict(batch_g=300,fill_mg=25,titre_ind=1,titre_gly=1,mgst_mode='pct_poudre',mgst_value=.15)
    rng = random.Random(20260912)
    for _ in range(200):
        args = dict(base, batch_g=rng.uniform(100,2000),fill_mg=rng.uniform(15,35),titre_ind=rng.uniform(.9,1),titre_gly=rng.uniform(.9,1),fines_pct=rng.uniform(0,9),ml001_fraction=rng.random())
        result = calculate(**args); masses = result['masses_g']; q=result['controles']
        assert math.isclose(sum(masses.values()),args['batch_g'],abs_tol=1e-9)
        assert math.isclose(masses['IND_maleate_g']*args['titre_ind']/fi/q['unites_theoriques']*1e6,110,abs_tol=1e-9)
        assert math.isclose(masses['GLY_matiere_g']*args['titre_gly']/fg/q['unites_theoriques']*1e6,50,abs_tol=1e-9)
        assert all(v >= 0 for v in masses.values())
    bad = [dict(batch_g=0),dict(batch_g=True),dict(fill_mg=-1),dict(titre_ind=0),dict(titre_gly=1.1),dict(titre_ind=float('nan')),dict(mgst_value=float('inf')),dict(ml001_fraction=-.1),dict(fines_pct=100),dict(mgst_mode='implicite'),dict(mgst_value=-.1),dict(gly_route='PI',titre_gly=.95,mgst_fraction_pi=.1),dict(gly_route='PI',titre_gly=.1,mgst_fraction_pi=.9),dict(mgst_fraction_pi=.01)]
    # Même un PI mathématiquement cohérent est exclu du programme actuel.
    bad.append(dict(gly_route='PI',titre_gly=.949,mgst_fraction_pi=.049,titre_ind=.986))
    for change in bad:
        try:
            calculate(**dict(base,**change))
        except ValueError:
            pass
        else:
            raise AssertionError(f'Entrée invalide acceptée : {change}')
    fixed_pct = calculate(**dict(base,fill_mg=23.75))['controles']
    fixed_ug = calculate(**dict(base,fill_mg=23.75,mgst_mode='ug_par_gelule',mgst_value=37.5))['controles']
    assert math.isclose(fixed_pct['MgSt_total_ug_par_gelule'],35.625)
    assert math.isclose(fixed_ug['MgSt_total_ug_par_gelule'],37.5)
    low = calculate(**dict(base,min_weigh_g=1))['controles']['masses_sous_poids_minimal']
    assert set(low) == {'GLY_matiere_g','MgSt_externe_g'}
    print(json.dumps({
        'statut':'CONTROLES_PASSES_ANOMALIES_HISTORIQUES_DOCUMENTEES',
        'originaux_controles':len(records), 'fichiers_historiques_modifies':0,
        'Astra_19_lots':{'sommets':16,'centres':3,'equilibre_par_facteur':'8/8','bilans':'conformes aux arrondis','rang_modele_quadratique_complet':12},
        'Fable_DSD':{'lignes':15,'reglages_distincts':13,'rang_lineaire_carres':13,'ddl_residuels':2,'ddl_manque_ajustement':0,'colonnes_quadratique_complet':28,'rang_quadratique_complet':13},
        'MCDA':{'C1':scores[c1],'C2':scores[c2],'C2_si_GLY_et_stabilite_moins_un_point':changed,'frequence_C2_premier_poids_seuls':freqs[c2],'interpretation':'Aucune probabilité de bioéquivalence'},
        'scores_lactose_a_corriger':score_errors,
        'ancien_calculateur_MgSt_negatif_accepte_g':negative,
        'nouveau_calculateur':{'bilans_aleatoires_valides':200,'cas_invalides_rejetes':len(bad),'voie_PI_refusee':True,'remplissage_23_75_mg_pct_fixe':fixed_pct,'remplissage_23_75_mg_ug_fixe':fixed_ug,'poids_minimal_signale':low},
        'budget_scenario_4_lots':{'NGI':27+12+3+18+18+6,'DD':54+24+6+36+36+12,'capsules_RLD_disponibles':270,'allocation_RLD_avec_reserves':3*52+34},
        'exemples_theoriques':examples()
    },ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
