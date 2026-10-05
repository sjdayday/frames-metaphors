#!/usr/bin/env python3
"""Look up FrameNet 1.7 lexical units for words in the LS11/FR11 corpus statements.
Usage: python3 fn_lookup.py word1 word2 ...   (word may include POS, e.g. fit.v)
Prints: LU name -> frame, frame definition (truncated), core FEs.
"""
import sys, re, textwrap
from nltk.corpus import framenet as fn

def lus_for(word):
    if '.' in word:
        pat = r'^' + re.escape(word) + r'$'
    else:
        pat = r'^' + re.escape(word) + r'\.(v|n|a|adv|prep|num|idio|scon|art|c|intj)$'
    return fn.lus(pat)

def core_fes(frame):
    return [name for name, fe in frame.FE.items() if fe.coreType == 'Core']

def main(words):
    for w in words:
        lus = lus_for(w)
        print('=' * 78)
        print(f'WORD: {w}   ({len(lus)} LU(s))')
        if not lus:
            # try substring search
            alt = fn.lus(r'^' + re.escape(w.split('.')[0]))
            if alt:
                print('  no exact LU; nearby LUs:', ', '.join(sorted({f"{l.name}->{l.frame.name}" for l in alt})[:12]))
            continue
        for lu in lus:
            fr = lu.frame
            defn = re.sub(r'\s+', ' ', fr.definition)
            short = textwrap.shorten(defn, 330, placeholder=' …')
            print(f'  LU {lu.name:28s} -> FRAME {fr.name}')
            print(f'     def: {short}')
            print(f'     core FEs: {", ".join(core_fes(fr))}')
            ludef = textwrap.shorten(re.sub(r"\s+"," ",lu.definition), 160, placeholder=' …')
            print(f'     LU def: {ludef}')

if __name__ == '__main__':
    main(sys.argv[1:])
