# FrameNet 1.7 frames used in frames-metaphors annotations

Generated from the FrameNet 1.7 release as distributed with NLTK (`framenet_v17`), Berkeley FrameNet, ICSI. Frame and FE definitions are FrameNet's own text, lightly whitespace-normalized; FE definitions are truncated. Regenerate with `python3 scripts/fn_dump.py <Frame ...> > framenet/framenet-frames-used.md` (the frame list used is in the file name order below).

## Artificiality  (frame id 1660)

An Entity is evaluated for whether or not it belongs to a particular Reference_category in a context where its category membership is doubtful. The criterion or criteria that are relevant to evaluating Reference_category membership depend on the individual lexical units and/or on the context. Typically, either the material composition of the Entity, its method of creation, or the identity (and proper authority) of its creators are critical for proper category membership. Note that Entity also covers behaviors. 'It can be hard to get your money back after discovering you've bought a bogus autograph for hundreds or thousands of dollars! ' 'It can be hard to get your money back after discovering you've bought a BOGUS autograph for hundreds or thousands of dollars! ' 'A bogus policeman pulling over motorists was arrested after stopping a car carrying four real officers.' 'A BOGUS policeman pulling over motorists was arrested after stopping a car carrying four real officers.' 'You people are pretty thick if you think you have evidence to prove that the moon landing was fake.' 'You people are pretty thick if you think you have evidence to prove that the moon landing was fake.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The Entity that is being evaluated in terms of whether it is an instance of the Reference_category. 'The bomb found at the US Embassy in Berlin was fake.' |
| Reference_category | Core | The type relative to which the Entity is evaluated. |
| Degree | Peripheral | The extent to which the Entity seems to belong (or not, if so specified by the lexical unit) to the category of the Reference_category is clear. Typically, this frame element is realized as an end-of-scale expression. … |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Artificiality
- ReFraming_Mapping: Feigning → Artificiality
- Using: Artificiality → Forging

**Lexical units** (14): actual.a, artificial.a, bogus.a, counterfeit.a, disingenuous.a, ersatz.a, fake.a, false.a, genuine.a, phoney.a, phoney.n, pseudo.a, real.a, true.a

## Being_named  (frame id 228)

This frame concerns entities conventionally being referred to by particular names. 'Her name was Lola.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The Entity is the person the speaker intends to refer to by using a particular name. 'You have an unusual surname.' |
| Name | Core | Name identifies the linguistic expression used to refer to Entities. 'My name is Bond.' |
| Context | Peripheral | The context is the region or domain in which the name applies. 'The Spanish name 'Juan' begins with an English 'w'.' |
| Descriptor | Extra-Thematic | Describes the Name in some manner. 'His favorite nickname is 'The Dark Knight'.' |
| Etymological_root | Extra-Thematic | The source language or inspiration for the Name. 'His name in Spanish is 'Santiago', from the Latin.' |
| Language | Peripheral | Language is used for a person or thing to whose name the Name of the Entity is taken or in honor of. 'Spanish and Indian names were precedents to other non-English-sounding names.' |
| Type | Peripheral | The FE Type denotes sub-type of names. 'My given name used to be John.' |

**Frame relations** (super → sub)

- Causative_of: Name_conferral → Being_named
- Inheritance: Being_named → Appellations
- ReFraming_Mapping: Being_named → Namesake
- ReFraming_Mapping: Being_named → Referring_by_name
- Using: Being_named → Namesake
- Using: Being_named → Referring_by_name

**Lexical units** (46): Christian name.n, agnomen.n, aka.a, alias.n, allonym.n, also known as.a, brand name.n, by-name.n, caconym.n, codename.n, codenamed.a, cognomen.n, designated.a, entitled.a, eponym.n, family name.n, first name.n, forename.n, full name.n, given name.n, go.v, known.a, last name.n, maiden name.n, married name.n, metronymic.n, middle name.n, misnomer.n, moniker.n, name.n, named.a, nameless.a, nee.a, nickname.n, nom de guerre.n, nom de plume.n, patronymic.n, pen name.n, pet name.n, praenomen.n, pseudonym.n, so-called.a, soubriquet.n, stage name.n, surname.n, trivial name.n

## Certainty  (frame id 141)

This frame concerns a Cognizer's certainty about the correctness of beliefs or expectations. It only includes uses where a Cognizer is expressed. 'Lermontov was certain he would come to the party.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The Cognizer is the person whose certainty or uncertainty is at issue. 'Marcel was sure that she had seen Eldridge on the balcony.' |
| Content | Core | The Content denotes the mental content that the Cognizer is certain or uncertain about. 'I am sure that we'll arrive on time.' |
| Expressor | Core | The Expressor is the body part or action by a body part that conveys the mental state of the Cognizer. 'She caught sight of her mother's dubious expression.' Notice that we do NOT tag possessives such as 'her mother's' … |
| Topic | Core | The Topic is the entity that a Cognizer has a certain/uncertain belief about. 'She talked of quests , of finding this absurd religious character , but he was unsure of her conviction.' 'I 'm dubious about this Mafia … |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Degree | Peripheral | This FE indicates the Degree to which the Cognizer is certain or uncertain. 'Charles felt fairly confident of her safety for the time being.' |
| Explanation | Extra-Thematic | The reason for which the Cognizer is certain. |
| Manner | Peripheral | The FE Manner denotes the manner of the certainty or uncertainty. |

**Frame relations** (super → sub)

- Inheritance: Certainty → Trust
- Inheritance: Gradable_attributes → Certainty
- ReFraming_Mapping: Certainty → Likelihood
- See_also: Awareness → Certainty
- Using: Awareness → Certainty
- Using: Certainty → Reliance_on_expectation

**Lexical units** (20): believe.v, certain.a, certainty.n, confidence.n, confident.a, convinced.a, doubt.n, doubt.v, doubtful.a, dubious.a, know.v, positive.a, skeptic.n, skeptical.a, skepticism.n, sure.a, trust.v, uncertain.a, uncertainty.n, unsure.a

## Statement  (frame id 43)

This frame contains verbs and nouns that communicate the act of a Speaker to address a Message to some Addressee using language. Instead of (or in addition to) a Speaker, a Medium may also be mentioned. Likewise, a Topic may be stated instead of a Message. A number of the words can be used performatively, such as declare and insist. 'I now declare you members of this Society.' 'She said that I would be late .' 'The announcement about raffle winners came across the loudspeaker.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Medium | Core | Medium is the physical entity or channel used by the Speaker to transmit the statement. 'Kim preached to me over the phone.' |
| Message | Core | The Message is the FE that identifies the content of what the Speaker is communicating to the Addressee. It can be expressed as a clause or as a noun phrase. 'Evelyn said that she was not ready to leave.' 'Evelyn … |
| Speaker | Core | The Speaker is the sentient entity that produces the Message (whether spoken or written). It is normally expressed as the External Argument of predicative uses of the target word, or as the Genitive modifier of the … |
| Topic | Core | The Topic is the subject matter to which the Message pertains. It is normally expressed as a PP Complement headed by "about", but in some cases it can appear as a direct object. 'Evelyn spoke candidly about her past.' … |
| Addressee | Extra-Thematic | The Addressee is the person to whom the Message is communicated. When this FE is expressed, it often appears in a prepositional phrase introduced by "to", or as a direct object. 'Evelyn reported to me about what … |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the Message is expressed (often denoted by words such as "officially," "formally," "technically," etc.). |
| Containing_event | Extra-Thematic | This FE identifies an event during which the Speaker produces the Message. |
| Degree | Extra-Thematic | This FE selects some gradable attribute and modifies the expected value for it. |
| Depictive | Extra-Thematic | The state of the Speaker during the Message. 'Let's see if you say that sober!' |
| Event_description | Extra-Thematic | This FE describes the Message event. |
| Frequency | Extra-Thematic | This FE is defined as the number of times an event occurs per some unit of time. |
| Group | Extra-Thematic | The Group of Speakers or Mediums within which the Message is made. 'Much would be achieved if these were more widely acknowledged.' |
| Internal_cause | Extra-Thematic | The emotional or physical state of the Speaker that leads to their speaking. 'He wrote in bitterness of the treatment the Malloreans had given him.' |
| Iterations | Extra-Thematic | The FE Iterations is used for expressions that indicate the number of times an event or state (of the kind denoted by the target in its clause) has taken place or held. |
| Manner | Peripheral | The Manner of performing an action. |
| Means | Peripheral | An act whereby the Speaker makes a Message. 'Bilio commented on the paper by scrawling innumerable post-its in a range of colors and sticking them all over it.' |
| Occasion | Extra-Thematic | The Occasion is the reason a public Message is given. 'The New Year address was well received.' |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE indicate that the particular Message event referred to is conceived as embedded within an iterated series of similar events or states. Most expressions of … |
| Place | Peripheral | The FE specifies the location where the Message takes place. 'In some remarks at the National Press Club, Mr. Keating said he would make a better prime minister tha nMr. Hawke.' |
| Time | Peripheral | The Time at which the Message is made. |

**Frame relations** (super → sub)

- Inheritance: Statement → Affirm_or_deny
- Inheritance: Statement → Complaining
- Inheritance: Statement → Predicting
- Inheritance: Statement → Reading_aloud
- Inheritance: Statement → Recording
- Inheritance: Statement → Reveal_secret
- Inheritance: Statement → Telling
- ReFraming_Mapping: Body_movement → Statement
- ReFraming_Mapping: Categorization → Statement
- ReFraming_Mapping: Encoding → Statement
- ReFraming_Mapping: Speak_on_topic → Statement
- ReFraming_Mapping: Statement → Affirm_or_deny
- ReFraming_Mapping: Statement → Bragging
- ReFraming_Mapping: Statement → Commitment
- ReFraming_Mapping: Statement → Complaining
- ReFraming_Mapping: Statement → Encoding
- ReFraming_Mapping: Statement → Expressing_publicly
- ReFraming_Mapping: Statement → Reveal_secret
- ReFraming_Mapping: Statement → Speak_on_topic
- ReFraming_Mapping: Statement → Successfully_communicate_message
- ReFraming_Mapping: Statement → Telling
- ReFraming_Mapping: Statement → Translating
- Using: Communication → Statement
- Using: Statement → Adducing
- Using: Statement → Attributed_information
- Using: Statement → Chatting
- Using: Statement → Judgment_communication
- Using: Statement → Renunciation
- Using: Statement → Unattributed_information

**Lexical units** (79): acknowledge.v, acknowledgment.n, add.v, address.v, admission.n, allegation.n, allege.v, allow.v, announce.v, announcement.n, assert.v, assertion.n, attest.v, aver.v, avow.v, avowal.n, be like.v, caution.n, caution.v, challenge.v, claim.n, claim.v, comment.n, comment.v, concession.n, confirm.v, conjecture.n, conjecture.v, contend.v, contention.n, declaration.n, declare.v, denial.n, describe.v, detail.v, exclaim.v, exclamation.n, explain.v, explanation.n, gloat.v, hazard.v, insist.v, insistence.n, maintain.v, mention.n, mention.v, message.n, note.v, observe.v, pout.v, preach.v, proclaim.v, proclamation.n, profess.v, promulgation.n, pronounce.v, pronouncement.n, proposal.n, propose.v, proposition.n, reaffirm.v, recount.v, refute.v, reiterate.v, relate.v, remark.n, remark.v, report.n, report.v, say.v, smirk.v, speak.v, state.v, statement.n, suggest.v, talk.v, tell.v, venture.v, write.v

## Attention  (frame id 791)

This frame concerns a Perceiver's state of readiness to process and consider impressions of a Figure within a Ground. It is often unknown to the Perceiver whether or not the Figure exists within the Ground. Alternatively, the Expressor may be expressed as showing signs of the Perceiver's state of attentiveness. 'Legislator tells consumers to be alert to dioxin levels.' 'They demand an attentive gaze, a careful accounting of parts.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Expressor | Core | An entity (or event) associated with a Perceiver that gives evidence for a Perceiver's attentiveness. |
| Figure | Core | The entity that the Perceiver is specifically focussing on within the Ground. |
| Perceiver | Core | The individual that pays attention to the Ground. |
| Circumstances | Extra-Thematic | The situation within which the Perceiver is alert. |
| Degree | Peripheral | The amount of attention that the Perceiver is paying to the Figure or Ground. |
| Ground | Peripheral | The sensory field or subset of a sensory field that the Perceiver is attending to. |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), force (hard, softly), secondary effects (quietly, loudly), and general … |

**Frame relations** (super → sub)

- Inheritance: State → Attention
- ReFraming_Mapping: Awareness → Attention
- Using: Attention → Emotions_of_mental_activity
- Using: Attention → Perception_active
- Using: Attention → Searching_scenario

**Lexical units** (8): alert.a, attend.v, attention.n, attentive.a, close.a, closely.adv, ignore.v, keep an eye.v

## Causation  (frame id 5)

A Cause causes an Effect. Alternatively, an Actor, a participant of a (implicit) Cause, may stand in for the Cause. The entity Affected by the Causation may stand in for the overall Effect situation or event. '' Those frames that inherit the Causation frame have as their background the idea that some event is responsible for the occurrence of another event (or state). In the inheriting frame, typically an FE like Agent or Causer is proposed in the place of the Actor, but in the daughter frames, as in this frame, the Actor is semantically dependent on the idea of a Cause (an event or state-of-affairs) that the Actor is a participant in. Similarly, most inheriting frames profile only the Affected entity, not the full Effect situation which is often incorporated into the frame or the particular target. So, for example, paint.v in the Filling frame entails the final situation of something (the Affected) being covered in paint (the Effect). 'He made me angry.' 'If such a small earthquake causes problems, just imagine a big one!' 'The strange mutations of the rumor mill in the end led to it being said that he was actually a woman.' 'You 've made it impossible to continue!' 'The ending left me feeling kinda empty.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Actor | Core | An entity which participates in a Cause, perhaps volitionally and perhaps not. 'That one stone, apparently, caused the avalanche that engulfed square miles of forest.' 'Stephen Hawking caused an uproar when the results … |
| Affected | Core | Agents in a joint or reciprocal action (e.g. exchange) |
| Cause | Core-Unexpressed | A force, process, or event that produces an effect. 'The wind made the door rattle.' 'The accident caused them to be more careful the next time.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Effect | Core-Unexpressed | A positive or negative evaluation of the Phenomenon. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Frequency | Extra-Thematic | How often the action denoted by the target occurs. |
| Manner | Peripheral | Any holistic description of the event, including overall depictions (the same way) and descriptions pertaining to the Actor's influence on the character of the event (eagerly, quietly). |
| Means | Peripheral | An action through which the Actor or Cause accomplishes the action indicated by the target. |
| Place | Peripheral | Where the event takes place. |
| Time | Peripheral | This FE identifies the Time when the event occurs. |

**Frame relations** (super → sub)

- Inheritance: Causation → Cause_to_start
- Inheritance: Eventive_affecting → Causation
- Perspective_on: Causation → Means
- Perspective_on: Causation_scenario → Causation
- ReFraming_Mapping: Attempt_suasion → Causation
- ReFraming_Mapping: Causation → Subjective_influence
- ReFraming_Mapping: Suasion → Causation
- Using: Causation → Level_of_force_exertion

**Lexical units** (39): because of.prep, because.c, bring about.v, bring on.v, bring.v, causative.a, cause.n, cause.v, consequence.n, consequent.a, consequential.a, dictate.v, due to.prep, for.c, force.v, give rise.v, induce.v, lead (to).v, leave.v, legacy.n, make.v, mean.v, motivate.v, precipitate.v, put.v, raise.v, reason.n, render.v, responsible.a, result (in).v, result.n, resultant.a, resulting.a, see.v, send.v, since.c, so.c, sway.v, wreak.v

## Change_position_on_a_scale  (frame id 91)

