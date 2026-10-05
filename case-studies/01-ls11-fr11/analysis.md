# Case study 01 — paired analyses: L&S11 and F&R11 public communications

**Status:** v0.1, 2026-10-05. First three pairs (P1–P3) analysed in both modes; P4–P5 queued. Written by Claude at Steve's request; a draft to be checked, not a source.

**What this file is for.** The project's use case is a conversation: Steve hears a claim from a climate-sceptical friend, writes down what he thinks he heard, and asks for the claim to be unpacked. This case study rehearses that unpacking on real statements from both sides of one dispute, so that the method is tested before it is used. Each pair is analysed twice — once by literal FrameNet annotation (**Mode A**), once with the wider cognitive-linguistic toolkit (**Mode B**) — and each ends with the short "second look" that the conversation would actually need. The statements are quoted in `corpus.md`; IDs refer to it.

**Two rules kept throughout.**

1. *Symmetry of method, not of verdict.* Both sides are analysed with the same instruments. That does not make the underlying claims equally well supported, and this file says where the substance is asymmetric, in a separate section for each pair, so that a framing finding is never mistaken for a scientific one.
2. *Did they say it?* Every frame or metaphor attributed to a speaker is anchored in a quoted word. Where FrameNet has no entry for a word, the gap is recorded rather than papered over.

**Mode A conventions.** FrameNet 1.7 (the release distributed with NLTK) is the reference; frame and frame-element names are FrameNet's, in `Code_style`; the frames used are documented in `../../framenet/framenet-frames-used.md`. A target word is given in SMALL CAPS; `(gap)` means FrameNet has no lexical unit for the word in the relevant sense. Annotation is of the word's *evoked* frame; whether the frame is used literally or metaphorically is a Mode B judgment.

---

## Pair 1 — The method: "circular" models vs. "removing" the noise

### The statements

LS side (Loehle, 2011-07-25):

> How do we detect the influence of humans on the climate system? Current methods based on climate models are unfortunately circular: their estimate of human effects is only valid if the models are correct, but the models make certain assumptions and also are fitted to the historical temperature record. A model-independent estimate of climate response is needed and is provided by this study. (LS-1)

> Mosh: You call it calibration, I call it fitting. (LS-5)

> This is not a polynomial fit to the data. We factor out the natural cycles based on solar activity first, then identify the human signal. (LS-6)

FR side (Foster, 2011-12-06; Rahmstorf, 2011-12-05):

> Natural factors cause temperature fluctuations which make the man-made global warming signal less clear, fluctuations which are often exploited by fake skeptics to suggest that global warming has paused, or slowed down, or isn't happening at all. A new paper by Foster & Rahmstorf accounts for some of those other factors, and by removing their influence from the temperature record makes the progress of global warming much more clear. (FR-1)

> Once the effect of the three known factors was estimated, it could be removed from the temperature data to create adjusted temperature data which is mostly (but not completely!) free of their influence. (FR-2)

> With the bulk of the fluctuations removed, the continued course of warming over the entire time span (including the last decade) is undeniable. (FR-3)

> It shows that differences between the five data sets reside, to a large extent, in their short-term variability and not in the climatic trend. After the variability is removed, all five data sets are very similar. (FR-7)

### Mode A — FrameNet-literal annotation

**LS-1, LS-5, LS-6**

