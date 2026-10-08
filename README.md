# frames-metaphors

**Status:** v0.3, 2026-10-07. A working analysis, meant to be revised. Written by Claude at Steve's request; everything here is a draft to be checked, not a source. The brief is `frames-metaphors-context` (kept as written).

## Purpose

To use concepts from cognitive linguistics — frames, metaphors, construal, and their relatives — to analyse statements about climate science and climate policy, so that a first automatic reaction to a statement can be given a second look.

The concrete use case: Steve, in conversation with a climate-sceptical friend, writes down what he thinks the friend just said and asks for it to be unpacked. The output is a short "second look" both of them can read. The method must therefore work on paraphrased claims, be short, be visibly even-handed, and describe words rather than motives. The limits of what any such analysis can do are set by Haidt's rider and elephant and Kahneman's two systems; the second look is a cue, not an argument.

## Method

**Two levels.**

1. *Statements* are analysed in two modes. **Mode A** is literal FrameNet annotation: which frames the words evoke, which frame elements are filled, and where FrameNet has no entry (a "gap"). It is exact and checkable, strong on the social and epistemic vocabulary (authenticity, certainty, deception, judgment, obviousness), and silent on technical vocabulary (fit, filter, signal, noise, trend, cycle, model, attribution). **Mode B** uses the wider toolkit — hand-built scenario frames (scripts), conceptual metaphor with entailments pressed and hidden, construal, force dynamics, metonymy, presupposition, blends — and does the inferential work.
2. *Arguments and papers* are analysed as narratives: cast (hero, villain, victim), causal story, the chain of frames that carries a reader from problem to moral to remedy, and the master narrative the piece is a scene from.

**Symmetry rule.** Mainstream and sceptical statements are analysed with the same instruments, in pairs matched by the job a statement does (framing the method; framing the headline result; framing the opponent; …). Symmetry of method does not mean symmetry of verdict: each case records the substance separately, so that a framing finding is never read as a scientific one and a scientific judgment never hides inside a framing analysis.

**Did they say it?** Every frame or metaphor attributed to a speaker is anchored in a quoted word. Quotations are verbatim from provenance-tagged captures. FrameNet frame and element names are real names from the 1.7 release, checked locally.

## Repository map

| Path | What it is |
|---|---|
| `frames-metaphors-context` | The project brief, as written by Steve. Not edited. |
| `README.md` | This file. |
| `glossary.md` | The vocabulary used here, grouped by level of analysis, with one climate example per term. |
| `references.md` | Sources, each tagged by how it was verified (`[V]`, `[V-s]`, `[K]`). |
| `method/unpack-protocol.md` | The in-conversation procedure (v0.1): fix the paraphrase; lexical scan; the frame carrying the argument; substance kept separate; the second look. |
| `case-studies/01-ls11-fr11/` | Case 01: paired public communications about Loehle & Scafetta 2011 and Foster & Rahmstorf 2011. `corpus.md` (16 + 15 verbatim statements with provenance, five pairs), `analysis.md` (pairs P1–P5 in both modes, substance notes, second looks, assessment of the modes), `README.md`. |
| `case-studies/02-pause-hiatus/` | Case 02: the "pause"/"hiatus"/slowdown, 2006–2018. `corpus.md` (10 + 14 statements with provenance classes; four pairs), `analysis.md` (Q1 the naming scale; Q2 the inference about the models; Q3 the scoreboard with Figure Q3-1; Q4 the meta-pair and the master frames; additions to the method), `sources/` (captures of four primaries Steve supplied), `figures/` (the start-date/dataset figure, its data and computed trends), `README.md`. |
| `framenet/framenet-frames-used.md` | Generated reference: full FrameNet 1.7 records (definition, frame elements with core types, relations, lexical units) for the 116 frames used in annotations. |
| `scripts/fn_lookup.py`, `scripts/fn_dump.py`, `scripts/check_quotes.py`, `scripts/fig_startdate_sensitivity.py` | Look up lexical units for words; regenerate the frames reference; verify quotations against the paper-behavior captures and the case-local captures; build Figure Q3-1 (needs numpy and matplotlib, and the climate-explain data snapshot or `$ANNUAL_CSV`). The first two require NLTK with the `framenet_v17` corpus (see below). |

## The climate folders

Six folders are linked for context. Five are maintained in other projects and are **read-only** here: `climate-skeptical-individuals`, `climate-science-evolution`, `climate-paper-behavior`, `climate-paper-discussion`, `climate-explain`. They supply statements to analyse and the substance behind them. Case 01 quotes from the verbatim captures in `climate-paper-behavior/pilot/communications/sources/` (with its `MANIFEST.md` hashes) and from the translation review packet there; it cites `climate-science-evolution` for the scientific record and `climate-explain` for the curve-fitting substance. Nothing in those folders is changed by this project.

## Tooling

FrameNet 1.7 is used offline through NLTK (`nltk.corpus.framenet`). The data file is the `framenet_v17` package from the NLTK data repository; in an environment where NLTK's downloader is blocked, fetch the zip directly and unpack it into `nltk_data/corpora/`. `scripts/fn_lookup.py circular fit.v remove.v` prints the lexical units and frames for each word; `scripts/fn_dump.py [Frame ...]` regenerates `framenet/framenet-frames-used.md`. The FrameNet website (framenet.icsi.berkeley.edu) is the same data with a browsing interface.

## Conventions

