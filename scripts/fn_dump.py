#!/usr/bin/env python3
"""Dump full FrameNet 1.7 frame records (definition, FEs with core types, relations, sample LUs)
for the frames used in frames-metaphors annotations. With no arguments, the frames are collected from the
analyses, the protocol, the glossary and the literature file (backticked names that FrameNet 1.7 knows). Output: Markdown to stdout."""
import sys, re, textwrap
from nltk.corpus import framenet as fn

def frames_in_use():
    """Every backticked Capitalized_name in the analyses, protocol and glossary that FrameNet knows."""
    import glob, os
    here = os.path.dirname(os.path.abspath(__file__)); repo = os.path.join(here, '..')
    files = glob.glob(os.path.join(repo, 'case-studies', '*', 'analysis.md')) + \
            [os.path.join(repo, 'method', 'unpack-protocol.md'), os.path.join(repo, 'glossary.md'),
             os.path.join(repo, 'literature', 'climate-metaphor-research.md')]
    names = set()
    for fpath in files:
        if os.path.exists(fpath):
            names.update(re.findall(r'`([A-Z][A-Za-z_]*)`', open(fpath, encoding='utf-8').read()))
    out = []
    for n in sorted(names):
        try:
            fn.frame(n); out.append(n)
        except Exception:
            pass
    return out

FRAMES = sys.argv[1:] or frames_in_use()

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', s).strip()

def dump(name):
    try:
        f = fn.frame(name)
    except Exception as e:
        print(f'## {name}\n\n*not found: {e}*\n'); return
    print(f'## {f.name}  (frame id {f.ID})\n')
    print(clean(f.definition) + '\n')
    print('**Frame elements**\n')
    print('| FE | core type | definition |')
    print('|---|---|---|')
    for fe_name, fe in sorted(f.FE.items(), key=lambda kv: (kv[1].coreType != 'Core', kv[0])):
        d = textwrap.shorten(clean(fe.definition), 220, placeholder=' …')
        print(f'| {fe_name} | {fe.coreType} | {d} |')
    print()
    rels = []
    for r in f.frameRelations:
        rels.append(f'{r.type.name}: {r.superFrameName} → {r.subFrameName}')
    if rels:
        print('**Frame relations** (super → sub)\n')
        for r in sorted(set(rels)):
            print(f'- {r}')
        print()
    lus = sorted(f.lexUnit.keys())
    print(f'**Lexical units** ({len(lus)}): ' + ', '.join(lus) + '\n')

print('# FrameNet 1.7 frames used in frames-metaphors annotations\n')
print('Generated from the FrameNet 1.7 release as distributed with NLTK (`framenet_v17`), '
      'Berkeley FrameNet, ICSI. Frame and FE definitions are FrameNet\'s own text, lightly '
      'whitespace-normalized; FE definitions are truncated. Regenerate with `scripts/fn_dump.py`.\n')
for n in FRAMES:
    dump(n)