This frame consists of words that indicate the change of an Item's position on a scale (the Attribute) from a starting point (Initial_value) to an end point (Final_value). The direction (Path) of the movement can be indicated as well as the magnitude of the change (Difference). The rate of change of the value (Speed) is optionally indicated. Another scale (Correlate), which the values are correlated with, is indicated if it is not the default correlate (namely, absolute time). '' The distinction between Attributes and Items is not always an easy one. The clear cases involve the expression of the Attribute in an in-PP. 'Hawke's Bay winery doubled in size last year.' 'The amount you can deduct, then, depends on whether or not the stock has increased in value during the period you have owned it.' Other clear cases of Attributes involve NP's like size, quality, number, value that denote abstract attributes rather than events or classes of things. '' The analysis is more complicated when an event-denoting noun phrase occurs as the subject and the sentence has no in-PP. In the simplest cases, where the Attribute is the number of occurrences of the event, the Attribute is usually left implicit, as in exx. 1 and 2, the Attribute below. '(1)Accidents increased 20% to 345.' '(1--second FE layer)Accidents increased 20% to 345.' '(2) Attacks on civilians decreased over the last 4 months DNI.' In cases like (1), we will tag the Attribute on the second layer below the Final_value label, as that FE makes it clear that the Attribute is simply cardinality. In cases like (2), we tag it as DNI because in context the hearer has to understand a particular Attribute rather than just some or any appropriate Attribute of the Item. Note that the above pattern can be compared to cases involving tangible Items, where the Attribute may similarly be missing when the incidence or frequency of the Item is specified. '(3) Woodland birds increasedto their highest level since 1990 DNI.' A more complicated case involving event-denoting subjects is when the Attribute measured is not the incidence of the type of event specified but rather an Attribute of an event-participant. In (4), it is not the number of times that turbot was caught that has changed but the amount of fish caught. '(4) Turbot catches increased from around 100 tonnes in the 1960s to around 1,200 tonnes in the mid 1990s.' '(4-second FE layer) Turbot catches increased from around 100 tonnes in the 1960s to around 1,200 tonnes in the mid 1990s.' (Note the 2nd layer annotation of the Attribute below the Initial_value and Final_value FEs, since they indicate that the Attribute is implicitly weight.) Similarly, in (5), the report is (in context) about the total monetary value of the gifts, not about the number of donations made. '(5)Overall Giving by Church Members increased from 2000 to 2001' As can be seen from the above examples, we consider the event nouns in uses such as (4) and (5) to also specify Items. Note that in cases like (4), we do not want to treat the subject NP "turbot catches" as an Attribute that includes information about the Item, since it would not make sense to restate (4) as follows: '*Turbot increased in catches.' Two more complications arise. First, certain nouns that do not, by their etymology, denote abstract attributes have a second sense in which they do denote an Attribute. '(6) The population of Smallville increased fourfold to 807.' Under one reading, (6a), the population could be understood as referring to "the people", in which case the Attribute cardinality is understood as unexpressed, as in (1), (2), and (3). The Attribute could be overtly specified: '(6a) The population of Smallville increased fourfold in size to 807.' Under another reading, (6b), population is an Attribute that habitats or locations possess. In this case, the whole NP "the population of Smallville" is treated as the Attribute and on the second layer "of Smallville" is tagged as Item. '(6b) The population of Smallville increased fourfold to 807.' '(6b-second FE layer) The population of Smallville increased fourfold to 807.' Support for the possibility of this second reading comes from the fact that you can also state the facts as in (6c). '(6c) Smallville increased fourfold in population to 807.' The last complication is that Initial_value expressions can also function as the subject, which superficially look like expressions of Attribute. '(7) The 1999 price had increased to $3400 by 2001.' '(7--second layer) The 1999 price had increased to $3400 by 2001.' There is no Attribute "1999 price" here (though the concept is plausible in certain special statistical contexts where prices are indexed to prices of a particular year). (7) simply reports that the value of the price-Attribute changed from whatever it was in 1999 to the new value of $3400 by 2001. For sentence (7), Attribute would only be indicated as "price" on the 2nd layer.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Attribute | Core | The Attribute is a scalar property that the Item possesses.'Oil rose in price by 2%.' |
| Difference | Core | The distance by which an Item changes its position on the scale.'Oil rose in price by 2%.' |
| Final_state | Core | A description that presents the Item's state after the change in the Attribute's value as an independent predication. 'It was never bad (1 or 2 seizures a year), but this past decade, it has increased to having them 1 … |
| Final_value | Core | The position on the scale where the Item ends up. 'Microsoft shares fell to 7 5/8.' |
| Initial_state | Core | A description that presents the Item's state before the change in the Attribute's value as an independent predication. 'Diesels have increased from having a 20% market share in 1995 to just over 30% in 2004.' |
| Initial_value | Core | The initial position on the scale from which the Item moves away. 'Microsoft shares fell from 12 3/8 to 7 5/8.' |
| Item | Core | The entity that has a position on the scale. 'I fear this service will diminish in quality.' |
| Value_range | Core | A portion of the scale, typically identified by its end points, along which the values of the Attribute fluctuate. 'The patient's temperature fluctuated between 28.5 and 29.5.' |
| Circumstances | Extra-Thematic | The Circumstances under which the change of position takes place. 'The eggs will only increase under pressure.' |
| Containing_event | Extra-Thematic | An event that occurs or state of affairs that holds at a time that includes the time during which the quantity change takes place and of which it is taken to be a part. 'Hong Kong : Buying by London institutions helped … |
| Correlated_variable | Extra-Thematic | The Correlated_variable is an ordered progression of positions or values (most often a sequence of spatial locations) that the (dependent) Attribute is measured against. The Correlated_variable is metaphorically mapped … |
| Degree | Peripheral | Degree to which event occurs |
| Duration | Peripheral | The length of time over which the change takes place. 'The amount of troops in the war will no doubt double over the next several years.' |
| Explanation | Extra-Thematic | The situation or state-of-affairs that results in the change in quantity described in this instance of the frame. 'Her panic had declined because I spent two hours explaining what you did !' |
| Final_correlate | Peripheral | The value, location, or state-of-affairs that corresponds to the Final_value of the Attribute. 'From Monterrey to southern Oregon, tree height increases steadily in this species to a stunning 50 meters.' |
| Group | Extra-Thematic | The Group in which an Item changes the value of a Attribute in a specified way.'Colon cancer incidence fell by 50 % among men over 30.''Net foreign debt has more than tripled in Africa over this decade.' |
| Initial_correlate | Peripheral | The value, location, or state-of-affairs that corresponds to the Initial_value of the Attribute. 'From Monterrey to southern Oregon, tree height increases steadily in this species to a stunning 50 meters.' |
| Manner | Peripheral | Manner of performing an action |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Path | Peripheral | Any expression that gives information about points on the scale that the Item traverses between the starting and ending point of its movement along the scale.'The price of oil moved up last month.' |
| Period_of_iterations | Extra-Thematic | The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | A location where Attribute is measured |
| Result | Extra-Thematic | Result. of an event |
| Speed | Peripheral | The rate of change of the Value.'Prices are rising by 2% a year.' |
| Time | Peripheral | The Time is the time-frame in which the change of position occurs. |

**Frame relations** (super → sub)

- Causative_of: Cause_change_of_position_on_a_scale → Change_position_on_a_scale
- Inchoative_of: Change_position_on_a_scale → Position_on_a_scale
- Inheritance: Change_position_on_a_scale → Change_of_temperature
- Inheritance: Change_position_on_a_scale → Proliferating_in_number
- Inheritance: Event → Change_position_on_a_scale
- ReFraming_Mapping: Traversing → Change_position_on_a_scale
- Using: Change_position_on_a_scale → Change_of_quantity_of_possession
- Using: Change_position_on_a_scale → Remainder

**Lexical units** (56): accelerated.a, advance.v, balloon.v, climb.v, contract.v, contraction.n, decline.n, decline.v, decrease.n, decrease.v, depressed.a, depression.n, diminish.v, dip.v, double.v, down.prep, drop.v, dwindle.v, edge.v, elevated.a, elevation.n, escalation.n, explode.v, explosion.n, fall.n, fall.v, fluctuate.v, fluctuation.n, gain.n, gain.v, grow.v, growing.a, growth.n, hike.n, increase.n, increase.v, increasingly.adv, jump.v, lower.v, move.v, mushroom.v, plummet.v, reach.v, rise.n, rise.v, rocket.v, shift.n, shift.v, skyrocket.v, slide.v, soar.v, swell.v, swing.v, triple.v, tumble.n, tumble.v

## Objective_influence  (frame id 1084)

An Influencing_entity, an Influencing_situation, or an Influencing_variable has an influence on a Dependent_entity, Dependent_situation, or a Dependent_variable. '' Compare to Subjective_influence. Words in Objective_influence are used to make claims about correlations in the world, where words in Subjective_influence are used to explain emotional impacts made on cognizers. 'More and more doctors realise that diet can influence disease.' 'Our subject is the body clock; how it influences our physiology and behaviour and how it interacts with the rhythms in our environment.' 'But it is more likely that a physical restraint influenced the swirling liquids.' 'It claimed, perhaps hollowly, that NT had yet to impact its business.' 'This kind of elementary boo-boo would certainly impact video speed.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Dependent_entity | Core | An entity, usually a thing, that is influenced in its behavior by an Influencing_entity or an Influencing_situation. 'The Committee is responsible for making recommendations to the Board regarding the group's … |
| Influencing_entity | Core | A thing or person whose behavior has an effect on an Dependent_entity, Dependent_situation, or Dependent_variable. ' Much of the acreage in this round is closer to the coastline, and as such has many implications in … |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Degree | Core-Unexpressed | The Degree to which the Influencing_entity effects the Dependent_entity. |
| Dependent_situation | Core-Unexpressed | A situation that whose temporal or other characteristics are influenced by an Influencing_entity, Influencing_situation, or Influencing_variable. 'The new network file system server line supports database or backup … |
| Dependent_variable | Core-Unexpressed | A scalar variable, whose value depends on the behavior of an Influencing_entity, a Influencing_situation, or an Influencing_variable. 'This kind of elementary boo-boo would certainly impact video speed.' |
| Descriptor | Extra-Thematic | A Descriptor gives additional information about the influence. It may be affecting, as with 'positive impact on GDP'; or not, as in 'potential (or possible) influence of SSRIs on metabolism'. Descriptors are typically … |
| Influencing_situation | Core-Unexpressed | A situation whose temporal or other characteristics have an effect on a Dependent_entity, Dependent_situation, or Dependent_variable. |
| Influencing_variable | Core-Unexpressed | A scalar variable (with unspecified value) which has an effect on the Dependent_entity, Dependent_situation, or Dependent_variable. ' Factors which influence the stability of the combination include the softness of the … |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including force (hard, softly), secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may also … |
| Place | Peripheral | The location at which the influencing occurs. |
| Time | Peripheral | The Time at which the influence occurs. |

**Frame relations** (super → sub)

- Inheritance: Event → Objective_influence
- Inheritance: Objective_influence → Control
- Inheritance: Objective_influence → Transitive_action
- See_also: Subjective_influence → Objective_influence

**Lexical units** (7): affect.v, effect.n, impact.n, impact.v, influence.n, influence.v, power.n

## Contingency  (frame id 900)

The answer to one open question, the Outcome, is dictated (partially or completely) by the answer to another open question, the Determinant, i.e. if the answer to the Determinant is known, the answer to the Outcome can be predicted. The Degree of predictive power and the Circumstances under which the dependency holds can also be expressed. 'Economic policy is partially a function of cultural values.' 'Well, that depends ... DNI' 'In Mediaeval times, status was dependent on birth.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Determinant | Core | An open question that determines the Outcome. 'Price, in such a case, depends only on the whim of the supplier.' |
| Outcome | Core | An open question that is (to some degree) predictable from the Determinant. |
| Circumstances | Extra-Thematic | The conditions under which the Determinant dictates the Outcome. Oftentimes it is expressed in a fashion similar to Time and Place in other frames, but such cases are actually metonymic for the prevailing conditions of … |
| Degree | Peripheral | The amount of predictive power supplied by the Determinant with respect to the Outcome. 'His decision was somewhat dependent on who won the game' |

**Frame relations** (super → sub)

- Inheritance: Contingency → Have_as_requirement
- Using: Contingency → Reliance

**Lexical units** (14): depend.v, dependence.n, dependent.a, depends.v, determine.v, dictate.v, factor.n, function.n, hang (on).v, hinge.v, independence.n, independent.a, turn.v, variable.n

## Being_in_effect  (frame id 1510)

A particular Binding_principle is (or is not) operative, that is, any obligations, restrictions, and any other aspects of the Binding_principle are (or are not) in effect. The Binding_principle can be expressed as being in effect for a particular Duration, or at a particular Time or Place, or under certain Circumstances. 'This law will only become in effect during the last three weeks of the year.' 'The statutory wetlands definition is effective immediately.' 'This contract is binding on all parties.' Although the in effect is properly in this frame, (put) into effect is analyzed in the Execute_plan frame. This is in part because to put an (evacuation) plan into effect is to actually execute the plan (to evacuate), while to put a plan in effect is to determine that in the future the plan may have to executed, i.e., to make the plan binding. Similar observations can be made for come into effect.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Binding_principle | Core | The Binding_principle is the law, contract, principle, or other (set of) obligations that is (or is not) operational. 'Once the treaty is in effect, US port authorities and the Coast Guard will monitor compliance by … |
| Circumstances | Extra-Thematic | The state-of-affairs under which the Binding_principle is/isn't operational. |
| Degree | Extra-Thematic | This frame element selects some gradable attribute and modifies the expected value for it. |
| Duration | Peripheral | The length of time for which the Binding_principle is or is not in effect. 'The contract will be effectivefor three fiscal years.' |
| Explanation | Extra-Thematic | A cause, reason, or other Explanation for the status of the Binding_principle 'Your contract is null because you left the county.' |
| Obligated_party | Peripheral | The individual or group who is obligated to follow the Binding_principle. 'This statute is in effect for holders of H-1 visas until January.' |
| Place | Peripheral | The Place at which the Binding_principle is or is not operational. 'This promotion is void in the state of Florida.' |
| Time | Peripheral | The Time at which the Binding_principle is in effect. 'All patent applicants and owners should be aware of the current uncertainty as to what patent fees will be in effect on October 1, 1998' |

**Frame relations** (super → sub)

- Inchoative_of: Come_into_effect → Being_in_effect
- See_also: Being_in_effect → Execute_plan
- Using: Being_in_effect → Enforcing
- Using: Obligation_scenario → Being_in_effect

**Lexical units** (7): binding.a, effect.n, effective.a, force.n, null.a, valid.a, void.a

## Correctness  (frame id 1512)

A particular piece of Information is evaluated for its accuracy. The Degree of correctness may also be expressed. The Source of information may also metonymically stand in for the Information. 'Is your reputation at risk due to incorrect information?' 'If your dealership service people make such totally wrong claims, I would be uncomfortable trusting their warranty claims too.' 'All users must verify the correctness of their own information.' 'We found all of his information to be right.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Communicative_act | Core | The event which communicates the Information. |
| Information | Core | The Information matches or does not match the facts of the world. 'That statement is totally incorrect.' |
| Source | Core | The Source is the agent who holds the correct/incorrect information. 'He is correct' |
| Topic | Core | The Topic about which the Source has accurate information. |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the target operates (often denoted by words such as "officially," "formally," "technically," etc.). |
| Degree | Peripheral | The degree to which the Information matches or does not match the facts of the world. 'Vague prophecies, interpreted with maximum latitude, are likely to appear at least somewhat accurate.' |
| Domain | Extra-Thematic | The aspect of reality which is accurately modeled by the Information. 'That claim may be factually accurate in terms of in vitro pharmacology but that may have no clinical relevance.' |
| Frequency | Extra-Thematic | How often the Information is correct. |
| Manner | Peripheral | The way in which the Source is correct/incorrect. |
| Medium | Peripheral | The physcial context that the Information is found in. |
| Parameter | Extra-Thematic | The aspect of the Information which accurately models reality. 'Don't select an option just because it contains factually correct information about the clinical situation.' |
| Re-encoding | Extra-Thematic | This FE presents the current frame as an integral part of a larger conceptualization expressed by another frame, which typically corresponds to a Means action within the frame. |
| Result | Extra-Thematic | The outcome of the correctness if the Source or Information. |
| Time | Peripheral | The Time at which the Information or the Source is correct. |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Correctness
- Using: Correctness → Verification
- Using: Information → Correctness
- Using: Similarity → Correctness

**Lexical units** (8): accurate.a, correct.a, correctness.n, exact.a, incorrect.a, right.a, true.a, wrong.a

## Estimated_value  (frame id 1516)

A Cognizer has carried out an approximate calculation or considered some Evidence and produced an approximation of the Value of a feature of an Item. There are two alternative construals in which the relationship between the feature and the Value is conceived. Either a holistic Estimation by the Cognizer is presented, or the Question that is addressed by the Cognizer's estimating is given. 'You can list a ballpark figure for shipping and handling.' 'Moreover, their estimate of 0.27 °C mean surface warming per century due to land-use changes is at least twice as high as previous estimates based on urbanization alone.' 'Our decision to trust people depends on our estimate of how trustworthy they are.' 'To help you anticipate the cost of your move, movers will give you an estimate of the price.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The individual who has considered evidence or performed calculations to produce the approximation. 'Her estimation was that they had exported up to 180000 fish.' |
| Estimation | Core | A proposition expressing the Cognizer's approximation of a feature's Value. 'One estimate was that eventually I had lost about 80% of my blood.' |
| Item | Core | The entity that possesses a feature whose Value the Cognizer has approximated. 'He's an engineer and he is supposed to know the estimate of the house.' |
| Question | Core | An open proposition for which the Cognizer has approximated the Value of a variable. 'Galliard decided Rwanda was different, and he went public with his estimate of how many people had been killed in a matter of two … |
| Value | Core | The position or area on the feature scale that the Cognizer has concluded the Item occupies. 'Sotheby 's estimate of its value was $10m-$14m.' |
| Evidence | Peripheral | Some fact perceived by the Cognizer which has contributed to their estimation of the Value. 'The habitat area based estimate is probably the more reliable projection of the two.' |
| Place | Peripheral | The location in which the Cognizer has formed their estimate. |
| Time | Peripheral | The time period during which the Cognizer formed the estimate. 'That is 30000 higher than last year's estimate of 2.65 million' |

**Frame relations** (super → sub)

- Using: Estimating → Estimated_value

**Lexical units** (3): ballpark figure.n, estimate.n, estimation.n

## Estimating  (frame id 1513)

A Cognizer carries out an approximate calculation or considers some Evidence so as to arrive at an approximate Value for some Feature of an Item. There are two alternative construals. In one, the Feature is presented as a Question about the Item and the Value is conceived as an answer to the Question. In the second construal, a fully propositional Estimation by the Cognizer is presented which expresses the result of the Cognizer's approximation. 'Until 1971, dolphin mortality could be estimated only from analyses of vessels ' logbooks -- and the figures are probably underestimates. CNI' 'The UK government estimates that there is sufficient gas in the UK sector to meet UK demand for some 17 to 35 years .' 'The astronomers estimated how much energy was needed to create the cavities by calculating the density, temperature and pressure of the hot gas.' 'The banner is estimated in value at $500. CNI' 'When Congress passed the Medicare bill in late 2003, the Congressional Budget Office estimated its cost at $395 billion over 10 years.' 'We estimated how much we had at around 12 thousand.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The individual who considers evidence or performs calculations to arrive at an approximation. 'The government estimated the cost of meeting EC water standards at £3-4 billion.' |
| Estimation | Core | A proposition expressing the Cognizer's approximation of a Feature's Value. 'At the time they estimated there to be as many as four million to the acre.' |
| Feature | Core | The feature is a scalar property of the Item. 'In one march from 42 Street down to Washington Square Park, the crowds were estimated in size from 125000 (NYPD estimate) to over 200000 (march organizers).' |
| Item | Core | The entity that possesses the Feature whose Value the Cognizer seeks to approximate. 'I estimated the house at about 60-65% full.' |
| Question | Core | An open proposition for which the Cognizer seeks to approximate the Value of a variable. 'Then Sandia estimated how many people would die and be injured within the first year due to their radiation exposure.' ' He … |
| Value | Core | The position or area on the Feature scale that the Cognizer concludes the Item occupies. 'Sotheby 's have estimated its value at $10m-$14m.' |
| Circumstances | Extra-Thematic | Some specification of the Circumstances under which the Cognizer estimates. |
| Evidence | Peripheral | Some fact perceived by the Cognizer which contributes to their estimation of the Feature's Value. 'He then needs to estimate the desired shelf stock size on the basis of this record of use.' |
| Explanation | Extra-Thematic | A state-of-affairs enabling the estimating to occur. |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. |
| Manner | Peripheral | Manner is used for any expression which describes a property of the activity of Estimating |
| Means | Peripheral | An intentional action performed by the Cognizer enabling estimating. |
| Place | Peripheral | The location in which the Cognizer forms their estimate. 'At the London School of Economics they estimated that China would have to spend 2% of gross. domestic product on higher. education for 15 years' |
| Result | Extra-Thematic | This FE describes how the Estimation made by the Cognizer corresponds to reality. This FE can be represented by "correctly" or "wrong." |
| Time | Peripheral | The time period during which the Cognizer forms the estimate of the Feature's Value. 'The US Forest Service estimated last year that 45 million piñons have died so far in north-central New Mexico.' |

**Frame relations** (super → sub)

- Using: Estimating → Estimated_value
- Using: Mental_activity → Estimating

**Lexical units** (4): estimate.v, estimation.n, guess.v, put (at).v

## Have_as_requirement  (frame id 1491)