| Span | Target | FrameNet frame | Frame elements filled | Note |
|---|---|---|---|---|
| How do we DETECT the influence of humans… | detect.v | `Becoming_aware` | Cognizer = we; Phenomenon = the influence of humans on the climate system | The question presupposes the Phenomenon exists and asks only about Means. |
| the INFLUENCE of humans on the climate system | influence.n | `Objective_influence` | Influencing_entity = humans; Dependent_entity = the climate system | The IPCC's own term ("human influence"); the least loaded causal noun available. |
| Current methods … are unfortunately CIRCULAR | circular.a | `Shapes` only | — | **(gap)** FrameNet has no reasoning sense. The word is doing metaphorical work the lexicon does not record (see Mode B). |
| their ESTIMATE of human effects | estimate.n | `Estimated_value` | Cognizer = the methods/modellers; Item = human effects | |
| is only VALID if the models are correct | valid.a | `Being_in_effect` | Binding_principle = the estimate | FrameNet's only sense is the normative one (a valid ticket, a law in force). The logical sense is an extension of it: an inference "in force" only under a condition. |
| the models are CORRECT | correct.a | `Correctness` | Information = the models | |
| make certain ASSUMPTIONS | assumption.n | — | — | **(gap)** |
| are FITTED to the historical temperature record | fit.v | `Suitability` / `Capacity` | — | **(gap)** Neither FrameNet sense is the statistical one. |
| A model-INDEPENDENT estimate | independent.a | `Contingency` | Outcome = the estimate; Determinant = models (negated) | Exactly the right frame: the estimate's Outcome is claimed not to be contingent on the Determinant. |
| is NEEDED | need.v | `Have_as_requirement` | Dependent = (detecting the influence); Requirement = a model-independent estimate | |
| is PROVIDED by this study | provide.v | `Supply` | Supplier = this study; Theme = the estimate | |
| You CALL it CALIBRATION, I CALL it FITTING | call.v ×2 | `Labeling` | Speaker = you / I; Entity = it (the same operation); Label = calibration / fitting | A sentence *about* framing: two Labels for one Entity. |
| CALIBRATION | calibration.n | `Adjusting` | Agent = modellers; Part = model parameters; Feature = (output vs. record); Imposed_purpose = "accord with a standard or norm" (FrameNet's LU definition) | The frame presupposes an external standard. |
| FITTING | fitting.n | — | — | **(gap)** |
| We FACTOR OUT the natural cycles | factor out.v | — | — | **(gap)** |
| then IDENTIFY the human SIGNAL | identify.v; signal.n | `Verification` / `Categorization`; `Gesture` only | Inspector/Cognizer = we; Unconfirmed_content/Item = the human signal | signal.n **(gap)** — FrameNet has only the gestural sense. |

**FR-1, FR-2, FR-3, FR-7**

| Span | Target | FrameNet frame | Frame elements filled | Note |
|---|---|---|---|---|
| Many different factors AFFECT Global temperature | affect.v | `Objective_influence` | Influencing_entity = many different factors; Dependent_entity = global temperature | Same frame as LS-1's "influence". |
| FAKE "skeptics" | fake.a | `Artificiality` | Entity = these people; Reference_category = skeptic | The scare quotes mark the category membership as doubtful — the condition the frame's definition names. |
| "SKEPTICS" | skeptic.n | `Certainty` | Cognizer = (them); Content = accepted opinions (low certainty) | FrameNet defines a skeptic by a Cognizer's doubt — so "fake skeptic" = someone whose doubt is not real doubt. |
| like to CLAIM that mainstream climate scientists IGNORE everything but greenhouse gases | claim.v; ignore.v | `Statement`; `Attention` | Speaker = fake skeptics; Message = …; Perceiver = scientists; Figure = everything but GHGs | |
| Natural factors CAUSE temperature FLUCTUATIONS | cause.v; fluctuation.n | `Causation`; `Change_position_on_a_scale` | Cause = natural factors; Effect = fluctuations; Item = temperature | Nature is given a causal role — for the fluctuations only. |
| which make the MAN-MADE global warming SIGNAL less CLEAR | man-made; signal.n; clear.a | (no LU) / `Gesture` only / `Obviousness` | Phenomenon = the man-made global warming signal; Degree = less | "man-made" has no LU, but it is the `Artificiality` frame's own criterion ("method of creation… identity of its creators"). signal.n **(gap)**. |
| EXPLOITED by fake skeptics | exploit.v | — | — | **(gap)** |
| to SUGGEST that global warming has PAUSED, or SLOWED DOWN | suggest.v; pause; slow down | `Statement` / `Evidence`; `Activity_pause`; `Change_event_duration` | Speaker = fake skeptics; Agent/Activity = global warming; Event = global warming | pause.v has no LU; pause.n evokes `Activity_pause`, whose core FEs are **Agent** and Activity, and which FrameNet places in the chain `Activity_ongoing → Activity_pause → Activity_paused_state → Activity_resume`. |
| ACCOUNTS FOR some of those other factors | account for.v | — | — | **(gap)** |
| by REMOVING their influence from the temperature record | remove.v | `Removing` | Agent = Foster & Rahmstorf; Theme = their influence; Source = the temperature record | The Source is profiled: the record is a place from which something is taken. |
| makes the PROGRESS of global warming much more CLEAR | progress.n; clear.a | `Progression`; `Obviousness` | Entity = global warming; Phenomenon = its progress; Degree = much more | `Progression` is motion toward a goal, with positive valence in ordinary use. |
| ESTIMATED … REMOVED … ADJUSTED temperature data | estimate.v; remove.v; adjust.v | `Estimating`; `Removing`; `Adjusting` | Agent = the authors; Part = the data; Feature = the three influences | The same `Adjusting` frame as Loehle's "calibration" (LS-5). |
| FREE of their influence | free.a | `Expensiveness` only | — | **(gap)** FrameNet has only "free of charge". |
| the continued COURSE of warming … is UNDENIABLE | course.n; undeniable | `Path_traveled`; (no LU) | Theme = warming; Path = its course | undeniable fits `Obviousness`, whose Phenomenon FE FrameNet glosses as "the entity or facts that are undeniable given the Evidence". |
| differences … RESIDE in their short-term variability | reside.v | `Residence` | Resident = the differences; Location = short-term variability | A spatial metaphor (differences *live* somewhere) FrameNet records only in its literal frame. |
| the variability is REMOVED … very SIMILAR | remove.v; similar.a | `Removing`; `Similarity` | Agent = we; Theme = variability; Source = data sets; Entities = the five data sets | |

**What Mode A gave for Pair 1.** Three things worth having. (i) It separates the *social-epistemic* vocabulary, which FrameNet covers well — `Artificiality`, `Certainty`, `Statement`, `Obviousness`, `Labeling`, `Objective_influence`, `Contingency` — from the *technical* vocabulary, which it does not cover at all: circular, fit, factor out, signal, noise, account for, assumption. The gaps are not random; they are the words that carry each side's claim about method, which means the inferential work is being done by domain scripts FrameNet does not have (Mode B supplies them). (ii) It shows that both sides evoke the **same frames** for the same operations: `Objective_influence` for causation, `Removing` for subtraction, `Adjusting` for calibrating/adjusting, `Obviousness` for the result. (iii) It makes two lexical facts visible that a reader would miss: "valid" is at base a normative word (in force under a condition), and "pause" evokes a frame with an **Agent** slot and a resumption built in.

### Mode B — frames, metaphors, construal, scenario

**The shared scenario frame: DECOMPOSITION BY SUBTRACTION.** Neither side's description of its method is in FrameNet, so the frame has to be stated by hand:

| Role / step | Content |
|---|---|
| Analyst | the people doing the decomposition |
| Record | a time series taken as the total |
| Known components | parts of the total the Analyst says are understood and can be quantified |
| Operation | estimate the known components and subtract them |
| Residual | what is left |
| Reading | the Residual is identified with a quantity of interest |
| Inference licensed by the frame | if the known components really are known, the Residual is a cleaner view of the quantity of interest than the Record was |

Both statements instantiate it. Foster: known components = ENSO, volcanic aerosols, solar irradiance (each with its own measured index); Residual = the trend; Reading = "the real global warming signal". Loehle: known components = 60- and 20-year "natural cycles"; Residual = a linear rise after 1942; Reading = the anthropogenic component (LS-6: "factor out the natural cycles … first, then identify the human signal"). The frame makes the two operations look like the same kind of thing, and each side describes its own subtraction in the purifying register (remove, filter out, factor out) and the other side's modelling in the contaminating register (fitted, curve fitting). The frame's inference is licensed only to the extent that the known components are known *independently of the Record*. That is where the two cases differ — see Substance notes.

**LS metaphors.**

- *Circular* (LS-1): REASONING IS MOTION ALONG A PATH; a circular path returns to its start, so a circular argument makes no progress. Entailment pressed: the models' attribution depends on the models' correctness, which was itself established partly by matching the record, so the attribution adds nothing beyond the fit. Entailments hidden: (a) "no progress" is stronger than "dependent on" — a dependence can be partial; (b) model-based attribution uses more than the global-mean series (spatial and vertical patterns, ocean heat, the responses to volcanic eruptions), so the circle, if there is one, does not close on one curve; (c) the speaker's own method is fitted to the same record (the cycles' amplitudes and phases are estimated from 1850–1950 temperatures), which the path metaphor would make equally circular.
- *Fitted vs. calibration* (LS-5): the sentence is a construal contest in miniature. FrameNet's `Adjusting` (calibration) presupposes an external standard the Part is brought into accord with; "fitting" names the same operation with the Record itself as the standard. The choice of label is the choice of whether an external standard exists. The second clause (sulfate aerosols "assumed as input (which keeps sensitive models from running away from the data)") gives a concrete mechanism — and notably uses a *restraint* image (force dynamics: an antagonist holding back a model that would otherwise run away), which concedes that the record constrains the models.
- *Model-independent* (LS-1): `Contingency` negated — the estimate as an Outcome not determined by models. Hidden: it is contingent on a different determinant, the assumption that the pre-1950 record is natural and periodic.

