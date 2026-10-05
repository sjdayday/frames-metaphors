# frames-metaphors

**Status:** v0.1, 2026-10-05. A working analysis, meant to be revised. Written by Claude at Steve's request; everything here is a draft to be checked, not a source. The brief is `frames-metaphors-context` (kept as written).

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
| `case-studies/01-ls11-fr11/` | Case 01: paired public communications about Loehle & Scafetta 2011 and Foster & Rahmstorf 2011. `corpus.md` (statements with provenance and pairing), `analysis.md` (pairs P1–P3 in both modes, substance notes, second looks, assessment of the modes), `README.md`. |
| `framenet/framenet-frames-used.md` | Generated reference: full FrameNet 1.7 records (definition, frame elements with core types, relations, lexical units) for every frame used in annotations. |
| `scripts/fn_lookup.py`, `scripts/fn_dump.py` | Look up lexical units for words; regenerate the frames reference. Require NLTK with the `framenet_v17` corpus (see below). |

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

**Done in v0.1.** Scaffolding; glossary; verified reference list; FrameNet 1.7 loaded and the frames reference generated; case 01 corpus (13 + 13 statements, five pairs defined); pairs P1–P3 analysed in both modes with substance notes and second looks; protocol v0.1.

**Findings so far** (from `case-studies/01-ls11-fr11/analysis.md`): both sides describe their method with the same subtraction script and the other side's with the same contamination register; both use the same three deception frames with identical role assignments and the lay reader as victim; both claim the word "skeptic" through the same frame; "pause" evokes a frame with an agent and a built-in resumption; the technical vocabulary that carries each side's claim about method is absent from FrameNet. Mode A is worth keeping as a quick, allegiance-blind first pass; Mode B does the inferential work.

**Open with Steve.** The register and length of the second look; where substance notes should live; whether to keep full Mode A tables or summarize them.

**Queued.** Case 01 pairs P4 (the forecast contest and "pause") and P5 (nature and humans as causes); then the "pause/hiatus" case, the consensus / manufactured-consensus / settled cluster, and a single foundational metaphor ("greenhouse" or "fingerprint") traced from the technical literature into public use. A literature pass on climate-metaphor research (Nerlich, Koteyko, Deignan, Semino, Russill; Lakoff 2010 read as a primary statement) is listed in `references.md` and not yet read in full.

## Revision log

- **v0.1 — 2026-10-05.** First pass, as above.