The obtaining of a Requirement state of affairs or the presence of a Required_entity is profiled as a prerequisite for the obtaining or occurring of a Dependent state-of-affairs. 'This game demands great skill.' 'The war on terror requires little sacrifice for most Americans.' 'Glass art demands great patience from the student.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Dependent | Core | The state-of-affairs which cannot hold without the state of affairs of the Requirement or the presence of the Required_entity. |
| Required_entity | Core | An entity that has to be present for the Dependent state of affairs to obtain. 'Believe it or not, but this cake requires a pound of mild sausage.' |
| Requirement | Core | The state-of-affairs that must obtain in order for the Dependent to obtain. |
| Condition | Extra-Thematic | The conditions under which the the Requirement is necessary. 'This Par 5 demands great shotmaking if the player is to equal or better par.' |
| Degree | Peripheral | The extent to which the Dependent depends on the presence of the Required_entity or the obtaining of the Requirement. 'A performance like this absolutely demands charm.' |
| Domain | Extra-Thematic | The field of endeavor whose nature imposes the Requirement. |
| Explanation | Extra-Thematic | The state-of-affairs which militates that the Requirement is necessary for the Dependent to obtain. |
| Place | Peripheral | Place denotes a location in which the specified relation between Requirement and Dependent holds. 'In the US, putting this on the agenda requires the political weight and leadership of big city mayors.' |
| Required_individual | Extra-Thematic | An individual that has to provide the Required_entity or to see to it that the Requirement state of affairs holds. 'It's a sport that demands everything of me.' |
| Time | Peripheral | The time at which the Requirement is necessary for the Dependent. |

**Frame relations** (super → sub)

- Inheritance: Contingency → Have_as_requirement
- Perspective_on: Requirement_scenario → Have_as_requirement
- Using: Have_as_requirement → Needing

**Lexical units** (4): demand.v, need.v, require.v, take.v

## Supply  (frame id 1346)

A Supplier gives a Theme to a Recipient to fulfill a need or purpose (Imposed_purpose) of the Recipient. 'Habituating the ground nesting chimp groups is done by provisioning them with sugar cane. CNI INI' 'I have equipped my leech troopers with tiny subspace displacement thingummies. INI' ' She sat down on her bed, carefully folding her clothing and packing it into the small carryall Starfleet had provided her for the journey.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Imposed_purpose | Core | The Recipient's intended purpose for the Theme. 'God gave them the promise of victory and equipped them for the battle.' |
| Recipient | Core | The entity that ends up in possession of the Theme. 'VESID also supplied him with an all zone bus pass to help him travel to interviews.' |
| Supplier | Core | The person that begins in possession of the Theme and causes it to be in the possession of the Recipient. 'I approve of your having supplied him with a file of soldiers.' |
| Theme | Core | The object that is given to the Recipient . 'Cromwell merged men from multiple regiments into a single one and provisioned them with red uniforms to replace their former regiment colors. ' |
| Circumstances | Extra-Thematic | The Circumstances are the conditions under which the Theme is supplied. 'I supplied the food free of charge.' |
| Cotheme | Extra-Thematic | An additional theme which is supplied along with the main Theme. 'Several cables were provided with the printer, but I'm not sure which ones to use.' |
| Explanation | Extra-Thematic | The Explanation for which the Supplier gives the Theme to the Recipient. 'Jesus equipped them because if they tried to do it in their own strength they would have understood defeat in a whole new way.' |
| Manner | Peripheral | Any description of the supplying event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, loudly), and general descriptions … |
| Means | Peripheral | The Means by which the Supplier acquires or gives the Theme to the Recipient. 'Euell provisioned them by foraging, hunting, and trapping whenever his father was away.' |
| Period_of_iterations | Extra-Thematic | The period over which the Supplier engages in (multiple) supplying acts. 'Our company has supplied nations with voting machines since 2000.' |
| Place | Peripheral | The Place where the Supplier gives the Theme to the Recipient. 'The Harpley was launched in Launceston on the 2nd February, 1847, and with the exception of her chain cables, was there supplied with all her materials … |
| Purpose | Peripheral | The Purpose for which the Supplier gives the Theme to the Recipient. 'Some financial support can be provided in order to help you and MPI with the product approval process in an efficient and effective way.' |
| Source | Peripheral | The source of the Theme. 'We equipped them from our own supply of equipment.' |
| Time | Peripheral | The Time is when the Supplier gives the Theme to the Recipient. 'In Breidbach, water tankers were yesterday supplied to the community as the main water supply pipe had been washed away.' |

**Frame relations** (super → sub)

- Inheritance: Giving → Supply
- Inheritance: Supply → Funding

**Lexical units** (14): afford.v, equip.v, equipment.n, fix up.v, fuel.v, furnish.v, issue.v, outfit.v, provide.v, provision.n, provision.v, supplier.n, supply.n, supply.v

## Labeling  (frame id 1250)

A Speaker uses as a Label to refer to an Entity. The Label is not a conventional name for the Entity but a description categorizing the Entity and thereby expressing a judgment. 'Some labeled him a womanizer.' 'During her lifetime, her enemies branded her as a prostitute. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The concrete or abstract thing with which the Speaker has associated a particular linguistic sign. 'He termed it "a pretty incredible discovery" on par with two other 10,000- to 11,000-year-old specimens' |
| Label | Core | The linguistic sign that the Speaker uses to designate the Entity. 'In Texas, we call it walking".' 'Americans call it a faucet. What do the British call it ?' |
| Medium | Core | A text whose author applies a particular Label to an Entity. 'Your article labels him "Republican Senator Jim Exon".' |
| Speaker | Core | The Speaker is the person who conventionally uses a linguistic sign to refer to an Entity. 'They call it a Mutt Mitt.' |
| Duration_of_final_state | Extra-Thematic | Duration_of_final_state denotes the length of time from the beginning of a state resulting from the activity denoted by the target until the state no longer holds. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Place | Peripheral | A physical space whose occupants use the Label to refer to the Entity. 'I really loved this movie. In France, they called it "Turbo Interceptor".' |
| Time | Peripheral | A time period in which a Speaker uses the Label. 'Back in the olden days, they called it "Bohemian people."' |

**Frame relations** (super → sub)

- Inheritance: Referring_by_name → Labeling
- Using: Judgment_communication → Labeling

**Lexical units** (4): brand.v, call.v, label.v, term.v

## Adjusting  (frame id 1376)

An Agent changes a Part of a complex entity with regard to some Feature in order to achieve some Imposed_purpose affected by the Feature. The complex entity is often a device or mechanism, but may also be an abstract entity such as the economy. Also, the full entity may be used in place of the Part. 'I need to adjust the thermostat to around 80 degrees when she visits.' 'It didn't work the first time , so she had to tweak the oven a little .' 'Greenspan expressed confidence that the current calibration of interest rates was not an overcompensation .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The individual that controls the value of a Feature. |
| Feature | Core | The Feature with respect to which the Part is adjusted. 'She adjusted the temperature of the oven so that the pie crust would brown a little.' |
| Part | Core | The part of the complex entity which is changed in the process of adjusting. 'She adjusted the injectors to make the mixture leaner.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Degree | Peripheral | A characterization of the amount that the Final_value and Initial_value differ. 'Do n't adjust the pressure by more than two PSI .' |
| Final_value | Peripheral | The value associated with the Feature that the system ends up in. |
| Imposed_purpose | Extra-Thematic | The state of the Part with respect to the Feature that the Agent brings about by making the adjustment. 'You should adjust the antenna to poke outside the bag.' |
| Instrument | Peripheral | An entity manipulated by the Agent to adjust the Part and Feature. |
| Manner | Peripheral | Any description of the adjustment act which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may indicate … |
| Means | Peripheral | The action performed by the Agent which affects the Part. |
| Place | Peripheral | The location where the adjusting takes place. |
| Purpose | Peripheral | The state-of-affairs that the Agent hopes to bring about by adjusting. |
| Time | Peripheral | The time at which the adjusting occurs. |

**Frame relations** (super → sub)

- Inheritance: Intentionally_affect → Adjusting
- Using: Cause_change → Adjusting

**Lexical units** (6): adjust.v, adjustment.n, calibrate.v, calibration.n, tweak.n, tweak.v

## Verification  (frame id 1230)

An Inspector attains a degree of certainty in the Unconfirmed_content, generally by inspecting some evidence. 'This note confirms my suspicions.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Inspector | Core | The individual or individuals that ascertain that the Unconfirmed_content is true. 'His later verification of the facts is certainly beyond reproach.' |
| Medium | Core | The Medium is the piece of text or work in which the Inspector verifies the Unconfirmed_content: 'Chapter four confirms the reader 's suspicions completely.' |
| Unconfirmed_content | Core | An open proposition that the Inspector decides by examining evidence. It is usually a propostion put forward which some parties would disbelieve or contest. 'It is extremely difficult to confirm the absence of … |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the target operates (often denoted by words such as "officially," "formally," "technically," etc.). |
| Condition | Extra-Thematic | The conditions under which the the verification will occur. |
| Degree | Peripheral | The amount of certainty which the Inspector achieves after the process of verification. 'His involvement in the action has subsequently been completely confirmed.' |
| Descriptor | Extra-Thematic | This FE describes a characteristic of the verification event. |
| Explanation | Extra-Thematic | The reason for the state of the verification event. |
| Instrument | Peripheral | A tool or instrument used by the Inspector in the verification process. |
| Manner | Peripheral | Any description of the verification which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), force (hard, softly), secondary effects (quietly, loudly), and … |
| Means | Peripheral | An action performed by the Inspector by which the Inspector manages to establish the truth of the Unconfirmed_content. 'We confirmed our results by repeating the experiment and measuring the output with a mass spec.' |
| Place | Peripheral | This FE describes where the verificiation event takes place. |
| Purpose | Peripheral | The state of affairs that the Inspector hopes to bring about by going through the verification. 'I spent a few minutes confirming his visa number just to make him sweat.' |
| Time | Peripheral | This FE describes the Time at which the verification event takes place. |

**Frame relations** (super → sub)

- Inheritance: Scrutiny → Verification
- Using: Correctness → Verification

**Lexical units** (11): certify.v, confirm.v, confirmation.n, identify.v, make sure.v, substantiate.v, unconfirmed.a, unidentified.a, verifiable.a, verification.n, verify.v

## Categorization  (frame id 21)

A Cognizer construes an Item as belonging to a certain Category. In this process, the Cognizer may either passively perceive the Item and note that it fits the Criteria for a Category, or, alternatively, actively examine the Item for certain Criteria that define a Category (or set of Categorys). Most members of the frame can also describe a resulting cognitive state of the Cognizer with respect to the Item and Category which no longer requires the current perception or consideration of the Item. A few LUs (e.g. peg.v, pigeonhole.v) do not readily allow stative interpretation, and a few LUs (e.g. deem.v, regard.v) only allow stative interpretation. 'You 've already stereotyped me as a bimbo, have n't you?'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Category | Core | This frame element expresses a general type or class of which the Item is considered an instance. Typically, it is expressed in a prepositional phrase headed by as or under. 'Kim categorized the book as/under fiction.' |
| Cognizer | Core | This is the person who performs an act of categorization. Typically, this frame element is expressed as an External Argument. 'Kim categorized the books under fiction. Kim categorized them on the basis of genre.' |
| Criteria | Core | This frame element expresses properties of the Item which is used as a basis for categorization. Criteria are the general dimensions along which Items can potentially differ from one another and hence, fall into … |
| Item | Core | This is the entity which is construed or treated by the Cognizer as being an instance of a particular Category. Typically, the Item is expressed as an Object. 'Kim categorized the books under fiction.' |
| Circumstances | Extra-Thematic | The Circumstances are the set of conditions in which the categorization holds. 'Material posessions are defined as valuable in a particular society.' |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Explanation | Extra-Thematic | The reason for which the Cognizer categorizes the Item in the given way. |
| Manner | Peripheral | Manner of performing an action |
| Means | Peripheral | An act whereby the Cognizer categorizes. |
| Time | Peripheral | This Frame Element marks expressions that indicate when a certain Categorization was made. ' 20 years ago people would consider this as nothing unusual' |

**Frame relations** (super → sub)

- ReFraming_Mapping: Awareness → Categorization
- ReFraming_Mapping: Categorization → Awareness
- ReFraming_Mapping: Categorization → Communicate_categorization
- ReFraming_Mapping: Categorization → Statement
- Using: Categorization → Being_in_category
- Using: Categorization → Communicate_categorization
- Using: Instance → Categorization
- Using: Mental_activity → Categorization

**Lexical units** (28): bracket.v, categorization.n, categorize.v, category.n, class.v, classification.n, classify.v, conceive.v, consider.v, construe.v, count.v, deem.v, define.v, identify.v, interpret.v, interpretation.n, peg.v, perceive.v, pigeonhole.v, read.v, regard.v, render.v, see.v, stereotype.v, translate.v, typecast.v, understand.v, view.v

## Removing  (frame id 63)

An Agent causes a Theme to move away from a location, the Source. The Sourceis profiled by the words in this frame, just as the Goal is profiled in the Placing frame. 'I saw that several men in dark suits had removed all of the evidence from the scene.' 'With your index finger prise the meat out of the shell' 'The torrential winds dislodged most of the roof tiles.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the person (or other force) that causes the Theme to move. 'The waiter removed the dishes from the table.' |
| Cause | Core | The non-Agentive cause of the removing event. 'The raging fire quickly emptied the square of all people.' 'Magnetic storms on the sun sometimes eject hot gas from beneath the surface.' |
| Source | Core | The Source is the initial location of the Theme, before it changes location. 'The waiter removed the dishes from the table.' A few of the words in this frame participate in an alternation between a Theme object and a … |
| Theme | Core | Theme is the object that changes location. 'The waiter removed the dishes from the table. ' |
| Circumstances | Extra-Thematic | The state of the world when the Agent or Cause removes the Theme from the Source. |
| Co-timed_event | Extra-Thematic | An event the punctuates the larger Removing event. 'With a laugh, she tore a page from his diary.' |
| Cotheme | Extra-Thematic | The Cotheme is the second moving object, expressed as a direct object or an oblique. 'Pat removed the jam from the fridge along with the cheese.' |
| Degree | Peripheral | Degree to which event occurs |
| Depictive | Extra-Thematic | This FE describes a participant of the state of affairs introduced by the target as being in some state during the action. |
| Direction | Peripheral | This FE is used to indicate the Direction that the Theme travels when it is removed. |
| Distance | Peripheral | The Distance is any expression which characterizes the extent of motion. This frame element occurs throughout the motion domain but is very infrequent in Motion_Noise. 'John withdrew the gun a few feet.' |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the state of affairs expressed by the target, but not in all cases. |
| Goal | Peripheral | The Goal is the location where the Theme ends up. This Frame Element is not profiled by words in this frame, though it may occasionally be expressed, as with the word remove. 'Grandmother removed the fine china to a … |
| Instrument | Peripheral | The tool the Agent uses to remove the Theme from its Source. |
| Manner | Peripheral | Any expression which describes a property of motion which is not directly related to the trajectory of motion expresses the frame element Manner. Descriptions of speed, steadiness, grace, means of motion, and other … |
| Means | Peripheral | The Means is an act whereby the Agent achieves the removal. 'You'll have to eject it by sticking an unfolded paperclip into that little hole.' |
| Means_of_motion | Extra-Thematic | The Means_of_motion expresses the conveyance with which the Agent effects the motion of the Theme. The Means_of_motion holds and conveys the Theme. Means_of_motions can move in any way and in any medium. They are … |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Path | Peripheral | Any description of a trajectory of motion which is neither a Source nor a Goal expresses the frame element Path. In this frame, Path expressions almost always have a via-sense. 'The army evacuated the townspeople … |
| Place | Peripheral | The location where the removal takes place. 'You just take the dishes and rinse them in the kitchen, okay?' |
| Purpose | Peripheral | To what end the Agent or Cause removes the Theme. |
| Result | Extra-Thematic | Result of an event |
| Time | Peripheral | The time at which the removal takes place. 'That year they drained the swamp-water out of Higgs' bottomland.' |

**Frame relations** (super → sub)

- Inheritance: Transitive_action → Removing
- Perspective_on: Removing_scenario → Removing
- Precedes: Removing → Placing
- ReFraming_Mapping: Removing → Emptying
- ReFraming_Mapping: Removing → Escaping
- ReFraming_Mapping: Removing → Excreting
- ReFraming_Mapping: Removing → Kidnapping
- See_also: Cause_motion → Removing
- See_also: Placing → Removing
- Subframe: Cause_motion → Removing
- Using: Motion → Removing
- Using: Removing → Dunking
- Using: Removing → Undressing

**Lexical units** (50): amputate.v, clear.v, confiscate.v, cut.v, discard.v, disgorge.v, dislodge.v, drain.v, dust.v, eject.v, ejection.n, eliminate.v, elimination.n, empty.v, evacuate.v, evacuation.n, evict.v, eviction.n, excise.v, expel.v, expulsion.n, expunge.v, expurgate.v, extract.v, extraction.n, file.v, flush.v, oust.v, pluck.v, prise.v, purge.n, purge.v, removal.n, remove.v, rinse.v, rip.v, roust.v, scrape.v, shave.v, skim.v, snatch.v, strip.v, swipe.v, take.v, tear.v, unload.v, wash.v, weed.v, withdraw.v, withdrawal.n

## Progression  (frame id 1340)

An Entity changes from a Prior_state to a Post_state in a sequence that follows a pre-defined plan, expectation, or model of change. The change is usually assumed to be an improvement for the Entity. Because this frame is describing change according to some known model of the Entity, the Prior_state and Post_state are backgrounded, and often implicit. 'Their offensive armament has developed from short range missiles to long-range ballistic weaponry in a relatively short period .' 'The maturation of warhead technology is, perhaps, not far off .' 'Recovery in our major overseas markets has progressed tentatively and increased spending by consumers and government does not appear to be benefiting this' 'Why have we developed economically as we have?' This frame is not equivalent to the frame Improvement_or_decline for two reasons. Firstly, Progression implies a smooth or multi-stage change involving several different states of the Entity in an expected sequence, while Improvement_or_decline may be simple or complex, in accord with an expected sequence or not. Secondly, progression along an expected sequence does not necessarily mean that things get better (or worse) for the Entity. This is clear in the case of progression of a disease, since different ailments have very different expected sequenes, with initial onset leading to expected disappearance (for cases like the cold), or to permanent impairment (in the case of Parkinsons), or to death (in many forms of cancer). However, it is more confusing in the very common case of the progress of a biological Entity from birth to death, where this frame often emphasizes the phases of the lifespan where the organism increases in ability, thus reaching a more desirable state. Plans are also spoken of as progressions, and because the expected sequence is towards the goal of the agents that formed the plan, these uses of the progress frame also emphasize improvement.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The object that undergoes change. 'Advances in marketing techniques have since rendered it obsolete.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Degree | Peripheral | The amount of advancement that the Entity has attained. 'Robert's music is developing further as he hones his live set to bring in the diverse elements of pan-African music.' |
| Domain | Peripheral | The relevant dimension of development. 'Why have we developed economically as we have? ' |
| Duration | Peripheral | The period over which the progress occurs. 'Screwcap wine seals enable bottle maturation, and provide ideal conditions for maturation of wines over a long period of time.' |
| Event_description | Extra-Thematic | This FE describes the state of affairs denoted by the target as role fillers in other frames |
| Explanation | Extra-Thematic | An event or state of affairs that brings about the development of the Entity. |
| Frequency | Extra-Thematic | How often the Progress event occurs. |
| Manner | Peripheral | A description of the progress, generally a description comparing events (the same way). 'Recovery in our major overseas markets has progressed tentatively and increased spending by consumers and government does not … |
| Place | Peripheral | The location where the Progress occurs. |
| Post_state | Peripheral | The state of the Entity following an advance. 'The roads have now advanced to a level of perfection not seen since Rome .' |
| Prior_state | Peripheral | The former state of the Entity. 'I think we have advanced somewhat from that way of thinking .' |
| Rate | Peripheral | The rate at which the change happens. 'His captaincy has slowly matured until he has made us forget the sulky Nasser Hussian era' |
| Time | Peripheral | The time at which the progress occurs. 'When did the X-wing progress beyond the drawing board?' |

