#!/usr/bin/env python3
"""Dump full FrameNet 1.7 frame records (definition, FEs with core types, relations, sample LUs)
for the frames used in frames-metaphors annotations. Output: Markdown to stdout."""
import sys, re, textwrap
from nltk.corpus import framenet as fn

FRAMES = sys.argv[1:] or [
    'Artificiality', 'Intentional_deception', 'Prevarication', 'Manipulate_into_doing',
    'Deception_success', 'Obviousness', 'Evidence', 'Certainty', 'Adjusting', 'Removing',
    'Causation', 'Activity_pause', 'Activity_stop', 'Process_stop', 'Beat_opponent',
    'Competition', 'Confronting_problem', 'Hostile_encounter', 'Stimulus_focus',
    'Experiencer_obj', 'Predicting', 'Expectation', 'Eclipse', 'Hiding_objects',
    'Becoming_aware', 'Reasoning', 'Statement', 'Success_or_failure', 'Endeavor_failure',
    'Adopt_selection', 'Suitability', 'Shapes', 'Hindering', 'Change_event_duration',
]

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
