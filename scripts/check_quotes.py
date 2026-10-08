#!/usr/bin/env python3
"""Check that every quoted passage in corpus.md / analysis.md appears verbatim — modulo quote-mark
style, whitespace, and editorial marks — in the staged capture files or the translation packet.
Second-look blockquotes (Claude's own text, introduced by an '*If ...' line) are skipped.
Usage: check_quotes.py [--report] file.md ...   (--report: print misses but exit 0; use for case files whose
quotations come partly from web or secondary sources that the captures cannot verify)."""
import re, glob, sys, unicodedata

import os
# Location of the climate-paper-behavior captures: $CAPTURES if set, else the sibling repo
# (../climate-paper-behavior relative to this repo), else the session upload path used in the cloud container.
_here = os.path.dirname(os.path.abspath(__file__))
_candidates = [os.environ.get('CAPTURES', ''),
               os.path.join(_here, '..', '..', 'climate-paper-behavior', 'pilot', 'communications'),
               '/mnt/user-data/uploads/climate-paper-behavior/pilot/communications']
BASE = next((c for c in _candidates if c and os.path.isdir(c)), None)
if BASE is None:
    sys.exit('captures not found; set CAPTURES=/path/to/climate-paper-behavior/pilot/communications')
SRC = glob.glob(os.path.join(BASE, 'sources', '*.txt')) + glob.glob(os.path.join(BASE, 'translation-review', '*.md'))
# case-local captures (this repo): case-studies/*/sources/*.txt, with provenance headers
SRC += glob.glob(os.path.join(_here, '..', 'case-studies', '*', 'sources', '*.txt'))
if not SRC:
    sys.exit(f'no capture files under {BASE}')

def norm(s):
    s = unicodedata.normalize('NFC', s)
    for a, b in [('“','"'),('”','"'),('„','"'),('‟','"'),('‘',"'"),('’',"'"),
                 ('‚',"'"),(' ',' '),('–','-'),('—','-'),('°',' deg ')]:
        s = s.replace(a, b)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

corpus_text = norm(' '.join(open(f, encoding='utf-8').read() for f in SRC))

def segments(q):
    q = re.sub(r'\((?:LS|FR|S|M|T)-\d+[a-z]?(?:,[^)]*)?\)\s*$', '', q)   # trailing ID tags, e.g. (FR-8, publisher), (S-10, Carter 2006)
    q = re.sub(r'[.,;:!?]+\s*$', '', q)                                  # terminal punctuation (source may end a quote with a comma before "said")
    q = re.sub(r'\[sic[^\]]*\]', '|', q)
    q = re.sub(r'\[…\]|\[\.\.\.\]|…|\.\.\.', '|', q)
    q = re.sub(r'\[[^\]]*\]', '|', q)
    q = q.replace(' / ', '|').replace('*', '')
    parts = (re.sub(r'^\([^)]*\)\s*', '', norm(x)) for x in q.split('|'))   # leading speaker/role tags, e.g. (the remedy:), (SAR 1995:)
    parts = (re.sub(r'\((?:LS|FR|S|M|T)-\d+[a-z]?(?:,[^)]*)?\)\s*$', '', x).strip() for x in parts)   # ID tags before a ' / ' join
    return [re.sub(r'[.,;:!?]+$', '', p) for p in parts if len(p) >= 12]

def check_file(path):
    ok = bad = skipped = 0
    lines = open(path, encoding='utf-8').read().split('\n')
    paras, cur, skip_block, prev = [], [], False, ''
    for ln in lines:
        if ln.startswith('>'):
            body = ln[1:].strip()
            if not cur and not body:
                continue
            if not cur:
                skip_block = prev.startswith('*If ')
            if body == '':
                paras.append((' '.join(cur), skip_block)); cur = []
            else:
                cur.append(body)
        else:
            if cur:
                paras.append((' '.join(cur), skip_block)); cur = []
            if ln.strip():
                prev = ln.strip()
    if cur: paras.append((' '.join(cur), skip_block))
    for p, skip in paras:
        if skip:
            skipped += 1; continue
        p = re.sub(r'^\((?:[^)]*quoted[^)]*|Curry quotes the IPCC|Curry|Daily Caller|Monckton, quoted|Monbiot|Homewood\'s fragments)[^)]*:\)\s*', '', p)   # speaker tags inside quotes
        for seg in segments(p):
            if seg in corpus_text:
                ok += 1
            else:
                bad += 1
                print(f'  MISSING in sources: {seg[:200]}')
    print(f'{path}: {ok} segments verified, {bad} not found, {skipped} second-look blocks skipped')
    return bad

args = [a for a in sys.argv[1:] if not a.startswith('--')]
report_only = '--report' in sys.argv   # for files that mix capture-verified ([C]) quotations with web/secondary ones
bad = sum(check_file(f) for f in args)
if report_only:
    print('(--report: misses above are expected for quotations not taken from the captures; exit 0)')
    sys.exit(0)
sys.exit(1 if bad else 0)