**Frame relations** (super → sub)

- Causative_of: Cause_to_make_progress → Progression
- Inheritance: Progression → Ontogeny
- See_also: Progression → Improvement_or_decline
- Using: Process → Progression
- Using: Progression → Stage_of_progress
- Using: Undergo_change → Progression

**Lexical units** (11): advance.n, advance.v, advancement.n, develop.v, development.n, maturation.n, mature.v, progress.n, progress.v, progression.n, stagnate.v

## Path_traveled  (frame id 1592)

A Path, a series of connected locations, is traversed by a Theme, moving under its own power or under the influence of a physical force. The Path may be described in various terms depending on whether it is bounded or not. If it is bounded, the Path may be identified by its Endpoints, which may be presented separately as Source and Goal. 'For Earth, these perturbations slowly change the eccentricity of the planet's orbit around the Sun.' 'From the eyewitness accounts, as well as satellite data, videos and photos, Brown and his team have worked out the meteor's path through space.' 'Its period around Saturn is just under one Earth day, meaning that it really barrels along, to cover its 700,000 mile orbit in such a short time.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Path | Core | The series of interconnected locations that the Theme traverses. 'In insects, blood is confined to vessels during only a portion of its circuit through the body.' |
| Theme | Core | The moving object whose motion describes the Path. 'The thick white line shows the army's path from Uzbekistan through Iran, Iraq, Palestine, and into Italy.' |
| Characteristic | Peripheral | The Characteristic is a characteristic(s) of the Path. 'Unlike Hubble, Compton was not designed to be serviced by astronauts in its 270 mile orbit.' |
| Direction | Peripheral | The Direction is the direction or directions the Path runs. 'There was huge relief that Hurricane Emily's projected westward path across the Caribbean is likely to track to the south of oil and gas fields.' |
| Endpoints | Peripheral | The Endpoints are two (or more) named endpoints of the Path. 'This Pacific typhoon traveled far inland, knocking down everything in its path between Los Angeles and Denver.' |
| Goal | Peripheral | The Goal is the endpoint of the Path. 'The Cassini spacecraft will travel 3.5 billion kilometers (2.175 billion miles) along its path from Earth to Saturn.' |
| Ground | Peripheral | A setting location through which the Path goes. 'Hurrican Dennis was blamed for five deaths in Florida and Georgia -- but was much more brutal in its path across the Caribbean.' |
| Landmark | Peripheral | An entity relative to which the Theme moves on its Path . 'Lenny killed at least nine people and caused millions of dollars in damage on its course past 16 Caribbean islands.' |
| Length | Peripheral | The Length is the distance the Path extends. 'The bolt traveled smoothly in its short path through the air to Santa.' |
| Source | Peripheral | The Source is one of the Endpoints treated as a source. 'The Cassini spacecraft will travel 3.5 billion kilometers (2.175 billion miles) along its path from Earth to Saturn.' |

**Frame relations** (super → sub)

- Using: Motion → Path_traveled

**Lexical units** (4): circuit.n, course.n, orbit.n, path.n

## Residence  (frame id 110)

This frame has to do with people (the Residents) residing in Locations, sometimes with a Co-resident. 'Peter lives in New York.' 'Sue is an inhabitant of Los Angeles.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Co_resident | Core | A person or group of people that the resident is staying with or among. 'Boris still lives with his parents.' |
| Location | Core | The place in which somebody resides. 'Sue lives in Berkeley.' |
| Resident | Core | The individual(s) that reside at the Location. 'Hannah lives in San Francisco.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Depictive | Extra-Thematic | The state of a Resident during their residence. |
| Frequency | Extra-Thematic | Frequency at which event occurs. |
| Manner | Peripheral | Manner of performing an action |
| Means | Peripheral | An act of the Resident that enables them to reside in the Location. 'He dwelt in the wild for years by foraging nuts and berries and occasionally stealing.' |
| Time | Peripheral | This FE refers to the Time when the Resident resides. |

**Frame relations** (super → sub)

- Inheritance: Residence → Temporary_stay
- Using: Residence → Colonization
- Using: Residence → People_by_residence

**Lexical units** (23): bivouac.n, bivouac.v, camp.n, camp.v, camped.a, camper.n, dwell.v, dweller.n, inhabit.v, inhabitant.n, live.v, lodge.v, occupant.n, occupy.v, reside.v, resident.n, room-mate.n, room.v, shack up.v, squat.v, squatter.n, stay.v, tenant.n

## Similarity  (frame id 481)

Two or more distinct entities, which may be concrete or abstract objects or types, are characterized as being similar to each other. Depending on figure/ground relations, the entities may be expressed in two distinct frame elements and constituents , Entity_1 and Entity_2, or jointly as a single frame element and constituent, Entities. The similarity may be based on appearance, physical properties, or other characteristics of the two entities. However, no such Dimension has to be specified explicitly. The Entities may be like each other to a greater or lesser Degree. Rather than specifying the Dimension of difference, a Differentiating_fact may be mentioned. '' Notice that, although similarity presupposes the notion of a judge who assesses similarity, that judge is not part of the frame of similarity. 'A mulberry is very similar in shape to a loganberry' 'Recovering it afterwards can also be similar to collecting an unsecured loan ' 'Great Britain and Germany were only alike in one respect.' 'Lothlorien is quite like most of their other war games really.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Differentiating_fact | Core | A fact about Entity_1 or the Entities that reveals how Entity_1 is the same or different from other entities. (Note the contrast with 'as to'.) 'His presidency was different in that it offered a way forward for the … |
| Dimension | Core | This FE marks constituents which express a property in respect to which the similarity of the entities is assessed. 'The disc announced Friday is physically similar to current music CDs ' |
| Entities | Core | This FE marks constituents that express the set of objects or types whose similarity is at issue. ' The two painters were alike in being unable to draw acceptably . ' 'Agbenugba confirms the resemblances between his … |
| Entity_1 | Core | When there is an asymmetry, Entity_1 is the entity characterized by its similarity to Entity_2, whose characteristics are assumed to be known. Entity_1 is often an external argument. 'In the first phase Barthes's … |
| Entity_2 | Core | When the Entities are expressed separately, Entity_2 is the one whose characteristics are assumed to be known; it serves as a basis for establishing characteristics of Entity_1. 'The results of Method 2 show remarkable … |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Degree | Peripheral | The extent to which entities are similar to each other, in general or with respect to some Dimension(s) 'The twins are very similar.' |
| Depictive | Extra-Thematic | This FE is used for any Depictive phrase describing the state of the Entities |
| Explanation | Extra-Thematic | An inanimate entity or process that causes the similarity. |
| Manner | Peripheral | This FE identifies the Manner in which Dimension is similar or different |
| Place | Peripheral | The Place is the general area in which similarity occurs or exists |
| Time | Peripheral | This FE identifies the Time when the similarity occurs or exists. |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Similarity
- Inheritance: Reciprocality → Similarity
- Inheritance: Similarity → Be_in_agreement_on_assessment
- Inheritance: Similarity → Diversity
- Using: Similarity → Correctness
- Using: Similarity → Distinctiveness
- Using: Similarity → Imitating
- Using: Similarity → Typicality

**Lexical units** (33): alike.a, differ.v, difference [count].n, difference.n, different.a, discrepancy.n, discrepant.a, disparate.a, disparity.n, dissimilar.a, dissimilarity [mass].n, dissimilarity.n, distinct.a, distinction.n, image.n, like.a, like.n, like.prep, mimic.v, parallel.n, resemblance.n, resemble.v, ringer.n, similar.a, similarity [count].n, similarity [mass].n, spitting image.n, take after.v, unlike.a, unlike.prep, variant.n, vary.v, very image.n

## Obviousness  (frame id 1360)

A Phenomenon is portrayed with respect to the Degree of likelihood that it will be perceived and known, given the (usually implicit) Evidence, Perceiver, and the Circumstances in which it is considered. For several of the LUs, such as visible, audible, etc., the type of the Evidence is fixed by the targets themselves being a perceptual experience. 'It's abundantly obvious that we'll need to spend more time on public perception.' 'Are you certain that the shovel was visible from the door of the apartment?' ' I think they miss some of the important impacts of the work that are not visible just from looking at the vote tally.' 'That the defense will declare a mistrial regardless is quite evident from their consistent obstructionist tactics.' 'In late July 2000 it was barely visible to the unaided eye.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Attribute | Core | The gradable aspect of a Phenomenon which concerns how likely it is that the Phenomenon be known. This frame element is incorporated by the lexical units in this frame. |
| Degree | Core | A modifier expressing the deviation of the Phenomenon from the norm or from the value for another Phenomenon in terms of how likely the Phenomenon would be known. 'It is abundantly obvious you have not a clue how the … |
| Phenomenon | Core | The entity or facts that are undeniable given the Evidence. 'It is obvious for example that 9/10 is not the same as 1.' |
| Circumstances | Extra-Thematic | Some specification of the conditions under which the Phenomenon is likely to be known. |
| Direction | Peripheral | This frame element is used for all path-like expressions, except those indicating the location of the perceiver (see above), that describe how the perceiver's attention is directed during the act of perception. 'The … |
| Evidence | Peripheral | A state-of-affairs that has a bearing on whether the Phenomenon will be perceived or apprehended cognitively. Evidence is often metonymically indicated by the mention of an entity whose existence or whose properties … |
| Group | Extra-Thematic | The likelihood of a Phenomenon to be observed perceptually or cognitively in a particular Group of comparable background items may be contrasted, implicitly or explicitly, with different groups. 'This correlation was … |
| Location_of_protagonist | Extra-Thematic | The physical location of a Perceiver of the Phenomenon or a metaphorical point-of-view location of a cognizer relative to the Phenomenon. 'It is obvious from here that the crux of the climb is the ascent up to the … |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. In addition, most … |
| Perceiver | Peripheral | The sentient entity for whom perception or cognition of the Phenomenon is judged to be more or less likely. 'It was obvious to Peter he had made a wise choice.' |
| Time | Extra-Thematic | The Time during which the Phenomenon is obvious 'It is obvious now that Senator O. T. Tawa has no plan.' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Obviousness

**Lexical units** (14): audible.a, clarity.n, clear.a, clearly.adv, evident.a, manifest.a, noticeable.a, obvious.a, obviously.adv, show up.v, show.v, stand out.v, unclear.a, visible.a

## Evidence  (frame id 25)

The Support, a phenomenon or fact, lends support to a claim or proposed course of action, the Proposition, where the Domain_of_relevance may also be expressed. Some of the words in this frame (e.g. argue) are communication words used in a non-communicative, epistemic sense. 'The latest poll results show that support of the president is at an all-time low.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Proposition | Core | This is a belief, claim, or proposed course of action to which the Support lends validity. Normally it is expressed as a Finite Clause Complement: 'The fact that you lied to me shows that I shouldn't trust you.' Some … |
| Support | Core | Support is a fact that lends epistemic support to a claim, or that provides a reason for a course of action. Typically it is expressed as an External Argument. 'The fact that you lied to me shows that I shouldn't trust … |
| Cognizer | Peripheral | The person for whom the Proposition is supported by the Support. 'The behavior of the children indicated to the teacher that further action was required on his part.' |
| Degree | Peripheral | This FE identifies the degree to which a Proposition is supported. |
| Depictive | Extra-Thematic | A description of the status of the Support within its relationship to the Proposition. This proves my conclusions all by itself. |
| Domain_of_relevance | Extra-Thematic | This FE identifies the domain (usually, time or space) for which a given Proposition is true. |
| Manner | Peripheral | This FE identifies the manner in which a Proposition is supported. 'The results of the experiments proved the hypothesis brilliantly.' |
| Means | Peripheral | An intermediate logical step that justifies the relationship of the Support to the Proposition. 'Tiny patterns in fossil rocks can demonstrate that dinosaurs and pterosaurs were (at least potentially) warm blooded by … |
| Result | Extra-Thematic | Result of an event |

**Frame relations** (super → sub)

- Using: Evidence → Explaining_the_facts
- Using: Evidence → Sign

**Lexical units** (31): argue.v, argument.n, assure.v, attest.v, confirm.v, contradict.v, corroborate.v, credence [lend].n, demonstrate.v, demonstration.n, disprove.v, evidence.n, evidence.v, evince.v, from.prep, illustrate.v, imply.v, indicate.v, mean.v, point (to).v, proof.n, prove.v, reveal.v, rule out.v, show.v, substantiate.v, suggest.v, support.v, tell.v, testify.v, verify.v

## Expectation  (frame id 26)

Words in this frame have to do with a Cognizer believing that some Phenomenon will take place in the future. Some words in the frame (e.g. foresee.v) indicate that the Phenomenon is asserted also to be true, while others do not. 'Michael expected Abby to demand examples.' 'From the look on her face Michael expected that she would say she got the job.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | This is the person who believes some Phenomenon will take place in the future. It is normally expressed as an External Argument: Pat expects that the Yankees will win the World Series. |
| Phenomenon | Core | This is what the Cognizer believes will happen in the future. It can be expressed as a Finite Clause Complement, an NP Object, or a VP Complement with or without an NP Object (see General Grammatical Observations): … |
| Topic | Core | An entity that serves as the focus of a predicted Phenomenon. 'Predictions about stock prices are notoriously undependable.' |
| Degree | Peripheral | Degree to which event occurs |
| Depictive | Extra-Thematic | Depictive phrase describing the actor of an action 'We awaited the lunar eclipse sitting atop a hill.' |
| Evidence | Peripheral | Words in this frame may occur with a PP headed by from which expresses the Evidence on which knowledge or belief is based: I have learned from experience that poison oak can be painful. |
| Manner | Peripheral | Manner of performing an action |
| Place | Peripheral | The location where the Cognizer foresees the Phenomenon. 'Even at the far side of the house I could predict what was going on the kitchen.' |
| Time | Peripheral | The time when the Cognizer makes the prediction. 'She predicted the outcry several months ago.' |
| Time_of_phenomenon | Peripheral | The time that the Cognizer expects the Phenomenon to occur. Note that it is distinct from simple Time, which is when the Cognizer is actually involved in thinking about the Phenomenon. 'Another arrival is expected this … |

**Frame relations** (super → sub)

- Inheritance: Awareness → Expectation
- See_also: Omen → Expectation
- Using: Expectation → Predicting

**Lexical units** (14): anticipate.v, await.v, expect.v, expectation.n, foresee.v, foreseeable.a, predict.v, predictable.a, prediction.n, premonition.n, unexpected.a, unforeseeable.a, unpredictable.a, wait.v

## Sign  (frame id 428)

A phenomenon, the Indicator, exists as an indication of another phenomenon, the Indicated. The relationship is asymmetric: the Indicated is not necessarily a sign for the existence or presence of an Indicator. The Indicated can be a past, present, or future entity or eventuality. The relationship between Indicator and Indicated is not one of symbolization or iconicity. Rather the Indicator is an index of the Indicated. 'This is a sign of things to come.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Indicated | Core | The phenomenon that is signified by the Indicator. 'We now exhibt the same symptoms of the same disease.' |
| Indicator | Core | The phenomenon that signifies the Indicated. 'He was unable to display any sign of pain.' |
| Descriptor | Peripheral | Any description of the Indicator not covered by a more specific FE. |
| Frequency | Extra-Thematic | This FE depicts how often the Indicated manifests itself. 'A 24-hour Holter moniter should be considered only for patients with daily symptoms.' |
| Reliability | Peripheral | This FE indicates the Reliability of the Indicator as a sign of the Indicated. |

**Frame relations** (super → sub)

- Inheritance: Sign → Leaving_traces
- Inheritance: Sign → Omen
- Using: Evidence → Sign

**Lexical units** (9): indicate.v, indication.n, indicative.a, mark.v, sign.n, signify.v, symptom.n, symptomatic.a, usher in.v

## Change_event_duration  (frame id 1770)

In this frame, an Agent or Cause changes the duration of an Event. The Event will then take place for a New_duration, rather than the Initial_duration. This can be done with by certain Means, in a certain Manner or to a certain Degree. 'Don't let him prolong the discussion to an absurd length.' 'Harsh weather made it necessary to cut the tour short from its original four months to three. CNI'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The sentient entity that changes the duration of the Event. 'Don't let him prolong the discussion to an absurd length.' |
| Cause | Core | An event that causes the change in Event duration. 'Rain so cruelly cut short the game against Bangladesh.' |
| Event | Core | The Event's duration is changed. 'Don't let him prolong the discussion to an absurd length.' |
| Degree | Peripheral | The extent to which the initial and final durations differ from each other. 'Too bad we can't extend our vacation even more.' |
| Explanation | Extra-Thematic | A state of affairs that the Agent is responding to in bringing about the change of duration. 'Why would someone cut our time short like that?' |
| Initial_duration | Peripheral | The planned duration of the Event before the change takes place. 'Harsh weather combined made it necessary to cut the tour short from its original four months to three.' |
| Manner | Peripheral | Any description of the event causing the change of the Event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, loudly), and … |
| Means | Peripheral | An intentional action performed by the Agent (or event resulting from the Cause) that produces a change in the Event's duration. 'It seems they are bent on prolonging conflict by ignoring normal wartime conventions.' |
| New_duration | Peripheral | The new duration of the Event. 'Don't let him prolong the discussion to an absurd length.' |
| Purpose | Peripheral | An action that the Agent intends to accomplish by changing the duration of the Event. |
| Time | Peripheral | The time at which the change in duration of the Event is caused. 'Last week, he unnecessarily prolonged the agony, thinking that he could tough it out.' |

**Frame relations** (super → sub)

- Inheritance: Cause_change → Change_event_duration

**Lexical units** (8): abbreviate.v, cut short.v, drag out.v, extend.v, prolong.v, protract.v, shorten.v, slow.v

## Hindering  (frame id 480)

In this frame a Hindrance makes it more difficult for a Protagonist to complete their intended Action or a Hindrance directly affects an Action where the Action can be a natural act or the actions of many individuals in a collective endeavor. Crucially, these lexical units do not entail that the Protagonist was unable to complete the Action or that the Action did not occur. The Hindrance may indicate a lack of enablement or an obstacle on the natural progression of the Protagonist or Action ' Malcolm was hindered by his drinking problem . ' ' A lack of money hampered our plans . ' ' Many candidates' progress is severely impeded because they have to resit for the exam. ' ' The new dam impeded the flow of water . '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Action | Core | The Action is what the Protagonist desires to do, which is made more difficult by the Hindrance. It can also be a natural act or collective endeavor, not linked to an overt Protagonist. |
| Hindrance | Core | The Hindrance is the force which makes the Action more difficult or less likely to be successfully completed. The Hindrance may be a lack of enabling force: ' The project was hampered by a lack of funds. ' or the … |
| Protagonist | Core | The Protagonist is the entity that tends towards or plans some Action which the Hindrance causes to be more difficult. |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Degree | Extra-Thematic | The Degree is the extent to which the Hindrance affects the Protagonist or Action. |
| Duration | Extra-Thematic | The length of time over which the hindering takes place. 'The exporting of goods from the United States was impeded for several months while negotiations continued.' |
| Explanation | Extra-Thematic | This FE label is used for the cause of the Hindrance |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. |
| Manner | Peripheral | The manner in which hindering occurs |
| Means | Peripheral | This FE describes the means by which hindering occurs |
| Place | Peripheral | The Place is the location where he Hindrance affects the Protagonist or Action. |
| Time | Peripheral | The Time is when the Hindrance affects the Protagonist or Action. |