- Statement IDs: `LS-n` for the sceptical side of a case, `FR-n` for the mainstream side (letters per case); pairs `P1`, `P2`, … Non-author statements (a host, a publisher) are kept when they frame the authors' words for readers, and flagged.
- Mode A tables give span, target word, FrameNet frame in `Code_style`, frame elements filled, and a note; `(gap)` marks a word FrameNet does not cover in the relevant sense.
- Hand-built scenario frames are named in SMALL CAPS (DECOMPOSITION BY SUBTRACTION); conceptual metaphors as TARGET IS SOURCE.
- "Second looks" are written for the table: three to five sentences, the frame named as a picture, the worry granted, one or two questions, the symmetric instance, and a full stop.
- German originals are authoritative for Rahmstorf's KlimaLounge statements; translations are from the review packet and marked as such.

## Status and next steps

**Done in v0.1 (2026-10-05).** Scaffolding; glossary; verified reference list; FrameNet 1.7 loaded and the frames reference generated; case 01 corpus and pairs P1–P3 in both modes; protocol v0.1. Steve's decisions on the v0.1 open questions: the second-look register stays; substance notes stay in the case files; Mode A tables stay in full.

**Done in v0.2 (2026-10-06).** Case 01 completed (pairs P4 and P5; corpus extended to 16 + 15). Case 02 (the pause/hiatus) built from sources reachable from the cloud environment plus the case-01 captures: corpus with provenance classes, four pairs in both modes, additions to the method. Protocol v0.2 (reification marks, the "significant" translation, the naming scale, frame concession, meta-frames). Glossary v0.2. References v0.2.

**Findings so far.** Case 01: both sides describe their method with the same subtraction script and the other side's with the same contamination register; both use the same three deception frames with identical role assignments and the lay reader as victim; both claim the word "skeptic" through the same frame; both reason inside a partition of warming into natural and human shares, which is lexically a partition into the genuine and the made (`Artificiality`); each side hedges where readers do not look. Case 02: the names for the slower warming after 1998 form a scale by explanatory burden (STOPPED → NO WARMING AT ALL → THE PAUSE → HIATUS → SLOWDOWN → FLUCTUATION); the mainstream's adoption of "pause"/"hiatus" was handled four ways (explain, disarm, redefine, refuse); capitalization, the definite article and a "record" reify a fitted trend into an object, which is why its revision later had to be an act ("airbrushed"); each side's account of the other's naming is a corruption frame (seepage vs. airbrushing); and FrameNet's lack of a statistical sense for "significant" is where the scoreboard works on lay readers in both directions. Across both cases: Mode A is a quick, allegiance-blind first pass; Mode B does the inferential work; the technical vocabulary is absent from FrameNet on both sides.

**Done in v0.3 (2026-10-07).** Case 02 reworked from four primaries Steve supplied (Carter 2006, Koonin 2014, Monbiot 2010 quoting Rose 2010, Monckton 2017), with captures in `sources/`; Figure Q3-1 (start-date and dataset sensitivity, HadCRUT4 and NOAA) and its script; frames reference regenerated (137 frames). Steve's decisions: Lewandowsky et al. stay analysed symmetrically; the figure was wanted.

**Added by v0.3.** Koonin's own name for the episode is "this slowing in the temperature rise" — the mainstream end of the naming scale — while he draws the sceptical inference; Carter's 2006 body text is hedged ("not at a rate that differs significantly from zero") under the headline "it stopped in 1998", so the headline/body hedge asymmetry holds on the sceptical side too; Carter also made the "your window too" move in 2006, which means a second look cannot rest on symmetry and must state the criterion (window length relative to the variability, and the start point — Figure Q3-1); Monckton 2017 stacks eight master frames (religion, the Party, the conjuror, torture, cooking, commerce, law, Humpty Dumpty) and concedes in its own words that the El Niño ended the Pause; the mainstream mirrors of those frames are in Monbiot 2010 ("the Mail pays well for this crap", "Mystic Meg", the undying "monster"); and on the current NOAA series the 1998–2012 trend is +0.12 °C per decade against HadCRUT4's +0.06 — the dataset gap is the checkable content behind "airbrushed".

**Open with Steve** (also at the end of `case-studies/02-pause-hiatus/analysis.md`): the AR5 sentences, Rose's 2012 headline, Homewood 2013 and Muller 2013 are still quoted through secondaries; a monthly-data version of Figure Q3-1 (RSS v3.3/v4.0, UAH) would reproduce the "N years N months" scoreboard exactly.

**Queued.** The consensus / manufactured-consensus / settled cluster (from `08`'s primary statements); a single foundational metaphor ("greenhouse" or "fingerprint") traced from the technical literature into public use; the literature pass on climate-metaphor research (Nerlich, Koteyko, Deignan, Semino, Russill; Lakoff 2010 read as a primary statement).

## Revision log

- **v0.3 — 2026-10-07.** Case 02 to v0.2 on primaries; Figure Q3-1; captures and manifest in `case-studies/02-pause-hiatus/sources/`; checker extended to case-local captures; references and frames reference updated.
- **v0.2 — 2026-10-06.** Case 01 pairs P4–P5; case 02 (four pairs); protocol, glossary and references to v0.2; frames reference regenerated (116 frames). Written unattended while Steve was offline; the commit author line is Steve's identity with Claude as co-author, as in v0.1.
- **v0.1 — 2026-10-05.** First pass: scaffolding, glossary, references, protocol v0.1, case 01 pairs P1–P3.
