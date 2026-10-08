# Case study 04 — the "greenhouse": a foundational metaphor traced from the technical literature into public use (1824–2026)

**Status:** v0.1, 2026-10-08. The nineteenth-century primaries are quoted through translations, transcriptions and one historian's essay (Fourier in the 1837 translation; Tyndall 1859 and 1863 via two tracings; Arrhenius 1896 from a scan and 1908 from Project Gutenberg; Ekholm 1901 via two secondaries; Wood 1909 via a transcription); the modern ones from fetches (Hansen 1988, UNFCCC 1992, Lindzen 1992, RealClimate 2007, Gerlich 2009, Lacis 2010, Happer 2011, NASA, the CO2 Coalition, Steffen 2018, the AMS glossary, the EPA) and three of the case-02 captures (GCC 1996 via `08`, Koonin 2014, Dessler via Monbiot 2010). `sources/fetch-log.md` records each fetch.

## Why this case

The other cases are about words one side introduced and the other adopted. "Greenhouse" is a word the field chose for itself, between 1896 and 1908, for a mechanism it had already described in four other pictures (Fourier's two kinds of heat; Tyndall's gate, blanket and dam); its own glossary calls it a misnomer; it is still the first sentence of the agency explainer; and the sceptical side's two most durable objections to the mechanism — that the atmosphere is not a greenhouse (Wood 1909; Gerlich 2009) and that the effect is saturated (Ångström 1900; "declines as its concentration increases", 2015) — are entailments of the picture rather than of the physics. The substance is `climate-science-evolution/02-problems/P01` (`SETTLED`); this case is about what the picture does.

## Files

| File | Contents |
|---|---|
| `corpus.md` | The trace table (T-1 … T-32: every form the mechanism has been given, each anchored in a quotation with provenance), the paired statements (9 S, 14 M), five pairs by job. |
| `analysis.md` | The trace read as frames (what each form presses and hides); G1 naming the mechanism; G2 reasoning from the picture to the dose (saturation; percent of what; share against control); G3 the substance (pollution vs. plant food); G4 the extreme (Hothouse Earth vs. the impossible machine); G5 the history; Figure G-1; eight additions to the method; open questions. |
| `figures/` | `pane-and-ladder.png` / `.svg` (Figure G-1: the single-pane picture beside the emission-height mechanism), built by `scripts/fig_pane_and_ladder.py`. A schematic, not data. |
| `sources/fetch-log.md` | The URLs, dates and classes of everything fetched, and what could not be obtained. |

## The three findings that organize the case

FrameNet puts *greenhouse* in `Buildings` (an enclosure that protects plants from cold), *trap* in `Trap` (a snare with a Deceiver and a Victim), *absorb* in `Soaking_up` and *saturated* in `Being_wet` — so the field's public verbs are a snare and a sponge, and the sceptical "saturated" is the sponge full. The building came late and from outside: Arrhenius attributed the "hot-house" to Fourier, who never used it; "green-house" is Ekholm's (1901), offered beside a second picture, the heat store, that the field dropped; "greenhouse effect" was born in Poynting's scare quotes (1907). And the field has disowned the picture at least four times without being able to put it down, because its substitutes ("trapped", "blanket") carry the same hidden entailment — while Tyndall's dam and his blanket, read carefully, carry the one the physics needs.

## Verification

Only the three `[U]` quotations (Koonin 2014; Dessler via Monbiot 2010; and, through `08`, the GCC) are checkable by `scripts/check_quotes.py --report`. The `[W]` and `[S]` items are quoted as the fetch tool returned them and can be re-fetched; the trace table's first eight rows would become `[U]` if the originals (Tyndall's *Heat considered as a Mode of Motion*; Ekholm in *QJRMS*) were supplied. The `[K]` items that carry weight — Kiehl & Trenberth 1997 (the ~155 W m⁻² total effect), Schmidt et al. 2010, Zhu et al. 2016, Peterson et al. 2008 — are listed in the analysis's open questions.

## Reading order

The trace table in `corpus.md`, then "The trace read as frames" and G2 in `analysis.md` (the saturation argument as the glass picture's entailment, and Figure G-1); G3 (food and pollution) is the one most likely to come up at the table; G1 and G4 are the symmetric bookends.