**Frame relations** (super → sub)

- Using: Event → Hindering
- Using: Hindering → Difficulty

**Lexical units** (29): block.v, constrain.v, curtail.v, delay.v, encumber.v, encumbrance.n, hamper.v, handicap.v, hardship.n, hinder.v, hindrance.n, hold back.v, hurdle.n, impede.v, impediment.n, inhibit.v, interfere.v, interference.n, obstruct.v, obstruction [act].n, obstruction [entity].n, obstructive.a, repress.v, repressive.a, restrain.v, restraint.n, retard.v, slow.v, trammel.v

## Activity_pause  (frame id 167)

An Agent pauses in the course of an Activity. '' 'The government froze settlement construction in 1992 to facilitate peace talks.' 'The lifting of the nuclear freeze was deemed necessary to generate needed electricity.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | This FE identifies the Activity for which an Agent is pausing. |
| Agent | Core | An Agent pauses in the course of an Activity. |
| Completeness | Peripheral | The extent to which the Agent pauses in the Activity. |
| Depictive | Extra-Thematic | This FE is used for the Depictive phrase describing the actor or undergoer of an action. |
| Duration | Peripheral | The length of time of the pause in the Activity. |
| Event_description | Extra-Thematic |  |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Legal_basis | Extra-Thematic | This FE describes the legal basis or precedent by which the Agent pauses the Activity. 'The negotiations have been frozen under the Act of 2004.' |
| Manner | Peripheral | This FE identifies the Manner in which an Agent pauses during the course of an Activity. |
| Means | Peripheral | This FE identifies the Means by which an Agent pauses in the course of an Activity. |
| Place | Peripheral | This FE identifies the Place where an Agent pauses in the course of an Activity. |
| Purpose | Peripheral | This FE identifies the Purpose for which an Agent pauses in the course of an Activity. |
| Time | Peripheral | This FE identifies the Time at which an Agent pauses in the course of an Activity. |

**Frame relations** (super → sub)

- Inheritance: Process_pause → Activity_pause
- Precedes: Activity_ongoing → Activity_pause
- Precedes: Activity_pause → Activity_paused_state
- Subframe: Activity → Activity_pause
- Using: Eventive_affecting → Activity_pause

**Lexical units** (7): adjourn.v, freeze.n, freeze.v, moratorium.n, pause.n, suspend.v, take break.v

## Activity_resume  (frame id 1156)

An Agent resumes participation in an Activity. Progress on the Activity is retained from before the interruption. 'Normal Service Will Be Resumed Shortly. CNI' The Kinshasa government has resumed supporting Rwandan rebels.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | The Activity which is being resumed by the Agent. 'We have renewed our efforts to gain federal recognition. ' |
| Agent | Core | The Agent who resumes an Activity that they were engaged in earlier. ' We renewed our efforts to get things completed.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Depictive | Extra-Thematic | his FE describes a participant of the state of affairs introduced by the target as being in some state during the action. The depicted state does not necessarily or usually facilitate or cause the state of affairs … |
| Duration | Peripheral | The amount of Time for which the Activity is resumed |
| Event_description | Extra-Thematic | n general, this FE is used for phrases that describe the clause of the target as a whole. |
| Explanation | Extra-Thematic | The Explanation for which the Activity is resumed. |
| Manner | Peripheral | Any description of the Activity which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, loudly), and general descriptions comparing … |
| Place | Peripheral | Where the event takes place. |
| Result | Extra-Thematic | The consequence of the resuming of the Activity. |
| Time | Peripheral | When the Activity is resumed. |

**Frame relations** (super → sub)

- Inheritance: Process_resume → Activity_resume
- Precedes: Activity_paused_state → Activity_resume
- Precedes: Activity_resume → Activity_ongoing
- Subframe: Activity → Activity_resume

**Lexical units** (3): renew.v, restart.v, resume.v

## Activity_ongoing  (frame id 164)

An Agent is performing the portion of an Activity in which there is dynamic stability. '' 'Not noticing the hoards of people rushing by the window, Manny continued eating his lunch.' 'Keep living the dream!'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | This FE identifies the name of the ongoing Activity in which an Agent engages. |
| Agent | Core | The Agent engages in an ongoing Activity. |
| Duration | Core | Duration denotes the length of Time from the beginning of a continuous situation (the one denoted by the target) to its end. In many cases, the continuous situation is a dynamic action which is ongoing, while in others … |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Co-timed_event | Extra-Thematic | This FE identifies the Co-timed_event with which the Agent continues an ongoing Activity.'We continued the meeting with a discussion of the crisis in Africa.' |
| Depictive | Extra-Thematic | This FE is used for the Depictive phrase describing the actor or undergoer of an Activity.'They continued arguing naked.' |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Manner | Peripheral | This FE identifies the Manner in which an Agent performs an ongoing Activity. |
| Means | Peripheral | This FE identifies the Means by which an Agent engages in an ongoing Activity. |
| Place | Peripheral | This FE identifies the Place where the ongoing Activity occurs. |
| Purpose | Extra-Thematic | This FE identifies the Purpose for which an Agent is engaged in an ongoing Activity. |
| Time | Peripheral | This FE identifies the Time when an ongoing Activity occurs. |

**Frame relations** (super → sub)

- Inheritance: Activity_ongoing → Retaining
- Inheritance: Process_continue → Activity_ongoing
- Precedes: Activity_ongoing → Activity_finish
- Precedes: Activity_ongoing → Activity_pause
- Precedes: Activity_ongoing → Activity_stop
- Precedes: Activity_resume → Activity_ongoing
- Precedes: Activity_start → Activity_ongoing
- Subframe: Activity → Activity_ongoing
- Using: Activity_ongoing → Being_active
- Using: Activity_ongoing → Cause_to_move_in_place
- Using: Activity_ongoing → Lively_place

**Lexical units** (6): carry on.v, continue.v, keep on.v, keep up.v, keep.v, maintenance.n

## Process_stop  (frame id 144)

A Process stops at a certain Time and Place. Reason may also be specified. A Duration may be included in order to indicate the length of the persistence of the Paused-state before action resumes. NB: Refer to Process frame. '' 'The strident, static-like hiss ceased abruptly.' 'The use of railway-owned vehicles on aggregates traffic ceased altogether in 1989.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Process | Core | The Process which is halting. |
| Degree | Peripheral | Degree to which the event occurs. |
| Depictive | Extra-Thematic | Depictive phrase describing the actor of an action. |
| Duration | Extra-Thematic | The amount of time that a process remains stopped. |
| Explanation | Extra-Thematic | This FE identifies the Explanation of an event occur. |
| Final_subevent | Extra-Thematic | The Final_subevent of an event. 'The peace march stopped with a prayer.' |
| Frequency | Extra-Thematic | The number of times that the Process stops., 'Mining activities on the opal fields ceased twice in the last two weeks due to heavy rain storms' |
| Manner | Peripheral | Manner of performing an action. |
| Place | Peripheral | Where the event takes place. |
| Result | Extra-Thematic | The Result of an event. |
| Time | Peripheral | When the event occurs. |

**Frame relations** (super → sub)

- Inheritance: Event → Process_stop
- Inheritance: Process_stop → Activity_stop
- Precedes: Process_continue → Process_stop
- Precedes: Process_stop → Process_stopped_state
- Precedes: Process_stop → Process_uncompleted_state
- Subframe: Process → Process_stop

**Lexical units** (11): cease.v, cessation.n, desist.v, discontinuation.n, discontinue.v, halt.n, kill.v, quit.v, shut down.v, shutdown.n, stop.v

## Stimulus_focus  (frame id 364)

In this frame either a Stimulus brings about a particular emotion or experience in the Experiencer or saliently fails to bring about a particular experience. Some words indicate that the Stimulus is characterized by the experience it is likely to evoke in an Experiencer and for these, the Experiencer may rarely be present. There may also be a Degree to which the Stimulus affects the Experiencer and Circumstances under which the experience occurs. There may also be a Comparison_set to which the Stimulus is compared and a Parameter that indicates the area in which the Stimulus has its effect. ' The view is breathtaking in January. ' ' That movie was quite fascinating. ' ' That was certainly a gratifying experience.' ' The report was very alarming to me. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Stimulus | Core | The Stimulus is the object or event which brings about the emotion in the Experiencer. |
| Circumstances | Extra-Thematic | This FE marks expressions that indicate a set of conditions under which the Stimulus is able to bring about the emotion. ' When sunny the view is impressive. ' |
| Comparison_set | Extra-Thematic | The Comparison_set is the set of individuals the Stimulus is compared to when determining the Degree of the emotional reaction. 'Randy is very stimulating for a curator. ' |
| Degree | Peripheral | Degree to which the Stimulus evokes the emotion in the Experiencer |
| Experiencer | Peripheral | The Experiencer experiences the emotion brought about by the Stimulus |
| Parameter | Peripheral | The Parameter is the area in which the Stimulus brings about an effect on the Experiencer. ' This art work is aesthetically pleasing.' 'The book is emotionally disturbing. ' |
| Property | Extra-Thematic | This FE indicates a Property of the Stimulus which causes a particular experience. 'The movie is terrifying in its realism' 'The movie is terrifying in its use of violence' 'The move was disappointing in every respect … |

**Frame relations** (super → sub)

- Inheritance: Stimulus_focus → Ineffability
- Perspective_on: Emotions → Stimulus_focus
- ReFraming_Mapping: Stimulus_focus → Mental_stimulus_stimulus_focus

**Lexical units** (179): abominable.a, absorbing.a, aggravating.a, aggravation.n, agonizing.a, agreeable.a, alarming.a, alienating.a, amazing.a, amusing.a, annoyance.n, annoying.a, appalling.a, astonishing.a, astounding.a, baffling.a, beguiling.a, bewildering.a, bewitching.a, blood-curdling.a, boring.a, bothersome.a, breathtaking.a, calming.a, captivating.a, charm [count].n, charm [mass].n, charming.a, cheering.a, chilling.a, color.n, comforting.a, comical.a, confusing.a, consoling.a, cool.a, dear.a, delight.n, delightful.a, depressing.a, devastating.a, disagreeable.a, disappointing.a, discomfiting.a, discomforting.a, disconcerting.a, discouraging.a, disgusting.a, disheartening.a, disillusioning.a, dismaying.a, disorientating.a, displeasing.a, distasteful.a, distressing.a, disturbing.a, dreadful.a, droll.a, dull.a, earth-shattering.a, electrifying.a, embarrassing.a, embittering.a, empty.a, enchanting.a, encouraging.a, engrossing.a, enjoyable.a, enraging.a, entertaining.a, enthralling.a, exasperating.a, exciting.a, exhilarating.a, fascinating.a, formidable.a, frightening.a, fulfilling.a, full.a, funny.a, galling.a, ghastly.a, gratifying.a, gripping.a, hair-raising.a, harrowing.a, heart-rending.a, heart-stopping.a, heart-warming.a, heartbreaking.a, heartening.a, hilarious.a, humorous.a, impressive.a, infuriating.a, insulting.a, intimidating.a, intriguing.a, invigorating.a, irksome.a, irritating.a, jaw-dropping.a, jolly.a, maddening.a, mind-boggling.a, mind-numbing.a, mortifying.a, mystifying.a, nerve-racking.a, nice.a, offensive.a, pacifying.a, pathetic.a, perplexing.a, pitiful.a, placating.a, pleasant.a, pleasing.a, pleasurable.a, poignant.a, reassuring.a, recreation.n, relaxation.n, relaxing.a, repellent.a, rest.n, revolting.a, rich.a, rousing.a, sad.a, saddening.a, satisfying.a, scary.a, shocking.a, sickening.a, side-splitting.a, sobering.a, solemn.a, soothing.a, spine-chilling.a, spine-tingling.a, startling.a, stimulating.a, stinging.a, stirring.a, stressful.a, strike a chord.v, striking.a, stupefying.a, surprising.a, suspenseful.a, tear-jerking.a, tedious.a, terrifying.a, thorny.a, thrilling.a, tiresome.a, tiring.a, tormenting.a, touching.a, traumatic.a, traumatising.a, troublesome.a, troubling.a, unexciting.a, unfulfilling.a, unfunny.a, unnerving.a, unpleasant.a, unpleasing.a, unsettling.a, uplifting.a, upsetting.a, vexation.n, vexatious.a, vexing.a, white-knuckle.a, worrisome.a, worrying.a

## Experiencer_obj  (frame id 47)

Some phenomenon (the Stimulus) provokes a particular emotion in an Experiencer. 'Nightmare on Elm Street scared me silly.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Experiencer | Core | The Experiencer reacts emotionally or psychologically to the Stimulus. 'Horror films terrify Edna.' |
| Stimulus | Core | The Stimulus is the event or entity which brings about the emotional or psychological state of the Experiencer. 'The news greatlyalarms all the women of the village.' |
| Circumstances | Extra-Thematic | The Circumstances is the circumstances under which the Stimulus brings about the experience. 'Soft music calms the children when they're wound-up.' |
| Degree | Peripheral | The Degree is the degree to which the Stimulus brings about an emotion in the Experiencer. |
| Depictive | Extra-Thematic | Depictive identifies a phrase which describes a state of the Experiencer. |
| Explanation | Extra-Thematic | The reason why the Stimulus causes the emotion in the Experiencer. |
| Manner | Peripheral | The Manner in which the Stimulus affects the Experiencer. |
| Means | Peripheral | The Means by which the Stimulus affects the Experiencer. |
| Result | Extra-Thematic | The Result of the Stimulus affecting the Experiencer. |
| Time | Peripheral | The Time when the Experiencer has an emotion as caused by the Stimulus. |

**Frame relations** (super → sub)

- ReFraming_Mapping: Experiencer_obj → Emotion_directed
- Using: Emotions → Experiencer_obj

**Lexical units** (136): abash.v, aggravate.v, aggrieve.v, agonize.v, alarm.v, amaze.v, anger.v, annoy.v, antagonize.v, appeal.v, arouse.v, astonish.v, astound.v, baffle.v, beguile.v, bewilder.v, bewitch.v, boggle.v, bore.v, calm.v, captivate.v, charm.v, cheer.v, comfort.v, conciliate.v, confuse.v, console.v, crush.v, dazzle.v, delight.v, demolish.v, depress.v, destroy.v, devastate.v, disappoint.v, discomfit.v, disconcert.v, discourage.v, dishearten.v, displease.v, distress.v, disturb.v, embarrass.v, embitter.v, enchant.v, encourage.v, engage.v, enrage.v, entertain.v, enthrall.v, exasperate.v, excite.v, exhilarate.v, fascinate.v, faze.v, flabbergast.v, floor.v, flummox.v, fluster.v, frighten.v, frustrate.v, fulfill.v, gall.v, gladden.v, grate.v, gratify.v, harass.v, hearten.v, humiliate.v, impress.v, incense.v, infuriate.v, interest.v, intimidate.v, intrigue.v, irk.v, irritate.v, kill.v, let down.v, madden.v, mollify.v, mortify.v, mystify.v, nettle.v, nonplus.v, offend.v, outrage.v, pacify.v, perplex.v, perturb.v, petrify.v, placate.v, please.v, puzzle.v, rankle.v, rattle.v, reassure.v, repel.v, revolt.v, rile.v, sadden.v, satisfy.v, scare.v, shake.v, shame.v, shock.v, shocker.n, sicken.v, sober.v, solace.v, soothe.v, spook.v, stagger.v, startle.v, stimulate.v, sting.v, stir.v, stun.v, stupefy.v, surprise.n, surprise.v, terrify.v, thrill.v, tickle.v, torment.v, traumatize.v, trouble.n, trouble.v, unnerve.v, unsettle.v, upset.v, vex.v, vexation.n, worry.v, wound.v, wow.v

## Emotion_directed  (frame id 46)

The adjectives and nouns in this frame describe an Experiencer who is feeling or experiencing a particular emotional response to a Stimulus or about a Topic. There can also be a Circumstances under which the response occurs or a Reason that the Stimulus evokes the particular response in the Experiencer. 'Mr. Whiskers is upset that there are no more cat treats.' 'The furious parent stormed into the office.' 'Franz gets infuriated at the thought of his ex-wife remarried.' ' She flashed a jubilant smile.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Event | Core | The Event is the occasion or happening that Experiencers in a certain emotional state participate in. 'The end of the film was filled with jubilant scenes.' [Here we know that the scenes are filled with jubilant … |
| Experiencer | Core | The Experiencer is the person or sentient entity that experiences or feels the emotions. 'Nan Ho turned, his extreme agitation unnoticed by the Prince.' |
| Expressor | Core | The Frame Element Expressor marks expressions that indicate a body part, gesture or other expression of the Experiencer that reflects his or her emotional state. They describe a presentation of the experience or … |
| State | Core | The State is the abstract noun that describes a more lasting experience by the Experiencer. 'Tracy was in an irritated mood.' |
| Stimulus | Core | The Stimulus is the person, event, or state of affairs that evokes the emotional response in the Experiencer. 'Liz's anger towards Raquel dates back to a charity dinner this year.' 'The feeling the bereaved find most … |
| Topic | Core | The Topic is the general area in which the emotion occurs. It indicates a range of possible Stimulus. 'I was angry about the war.' 'So tell the world, and its boredom about your troubles will heal you.' |
| Circumstances | Extra-Thematic | The Circumstances is the condition(s) under which the Stimulus evokes its response. In some cases it may appear without an explicit Stimulus. 'One career wife spoke about her exasperation when her husband listened to … |
| Degree | Peripheral | The Degree is the degree to which the Experiencer feels the emotion. 'Nan Ho turned, his extreme agitation unnoticed by the Prince .' |
| Empathy_target | Extra-Thematic | The Empathy_target is the individual or individuals with which the Experiencer identifies emotionally and thus shares their emotional response. 'I am happy for Sara.' |
| Explanation | Extra-Thematic | The Explanation is the explanation for why the Stimulus evokes a certain emotional response. 'The feeling the bereaved find most difficult to acknowledge is their anger against the dead person for abandoning them to … |
| Frequency | Extra-Thematic |  |
| Manner | Peripheral | The Manner is the way in which the Experiencer experiences the Stimulus. |
| Parameter | Peripheral | The Parameter is a domain in which the Experiencer experiences the Stimulus. |

**Frame relations** (super → sub)

