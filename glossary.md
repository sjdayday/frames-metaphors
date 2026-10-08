# Glossary — the vocabulary this project uses, with one climate example each

**Status:** v0.2, 2026-10-06 (reification, naming scale, frame concession and meta-frame added from case 02). Terms are grouped by the level of analysis they belong to. Definitions are deliberately plain; the sources behind them are in `references.md`. Examples are drawn from `case-studies/01-ls11-fr11/` where possible, so that each term can be seen doing work on a real statement.

---

## A. Lexical level — frames in Fillmore's and FrameNet's sense

**Frame (FrameNet sense).** A schematic situation type that a word evokes, with named participants and props. FrameNet (Berkeley, Fillmore's project) describes about 1,200 such frames for English, each defined in prose with its elements listed, and links some 13,500 words (lexical units) to them. FrameNet frames are fine-grained and general-purpose; they describe what a word presupposes about a situation, not what a speaker believes.
*Example.* "Global warming has **paused**": pause evokes `Activity_pause`, whose core elements are an Agent and an Activity. The word presupposes an ongoing activity and, by FrameNet's own scenario chain, a resumption.

**Frame element (FE).** A named participant or prop in a frame. *Core* elements are conceptually necessary (a Deceiver, a Victim and a Topic for `Intentional_deception`); *peripheral* ones (Time, Place, Means) can be added to any event. In annotation, the question is which core elements the statement fills, which it leaves empty, and which it fills metaphorically.
*Example.* "a trick to fool the ignorant": Deceiver = skepticalscience, Victim = "the ignorant", Topic = model validation; Means (the 2σ envelope) given in the surrounding sentence.

**Lexical unit (LU).** A word in one of its senses, paired with the frame it evokes. `skeptic.n` is one LU, in `Certainty`; `real.a` is two LUs, in `Existence` and in `Artificiality`. Looking a word up means asking which of its LUs is in play.
*Example.* "the **real** global warming signal" takes the `Artificiality` sense (genuine as opposed to fake), not the `Existence` sense — which is why it implicitly makes the unadjusted record less genuine.

**Frame-to-frame relations.** FrameNet links frames by *Inheritance* (a more specific frame of a general one), *Subframe* (a stage of a larger scenario), *Precedes* (temporal order of stages), *Perspective_on* (the same situation seen from one participant's side), *Using*, *Causative_of* and *Inchoative_of*. The Subframe and Precedes relations are FrameNet's small-scale machinery for narrative: a scenario is a frame whose subframes are ordered.
*Example.* `Activity` has subframes `Activity_start`, `Activity_ongoing`, `Activity_pause`, `Activity_paused_state`, `Activity_resume`, `Activity_stop`, `Activity_finish`; Precedes orders them. "Pause" is therefore understood as a stage inside a story that continues.

**Gap.** A word, in the sense used, for which FrameNet has no lexical unit. Gaps are recorded, not papered over; they mark where the inferential work is done by a domain script FrameNet does not have (see B).
*Example.* fit, filter, factor out, signal, noise, trend, cycle, model, attribution, urgency, circular (in the reasoning sense) are all gaps. They are the words that carry each side's claim about method in case 01.

**Mode A.** This project's name for literal FrameNet annotation of a statement: target words, frames, frame elements, gaps. Strong on the social and epistemic layer (who is cast as what; how certain; how authentic), silent on the technical layer.

---

## B. Scenario level — scripts and hand-built frames

**Scenario frame / script.** A template for a kind of situation with roles, ordered steps, and permissible outcomes — Fillmore's earlier "scenes," Schank and Abelson's "scripts," Minsky's "frames." This is the sense in the project brief ("a template for dealing with particular kinds of situations… roles, other elements, and permissible scenarios of action"). It is where inference happens: a script says what comes next and what is normal. When FrameNet has a gap, the script has to be written by hand.
*Example.* DECOMPOSITION BY SUBTRACTION (case 01, Pair 1): Analyst, Record, Known components, Operation, Residual, Reading; its inference — the Residual is a cleaner view of the quantity of interest — is licensed only if the known components are known independently of the Record. Both Foster & Rahmstorf and Loehle & Scafetta describe their methods in this one script.

**Idealized cognitive model (ICM).** Lakoff's term for the structured background knowledge a category or word carries — a cluster of expectations rather than a definition. ICMs supply stock characters.
*Example.* The con-man ICM behind Rahmstorf's *Bauernfängertricks* and Scafetta's "trick to fool the ignorant": a clever deceiver, a naïve mark, a hidden mechanism — and a role for the speaker as the one who sees through it on the mark's behalf.

**Prototype and radial category.** Categories have central members and extensions; much argument is over who counts as a central member. The word is fought over because the honorific goes with the center.
*Example.* "skeptic": center = one who withholds belief for want of evidence (the scientific virtue). Foster's "fake skeptics" and "real skeptics" and Scafetta's "take his … comments with the proper skepticism" both claim the center for their own side.

---

## C. Mapping level — metaphor and its relatives

**Conceptual metaphor.** A systematic mapping from a *source* domain (something concrete and well structured) onto a *target* domain (something abstract or less structured), written TARGET IS SOURCE. The mapping carries the source's logic — its roles, its typical scenarios — into the target, where it licenses inferences. Metaphors *highlight* some aspects of the target and *hide* others (Lakoff & Johnson).
*Example.* "Current methods based on climate models are … **circular**": REASONING IS MOTION ALONG A PATH; a path that returns to its start makes no progress. Highlighted: dependence of the attribution on the models. Hidden: that the dependence can be partial, and that the speaker's own method is fitted to the same record.

**Entailment pressed / entailment hidden.** This project's working terms for the two halves of a metaphor analysis: the inference the speaker wants drawn, and the inferences the source domain brings along that the target does not license (or that the frame leaves no role for).
*Example.* "removing the noise": pressed — the signal exists independently and is merely obscured; hidden — the regression specifies the signal's form in advance, so "the signal" is partly the analyst's model.

**Primary metaphor.** The simplest mappings, grounded in bodily experience and shared across cultures (Grady): MORE IS UP, CAUSES ARE FORCES, KNOWING IS SEEING, STATES ARE LOCATIONS. Complex metaphors are built from them.
*Example.* "the warming trend," "rising temperatures," "upward" (MORE IS UP) are so conventional they read as literal; "makes the progress of global warming much more **clear**" (KNOWING IS SEEING) likewise.

**Image schema.** Pre-conceptual spatial patterns — PATH (source–path–goal), CONTAINER, BALANCE, FORCE, UP–DOWN, LINK, CENTER–PERIPHERY — that structure both primary metaphors and many frames (Johnson).
*Example.* "pause," "course," "progress" (PATH); "tipping point" (BALANCE); "carbon budget" (CONTAINER with a limit); "unabated warming" (FORCE that has not been checked).

**Force dynamics.** Talmy's analysis of how language encodes forces: an *agonist* with a tendency (to move or to rest) and an *antagonist* that opposes it; causing, letting, hindering, helping, blocking, overcoming. Much causal and attributional language is force-dynamic.
*Example.* Loehle: sulfate aerosols "keep sensitive models from **running away** from the data" (antagonist restraining an agonist). Foster: "the **unabated** warming" (an agonist whose tendency persists against resistance). Natural factors that "**mask**" or "**obscure**" a trend are antagonists blocking perception.

**Metonymy.** Letting one thing stand for another it is associated with — a part for a whole, a place or person for an institution, a salient example for a category. Metonyms are cognitive shortcuts and so are exactly where Kahneman's availability and representativeness heuristics enter language.
*Example.* "skepticalscience," "Watts," "Leif," "the IPCC models," "Vahrenholt" each stand for a position; "Climategate," "the hockey stick," "97%," "the pause" each stand for an entire dispute.

**Conceptual blend.** Fauconnier and Turner's generalization of metaphor: two or more *input spaces* are projected into a *blended space* that has emergent structure neither input had. Blends explain inferences a two-domain mapping cannot.
*Example.* "carbon budget": inputs = household accounting and the physics of cumulative emissions; emergent structure = "overspending," "running out," "debt" — none of which is in the physics, where the relation is a continuum.

**Construal.** Langacker's term for the fact that the same situation can be presented in different ways: what is *profiled* (foregrounded) and what is backgrounded; the *granularity* (a 15-year window or a 150-year series); the *vantage point*; whether an actor is named (active voice, first person) or suppressed (passive, agentless). Construal is the most general tool here, and the one closest to the project's goal: "adding perspective" means offering a second construal of the same facts.
*Example.* Loehle: models "are fitted to the historical temperature record" (agentless passive for the suspect step), "we factor out the natural cycles" (first-person agency for the trusted step). Foster uses the same pattern with the roles reversed.

**Presupposition.** What a sentence takes for granted rather than asserts, so that denying the sentence does not deny it. Definite descriptions ("the X") presuppose that X exists; "fake X" presupposes a real X; "not alarming" presupposes an alarm.
*Example.* "the idea that the global warming trend has slowed or even **paused**": the definite "the pause" (common in both sides' writing) presupposes there is one; the argument then becomes whether it is explained, rather than whether it exists.

**Reification.** Turning a description into a thing by grammatical means — a capital letter, a definite article, a length, a record. Once a thing, it can only be removed by an act, so its disappearance from later data has to be someone's doing.
*Example.* Monckton's "the Pause", which "lengthens" and "sets a new record"; when the RSS record was revised the Pause had been "airbrushed out" (case 02, Q1 and Q4).

**Naming scale.** This project's instrument for a contested phenomenon: the names in play, ordered by what each presupposes about before and after and by the explanatory burden it imposes. Each name sets who owes an explanation of what.
*Example.* STOPPED → NO WARMING AT ALL → THE PAUSE → HIATUS → SLOWDOWN → FLUCTUATION for the slower warming after 1998; "pause" and "hiatus" demand an explanation of a gap, "fluctuation" says none is needed (case 02, Q1).

**Frame concession.** Adopting the other side's noun, and with it the noun's presupposition. Four ways it was handled in one episode: adopt and explain (the Met Office's "recent pause"), adopt and disarm in the title (Muller's "A Pause, Not an End"), adopt and redefine (the IPCC's "hiatus, defined as the reduction in trend"), refuse with scare quotes or "putative" (Rahmstorf; Lewandowsky et al.). Each has a cost a second look can name.

**Meta-frame.** A frame about the other side's *process* rather than about the data — contamination ("seepage"), falsification ("airbrushed out", "hide the decline"), manufacture ("manufactured consensus"). Its appearance marks that the argument has left the series; the second look goes back to what is checkable.

**Mode B.** This project's name for analysis with the tools in sections B–E: scripts, metaphors and their entailments, construal, metonymy, narrative cast. It does the inferential work; it is interpretive, so every attribution must be anchored in a quoted word ("did they say it?").

---

## D. Framing in the social sciences — related but distinct senses

**Framing effect (Kahneman & Tversky).** The finding that logically equivalent descriptions ("90% survive" / "10% die") produce different choices. Framing in this sense is about *which equivalent description* is offered, and it is the direct bridge to System 1.
*Example.* "0.66 °C/century is not alarming, in comparison to the IPCC's 2.3" — the Standard_item against which the number is judged is the speaker's choice; a different standard (the harm threshold) would frame the same number differently.

**Frame (Goffman; Entman; media studies).** A principle of organization that tells the audience what kind of situation this is. Entman's four functions: a frame *defines the problem*, *diagnoses its cause*, *makes a moral judgment* and *suggests a remedy*. Useful as a checklist for what a single sentence smuggles in.
*Example.* "The unabated warming is powerful evidence that we can expect further temperature increase …, emphasizing the urgency of confronting the human influence on the climate": problem (warming continues), cause (human influence), moral (urgency), remedy (confront) in one sentence.

**Frame (Lakoff's political sense).** A conceptual structure, often metaphor-built and value-laden, activated by words ("tax relief"), such that evoking it does the persuasive work. Lakoff's program is prescriptive — reframe to win — and partisan; this project borrows his descriptive tools and keeps the program at arm's length. His "hypocognition" (the lack of a frame for something that matters) is a claim worth testing against climate discourse, not assuming.

**Movement framing (Snow & Benford).** *Diagnostic* (what is wrong and who is to blame), *prognostic* (what to do) and *motivational* framing (why act now). Maps closely onto Entman and onto the narrative cast below.

---

## E. Narrative level

**Narrative cast.** Hero, villain, victim (and helper); in the Narrative Policy Framework these, plus a setting, a plot and a moral, define a policy narrative. A sentence is usually understood as a scene from a story the reader already knows; naming the cast shows which story.
*Example.* Rahmstorf: villain = Watts and Vahrenholt, victim = *der Laie*, hero = "we show what the graphic would look like if done correctly," moral = the tobacco playbook. Scafetta: villain = skepticalscience and the IPCC models, victim = readers "with modest scientific knowledge," hero = "my empirical model … a full forecast since Jan/2000," moral = the models "do not belong to the realm of science."

**Causal story (Stone).** Policy problems are framed by the kind of cause assigned: *mechanical* (no one's doing), *accidental* (unintended, unforeseeable), *inadvertent* (unintended consequence of intended action), *intentional*. Each assigns blame and remedy differently.
*Example.* Both sides in case 01 accept an inadvertent story for warming ("human influence"); the dispute is magnitude and tempo. The *deception* frame, by contrast, assigns an intentional story to the opponent's graphs.

**Master narrative.** The large story a side's statements are scenes from — on one side *Merchants of Doubt* (organized, funded doubt), on the other *manufactured consensus* (institutionally produced agreement). Frame analysis of a single sentence tends to lead straight to one of them; the reader's allegiance decides which.

---

## F. Limits and the use case

**Rider and elephant (Haidt); System 1 and System 2 (Kahneman).** The intuitive, fast system responds to frames and metonyms; the deliberate, slow system can take a second look when cued and when it has resources, but mostly serves the intuition. For this project: a second look is a cue, not an argument; it has to be short, symmetric and about the words.

**Second look.** This project's unit of output: three to five sentences that name the frame plainly, grant the worry underneath it, say what the picture adds that the facts don't settle, show the same frame in use on the other side, and stop. Specified in `method/unpack-protocol.md`.

**Symmetry rule.** Mainstream and sceptical statements are analysed with the same instruments, ideally in pairs matched by the job the statement does. Symmetry of method does not imply symmetry of verdict; substance is recorded separately so that neither is mistaken for the other.

**Calibrated language.** The IPCC's controlled vocabulary of likelihood and confidence ("likely" = 66–100%, "very likely" = 90–100%) — an engineered attempt to replace System-1 certainty words with a lexicon. What happens to it downstream, in press releases and blogs, is itself a framing question (see `climate-science-evolution/06-assessment-language.md` for the lexicon as used).

**Register.** The tone a statement is pitched in — dismissive, forensic, collegial — as distinct from its frames. The `climate-paper-behavior` repository's dismissive-register lexicon is the adjacent instrument; frame analysis records register ("since last Thursday"; "childish trick") but does not score it.
