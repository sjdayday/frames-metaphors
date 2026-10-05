#!/usr/bin/env python3
"""Check that every quoted passage in corpus.md / analysis.md appears verbatim — modulo quote-mark
style, whitespace, and editorial marks — in the staged capture files or the translation packet.
Second-look blockquotes (Claude's own text, introduced by an '*If ...' line) are skipped."""
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
    q = re.sub(r'\((?:LS|FR)-\d+(?:,\s*[A-Za-z0-9-]+)*\)\s*$', '', q)   # trailing ID tags, e.g. (FR-8, publisher)
    q = re.sub(r'[.,;:!?]+\s*$', '', q)                                  # terminal punctuation (source may end a quote with a comma before "said")
    q = re.sub(r'\[sic[^\]]*\]', '|', q)
    q = re.sub(r'\[…\]|\[\.\.\.\]|…|\.\.\.', '|', q)
    q = re.sub(r'\[[^\]]*\]', '|', q)
    q = q.replace(' / ', '|').replace('*', '')
    return [re.sub(r'[.,;:!?]+$', '', p) for p in (norm(x) for x in q.split('|')) if len(p) >= 12]

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
        for seg in segments(p):
            if seg in corpus_text:
                ok += 1
            else:
                bad += 1
                print(f'  MISSING in sources: {seg[:200]}')
    print(f'{path}: {ok} segments verified, {bad} not found, {skipped} second-look blocks skipped')
    return bad

bad = sum(check_file(f) for f in sys.argv[1:])
sys.exit(1 if bad else 0)