- ReFraming_Mapping: Awareness → Emotion_directed
- ReFraming_Mapping: Emotion_directed → Emotion_active
- ReFraming_Mapping: Emotion_directed → Experiencer_focus
- ReFraming_Mapping: Experiencer_focus → Emotion_directed
- ReFraming_Mapping: Experiencer_obj → Emotion_directed
- Using: Emotions → Emotion_directed

**Lexical units** (182): OK.a, abashed.a, affronted.a, agitated.a, agitation.n, agonized.a, agony.n, alarmed.a, all about.prep, amused.a, amusement.n, anger.n, angry.a, anguish.n, anguished.a, annoyance.n, anxious.a, appalled.a, ashamed.a, astonished.a, astonishment.n, astounded.a, baffled.a, bafflement.n, befuddled.a, bewildered.a, bewilderment.n, bitterness.n, blue.a, bored.a, boredom.n, chagrin.n, chagrined.a, concern.n, concerned.a, contented.a, covetous.a, crestfallen.a, cross.a, crushed.a, dejected.a, dejection.n, delight.n, delighted.a, demolished.a, depressed.a, desolate.a, despair.n, despondency.n, despondent.a, devastated.a, disappointed.a, disappointment.n, discomfited.a, discomfiture.n, disconcerted.a, disconcertion.n, disconsolate.a, discouraged.a, discouragement.n, disgruntled.a, disgruntlement.n, disheartened.a, dismay.n, dismayed.a, disorientation.n, disoriented.a, displeased.a, displeasure.n, disquiet.n, disquieted.a, distress.n, distressed.a, downcast.a, downhearted.a, ecstatic.a, elated.a, elation.n, embarrassed.a, embarrassment.n, embittered.a, enraged.a, exasperated.a, exasperation.n, excited.a, excitement.n, exhilarated.a, exhilaration.n, fed up.a, fed-up.a, fine.a, flabbergasted.a, flummoxed.a, flustered.a, frightened.a, furious.a, fury.n, glee.n, gleeful.a, glum.a, glumness.n, gratification.n, gratified.a, grief-stricken.a, grief.n, grim.a, happy.a, harried.a, heartbreak.n, heartbroken.a, horrified.a, horror.n, humiliated.a, incensed.a, inconsolable.a, indignant.a, infuriated.a, interest.n, irate.a, irked.a, jubilant.a, livid.a, low-spirited.a, lugubrious.a, mad.a, miffed.a, miserable.a, misery.n, mortification.n, mortified.a, mournful.a, mourning.n, mystification.n, mystified.a, nervous.a, nettled.a, nonplussed.a, offended.a, outrage.n, overjoyed.a, overwrought.a, peeved.a, perplexed.a, perplexity.n, perturbed.a, petrified.a, pleased.a, puzzlement.n, rattled.a, relaxed.a, resentful.a, revolted.a, revulsion.n, riled.a, ruffled.a, sad.a, saddened.a, sadness.n, sickened.a, sore.a, sorrow.n, sorrowful.a, startled.a, stressed.a, stunned.a, stupefaction.n, stupefied.a, sympathetic.a, sympathize.v, sympathy.n, terror-stricken.a, thrilled.a, tormented.a, traumatised.a, unsettled.a, unsympathetic.a, upset.a, vexation.n, vexed.a, woebegone.a, worried.a, wretched.a

## Noise_makers  (frame id 1017)

The Noise_maker is an artifact used to produce sound, especially for musical effect. 'The church bells rang' 'The car alarm went off again' 'I have never played an acoustic guitar.' 'Each artist personally owns a Steinway and has chosen to perform on the Steinway piano professionally'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Noise_maker | Core | This FE identifies the entity or substance that is designed to produce sound. |
| Creator | Peripheral | An individual or individuals that bring the Noise_maker into existence. |
| Ground | Peripheral | The location with which the Noise_maker is associated. |
| Material | Peripheral | Any indication of what makes up the Noise_maker, including components, etc. |
| Name | Peripheral | The term used to refer to an Noise_maker. |
| Time_of_creation | Peripheral | The time at which a Noise_maker comes into existence. |
| Type | Peripheral | An indication of the subtype of Noise_maker. |
| Use | Peripheral | The use for which an Noise_maker is intended. |

**Frame relations** (super → sub)

- Inheritance: Artifact → Noise_makers

**Lexical units** (10): alarm.n, bell.n, cello.n, drum.n, guitar.n, piano.n, rattle.n, saxophone.n, siren.n, xylophone.n

## Evaluative_comparison  (frame id 353)

This frame is about the static comparison of an Profiled_item to a Standard_item, often with respect to some Attribute. In this frame, there is an inherent asymmetry between Profiled_item and Standard_item in that the two cannot be expressed jointly as a subject. Degree expressions are also found that indicate how close the items are to each other on the scale evoked by the Attribute. Furthermore, the particular value of the standard or item on a certain scale may be given by the Standard_attribute of the Profiled_attribute respectively. ' The Sun is putting on a show that rivals the most sizzling Hollywood thrillers.' 'Mexico's Copper Canyon rivals the Grand Canyon in sheer beauty and drama. ' ' Peyton Manning's passing yards are equaled among NFL quarterbacks by only a select few. ' ' Few pianists have ever equaled the lightness and vivacity of his rhythm . ' ' The current price matches the price last year . '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Attribute | Core | This Frame Elements marks constituents that indicate in which respect Item-1 and Item-2 are equal to each other. ' The Tri-Cities stack up well against the competition in the area of innovation' |
| Profiled_attribute | Core | The Profiled_attribute is a particular value on a scale which is being compared to a Standard_item or Profiled_attribute. |
| Profiled_item | Core | In active sentences, the Profiled_item is the grammatically more prominent one of the items that are compared and realized as the subject. . 'This PC stacks up well against its competitors ' |
| Standard_attribute | Core | The Standard_attribute is used when the standard is a specific value on a scale. ' We equalled father's skills . ' |
| Standard_item | Core | In active setnnces, the Standard_item is the grammatically less prominent element, i.e. the object or an oblique. ' This PC stacks up well against its competitors' |
| Comparison_set | Extra-Thematic | The Comparison_set includes the Standard_item and is what the Profiled_item is judged with respect to. |
| Degree | Peripheral | This Frame Element marks expressions that indicate how close the Profiled_item and the Standard_item are to each other on the scale evoked by the Attribute. 'A peanut butter and jelly sandwich stacks up well against … |
| Manner | Peripheral |  |
| Place | Peripheral | The location where the Profiled_item rivals the Standard_item. 'In Africa, the level of drug resistance rivals even Noatirtin's vaunted efficacy.' |
| Time | Peripheral | The time at which the Profiled_item rivals the Standard_item. 'American caviar now rivals Russia's in quality.' |

**Frame relations** (super → sub)

- Inheritance: Position_on_a_scale → Evaluative_comparison

**Lexical units** (8): comparable.a, compare.v, equal.v, match.n, match.v, measure up.v, rival.v, stack up.v

## Confronting_problem  (frame id 2054)

An Agent becomes involved in an Issue which has negative consequences for them. The Agent will normally respond to resolve the Issue. 'I confronted both issues.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the person who is acting to deal with the Issue. |
| Issue | Core | This FE identifies the Issue that the Agent deals with. |
| Domain | Extra-Thematic | The Domain within which the Agent acts. |
| Event_description | Extra-Thematic | This FE gives a description of the confronting event as a whole. |
| Explanation | Extra-Thematic | Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the state of affairs expressed by the target, but not in all cases. |
| Frequency | Extra-Thematic | The Frequency with which the Agent does the Act in a given period of time. |
| Manner | Peripheral | Any description of the intentional act which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may indicate … |
| Means | Peripheral | This FE identifies the way in which an Agent goes about facing the Issue. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Period_of_iterations | Extra-Thematic | The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | This FE identifies the Place where the intentional act occurs. |
| Purpose | Peripheral | This FE identifies the reason why the Agent confronts the issue. |
| Result | Extra-Thematic | The Result describes the resulting outcome of the confronting act. |
| Time | Peripheral | This FE identifies the time when the Agent acts intentionally. |

**Frame relations** (super → sub)

- Inheritance: Intentionally_act → Confronting_problem
- Precedes: Confronting_problem → Resolve_problem

**Lexical units** (2): confront.v, face.v

## Hostile_encounter  (frame id 93)

This frame consists of words that describe a hostile encounter between opposing forces (Side_1 and Side_2, collectively conceptualizable as Sides) over a disputed Issue and/or in order to reach a specific Purpose. '' 'He still wants to fight Mike Tyson in about 8 months.' 'Dennis Andries's European cruiserweight title clash against Akim Tafer of France in Beausoleil last February has been voted as the EBU's fight of the year.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Issue | Core | An unresolved question over which the two sides of a hostile encounter are in disagreement. 'They had a dust-up over who was prettier .' Quite often it takes the form of a covert question of various sorts. So in an … |
| Purpose | Core | The desired result of the outcome of the hostile encounter for the Side_1 or for all the Sides collectively. It may either directly refer to the state of affairs that is desired, e.g. 'He dueled with his former second … |
| Side_1 | Core | One of two participants in a hostile encounter. 'While the U.S.'s battle with terrorist-harboring nations is far off ...' |
| Side_2 | Core | One of two participants in a hostile encounter, usually the second mentioned. 'While the U.S.'s battle with terrorist-harboring nations is far off ...' |
| Sides | Core | The jointly expressed sides in a hostile encounter. 'They fought over the right to own land.' |
| Degree | Peripheral | The Degree to which an event occurs. |
| Depictive | Extra-Thematic | A Depictive phrase describing the actor of an action. |
| Duration | Peripheral | The amount of time for which a state holds or a process is ongoing. |
| Explanation | Extra-Thematic | The Explanation for which an event occurs. |
| Instrument | Peripheral | The Instrument with which an intentional act is performed. |
| Internal_cause | Extra-Thematic | The body movement may be prompted by either some outside phenomenon or occurrence, or by an Internal Cause, the Agent's mental or emotional state. Internal Cause is expressed in a PP complement. |
| Manner | Peripheral | Any expression which describes a property of the hostile encounter. Descriptions of the intensity count as Manner expressions. 'After Brundle's Jaguar took off like a scalded cat, it was Mass who hunted it down, an … |
| Means | Peripheral | Means describes the way in which a side engages in a hostile encounter. 'President Corazon Aquino of the Philippines is bracing herself for a legal battle over her decision to allow the remains of the former president, … |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Place | Peripheral | The location at which the hostile encounter takes place. 'Following the battle of Naseby in 1645 ...' |
| Result | Extra-Thematic | The Result of an event. |
| Time | Peripheral | The Time at which the hostile encounter occurs. 'Following the battle of Naseby in 1645 he died.' |

**Frame relations** (super → sub)

- Inheritance: Hostile_encounter → Fighting_activity
- Inheritance: Intentionally_act → Hostile_encounter
- Metaphor: Hostile_encounter → Firefighting
- Perspective_on: Hostile_encounter → Attack
- Using: Hostile_encounter → Firefighting
- Using: Hostile_encounter → Friendly_or_hostile
- Using: Hostile_encounter → Irregular_combatants
- Using: Hostile_encounter → Member_of_military
- Using: Taking_sides → Hostile_encounter

**Lexical units** (47): altercation.n, battle.n, battle.v, bout.n, brawl.n, brawl.v, bw.n, clash.n, clash.v, combat.n, conflict.n, confront.v, confrontation.n, cw.n, duel.n, duel.v, dust-up.n, engage.v, engagement.n, fight.n, fight.v, fighting.n, firefight.n, fistfight.n, gunfight.n, hostility.n, infighting.n, row.n, scuffle.n, scuffle.v, shootout.n, showdown.n, skirmish.n, skirmish.v, spat.n, squabble.n, stalemate.n, standoff.n, strife.n, struggle.n, struggle.v, tiff.n, tussle.n, war.n, war.v, warfare.n, wrangling.n

## Attack  (frame id 424)

An Assailant physically attacks a Victim (which is usually but not always sentient), causing or intending to cause the Victim physical damage. A Weapon used by the Assailant may also be mentioned, in addition to the usual Place, Time, Purpose, Explanation, etc. Sometimes a location is used metonymically to stand for the Assailant or the Victim, and in such cases the Place FE will be annotated on a second FE layer. 'As soon as he stepped out of the bar he was set upon by four men in ski-masks.' 'Is he invading Iraq just to cover other shortcomings?' 'Then Jon-O's forces ambushed them on the left flank from a line of low hills.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Assailant | Core | The person (or other self-directed entity) that is attempting physical harm to the Victim. 'The mysterious fighter attacked the guardsmen with a sabre.' |
| Victim | Core | This FE is the being or entity that is injured by the Assailant's attack. 'The mysterious fighter attacked the guardsmen with a sabre.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Containing_event | Extra-Thematic | This FE denotes an event that occurs or state of affairs that holds at a time that includes the time during which the event or state of affairs reported by the target occurs and of which it is taken to be a part. |
| Depictive | Extra-Thematic | This FE is used for any Depictive phrase describing the state of the Assailant or Victim while the attack occurs. 'They attacked us in large numbers.' |
| Direction | Peripheral | This FE is used for expressions that indicate motion along a line from the deitic center towards a reference point (which may be implicit) that is neither the goal of motion nor a landmark along the way. 'They will no … |
| Duration | Peripheral | The amount of time that the attack lasts. 'The day-long attack crushed our morale.' |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. There are two somewhat distinct subgroups of sentence modifiers that cover this function. |
| Explanation | Extra-Thematic | A state of affairs that the Assailant is responding to that leads them to make an assault on the Victim. 'Gloria attacked Michael for the cause of Justice.' |
| Frequency | Extra-Thematic | The number (or description of the number) of times an attack takes place over a period of time. 'They attack daily.' |
| Iterations | Extra-Thematic | The frame element Iterations is used for expressions that indicate the number of times an event or state (of the kind denoted by the target in its clause) has taken place or held. Form: once, twice, Cardinal expression … |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), force (hard, softly), secondary effects (quietly, loudly), and general … |
| Means | Peripheral | An intentional action performed by the Assailant that accomplishes the assault. 'Japanese ambushed Americans by bombing Pearl Harbor.' |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. In addition, most … |
| Path | Peripheral | The Path refers to (a part of) the ground over which the Assailant travels. |
| Place | Peripheral | This FE identifies the place where the Assailant makes an assault on the Victim. 'Then Jon-O's forces ambushed them on the left flank from a line of low hills.' |
| Purpose | Peripheral | This FE identifies the purpose for which an Assailant attacks the Victim. 'John assaulted Thibault to prove his manhood.' |
| Re-encoding | Extra-Thematic | This FE presents the current frame as an integral part of a larger conceptualization expressed by another frame. The frame expressed by the target typically corresponds to a Means action within the frame expressed by … |
| Result | Extra-Thematic | The Result of the attack on the Victim by the Assailant. |
| Source | Peripheral | The starting-point of the motion of the Assailant or projectiles of the Assailant as they move toward the the Place that the Victim is occupying in the attack. In prepositional phrases, the prepositional object … |
| Time | Peripheral | This FE identifies the time when the Assailant attacks the Victim. 'As soon as he stepped out of the bar he was set upon by four men in ski-masks.' |
| Weapon | Peripheral | An entity used by the Assailant to cause damage to the Victim. 'The mysterious fighter attacked the guardsmen with a sabre.' |

**Frame relations** (super → sub)

- Inheritance: Attack → Besieging
- Inheritance: Attack → Counterattack
- Inheritance: Attack → Invading
- Inheritance: Attack → Suicide_attack
- Inheritance: Intentionally_affect → Attack
- Perspective_on: Hostile_encounter → Attack
- ReFraming_Mapping: Attack → Invading
- Using: Attack → Defending

**Lexical units** (38): SAF.n, airstrike.n, ambush.n, ambush.v, assail.v, assailant.n, assault.n, assault.v, attack.n, attack.v, attacker.n, bomb.v, bombard.v, bombardment.n, bombing.n, charge.n, charge.v, drive-by.n, fall (upon).v, fire.n, hit.v, incursion.n, infiltrate.v, infiltration.n, jump.v, lay (into).v, offensive.a, offensive.n, onset.n, onslaught.n, raid.n, raid.v, safire.n, set (upon).v, small arms fire.n, storm.v, strike.n, strike.v

## Judgment_communication  (frame id 219)

A Communicator communicates a judgment of an Evaluee to an Addressee. The judgment may be positive (e.g. praise) or negative (e.g. criticize), and this is indicated by the semantic types Positive and Negative attached to the lexical units. This frame does not contain words where Evaluee and the Addressee are necessarily the same . 'I commended his handling of the crisis.' 'Gaston denounced him to the committee.' This is distinct from the Judgment frame in that it involves the communication of an evaluation, rather than merely forming and holding a particular evaluation.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Communicator | Core | The Communicator uses language in the written or spoken modality to convey his or her evaluation of the Evaluee to another person. 'Jon belittled Madie to her colleagues.' |
| Evaluee | Core | A judgment is made about the Evaluee With verbs this FE is typically expressed as Object: 'Jon belittled Madie to her colleagues.' |
| Expressor | Core | Expressor is the body part or action by a body part that conveys the judgment made by the Communicator. 'She viewed him with a critical gaze.' |
| Medium | Core | Medium identifies the physical or abstract setting in which the evaluation is conveyed. 'Jon belittled Madie over the telephone.' 'The party denounced the General in vehement terms.' 'Mayor Quimby criticized the … |
| Reason | Core | Typically, there is a constituent expressing the Reason for the Communicator's judgment. It is usually a for-PP. 'Jon extolled Madie for her efforts.' It can also sometimes be expressed as an as-phrase, when that … |
| Topic | Core | Topic identifies the entity to which the proposition or propositions conveyed relate. 'Jon criticized Madie about her managerial style.' |
| Addressee | Peripheral | The Addressee hears the judgement from the Communicator. ' Jon belittled Madie to her colleagues.' |
| Degree | Extra-Thematic | This FE identifies the Degree to which the Communicator judges the Evaluee to be good or bad. |
| Depictive | Extra-Thematic | Depictive identifies any expression describing the state of a participant in the event. |
| Extent_of_acclaim | Extra-Thematic | The Extent_of_acclaim provides a description of the number or whereabouts of the Communicator. 'The movie met with international acclaim.' |
| Frequency | Extra-Thematic | This FE describes the frequency with which the specified communication occurs |
| Grounds | Extra-Thematic | The Grounds is the standard by which the Evaluee is judged. 'The proposal was critiqued on this basis.' |
| Internal_cause | Extra-Thematic | The emotional or physical state of the Communicator that leads to their communication of a judgment. 'He criticized his compatriots out of a deep hatred for all who are better than him.' |
| Manner | Peripheral | This FE identifies the Manner in which the judgmental communication occurs. |
| Means | Peripheral | This FE identifies the Means by which a judgmental communication is accomplished. |
| Place | Peripheral | Where the communication of the judgment takes place. 'He was belittled by his long-time friend in front of his family.' |
| Result | Extra-Thematic | This FE identifies the Result of an event. |
| Role | Extra-Thematic | Role is used for the capacity in which the Evaluee is judged, and is expressed in as-PPs. ' Jon belittled Madie as a nurse.' |
| Time | Peripheral | When the communication of the judgment takes place. 'He received critical acclaim last week.' |