**FR metaphors.**

- *Signal and noise* (FR-1, FR-3, FR-4): a COMMUNICATION frame used metaphorically — warming is a Message, natural fluctuations are interference (FrameNet's `Eclipse`: an Obstruction hides the Eclipsed), the analyst a receiver who filters. Entailments pressed: the signal exists independently and is merely obscured; removing noise reveals rather than creates; the operation is passive and epistemic. Entailments hidden: the regression specifies the signal's form in advance (a straight line in time), so "the signal" is partly the analyst's model; the adjusted series is itself a model output. Foster's own parenthesis — "mostly (but not completely!) free of their influence" (FR-2) — is the author's concession to exactly this point, and it survives nowhere in the headline framings (FR-4, FR-8).
- *Real* (FR-4: "the real global warming signal"; FR-8: "the true global warming trend"): `Artificiality` applied to the data — the adjusted series is the genuine one, which makes the measured series the less genuine one. Hidden: both are constructions; "real" transfers the authenticity of the physics to a statistical product.
- *Progress / course* (FR-1, FR-3): warming as a traveler on a path (`Progression`, `Path_traveled`). "Progress" carries the valence of improvement, an odd fit for warming, and it is what makes "pause" (the opposing side's word) grammatical: travelers pause. Both sides are inside the JOURNEY metaphor; they disagree about whether the traveler stopped.
- *Exploited* (FR-1): fluctuations as a resource used by bad actors — intent is attributed to the other side's reading of the same wiggles (this becomes the main business of Pair 3).

**Construal.** Both sides profile a decomposition and background the choices that make it possible. Loehle backgrounds the fitted origin of his cycles; Foster backgrounds the assumed form of his trend. Both use agentless or thing-agent constructions for the suspect step ("are fitted to", "it could be removed") and first-person agency for the trusted step ("we factor out", "we … identified"). Each side describes nature as the cause of what it wants to subtract (LS: cycles cause the 60-year swing; FR: natural factors cause the fluctuations) and reserves the residual for its preferred cause.

**Scenario / narrative.** Both are REVEAL-THE-HIDDEN-TRUTH narratives (Entman's four functions in one paragraph each): problem (the record is confounded), cause (models fitted to data / natural fluctuations), moral (the confound misleads), remedy (our decomposition). Cast: LS — hero = a model-independent method; villain = circular models. FR — hero = an analysis that strips away noise; villain = fake skeptics who exploit the noise; victim = public understanding.

### Substance notes (not framing)

Symmetry of frames does not settle the merits, and here the asymmetry is real and specific. Foster & Rahmstorf's "known factors" are quantified by indices measured independently of the temperature record (the Multivariate ENSO Index, aerosol optical depth, total solar irradiance), so their subtraction has an external standard in exactly the sense `Adjusting` presupposes. Loehle & Scafetta's cycles are estimated from the temperature record itself and justified by a claimed link to solar-system motion; the external standard is the claimed astronomical period, not an independent measurement of the cycle's effect. That difference is what Loehle's "fitting vs. calibration" question is really about, and it cuts against the side that raised it. On the other side, Foster's "undeniable" and the release's "proving" and "true" overstate what a 32-year regression with a pre-specified linear trend can show; the paper's own more careful language ("mostly (but not completely!)") is the better statement of its result. The `climate-explain` case file on Loehle & Scafetta covers the curve-fitting substance in detail; this project does not redo it.

### Second looks

*If a friend says:* "Climate models are circular — they're tuned to the same temperature record they're then used to explain."

> "Circular" is a path picture: it says the argument comes back to its starting point and gains nothing. The worry underneath is real — a model's attribution does lean on the model being right — but "circular" claims more than that: it claims zero information. Two questions open it up. First, is the attribution resting only on the global-mean curve, or also on patterns the models weren't tuned to (where warming shows up, how the system responds to eruptions)? Second — the same question for any method that subtracts "known" parts, including the alternatives — what is the outside standard the known parts are checked against? Loehle himself put it as "you call it calibration, I call it fitting"; the honest answer is that the label depends on whether there's an outside standard, and that question applies to his cycles too.

*If I say (or a mainstream friend says):* "Once you remove the noise, the real warming signal is undeniable."

> "Noise," "remove," and "real" each make a choice. The analysis assumed in advance that the signal is a straight line in time and then took out three known wiggles; the adjusted series is a model result too, which Foster himself flagged ("mostly (but not completely!) free of their influence"). The strength worth crediting is that the three wiggles were measured independently of the temperature record — that is what distinguishes this subtraction from fitting cycles to the same series. "Undeniable" is a word about the listener, not the data; a friend will hear a claim about themselves.

---

## Pair 2 — The headline: "not alarming" vs. "the urgency of confronting"

### The statements

LS side (Loehle & Scafetta, 2011-07-25):

> Human Effect on Climate Clearly Detected / (but is 0.66 deg C/100yr since ~1950!) (LS-2)

> Warming due to anthropogenic GHG+Aerosol of 0.66 oC/Century is not alarming, in comparison to the IPCC protected [sic] 2.3 oC/Century This 0.66 value is an upper bound in our estimation […] (LS-3)

> […] which is about 3.5 times smaller than the average 2.3°C/century anthropogenic warming rate projected by the IPCC during the first decades of the 21st century. (LS-7)

FR side (Foster, press release, 2011-12-05; ScienceDaily lede):

> The unabated warming is powerful evidence that we can expect further temperature increase in the next few decades, emphasizing the urgency of confronting the human influence on the climate. (FR-6)

> Researchers have added further clarity to the global climate trend, proving that global warming is showing no signs of slowing down and that further increases are to be expected in the next few decades. (FR-8, publisher)

### Mode A — FrameNet-literal annotation

| Side | Span | Target | FrameNet frame | Frame elements | Note |
|---|---|---|---|---|---|
| LS | Human Effect on Climate CLEARLY DETECTED | clearly.adv; detect.v | `Obviousness`; `Becoming_aware` | Phenomenon = human effect on climate; Degree = clearly | The headline grants the mainstream frame in full before the parenthesis takes it back. |
| LS | (but IS 0.66 deg C/100yr since ~1950!) | — | (quantity) | — | The concessive "but" plus exclamation: the detection is conceded, the magnitude is the news. |
| LS | is not ALARMING | alarming.a | `Stimulus_focus` | Stimulus = 0.66 °C/century warming; Experiencer = (the public), negated | FrameNet's alarm family: alarm.n → `Noise_makers` (the device), alarm.v → `Experiencer_obj`, alarmed.a → `Emotion_directed`. The lexical base is a bell that signals danger. |
| LS | in COMPARISON to the IPCC projected 2.3 oC/Century | comparison.n | `Evaluative_comparison` (via compare.v; the noun has no LU) | Profiled_item = 0.66; Standard_item = 2.3 | The Standard_item is the IPCC's number — the comparison is run on the opponent's scale. |
| LS | an UPPER BOUND in our estimation | bound.n | — | — | **(gap)** (`Boundary` exists for physical limits; `Limitation` for abstract ones.) |
| LS | about 3.5 times SMALLER than … PROJECTED by the IPCC | project.v | — | — | **(gap)** for the forecasting sense (only project.n → `Project`). forecast.v → `Predicting`. |
| FR | The UNABATED warming | unabated | — | — | **(gap)** |
| FR | is powerful EVIDENCE that we can EXPECT further temperature increase | evidence.n; expect.v | `Evidence`; `Expectation` | Support = the unabated warming; Proposition = further increase; Cognizer = we | "powerful" fills the Degree of `Evidence`. |
| FR | emphasizing the URGENCY | urgency.n | — | — | **(gap)** — no FrameNet frame for time pressure as such. |
| FR | of CONFRONTING the human INFLUENCE on the climate | confront.v; influence.n | `Confronting_problem` **or** `Hostile_encounter`; `Objective_influence` | Agent = we; Issue = the human influence — or Side_1 = we; Side_2 = the human influence | FrameNet lists confront.v in both frames; the sentence does not disambiguate. |
| FR | PROVING that global warming is showing no SIGNS of SLOWING DOWN | prove.v; sign.n; slow down | `Evidence`; `Sign`; `Change_event_duration` | Support = the analysis; Proposition = no slowing; Indicator = (none); Indicated = slowing; Event = global warming | prove.v is the strongest LU in `Evidence`. |
| FR | further increases are to be EXPECTED | expect.v | `Expectation` | Cognizer = (unexpressed) | |

**What Mode A gave for Pair 2.** The two evaluative keywords — *alarming* and *urgency* — are handled unequally: FrameNet locates "alarming" precisely (a `Stimulus_focus` adjective in a lexical family whose base is a noise-making warning device) and has nothing for "urgency". It also shows the one place the two sides use the same frame with opposite force: `Evidence`. Loehle's "clearly detected" and Foster's "powerful evidence … proving" are both strong-certainty uses; neither side hedges at the headline level. And it flags the latent adversary in "confronting": FrameNet gives both the problem-solving and the hostile reading, which is exactly the ambiguity a listener resolves by prior allegiance.

### Mode B — frames, metaphors, construal, scenario

**LS: the ALARM script and the concede-then-deflate move.** "Not alarming" presupposes the scenario in which an alarm is rung: danger → bell → response. By negating the adjective, the authors cast the IPCC number as the alarm and their own as the all-clear; the lexical base (the bell) is also what makes "alarmist" an available epithet for the other side — one who rings the bell without cause. Entailment pressed: a lower rate is less dangerous. Entailments hidden: (a) the two numbers are different kinds of quantity — 0.66 is a rate fitted to the post-1942 residual of a past record, 2.3 is a projected rate for the early twenty-first century under an emissions scenario — and the comparison treats them as commensurable; (b) "alarming" is about consequences and thresholds, not rates as such, so the frame converts a magnitude into a feeling without stating what level of warming would warrant the bell; (c) the sentence's own hedge, "upper bound in our estimation", pushes the estimate down further by the same construal (urban heat and land-use effects counted as contaminants of the human signal rather than as part of it). The headline (LS-2) is a textbook concession frame: grant the opponent's strongest word ("Clearly Detected"), then deflate the quantity in a parenthesis with an exclamation mark — the reader keeps the concession as a sign of fairness and the deflation as the news. Note what the concession commits the speaker to: a human effect on climate, clearly detected. A sceptical friend quoting this paper has, in the paper's own headline, conceded attribution.

**FR: UNABATED FORCE, TIME PRESSURE, and the latent ADVERSARY.** "Unabated" construes warming as a force that has not let up (Talmy's force dynamics: an agonist whose tendency toward motion persists against whatever resists it). "Urgency" imports a deadline — a `Required_event` with a closing window — that the paper does not contain; its result is that the 1979–2010 trend rate did not change once three fluctuations were removed. "Confronting the human influence" puts "the human influence" in the Issue role of `Confronting_problem`, but FrameNet's second reading, `Hostile_encounter`, is live: the human influence as an opponent to be faced down. Entailment pressed: warming has not slowed, therefore it will continue, therefore delay is costly, therefore act now. Entailments hidden: each "therefore" needs a premise not in the paper — persistence of the forcing, the harms of further warming, the cost of acting now rather than later. The press release moves from a statistical finding to a policy stance in one sentence, and the publisher's lede (FR-8) hardens "strong evidence" into "proving" and "the true global warming trend", the same escalation Koonin later called a "long game of telephone" (`climate-science-evolution/08`, §4).

**Construal.** LS profiles a ratio (3.5 times smaller) and backgrounds the unlike kinds of the two numbers. FR profiles persistence ("no signs of slowing down") and backgrounds the pre-specified linear form that persistence was measured against. Both convert a finding about the *past* record into a stance about the *future* — LS by forecast ("may remain approximately steady until 2030-2040"), FR by expectation ("we can expect further temperature increase in the next few decades") — and neither headline marks the step.

**Scenario / narrative.** The two sentences end the same narrative differently. Both accept, in Deborah Stone's terms, an *inadvertent* causal story (humans cause warming without intending to — "human influence" on both sides); the dispute is about magnitude and tempo, not causation. From there Loehle's moral is "the bell is false; no remedy needed" and Foster's is "the bell is ringing; confront the cause." Each sentence performs Entman's problem-definition, causal diagnosis, moral judgment and remedy in under thirty words, which is why each lands as a verdict rather than a finding.

### Substance notes (not framing)

Loehle & Scafetta's 0.66 °C/century is the slope of a residual after subtracting fitted cycles; it is an estimate of the anthropogenic rate only if the cycles are correctly attributed to nature and the pre-1950 record is free of a human contribution (the "upper bound" claim then rests on treating UHI and land-use effects as non-anthropogenic, which is itself a construal). The IPCC's 2.3 °C/century is not a comparable quantity: it is a scenario projection for the early twenty-first century, not a fit to the past. Foster & Rahmstorf's finding — that the 1979–2010 trend rate shows no change once ENSO, volcanic and solar fluctuations are removed — is well supported for its window. Whether the underlying rate changed over roughly 1998–2013 became the "hiatus" debate, in which both positions were argued in the literature; that record is the place to check it (`climate-science-evolution/02-problems/P08`), not this file. "Urgency", however, is a policy inference the paper does not make and its data cannot make alone.

### Second looks

*If a friend says:* "Even that paper found only 0.66 degrees a century — a third of what the IPCC says. That's not alarming."

> Two things are being compared as if they were the same kind of number: a slope fitted to the past (after taking out cycles the authors chose) and a projection of the next few decades under rising emissions. "Not alarming" is a bell metaphor — it presupposes someone rang a false alarm — but rates alone don't say where the danger line is; what level of warming would you count as alarming, and how fast is the estimated rate rising? And one thing worth noticing in the paper's own headline: "Human Effect on Climate Clearly Detected." The disagreement is about how much, not whether.

*If I say (or a mainstream friend says):* "Warming hasn't slowed at all once you account for natural variability — which shows how urgent it is to act."

> The finding is narrower than the sentence: between 1979 and 2010, with three known fluctuations removed, the warming rate didn't change. "Urgent" adds a deadline the analysis doesn't contain, and "confronting human influence" casts the cause as an opponent; a sceptical friend hears the policy, not the statistics. The step from "the trend persisted" to "act now" needs premises about future emissions, harms and costs — worth stating rather than smuggling in a word.

---

## Pair 3 — The opponent: "fake skeptics" and "trick graphics" vs. "a trick to fool the ignorant"

### The statements

FR side (Foster, 2011-12-06; Rahmstorf, 2012-09-27):

> Fake "skeptics" like to claim that mainstream climate scientists ignore everything but greenhouse gases […] fluctuations which are often exploited by fake skeptics […] (FR-1)

> And, it should put an end to real skeptics claiming that global warming has recently stopped or slowed down, because real skeptics base their beliefs on evidence. I don't expect it will have much effect on the behavior of fake skeptics. (FR-4)

> […] numerous false claims of silly things like "global warming stopped in 1998" […] meaningless statements about "no statistically significant warming for 15 years" (or 10 years, or 7, or since last Thursday). (FR-5)

> The so-called "climate sceptics" have an arsenal of misleading graphics with which the human influence on climate is to be played down […] (FR-10)

> It takes quite something to make, from the data shown, a graphic that deceives the layperson [*dem Laien vorgaukelt*] […] Anyone peddling this graphic has taken leave of any serious factual discussion and taken the path of deception. (FR-11)

> The layperson is amazed and the expert wonders: how can someone who presents himself as a scientist […] work with such con-man tricks [*Bauernfängertricks*]? (FR-12)

> […] The Register attacked it. We must be doing something right. […] commenters at their site want to torpedo the truth. (FR-13)

LS side (Scafetta, 2012-03-11):

> However, it is a trick to fool people with no statistical understanding to claim that by associating a huge error range to a model, the model is validated. (LS-8)

> Every smart person would understand that this is another skepticalscience's trick to fool the ignorant. (LS-9)

> My critics at skepticalscience are simply trying to hide the failure of the IPCC models […] So, skepticalscience employed a childish trick of pulling a too small coversheet from a too large bed. (LS-10)

> […] to take his unfair and unprofessional comments with the proper skepticism. (LS-13)

### Mode A — FrameNet-literal annotation

| Side | Span | Target | FrameNet frame | Frame elements | Note |
|---|---|---|---|---|---|
| FR | FAKE "skeptics" / REAL skeptics | fake.a; real.a | `Artificiality` | Entity = the people; Reference_category = skeptic | Both poles of one frame, used to partition a group. |
| FR | real skeptics base their beliefs on EVIDENCE | evidence.n | `Evidence` | Support = evidence; Proposition = their beliefs | Supplies the membership criterion for the Reference_category. |
| FR | "skeptics" / SKEPTICISM (LS-13) | skeptic.n; skepticism.n | `Certainty` | Cognizer; Content (doubted) | Both sides claim the word. |
| FR | like to CLAIM … FALSE CLAIMS … MEANINGLESS STATEMENTS | claim.v; false.a; statement.n | `Statement`; `Artificiality`/`Correctness`; `Statement` | Speaker = fake skeptics; Message = … | "false" is itself an `Artificiality` LU. |
| FR | EXPLOITED by fake skeptics | exploit.v | — | — | **(gap)** |
| FR | SO-CALLED "climate sceptics" | so-called.a | `Being_named` | Entity = them; Name = climate sceptics | Flags the Name as only a name — the German *sogenannte* does the same work as Foster's scare quotes. |
| FR | an ARSENAL of MISLEADING graphics | arsenal.n; mislead.v | `Weapon`; `Prevarication` / `Intentional_deception` | Weapon = graphics; Speaker/Deceiver = sceptics; Addressee/Victim = (readers) | ARGUMENT IS WAR, with graphics as weapons. |
| FR | PLAYED DOWN | play down.v | — | — | **(gap)** |
| FR | DECEIVES the layperson [*vorgaukelt*] | deceive.v | `Intentional_deception` | Deceiver = the graphic's maker; Victim = the layperson; Topic = CO2 vs. sun | The German verb adds the conjurer (*Gaukler*). |
| FR | PEDDLING this graphic | peddle.v | — | — | **(gap)** (Commerce frames cover sell.v; peddling adds the itinerant hawker.) |
| FR | the PATH of DECEPTION | path.n; deception.n | `Path_traveled`; `Prevarication` / `Deception_success` | Theme = the peddler; Path = deception | LIFE/CONDUCT IS A JOURNEY; a moral path chosen. |
| FR | CON-MAN TRICKS [*Bauernfängertricks*] | trick.n | — (trick.v → `Intentional_deception`, `Manipulate_into_doing`) | Manipulator = Vahrenholt/Watts; Victim = the public | **(gap)** for the noun; the verb's frames fit. The German names the con-man explicitly. |
| FR | The Register ATTACKED it … TORPEDO the truth | attack.v; torpedo.v | `Attack` / `Judgment_communication`; (no LU) | Assailant = The Register; Victim = the paper | FrameNet lists attack.v in both the physical and the verbal frame — the sentence rides the ambiguity. |
| LS | a TRICK to FOOL people with no statistical understanding | trick.n; fool.v | `Intentional_deception` / `Manipulate_into_doing` / `Prevarication` | Deceiver = skepticalscience; Victim = people with no statistical understanding; Topic = model validation | fool.v is listed in all three deception frames. |
| LS | another skepticalscience's TRICK to FOOL the IGNORANT | trick.n; fool.v | same | Victim = the ignorant | The Victim is named by a deficit. |
| LS | trying to HIDE the FAILURE of the IPCC models | hide.v; failure.n | `Hiding_objects`; `Success_or_failure` | Agent = my critics; Hidden_object = the failure | Agentive hiding (vs. Foster's non-agentive `Eclipse` for what hides *his* signal). |
| LS | a CHILDISH trick of pulling a too small coversheet from a too large bed | childish.a | — | — | **(gap)** An evaluation of the Deceiver; the image is proverb-shaped: a cover that cannot stretch — each adjustment uncovers something else. |
| LS | the IPCC models … do not belong to the REALM of SCIENCE (LS-11) | realm.n | `Political_locales` | Locale = science | FrameNet has only the literal sense (a kingdom); the use is metaphorical: science as a bounded territory with members and outsiders. |
| LS | his UNFAIR and UNPROFESSIONAL comments … the proper SKEPTICISM | unfair.a; skepticism.n | `Fairness_evaluation`; `Certainty` | Evaluee = Svalgaard's comments; Cognizer = readers | Scafetta claims the skeptic virtue for his side's reading of a critic. |

**What Mode A gave for Pair 3.** This is where literal annotation is strongest. The deception vocabulary on both sides lands in the same small cluster — `Intentional_deception`, `Prevarication`, `Manipulate_into_doing` — whose core roles are Deceiver, Victim and Topic, and it shows that each side fills them identically: Deceiver = the other side's bloggers; Victim = the lay reader (*der Laie*; "people with no statistical understanding"; "the ignorant"); Topic = how a graph should be drawn. It also shows that the category word *skeptic* is claimed by both sides through the same frame, `Certainty`, with `Artificiality` (fake/real/false/so-called) used by the FR side to police the boundary and `Fairness_evaluation` plus "the proper skepticism" by the LS side to reclaim it. And it catches one real asymmetry inside the symmetry: when Foster says what obscures *his* signal he uses a non-agentive frame (fluctuations "make … less clear"); when Scafetta says what obscures *his* finding he uses an agentive one ("trying to hide"). Both attribute agency to the other side's *people*; only one attributes it to the other side's *data*.

### Mode B — frames, metaphors, construal, scenario

**The shared frame: DECEPTION, with the GRAPH as the stage.** Both sides are arguing about how to draw a picture — baseline period, width of an uncertainty envelope, annual versus monthly values, the scaling of a CO₂ axis against temperature — and both describe the other side's drawing choices as a trick on the public. The DECEPTION frame has a cast (Deceiver, Victim, Topic, Means) and one strong entailment: *intent*. A deceiver acts "so that" the victim misunderstands. Applied to a graphing choice, the frame converts a contestable convention into a lie. What it hides is the possibility the frame has no role for: honest disagreement about presentation. Each of the disputed choices has arguments on both sides (a baseline matched to the calibration period versus to the comparison period; a 1σ envelope versus 2σ; whether to show monthly satellite data with its larger variance), and none of them is settled by the word "trick".

**The con-man ICM.** Rahmstorf's German is more specific than the English: *Bauernfängertricks* (a swindler who catches rubes), *vorgaukeln* (a conjurer's illusion), *hausieren gehen* (to hawk door to door). Scafetta's English reaches the same idealized cognitive model from the other side: "illusion trick", "fool the ignorant", "childish trick", critics who "hide" a failure. The ICM supplies a smart deceiver, a naïve mark, and a hidden mechanism — and it supplies the speaker's own role: the one who sees through the trick on the mark's behalf. Both authors address "the layperson" / "readers … with modest scientific knowledge" explicitly as the party to be protected.

**The category contest over *skeptic*.** Foster: the Reference_category is "someone who bases beliefs on evidence" — the scientific-virtue sense — and the other side are "fake" members of it; the scare quotes and Rahmstorf's *sogenannte* mark the name as a mere name (`Being_named`). Scafetta: the virtue is reclaimed by asking readers to apply "the proper skepticism" to a critic. Each side keeps the honorific for itself and denies it to the other, which is why the word settles nothing and inflames reliably.

**War and sport.** Rahmstorf's "arsenal" of graphics (ARGUMENT IS WAR), Foster's "attacked" and "torpedo the truth", Watts's "beating the pants off" (LS-12; FIGHT/SPORT), Scafetta's models that "cannot compete". The frames give the exchange sides, weapons and a scoreboard, and they make a graph a projectile. Within them, criticism of one's own work is read as evidence of being right ("We must be doing something right" — FR-13), a move available to either side and immune to content.

**Metonymy.** "skepticalscience", "Watts", "Leif", "the IPCC models", "Vahrenholt" each stand for a position; a person or site becomes the argument, which lets the deception frame attach to a person rather than to a claim.

**Scenario / narrative.** Both posts carry a complete cast and a moral, and each imports its side's master narrative. Rahmstorf: villain = Watts and Vahrenholt (a "former RWE manager" — the fossil-industry link stated), victim = *der Laie*, hero = "we show what the graphic would look like if done correctly", moral = the tobacco playbook quoted from Ed Markey ("discredit, deny, and delay") — the *Merchants of Doubt* narrative. Scafetta: villain = skepticalscience, Svalgaard and the IPCC models, victim = readers with "modest scientific knowledge", hero = "my empirical model … a full forecast since Jan/2000", moral = the models "do not belong to the realm of science" — the manufactured-consensus narrative. In each case the frame analysis of a single sentence leads straight to the master story the sentence is a scene from; the sentence is understood by its readers as that scene.

### Substance notes (not framing)

The frame symmetry here is close to exact, but the substantive disputes under it are not equivalent, and some are decidable. Scafetta's claim that "in statistics it is 1-sigma envelope width that is used; not 2-sigma or 3-sigma" is wrong as a general statement: a 1σ band covers about 68% of a Gaussian spread, and testing whether observations fall outside a model's spread conventionally uses a wider interval; SkepticalScience's point about envelope width is standard, whatever one thinks of its baseline. Scafetta's baseline argument (align over the models' calibration period) is a defensible convention with a stated rationale, as is the alternative (align over a common recent reference period); neither is a trick. Rahmstorf's redrawing of the Watts widget rests on a scaling argument (100 ppm CO₂ ≈ 0.8 °C of transient response) that he states and sources; the Watts widget's choice of axes is a presentation choice he is entitled to call misleading, and whether it was *intended* to mislead is exactly what the deception frame asserts without evidence. Foster's "silly things like 'global warming stopped in 1998'" is correct about the 1998 El Niño spike as a cherry-picked start point; "since last Thursday" is ridicule, which the frame analysis records as register, not as substance.

### Second looks

*If a friend says:* "SkepticalScience just plays tricks with the baseline and the error bars to hide how badly the models are doing."

> "Trick" and "hide" say the choice was made to deceive you. Baseline and envelope width are conventions with arguments on each side — matching the models' calibration period versus a recent reference period; one standard deviation versus two — so the question is which convention the comparison should use and why, not whether someone is a con artist. It may help to know the same frame is in use against your side, word for word: "trick graphic", "con-man tricks", "deceives the layperson". That doesn't tell us who's right about the graph; it tells us the word "trick" is carrying the argument.

*If I say (or a mainstream friend says):* "Those fake skeptics push the same misleading graphs over and over — it's straight out of the tobacco playbook."

> "Fake" takes the word "skeptic" away from them, and the playbook casts them as paid deceivers; both land as claims about the person, and a friend will defend the person before the graph. The graph itself has specific choices — axis scaling, monthly versus annual values, which temperature record — and each can be argued on its merits without the word "misleading". And the same deception frame is being used against us, with the roles reversed; the structure is identical even where the substance is not.

---

## After three pairs: what the two modes gave, and what to do next

**Mode A (FrameNet-literal) earned its place, within a boundary.** It is exact, checkable, and it produced findings I would not have reached by reading: that "pause" evokes a frame with an Agent slot and a built-in resumption; that "valid" is at base a normative word; that *alarming* sits in a lexical family whose base is a warning bell; that both sides' deception vocabulary lands in one three-frame cluster with identical role assignments; that "man-made" is the `Artificiality` frame's own criterion applied to warming. Its boundary is sharp: FrameNet has nothing for the technical vocabulary — fit, filter, factor out, signal, noise, trend, cycle, oscillation, model, attribution, forcing, urgency, circular (reasoning) — and those are the words that carry each side's claim about method. So Mode A is strong on the *social and epistemic* layer of a statement (who is cast as what; how certain; how authentic) and silent on the *technical* layer, where the inferential work is done by domain scripts that have to be written by hand.

**Mode B did the inferential work.** The entailments-pressed / entailments-hidden analysis, the hand-built scenario frame (DECOMPOSITION BY SUBTRACTION), construal (what is profiled and backgrounded; where agency is placed), and the cast-and-moral reading of narrative are what produced the second looks. Mode B is also where the risk lies: it is interpretive, and the "did they say it?" rule has to be enforced word by word.

**Proposal for the protocol (see `method/unpack-protocol.md`).** Use Mode A as a first pass — a quick lexical scan for the frames that FrameNet does cover, because it is cheap and it catches the loaded social vocabulary before the analyst's own allegiance does — and Mode B for the method and inference layer. The second look is then written from both. A friend's paraphrased claim rarely needs the full table; it needs the one frame that is carrying the argument, named plainly, and one alternative construal of the same facts.

**Queued for this case.** P4 (the contest and its scoring; "pause") and P5 (nature and humans as causes). P4 should be folded into the "pause/hiatus" case, where the record (`climate-science-evolution/02-problems/P08`) can be brought to bear.

**Open questions for Steve.**

1. Is the second-look register right — length, tone, the explicit "the same frame is in use against your side" move? That move is the heart of the symmetry rule, but it can read as a dodge if the friend wants a verdict.
2. Should the Substance notes stay inside the case files, or move to a separate place so that the framing analysis is never read as a verdict (and vice versa)?
3. Mode A tables are long. Keep them in full for the record, or summarize to the frames that mattered and keep the full tables in an appendix?
