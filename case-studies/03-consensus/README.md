# Case study 03 — "consensus", "manufactured consensus", "settled" (1996–2021)

**Status:** v0.1, 2026-10-07. Written from the primary statements that `climate-science-evolution/08-manufactured-consensus.md` and `09-problem-typology.md` read in the original, from three of the primaries Steve supplied for case 02 (Carter 2006, Koonin 2014, Monckton 2017), and from fetches (Crichton 2003, Cook et al. 2013 and 2016, the 2013 tweet). Two mainstream items are from memory or title only and are flagged in `corpus.md` (M-11, M-12). See the provenance classes there.

## Why this case

"Consensus" is the word the two sides most often fight *about* rather than *with*: one side says it is not a scientific category at all, the other measures it and reports a percentage, and both call the other's position a product ("manufactured consensus", "manufactured doubt"). The evolution project tests the testable forms of the manufactured-consensus claim and sets aside a fourth, rhetorical form — that invoking consensus "substitutes head-counting for evidence" — as untestable. That fourth form is a claim about a word, and it is this case's subject. The science of attribution is not in dispute at the grain the measurements cover; what the case can add is what the words do.

## Files

| File | Contents |
|---|---|
| `corpus.md` | Eleven S-side and fifteen M-side statements, 1996–2021, with provenance classes; four pairs by job: R1 what consensus is; R2 who made it; R3 settled/unsettled; R4 the labels. |
| `analysis.md` | The four pairs in both modes with substance notes and two second looks each; Figure R-1; seven additions to the method; open questions. |
| `figures/` | `consensus-surveyed-field.png` / `.svg` (Figure R-1: the Bray & von Storch surveys 1996–2015/16 under the assessments' attribution statements, and the 2015/16 human-share question), built by `scripts/fig_consensus_surveys.py` from the snapshot in `figures/data/` (a verbatim copy of `climate-science-evolution/data/bray-von-storch-series.json`). |

## The two findings that organize the case

FrameNet has no lexical unit for *consensus* and four frames for *agreement*; nearly every statement in the case sorts by whether it means agreement on what to do (`Make_agreement_on_action` — the political sense) or agreement on what is so (`Be_in_agreement_on_assessment` — the scientific sense), and the dispute's founding move (Crichton 2003) puts the second into the frame of the first and rejects it there. And *settle* lives in `Make_agreement_on_action` and `Colonization` only — "the science is settled" is, lexically, a deal or a closed frontier, never a finding — which is why the phrase appears in this corpus only inside the sceptical side's quotation marks, while the mainstream's own words are a ladder of calibrated likelihoods.

## Verification

The `[U]` statements (Carter, Koonin 2014, Monckton) are checked by `scripts/check_quotes.py --report` against the case-02 captures. The `[P-08]`/`[P-09]`/`[P-06]` statements are quoted as the evolution project quotes them from the originals, and can be checked there. Still to capture before the case is relied on: the NRC 2010 "settled facts" sentence (M-11, from memory); the CSI 2014 statement (M-12, title only); Oreskes 2004, Doran & Zimmerman 2009 and Anderegg et al. 2010 in the original rather than through `09`.

## Reading order

`analysis.md` R1 (the agreement frames) is the case's main result; R3 (settled) is the shortest; R2 (the two factories) carries most of the substance and Figure R-1; R4 (the labels) is the one most likely to be useful at the table.