**Frame relations** (super → sub)

- Inheritance: Judgment_communication → Bragging
- Inheritance: Judgment_communication → Judgment_direct_address
- ReFraming_Mapping: Judgment → Judgment_communication
- ReFraming_Mapping: Judgment_communication → Judgment
- ReFraming_Mapping: Judgment_communication → Judgment_direct_address
- ReFraming_Mapping: Judgment_direct_address → Judgment_communication
- See_also: Judgment → Judgment_communication
- Using: Judgment → Judgment_communication
- Using: Judgment_communication → Labeling
- Using: Statement → Judgment_communication

**Lexical units** (84): acclaim.n, acclaim.v, accusation.n, accuse.v, attack.n, attack.v, belittle.v, belittlement.n, belittling.n, blame.v, blast.v, castigate.v, censure.n, censure.v, charge.n, charge.v, cite.v, commend.v, commendable.a, commendation.n, commendatory.a, condemn.v, condemnation.n, critic.n, critical.a, criticism.n, criticize.v, critique.n, critique.v, damn.v, decry.v, denigrate.v, denigration.n, denigrative.a, denounce.v, denouncement.n, denunciation.n, denunciative.a, denunciatory.a, deprecate.v, deprecation.n, deprecative.a, deprecatory.a, deride.v, derision.n, disparage.v, disparagement.n, disparaging.a, dump.v, excoriate.v, excoriation.n, execrate.v, execration.n, execrative.a, extol.v, gibe.v, hail.v, harangue.n, harangue.v, kudos.n, laud.v, laudable.a, laudatory.a, malediction.n, maledictory.a, mock.v, mocking.a, pin.v, praise.n, praise.v, rave.v, recriminate.v, recrimination.n, remonstrance.n, remonstrate.v, reprehend.v, reprehension.n, ridicule.n, ridicule.v, rip.v, scathing.a, scoff.v, slam.v, tout.v

## Weapon  (frame id 426)

A Weapon is an artifact created specifically to cause harm or damage. In some cases, a Use, Material of construction, Part or Type may be more narrowly specified. 'Did you, or did you not, fire this gun with intent to harm my client?' 'Cyra tried to swing her sword to parry, but it was to heavy.' 'I investigated a specialist precious metal firearms manufacturer.' 'My neighbor, a member of the NRA since birth, has got an AK-47 fully automatic assault rifle.' 'Let 's just say that he 's the kind of guy who likes guns with hair triggers.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Weapon | Core | An entity prototypically used by a Wielder to cause damage. 'They used to shoot these long-range rifles with scopes and hit targets a mile away.' |
| Creator | Peripheral | The individual or group responsible for the creation of the Weapon. 'Colt pistols are, for some reason, considerably more likely to be missold in this fashion.' |
| Descriptor | Peripheral | A description or characteristic of the Weapon. 'He prefers to use a heavy bow for long-distance combat.' |
| Material | Peripheral | The substance that makes up the Weapon. |
| Name | Peripheral | The term used to refer to an Weapon. 'The sword Wirikidor was inadvertently cursed.' |
| Part | Peripheral | This FE identifies a part of the Weapon. This includes permanent, obligatory parts and mere attachments. 'I bought a rifle with a 2000-yard scope.' 'They practiced on swords with wooden blades first.' |
| Time_of_creation | Peripheral | The time at which a Weapon comes into existence. 'The fourth millennium BC spear has stimulated a lot of controversy.' |
| Type | Peripheral | This FE indicates what subtype of the general category the Weapon belongs to. 'Most people don't keep bastard swords in their livingrooms.' |
| Use | Peripheral | The type of activity that the Weapon is generally involved in. Often this can be considered a kind of Type specification also. 'a dueling pistol' 'anti-personnel mines' 'deer rifle' |
| Wielder | Peripheral | The person (or other sentient entity) that is using the Weapon. 'Reluctantly, he slid his guns back into their holsters.' |

**Frame relations** (super → sub)

- Inheritance: Artifact → Weapon
- Inheritance: Weapon → Improvised_explosive_device
- Using: Weapon → Ammunition
- Using: Weapon → Bearing_arms

**Lexical units** (69): AK-47.n, BW.n, C4.n, CW.n, EFP.n, ICBM.n, RPG.n, Scud-B missile.n, Scud-B.n, Scud-C missile.n, WMD.n, arms.n, arsenal.n, artillery.n, assault rifle.n, atomic bomb.n, atomic weapon.n, automatic weapon.n, ballistic missile.n, biological weapon.n, biological.a, bomb.n, bow.n, cannon.n, chemical weapon.n, chemical.a, club.n, crossbow.n, dynamite.n, explosive.a, explosive.n, firearm.n, flame-thrower.n, forty-four.n, garrotte.n, gat.n, grenade.n, gun.n, handgun.n, knife.n, machine-gun.n, mine.n, missile.n, mortar.n, mustard gas.n, nerve gas.n, nuclear weapon.n, nuclear.a, ordnance.n, phosgene.n, pistol.n, plastic explosive.n, revolver.n, rifle.n, rocket.n, shell.n, shooter.n, shotgun.n, six-shooter.n, small arms.n, spear.n, strategic nuclear weapon.n, strategic.a, sword.n, twenty-two.n, warhead.n, weapon of mass destruction.n, weapon.n, weaponry.n

## Prevarication  (frame id 287)

A Speaker communicates about a Topic in such a way as to mislead an Addressee, either by telling outright lies or by presenting a message in a misleading form. 'I lied to you about your Christmas present.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Addressee | Core | The person that receives a Message from the Speaker. 'You're kidding me!' 'Satan lies to everyone, including himself.' |
| Speaker | Core | The person who uses language in the written or spoken modality to convey a deceptive Message to the Addressee. 'Politicians do nothing but tell lies about money.' |
| Topic | Core | Topic is the entity to which the proposition or propositions relate, that they are about. 'You deceived me about the location of the diamonds.' |
| Degree | Peripheral | The extent to which the Speaker deceives the Addressee about the Topic. |
| Duration | Peripheral | The length of Time that the Speaker spends on the Topic. |
| Frequency | Peripheral | This FE describes how often the Speaker discusses the Topic with the Addressee. |
| Means | Peripheral | The (communicative) action performed by the Speaker in order to deceive the Addressee. |
| Place | Peripheral | The location at which the deception occurs. |
| Purpose | Peripheral | The goal of the Speaker's deceit of the Addressee |
| Time | Peripheral | The time at which the deception occurs. |

**Frame relations** (super → sub)

- Using: Communication → Prevarication
- Using: Prevarication → Front_for

**Lexical units** (26): bullshit artist.n, bullshit.v, deceive.v, deception.n, deceptive.a, dissemble.v, dissembler.n, equivocate.v, equivocation.n, fib.n, fib.v, fool.v, hoodwink.v, joke.v, kid.v, lie.n, lie.v, mislead.v, misrepresent.v, misrepresentation.n, prevaricate.v, prevarication.n, pull (someone's) leg.idio, pull the wool over (someone's) eyes.idio, shit.v, tell.v

## Intentional_deception  (frame id 2570)

A Deceiver performs some action so that the Victim ends up with an incorrect understanding about some Topic. The Means may be via communication, perceptual obscuration, or merely performing an action that the Victim will draw incorrect conclusions from. 'The government deceived the public last year about the existence of evidence in several corruption trials.' 'I can't believe they fooled me with that old trick.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Deceiver | Core | The person who acts so as to give the Victim an incorrect idea about a Topic. 'Politicians do nothing but deceive us about money.' |
| Topic | Core | The entity to which the misleading idea relates, what it is about. 'You deceived me about the location of the diamonds.' |
| Victim | Core | The person who receives an incorrect idea because of the Deceiver's actions. 'Practicing deception upon them , ' 'Sometimes it may be the case that the press itself stands as a monolith practicing deception upon the … |
| Means | Peripheral | The action performed by the Deceiver to fool the Victim. 'Chris misled me with her powers of persuasion.' |
| Place | Peripheral | The location at which the deception occurs. 'It's hard to fool someone in their own home.' |
| Time | Peripheral | The time at which the deception occurs. 'Some, looking for decent employment, said they were deceived soon after getting off the train.' |

**Frame relations** (super → sub)

- Inheritance: Deception_end → Intentional_deception
- Perspective_on: Deception_success → Intentional_deception
- Using: Intentional_deception → Trap

**Lexical units** (6): deceive.v, deception.n, fool.v, get.v, mislead.v, trick.v

## Manipulate_into_doing  (frame id 92)

A Manipulator gets his Victim to perform a Resulting_action against what their better judgment would have been at the time. The means by which the Manipulator overcomes or bypasses the Victim's resistance to act need not be linguistic expression. In some cases, the Goods may stand in for a Resulting_action of the Victim giving the Manipulator the Goods. '' 'Are you trying to tell me that Ace blackmailed you into becoming his lover?' 'Stephanopoulos skillfully cajoles him into keeping quiet.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Goods | Core | The FE goods is anything (including labor, time, or legal rights) that can be taken away. 'Leslie blackmailed the watch out of John.' |
| Manipulator | Core | The person who gets the Victim to act against their interest. |
| Resulting_action | Core | What the Manipulator intends to make the Victim do and the Victim actually does. |
| Victim | Core | The person who the Manipulator gets to do something they would not have done had no pressure or deception been applied. |
| Degree | Extra-Thematic | This FE identifies the Degree to which an event occurs. |
| Instrument | Peripheral | An entity that the Manipulator uses to get the Victim to perform the Resulting_action. |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including metaphorical force (hard, softly), secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may … |
| Means | Peripheral | An act of the Manipulator that enables them to alter the action of the Victim. 'I badgered her into coming by calling her every five minutes.' |
| Place | Peripheral | The location where the Manipulator manipulates the Victim. |
| Purpose | Peripheral | A state-of-affairs that the Manipulator is hoping to bring about by manipulating the Victim. |
| Time | Peripheral | The time when the manipulation occurs. |

**Frame relations** (super → sub)

- Inheritance: Intentionally_affect → Manipulate_into_doing
- Inheritance: Manipulate_into_doing → Talking_into
- Metaphor: Cause_motion → Manipulate_into_doing
- ReFraming_Mapping: Attempt_suasion → Manipulate_into_doing
- Using: Influencing_potential → Manipulate_into_doing

**Lexical units** (16): badger.v, blackmail.v, bully.v, cajole.v, cheat.v, con.v, deceive.v, defraud.v, dupe.v, flatter.v, fool.v, harass.v, hustle.v, lure.v, manipulate.v, trick.v

## Deception_success  (frame id 2573)

A Deceiver successfully causes a Victim to end up with incorrect beliefs about a Topic. The Victim comes to these beliefs from perceiving a Deception.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Deceiver | Core | The person who acts so as to give the Victim an incorrect idea about a Topic. |
| Phenomenon | Core | The Phenomenon, as percieved by the Victim, causes the Victim to have an incorrect understanding about a Topic. |
| Topic | Core | The entity to which the misleading idea relates, what it is about. |
| Victim | Core | The person who receives an incorrect idea because of the Deceiver's actions. |
| Means | Peripheral | The action performed by the Deceiver to fool the Victim. |
| Place | Peripheral | The location at which the deception occurs. |
| Time | Peripheral | The time at which the deception occurs. |

**Frame relations** (super → sub)

- Inheritance: Deception_end → Deception_success
- Perspective_on: Deception_success → Fall_for
- Perspective_on: Deception_success → Intentional_deception

**Lexical units** (2): deceit.n, deception.n

## Hiding_objects  (frame id 1673)

An Agent causes a Hidden_object to become perceptually inaccessible to potential perceivers by placing it in a Hiding_place or putting in place an Obstruction that screens the object. 'Therefore, as I passed the school, I hid the gun and holster in the mailbox' 'Gruenwald hid the money at a local garbage dump then retrieved it the following morning.' 'In later books Harry often tries to hide his scar with his hair. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the person who causes the Hidden_entity to be not perceptually accessible to potential perceivers. 'The deputy concealed the bayonet under his coat.' |
| Hidden_object | Core | The Hidden_object is the entity which is blocked from view. 'Michael Jackson gave wine to the 13-year-old cancer patient at the center of the molestation charges he's battling but concealed it inside a Coke can.' |
| Hiding_place | Core | The location in which the Hidden_object is placed so as not to be perceptually accessible. 'He had concealed the necklace behind him.' |
| Degree | Peripheral | The extent to which the Hidden_object becomes perceptually inaccessible. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the occurrence of the hiding event logically follows. |
| Manner | Peripheral | Any description of the intentional act which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may indicate … |
| Means | Peripheral | An action of the Agent that brings about the hiding of the Hidden_object. |
| Obstruction | Peripheral | The entity that the Agent uses to block the Hidden_object from being perceptible. 'She shrouded the tub with fabric featuring birds and flowers. ' |
| Place | Peripheral | The Place is the spatial setting in which the hiding event takes place. |
| Potential_observer | Extra-Thematic | The Potential_observer denotes a person who might perceive the Hidden_object if it was not hidden. 'The wife claims she hid the gun from him but retrieved it after he became abusive.' Phrases such as "from view" and … |
| Purpose | Peripheral | The state-of-affairs that the Agent hopes to bring about by hiding the Hidden_object. |
| Time | Peripheral | Time denotes the interval of time during which the Agent causes the Hidden_object to become hidden from perceptual access. |

**Frame relations** (super → sub)

- Causative_of: Hiding_objects → Eclipse
- Inheritance: Intentionally_affect → Hiding_objects

**Lexical units** (7): block.v, camouflage.v, conceal.v, cover.v, hide.v, mask.v, shroud.v

## Eclipse  (frame id 652)

An Obstruction blocks an Eclipsed entity partially or completely from view. The positions of the Obstruction and the Eclipsed entity are often reported relative to a Vantage_point. 'A small green bulb concealed behind the panel flashed on momentarily .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Eclipsed | Core | The entity which is blocked from view. 'The mists obscured the top of the tower.' |
| Obstruction | Core | The entity which blocks the Eclipsed entity from view. 'Wispy clouds shrouded the treetops.' |
| Degree | Peripheral | The extent to which the Eclipsed entity is blocked from view. 'The bungalow is completely obscured by thick foliage.' |
| Subregion | Extra-Thematic | The part of the Eclipsed entity which is blocked from view. 'The gazebo was screened by a hedge on one side.' |
| Vantage_point | Extra-Thematic | The position from which an observer, if an observer were present, would have their view of the Eclipsed entity blocked by the Obstruction. 'The gate screened the house from the road.' Phrases such as "from view" and … |

**Frame relations** (super → sub)

- Causative_of: Hiding_objects → Eclipse
- Using: Perception_experience → Eclipse

**Lexical units** (32): becloud.v, beclouded.a, befog.v, befogged.a, block.v, blot out.v, cloak.v, cloaked.a, conceal.v, concealed.a, cover.v, covered.a, eclipse.n, eclipse.v, enshroud.v, enshrouded.a, hidden.a, hide.v, mask.v, masked.a, obscure.v, obscured.a, obstruct.v, occlude.v, occlusion.n, occultation.n, screen.v, screened.a, shroud.v, shrouded.a, veil.v, veiled.a

## Success_or_failure  (frame id 1388)

An Agent has attempted to achieve a Goal, and the actual outcome of the Agent's action has been resolved, so that it either specifically matches the Agent's intent (e.g. success) or does not match it (e.g. failure). 'He pulled off his April Fool's Day prank by the barest of margins .' 'Unfortunately, we were n't successful. DNI' 'We failed miserably at getting the gay rights bill passed .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent makes an attempt to achieve a Goal. 'John managed a feeble smile.' |
| Circumstances | Extra-Thematic | This FE is applied to expressions which indicate the prevailing physical conditions for the event, or some concurrent states of affairs. 'And could anybody have succeeded under those conditions, using other methods?' |
| Containing_event | Extra-Thematic | This FE identifies an event during which the Agent attempts to achieve a Goal. 'He was successful in the Smithers v Burns case. ' |
| Degree | Peripheral | This FE identifies the Degree to which an attempt occurs. 'Your attempt at convincing me has utterly failed.' |
| Depictive | Extra-Thematic | The Depictive is a phrase which describes the Agent. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the success or failure logically follows. This often means that the Explanation causes the success or failure, but not in all cases. ' Kerry failed because of his … |
| Goal | Core-Unexpressed | The Goal is what the Agent attempts to achieve. 'If you don't succeed in your subterfuge, then report back for further orders.' |
| Means | Peripheral | This FE identifies the Means by which the Goal is achieved (or not). |
| Place | Peripheral | The place where an attempt succeeds or fails. 'On the bridge he succeeded in putting the wig on the corpse.' |
| Re-encoding | Extra-Thematic | Re-encoding presents the success or failure event as an integral part of a larger conceptualization expressed by another frame. |
| Role | Core-Unexpressed | A participant function in a particular event or in events of a particular kind. 'Benedikt was successful as a master brewer of beer.' |
| Time | Peripheral | This FE identifies the Time when the attempt succeeds or fails. |

**Frame relations** (super → sub)

- Causative_of: Thwarting → Success_or_failure
- Inheritance: Success_or_failure → Endeavor_failure
- Inheritance: Success_or_failure → Hit_or_miss
- Inheritance: Success_or_failure → Surviving
- Perspective_on: Result_of_attempt_scenario → Success_or_failure
- See_also: Success_or_failure → Personal_success
- Using: Success_or_failure → Accuracy
- Using: Success_or_failure → Finish_competition

**Lexical units** (12): ace.v, fail.v, failing.n, failure.n, get there.v, manage.v, miss.v, pull off.v, succeed.v, success.n, successful.a, unsuccessful.a

## Fairness_evaluation  (frame id 376)

In this frame an Action is evaluated with respect to how fairly, justly or equitably the Action affects the Affected_party. An Actor may also be identified, who performs the Action and may be characterized as fair, unfair, etc. based on how these actions affect the Affected_party. Grounds may also be identified. 'Smithers was being very fair about the distribution of supplies.' 'Smithers was being very fair about distributing the supplies.' 'The decision was fair to all involved.' ' It was not fair for the warning to remain in place.' 'The company was unfair to its loyal employees.' 'Smith received a fair trial.' ' The student loan system is socially unjust.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Action | Core | The Action is judged based on how just and appopriate it is to the Affected_party in a particular situation. |
| Actor | Core | The Actor is the individual who performs the Action and can thus be characterized with repsect to how that Action affects the Affected_party. |
| Affected_party | Core | The Affected_party's treatment is what determines the evaluation of the Actor's Action. |
| Grounds | Core | The Grounds is the event or state that requires some decision or action in response to it for which the Actor is judged. |
| Degree | Peripheral | The Degree is the extent to which the Action or Actor is evaluated as being fair or unfair. |
| Manner | Peripheral | A holistic characterization of the description of the Actor, including depictions of the Actor's state in terms of how it affects the entire description. 'You have been cruelly unfair to me !' |
| Parameter | Peripheral | The Parameter is the area in which the Action is judged. |

**Frame relations** (super → sub)

- Using: Social_interaction_evaluation → Fairness_evaluation

**Lexical units** (7): fair.a, fairly.adv, inequitable.a, unfair.a, unfairly.adv, unjust.a, unjustly.adv

## Political_locales  (frame id 195)

This frame covers words that name Locations as defined politically, or administratively. 'Berkeley is a wonderful city.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Locale | Core | A stable bounded area. It is typically the designation of the nouns of Locale-derived frames. 'There used to be a forest in that city' |
| Constituent_parts | Peripheral | The materials or Constituent_parts that make up a Locale. 'New York is a city of glass and steel' |
| Container_possessor | Peripheral | The location that the Locale is a part of. 'John spent several years wandering the villages of Romania.' |
| Descriptor | Peripheral | Any description, characteristic, or property of the Locale which is not covered by more specific FEs. 'He ruled the largest kingdom that ever existed.' |
| Name | Peripheral | ULTIMATELY TO BE REPLACED BY MULTIWORD TARGETS (in almost all cases). This FE is used for the Names of Locales. 'The city of Paris' 'The town of Smithersville' |
| Population | Peripheral | The people living in the jurisdiction of the locale. 'Stawiski was a city of laborers, of whom can be said ?You shall eat your bread by the sweat of your brow? ' |
| Relative_location | Peripheral | A place that a Locale is located with respect to. 'All the cities near the San Francisco bay are large.' |

**Frame relations** (super → sub)

- Inheritance: Locale_by_ownership → Political_locales
- Inheritance: Political_locales → Foreign_or_domestic_country
- Inheritance: Political_locales → Relational_political_locales
- Using: Leadership → Political_locales
- Using: Political_locales → Economy
- Using: Political_locales → People_by_jurisdiction

**Lexical units** (42): barony.n, borough.n, city-state.n, city.n, commonwealth.n, country.n, county.n, diocese.n, district.n, duchy.n, empire.n, federal.a, fiefdom.n, global.a, international.a, internationally.adv, jurisdiction.n, kingdom.n, land.n, local.a, locality.n, megalopolis.n, metropolis.n, multinational.a, municipal.a, municipality.n, nation.n, national.a, parish.n, principality.n, province.n, provincial.a, realm.n, state [internal].n, state [sovereign].n, territorial.a, territory.n, town.n, township.n, village.n, viscountcy.n, world.n

## Beat_opponent  (frame id 2074)

A Winner has victory over an Loser. 'He always beats me at chess.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Loser | Core | The individual or individuals that get beat by the Winner. |
| Winner | Core | The individual or individuals who beat the Loser. |
| Circumstances | Extra-Thematic | The state of the world when the Winner beats the Loser. |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the winning event operates (often denoted by words such as "officially," "formally," "technically," etc.). |
| Competition | Peripheral | The event in which the Competition competes. |
| Degree | Peripheral | A qualitative measure of how much the Winner beat the Loser. |
| Depictive | Extra-Thematic | This FE describes a participant of the state of affairs introduced by the target as being in some state during the action. |
| Event_description | Extra-Thematic | This FE applies to appraisals of the event, typically a judgment of its expectedness, or a description of the state-of-affairs introduced by the winning event. |
| Explanation | Extra-Thematic | The reason why the Winner has victory over the Loser. |
| Frequency | Extra-Thematic | How often the Winner beats the Loser. |
| Iterations | Extra-Thematic | The frame element Iterations is used for expressions that indicate the number of times the Winner beats the Loser. |
| Manner | Peripheral | Any description of the Winner or Loser which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, loudly), and general descriptions … |
| Margin | Peripheral | The amount by which the Winner 's and Loser 's Scores differ. |
| Means | Peripheral | An action of the Winner or Loser that makes the beating event possible. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Period_of_iterations | Extra-Thematic | The length of time from when winning events began to be repeated to when they stopped. |
| Place | Peripheral | The location where the Winner has victory Loser. |
| Prize | Peripheral | A socially and/or monetarily significant entity which is given to a Winner according to Score or Rank. |
| Rank | Peripheral | The rank (according to Score) that a Winner acheives. |
| Re-encoding | Extra-Thematic | The frame expressed by the target typically corresponds to a Means action within the frame expressed by the Re-encoding, but not necessarily. |
| Result | Extra-Thematic | The state-of-affairs that prevails as a result of the Winner beating the Loser. |
| Score | Peripheral | A quantity whereby progress is measured during the game, and Rank and Prizes are awarded to the Winner afterward. |
| Time | Peripheral | When the Winner has victory over the Loser. |
| Venue | Peripheral | This FE is for the named venue of a competition, particularly when the place has been built for the purpose of a competition. |

**Frame relations** (super → sub)

- Using: Win_prize → Beat_opponent

**Lexical units** (9): beat.v, defeat.n, defeat.v, demolish.v, prevail.v, rout.n, rout.v, trounce.v, upend.v

## Competition  (frame id 241)

This frame is concerned with the idea that people (Participant_1, Participant_2, or Participants) participate in an organized, rule-governed activity (the Competition) in order to achieve some advantageous outcome (often the Prize). Rank and Score are different criteria by which the degree of achievement of the advantageous outcome is judged. 'He and I played tennis.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Competition | Core | This FE is used for the name of the competition. 'Jo played in the foosball tournament' |
| Participant_1 | Core | This FE identifies the first (or only) participant in a competition. 'Jo played the lottery every day.' |
| Participant_2 | Core | This FE identifies the second participant in a competition. 'Jo played Leslie at tennis.' |
| Participants | Core | This FE is used for plural NP participants in a competition. 'Jo and Leslie played tennis.' |
| Degree | Peripheral | This FE describes the intensity of competition. |
| Duration | Peripheral | This FE is used to describe the length of time over which competition occurs. |
| Frequency | Extra-Thematic | This FE expresses how often the Competition occurs. |
| Manner | Peripheral | The way the Participants compete. |
| Means | Peripheral | The action the Participants (or Participant_1) are involved in that constitutes a Competition. 'They played by seeing who could get the ball to the far side of the parking lot.' |
| Place | Peripheral | Where the event takes place. A constituent tagged as Place may require annotation on a secondary FE-layer. 'First layer: John's first competition at Wimbledon astonished the crowd.' 'Second layer: John's first … |
| Prize | Extra-Thematic | This FE indicates a prize won in a competition. 'John was competing for a bronze medal.' |
| Purpose | Extra-Thematic | This FE is used to describe the intended outcome of the competition. |
| Rank | Peripheral | This FE is used for the ranked results of a competition, and is translatable into a numerical value. 'Jo came in third.' |
| Score | Peripheral | This FE is used for the score in a game. 'The Yankees won the game 2 to 0.' EX: The Yankees won the game by two points. |
| Time | Peripheral | The period of time when the Competition occurs. |
| Venue | Peripheral | This FE is for the named venue of a competition, particularly when the place has been built for the purpose of a competition. 'The Mets will play at the ball park on Sunday.' 'The Mets will play at Shea Stadium tonight.' |

**Frame relations** (super → sub)

- ReFraming_Mapping: Competition → Finish_competition
- Subframe: Competition → Finish_competition
- Using: Competition → Alliance
- Using: Competition → Sports_jargon
- Using: Intentionally_act → Competition

**Lexical units** (9): challenge.n, compete.v, competition.n, competitive.a, competitor.n, play.v, player.n, rival.n, rivalry.n

## Predicting  (frame id 425)

A Speaker states or makes known a future Eventuality on the basis of some Evidence. Instead of (or in addition to) a Speaker, a Medium may also be mentioned. Likewise, a more general Topic may be stated instead of an Eventuality. ' The Weather Centre predicted that it would be warmer but wet for the weekend.' 'Another seer who forecast a Tory majority -- without compromising his impartiality -- was Sir Robin Day .' 'Based on current calculations, the European market is forecast to grow 18.1% by the end of next fiscal year.' 'The website claimed to prophesy what the world would be like in the near-future.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Eventuality | Core | This FE marks expressions that indicate an event or state that is predicted to occur or hold at a future time. A single Eventuality may be expressed discontinuously in a raising construction. This FE is also used for … |
| Medium | Core | The Medium is the physical entity or channel used by the Speaker to transmit the prediction. 'The events that would occur over the next several years had been predicted in the Bible.' 'Her texts predict the future.' |
| Speaker | Core | The Speaker makes a prediction. 'The institute forecast an increase in leisure spending of 15 per cent.' |
| Topic | Core | The Topic is the subject matter to which the prediction pertains. It is normally expressed as a PP Complement headed by about. |
| Accuracy | Peripheral | This FE indicates the Accuracy of the prediction. 'Compary president Randall Johnson predicted correctly that a major reworking of infrastructure would be necessary.' 'It is hard to forecast with a high degree of … |
| Descriptor | Extra-Thematic | Descriptor describes a characteristic of the Eventuality. |
| Evidence | Peripheral | Evidence marks expressions that denote a set of facts on the basis of which the Speaker makes the prediction. 'Violence was predicted on the basis of disorder at demonstrations in Paris.' |
| Manner | Peripheral | Manner marks any description of the Speaker's prediction making that is not covered by more specific FEs. 'Smeagol confidently predicted that he would win the race.' 'One commentator rashly predicted that the fad for … |
| Means | Peripheral | An act whereby the Speaker makes a prediction. 'My regular psychic fortells my future by examining the configuration of spent coffee grounds.' |
| Place | Peripheral | The Place where the Speaker makes the prediction. ' Greenman predicted at a small dinner party that the market would rise again.' |
| Time | Peripheral | This FE identifies the Time when the prediction is made. 'John predicted last year that he would be finished by October.' |
| Time_of_eventuality | Peripheral | This FE marks expressions that indicate for what future time an Eventuality is predicted. ' Cocoa stocks reached a record 1.2m tonnes and a seventh year of surplus is forecast for the year to September 1991.' |

**Frame relations** (super → sub)

- Inheritance: Statement → Predicting
- Using: Expectation → Predicting

**Lexical units** (10): claim.v, forecast.v, foretell.v, predict.v, prediction.n, prognosticate.v, prophecy.n, prophesy.v, soothsay.v, vaticinate.v

## Becoming_aware  (frame id 20)

Words in this frame have to do with a Cognizer adding some Phenomenon to their model of the world. They are similar to Coming-to-believe words, except the latter generally involve reasoning from Evidence. '' The words in this frame take direct objects that denote entities in the world, and indicate awareness of those entities, without necessarily giving any information about the content of the Cognizer's belief or knowledge. These words also resemble perception words, since creatures often become aware of things by perceiving them. 'Later that night, they found the barely-alive victim inside the Red Hall estate flat.' 'Almost immediately, the police discovered the wrought-iron crypt gate swinging open.' 'In the bag on the tableI could vaguelydiscern two bottles of wine and several cartons of cakes and other goodies.' 'People passing through recognize it from afar, by the clouds of coal dust darkening the air.' General Grammatical Observations: Passive forms of the verbs in this frame can occur with extraposed clauses expressing Phenomenon: 'That year it was discovered that consumers preferred the older model.' 'It is not always recognized how much work goes into a dinner party.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The Cognizer is the person who becomes aware of a Phenomenon. It is normally expressed as an External Argument. 'Pat discovered a great little restaurant in Soho.' |
| Instrument | Core | The Cognizer uses an Instrument to (enable themselves to) become aware of the Phenomenon. In some cases, the Instrument may appear in subject position. 'Olson says the deputy came out to the farm and detected a … |
| Means | Core | This FE identifes the Means by which the Cognizer becomes aware of the Phenomenon. 'By opening the book to page 10, you will find the Van Eerdens' number.' |
| Phenomenon | Core | Thm Phenomenon is the entity or situation in the world of which a Cognizer becomes aware. It is normally expressed as an Object: 'Pat discovered a great little restaurant in Soho.' |
| Topic | Core | Topic indicates the general field within which the Phenomenon is found. 'Scientists attempt to make discoveries about the laws of nature.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Degree | Peripheral | This FE identifies the Degree to which becoming aware is occurring. 'Sue could faintly discern the shape of a skull under Cheeks ' plump face.' |
| Evidence | Peripheral | The Evidence is some fact that allows the Cognizer to become aware of something. It is normally expressed with PP-from: 'We discovered from their job performance that they were well-trained.' |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Frequency | Extra-Thematic | his frame element is defined as the number of times an event occurs per some unit of time. A Frequency expression answers the question how often. |
| Ground | Peripheral | The Ground is the background or context against which a Cognizer becomes aware of a Phenomenon. It is normally expressed by a locative PP: 'Pat discovered a great little restaurant in Soho.' 'I noticed a hint of … |
| Manner | Peripheral | This FE identifes the Manner in which becoming aware occurs. 'Pupils quickly discern what is acceptable to the teacher and merely aim to fulfil those expectations.' |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. In addition, most … |
| Period_of_iterations | Extra-Thematic | This FE is minimally distinct from Duration and Duration_of final_state in that the clause described is conveyed to be iterative. |
| Purpose | Peripheral | The goal that the Cognizer has in mind, which they believe to be accomplishable by finding the Phenomenon. |
| State | Peripheral | The State indicates the state or situation of the Phenomenon at the time when the Cognizer becomes aware of it. It is normally expressed by a Predicate expression (e.g. a PP or a participial VP): 'We discovered the … |
| Time | Peripheral | This FE identifies the Time when the Cognizer becomes aware of the Phenomenon. 'Robbie had wondered if they would be able to find the path at night.' |

**Frame relations** (super → sub)

- Inheritance: Perception → Becoming_aware
- ReFraming_Mapping: Becoming_aware → Coming_to_believe
- Using: Becoming_aware → Scrutiny

**Lexical units** (28): chance (across).v, chance (on).v, come (across).v, come (upon).v, descry.v, detect.v, discern.v, discover.v, discovery.n, encounter.v, espy.v, fall (on).v, find (oneself).v, find out.v, find.v, happen (on).v, learn.v, locate.v, note.v, notice.v, observe.v, perceive.v, pick up.v, recognize.v, register.v, spot.v, spy out.v, tell.v

## Reasoning  (frame id 308)

An Arguer presents a Content, along with Support, to an Addressee. The Content may refer elliptically to a course of action or it may refer to a proposition that the Addressee is to believe. Some lexical units (e.g. "prove") indicate the speaker's belief about the Content.'Jan argued that the evidence was inadmissable.''Jan argued against the admissability of the evidence.''Jan proved that the evidence was inadmissable.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Arguer | Core | The Arguer presents the Content before the Addressee.'Jan argued that the evidence was inadmissable.' |
| Content | Core | The Arguer wants the Addressee to entertain the Content, which can be a proposition to be believed or a course of action to be taken, based on the Support presented.'Jan argued that the evidence was inadmissable.' |
| Addressee | Peripheral | Addressee is the entity before whom the Arguer presents a Content. 'Jan argued to the court that the evidence was inadmissable.' |
| Degree | Peripheral | This FE identifies the Degree to which an arguing event occurs.'Jan argued the defendant's innocence beyond a shadow of a doubt.' |
| Depictive | Extra-Thematic | Depictive identifies a phrase describing a participant in an action.'Jan argued that the evidence was inadmissable in a tuxedo.' |
| Duration | Peripheral | The period of time for which the Arguer presents his or her reasoning to the Addressee. 'He argued for hours that chess is a sport ' |
| Group | Extra-Thematic | An entity related to the Content. |
| Manner | Peripheral | This FE identifes the Manner in which an Arguer argues.'Jan argued convincingly that the evidence was inadmissable. ' |
| Means | Peripheral | This FE identifies the Means by which an Arguer presents Content to an Addressee.'Jan argued the evidence was admissable by waving the warrant in the air.' |
| Medium | Peripheral | This FE identifies the physical or abstract setting in which the Content is conveyed.'Jan argued in writing that the evidence was inadmissable.' |
| Place | Peripheral | This FE identifies the location where an argument is made by an Arguer. 'The young men will be arguing their policies in the school auditorium.' |
| Result | Extra-Thematic | This FE identifies the Result of an arguing event. |
| Support | Peripheral | Support lends epistemic support to a claim, or provides a reason for a course of action.'Jan argued that gun was inadmissable as evidence because the police didn't have a search warrant.' |
| Time | Peripheral | The Time at which an Arguer makes an argument for the Content. ' The government argued in August that the prisoners should not be released' |

**Frame relations** (super → sub)

- Using: Communication → Reasoning

**Lexical units** (11): argue.v, argument.n, case.n, demonstrate.v, demonstration.n, disprove.v, polemic.n, prove.v, reason.v, reasoning.n, show.v

## Shapes  (frame id 328)

This frame contains words which describe the dimensional extent and Shape of a Substance. These words do not make reference to a Part-whole relationship. There can also be a descriptor of the Shape, Shape_prop. 'She held a square of cloth .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Shape | Core | This is the Shape that the Substance is in.'I ate a stick of butter.' |
| Substance | Core | A Substance of which pieces can be extracted.'Sue ate a big square of cake.' |
| Count | Peripheral | The number of units of the measured Substance. 'Serena found two squares of coth in the cabinet.' |
| Shape_prop | Peripheral | This describes a property of the Shape, e.g. it's size.'Sue ate a big square of cake.' |

**Frame relations** (super → sub)

- Inchoative_of: Go_into_shape → Shapes
- Using: Bounded_entity → Shapes

**Lexical units** (23): ball.n, circle.n, circular.a, coil.n, cube.n, curve.n, ellipse.n, expanse.n, length.n, line.n, oval.n, ribbon.n, round.a, row.n, shape.n, sheet.n, square.n, stick.n, stretch.n, strip.n, triangle.n, v.n, wedge.n

## Suitability  (frame id 368)

This Frame is concerned with evaluating an Evaluee as being suitable for a Purpose or a User, presupposing some choice that is being made about which Evaluee to use for the Purpose or User. An LU like suitable.a thus implies that, given a particular Purpose or User, the Evaluee is one which could be or ought to be chosen. The Evaluee may be deemed suitable to a greater or lesser Degree. This frame has some similarity to the compatibility frame where two Items are evaluated with respect to their compatibility with each other against some background. '(1) We need to build more houses suitable for local residents.' '(2) These chips are not verysuitable for parallel processing. ' '(3) We are not sure about the Cathedral's suitability for Philharmonic concerts.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Evaluee | Core | This Frame Element marks constituents expressing the entity that is judged to be more or less suitable for some Purpose or User. 'Being a project leader is not a job for which everybody is suited.' |
| Purpose | Core | This Frame Element marks constituents that express the Purpose for which the Evaluee is judged to be suitable or unsuitable. 'We need to plan more buildings suitable for disabled people.' |
| User | Core | This FE marks expressions that indicate a User to whom |
| Degree | Peripheral | This Frame Element marks constituents that express the Degree to which the Evaluee is suitable for the Context. 'Please advise on the most suitable design ' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Suitability

**Lexical units** (17): appropriate.a, become.v, correct.a, fit.a, fit.v, fitting.a, inappropriate.a, proper.a, right.a, suit.v, suitability.n, suitable.a, suitableness.n, suited.a, unsuitability.n, unsuitable.a, unsuitableness.n

