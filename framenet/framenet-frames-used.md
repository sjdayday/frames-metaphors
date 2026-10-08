# FrameNet 1.7 frames used in frames-metaphors annotations

Generated from the FrameNet 1.7 release as distributed with NLTK (`framenet_v17`), Berkeley FrameNet, ICSI. Frame and FE definitions are FrameNet's own text, lightly whitespace-normalized; FE definitions are truncated. Regenerate with `scripts/fn_dump.py`.

## Abandonment  (frame id 2031)

An Agent leaves behind a Theme effectively rendering it no longer within their control or of the normal security as one's property. 'Carolyn abandoned her car and jumped on a red double decker bus.' 'Perhaps he left the key in the ignition' 'Abandonment of a child is considered to be a serious crime in many jurisdictions.' There are also metaphorically used examples: 'She left her old ways behind .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the person who acts to leave behind the Theme. |
| Theme | Core | The Theme is the entity that is relinguished to no one from the Agent's possession. |
| Degree | Peripheral | The extent to which the Agent leaves the Theme behind. |
| Depictive | Extra-Thematic | The FE Depictive describes the Agent during the abandoning event. |
| Duration | Peripheral | For what expanse of time the Agent has given up the Theme. |
| Event_description | Extra-Thematic | A description of the event as a whole. |
| Explanation | Extra-Thematic | Explanation denotes a proposition from which the act of abandonment logically follows. |
| Manner | Peripheral | The style in which the Agent gives up the Theme. |
| Means | Peripheral | An action performed by the Agent that accomplishes the action indicated by the target. |
| Place | Peripheral | The location where the Agent gives up the Theme. |
| Purpose | Peripheral | The purpose for which the Agent abandons the Theme. |
| Time | Peripheral | When the Agent gives up the Theme. |

**Frame relations** (super → sub)

- Inheritance: Intentionally_affect → Abandonment

**Lexical units** (5): abandon.v, abandoned.a, abandonment.n, forget.v, leave.v

## Activity  (frame id 124)

This is an abstract frame for durative activities, in which the Agent enters an ongoing state of the Activity, remains in this state for some Duration of Time, and leaves this state either by finishing or by stopping. The Agent's Activity should be intentional. This frame is intended mostly for the inheritance of common FEs, and to provide the frame structure for the beginning, ongoing, finish, or stop stage of an Activity, each of which constitutes a subframe of this frame. This frame should be compared to the Process frame.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is engaged in the Activity. |
| Activity | Core-Unexpressed | This FE identifies the Activity in which the Agent is engaged. |
| Duration | Peripheral | This FE identifies the amount of Time an Activity takes. |
| Manner | Peripheral | Any description of the activity which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may also indicate salient … |
| Place | Peripheral | This FE identifies the Place where the Activity occurs. |
| Time | Peripheral | This FE identifies the Time when the Activity occurs. |

**Frame relations** (super → sub)

- Inheritance: Activity → Apply_heat
- Inheritance: Process → Activity
- Subframe: Activity → Activity_abandoned_state
- Subframe: Activity → Activity_done_state
- Subframe: Activity → Activity_finish
- Subframe: Activity → Activity_ongoing
- Subframe: Activity → Activity_pause
- Subframe: Activity → Activity_paused_state
- Subframe: Activity → Activity_prepare
- Subframe: Activity → Activity_ready_state
- Subframe: Activity → Activity_resume
- Subframe: Activity → Activity_start
- Subframe: Activity → Activity_stop

**Lexical units** (0): 

## Activity_finish  (frame id 165)

An Agent finishes an Activity, which can no longer logically continue. This frame is a subframe of Activity. '' 'Jason completed grading the papers late Sunday night.' 'Upon completion of the final exam, Ava tossed out her notes. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | This FE identifies the Activity that the Agent has finished. |
| Agent | Core | This FE identifies the Agent who has finished an Activity. |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Co-timed_event | Extra-Thematic | This FE identifies the last Co-timed_event of the finished Activity.'They finished the peace march with a prayer.' |
| Containing_event | Extra-Thematic | This FE identifies an event during which the Agent finishes the Activity. |
| Degree | Peripheral | This FE describes the how near the agent is to finishing. |
| Depictive | Extra-Thematic | This FE identifies the Depictive phrase describing an actor or an undergoer of an action. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Manner | Peripheral | This FE identifies the Manner an Agent is engaged in finishing an Activity. |
| Means | Peripheral | This FE identifies the Means by which an Agent finishes an Activity. |
| Place | Peripheral | This FE identifies the Place where the Agent finishes the Activity. |
| Purpose | Peripheral | This FE identifies the Purpose for which an Agent finishes for an Activity. |
| Result | Extra-Thematic | This FE identifies the Result of finished Activity. |
| Time | Peripheral | This FE identifies the Time when the Activity finishes. |

**Frame relations** (super → sub)

- Inheritance: Activity_finish → Finish_game
- Inheritance: Intentionally_act → Activity_finish
- Inheritance: Process_end → Activity_finish
- Precedes: Activity_finish → Activity_done_state
- Precedes: Activity_ongoing → Activity_finish
- ReFraming_Mapping: Activity_finish → Activity_stop
- Subframe: Activity → Activity_finish

**Lexical units** (7): complete.v, completion.n, conclude.v, finish.v, graduate.v, tie up.v, wrap up.v

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

## Activity_paused_state  (frame id 181)

An Agent remains in a particular stage of an Activity, without progressing in the activity.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | The overall event that the Agent is involved in. |
| Agent | Core | This FE identifies the Agent in the paused State of an activity. |
| Duration | Peripheral | The length of time that the Activity does not resume. |
| Time | Peripheral | The point at which the Agent |

**Frame relations** (super → sub)

- Inheritance: Process_stopped_state → Activity_paused_state
- Precedes: Activity_pause → Activity_paused_state
- Precedes: Activity_paused_state → Activity_resume
- Precedes: Activity_stop → Activity_paused_state
- Subframe: Activity → Activity_paused_state

**Lexical units** (0): 

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

## Activity_start  (frame id 146)

An Agent initiates the beginning of an ongoing Activity in which he will be continuously involved. '' 'At the same time, city-states began to grow in influence on the southern Greek mainland.' 'Naturally, I started crying to get out of work.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | This FE identifies the Activity that an Agent starts. |
| Agent | Core | This FE identifies the being that starts the intentional Activity. |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Co-timed_event | Extra-Thematic | This FE identifies the first Co-timed_event of the started Activity.'The peace march started with a prayer.' |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the target operates (often denoted by words such as "officially," "formally," "technically," etc.). |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Containing_event | Extra-Thematic | This FE identifies an event during which the Agent starts the Activity. |
| Depictive | Extra-Thematic | This FE identifies the Depictive phrase describing the actor or undergoer of an action. |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. There are two somewhat distinct subgroups of sentence modifiers that cover this function. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. I |
| Manner | Peripheral | This FE identifies the Manner in which an Agent starts an Activity. |
| Means | Peripheral | This FE identifies the Means by which an Agent starts an Activity. |
| New_situation | Extra-Thematic | A consecutive event to the starting of the Activity of the Agent. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. In addition, most … |
| Place | Peripheral | This FE identifies the Place where the Agent starts an Activity. |
| Purpose | Peripheral | This FE identifies the Purpose for which an Agent engages in a starting Activity. |
| Time | Peripheral | This FE identifies the Time when the Agent starts an Activity. |

**Frame relations** (super → sub)

- Inheritance: Process_start → Activity_start
- Precedes: Activity_ready_state → Activity_start
- Precedes: Activity_start → Activity_ongoing
- ReFraming_Mapping: Activity_start → Cause_to_start
- ReFraming_Mapping: Traversing → Activity_start
- Subframe: Activity → Activity_start
- Using: Eventive_affecting → Activity_start

**Lexical units** (14): begin.v, beginner.n, commence.v, enter.v, get started.v, initiate.v, launch (into).v, neophyte.n, open.v, set about.v, start.v, strike up.v, swing (into).v, take up.v

## Activity_stop  (frame id 166)

An Agent ceases an Activity without completing it. '' 'After the lawsuit, the company stopped producing the once very profitable toy.' 'The rugby club terminated negotiations with Argyll in September 1988.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | This FE identifies Agent that stops the Activity. |
| Activity | Core-Unexpressed | This FE identifies the Activity that the Agent stops. |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Co-timed_event | Extra-Thematic | This FE identifies the last Co-timed_event of the stopped Activity. 'With the arrival of the bishop, everyone stopped working.' |
| Containing_event | Extra-Thematic | This FE identifies an event during which the Agent stops the Activity. |
| Degree | Peripheral | This FE describes the completeness of stopping. |
| Depictive | Extra-Thematic | This FE is used for a Depictive phrase describing the actor or undergoer of an action. |
| Duration | Peripheral | This FE identifies the length of Time during which the Activity is stopped. |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. |
| Explanation | Extra-Thematic | The reason the Agent stops the Activity. |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. A Frequency expression answers the question how often. It is to be distinguished from Iteration, which pertains simply to the … |
| Manner | Peripheral | This FE identifies the Manner in which the Agent stops the Activity. |
| Means | Extra-Thematic | This FE identifies the Means by which the Agent stops the Activity. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Place | Peripheral | This FE identifies the Place where the Agent stops the Activity. |
| Purpose | Extra-Thematic | This FE identifies the Purpose for which an Agent stopped the Activity. |
| Re-encoding | Extra-Thematic | This FE presents the current frame as an integral part of a larger conceptualization expressed by another frame. |
| Result | Extra-Thematic | This FE identifies the Result of the stopped Activity. |
| Time | Peripheral | This FE identifies the Time when the Agent stops the Activity. |

**Frame relations** (super → sub)

- Inheritance: Activity_stop → Halt
- Inheritance: Process_stop → Activity_stop
- Precedes: Activity_ongoing → Activity_stop
- Precedes: Activity_stop → Activity_abandoned_state
- Precedes: Activity_stop → Activity_paused_state
- ReFraming_Mapping: Activity_finish → Activity_stop
- Subframe: Activity → Activity_stop
- Using: Eventive_affecting → Activity_stop

**Lexical units** (7): abandon.v, cease.v, discontinue.v, halt.v, quit.v, stop.v, terminate.v

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

## Adopt_selection  (frame id 1590)

An Agent has an Attribute which can take different Values, and the Agent selects and then begins to use some Value for that Attribute. The Attribute includes both physical (shape, color) and abstract (belief, practice) types. For some LUs in this frame, it is common for only the Value to be expressed, with the Attribute implicit. (Often this implicit attribute can be given second-layer expression on the Value. Note that such second-layer annotation should be assumed in the first two examples below.) 'They scoff at their opponents and assume an air of superior knowledge' 'There are times when teachers should adopt a neutral stance in discussion of morally controversial issues.' 'A person does not have to make the statement "I adopt this as my position" to do so.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent selects a Value for his/her Attribute and begins to use it. 'Some organizations, like the Sierra Club, have adopted a position of neutrality on US immigration policies.' |
| Attribute | Core | The Attribute of the Agent can take on several Values, selected by the Agent . 'The Council of Constance (1414-18) adopted conciliarism as a stance, hoping that it would permit the election of a pope acceptable to both … |
| Value | Core | The Value, chosen and made effective by the Agent, specifies the Attribute. 'He crammed his cap back again into his pocket and re-entered the office, assuming an air of absentmindedness.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the target operates (often denoted by words such as "officially," "formally," "technically," etc.). This may or may not reflect the actual reality of … |
| Containing_event | Extra-Thematic | This FE denotes an event that occurs or state of affairs that holds at a time that includes the time during which the event or state of affairs reported by the target occurs and of which it is taken to be a part. |
| Depictive | Extra-Thematic | This FE describes a participant of the state of affairs introduced by the target as being in some state during the action. |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of a continuous situation (the one denoted by the target) to its end. In many cases, the continuous situation is a dynamic action which is ongoing, while in others … |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. A Frequency expression answers the question how often. |
| Instrument | Peripheral | The instument through which an Agent adopts a Value for an Attribute. |
| Manner | Peripheral | A description of the adoption of a position which is not classified under more specific descriptions, including comparisons to other events (similarly), rates of adoption (slowly), and descriptions of the Agent which … |
| Means | Peripheral | The Means by which an Agent adopts a Value for an Attribute. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Place | Peripheral | This FE identifies the Place where the Agent has the Attribute which can take different Value. |
| Purpose | Peripheral | This FE identifies the Purpose for which an Agent adopts the Value of the Attribute. |
| Re-encoding | Extra-Thematic | This FE presents the current frame as an integral part of a larger conceptualization expressed by another frame. |
| Role | Extra-Thematic | This FE identifies the role filled by a particular participant of the clause headed by the target. In so doing, it relates the state of affairs evoked by the target to another background state of affairs by indicating … |
| Time | Peripheral | The time period when the Agent selects and begins to put into effect the Value. 'On January 1, 2001, our nation will adopt the US dollar as our official currency.' |

**Frame relations** (super → sub)

- Using: Choosing → Adopt_selection

**Lexical units** (3): adopt.v, assume.v, embrace.v

## Affirm_or_deny  (frame id 2974)

A Speaker uses language to affirm or deny the truth of a Message to some Addressee. Instead of (or in addition to) a Speaker, a Medium may also be mentioned. Likewise, a Topic may be stated instead of a Message. 'She affirmed her loyalty to the cause.' 'He denied that he had ever believed in the existence of God.' 'BBC News confirmed the story about the refugees.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Medium | Core | The Medium is the physical entity or channel used by the Speaker to transmit the Message. |
| Message | Core | The Message identifies the content whose truth the Speaker is affirming or denying. It can be expressed as a clause or as a noun phrase. 'They refute the criticisms that they are only interested in power and money.' … |
| Speaker | Core | The Speaker is the sentient entity affirming or denying the truth of the Message (this can be spoken or written). It is normally expressed as the External Argument of the predicative uses of the target word, or as the … |
| Topic | Core | The Topic is the subject matter to which the Message pertains. It is rarely mentioned in constructions with verbal targets, and is much more common with nominal targets, where it is usually expressed as a PP Complement … |
| Addressee | Extra-Thematic | The Addressee is the person to whom the truth of the Message is affirmed or denied. |
| Containing_event | Extra-Thematic | This FE identifies an event during which the Speaker affirms or denies the truth of the Message. |
| Degree | Extra-Thematic | Degree selects some gradable attribute and modifies the expected value for it. |
| Depictive | Extra-Thematic | The state of the Speaker while he/she affirms or denies the Message. |
| Event_description | Extra-Thematic | In general, Event_description is used for phrases that describe the clause of the target as a whole - here, the Message event. |
| Frequency | Extra-Thematic | Frequency is defined as the number of times an event occurs per some unit of time. |
| Internal_cause | Peripheral | The emotional or physical state of the Speaker that leads to their affirmation or denial of the Message. |
| Iterations | Extra-Thematic | Iterations is used for expressions that indicate the number of times an event or state (of the kind denoted by the target in its clause) has taken place or held. |
| Manner | Peripheral | Manner describes the way in which the Speaker affirms or denies a Message. |
| Means | Peripheral | Means expresses the act whereby the Speaker affirms or denies a Message. |
| Place | Peripheral | Place specifies the location where the Message is affirmed or denied. |
| Time | Peripheral | The Time at which the Message is affirmed or denied. |

**Frame relations** (super → sub)

- Inheritance: Statement → Affirm_or_deny
- ReFraming_Mapping: Statement → Affirm_or_deny

**Lexical units** (10): affirm.v, affirmation.n, attest.v, concede.v, confirm.v, confirmation.n, denial.n, deny.v, reaffirm.v, refute.v

## Agree_or_refuse_to_act  (frame id 1625)

A Speaker either agrees to or refuses to engage in a Proposed_action, proposed by an Interlocutor. '' 'They agreed to express their outrage with editorials in today's paper.' 'The man's refusal to accept blood severely hampered his treatment after the car accident.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Interlocutor | Core | This is the person who proposed the Proposed_action to the Speaker and to whom the Speaker communicates their response. |
| Proposed_action | Core | The Proposed_action is an action that the Speaker would perform if they were to accept or refuse the request or offer. |
| Speaker | Core | The Speaker is the person to whom a particular action has been proposed and who responds to the request or offer made. |
| Co-timed_event | Extra-Thematic | This FE identifies the subevent of the agreeing/refusing to act. |
| Depictive | Extra-Thematic | Depictive phrase describing the Speaker. |
| Event_description | Extra-Thematic | This FE applies to appraisals of the event, typically a judgment of its expectedness, and consists of any descriptions of the state of affairs denoted by the target as role fillers in other frames. The state of affairs … |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Frequency | Extra-Thematic | The number of times (within a given period) that the agreeing/refusing to act occurs. |
| Internal_cause | Extra-Thematic | The response may be prompted by either some outside phenomenon or occurrence, or by an Internal_cause, the Speaker mental or emotional state. |
| Manner | Peripheral | Any description of the event (or state) which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may indicate salient … |
| Means | Peripheral | This FE identifies the Means by which the Speaker responds to the request or offer made. |
| Medium | Peripheral | As with Medium in other communication frames, the physical entity or channel used to communicate can be expressed. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of response events. |
| Place | Peripheral | The location in which the Speaker gives their verbal response to the proposed action. |
| Purpose | Peripheral | An action that the Speaker intends to accomplish by agreeing or refusing to perform the Proposed_action that is requested of, or suggested to them. |
| Role | Peripheral | Role denotes the status that the Interlocutor requested to be granted. 'A serious injustice was committed by Citizenship and Immigration Canada (CIC) when it refused her as a political refugee.' |
| Time | Peripheral | The time interval during which the Speaker makes their verbal response concerning the proposed action. |

**Frame relations** (super → sub)

- Inheritance: Respond_to_proposal → Agree_or_refuse_to_act

**Lexical units** (4): agree.v, decline.v, refusal.n, refuse.v

## Ambient_temperature  (frame id 1052)

The Temperature in a certain environment, determined by Time and Place, is specified. 'It's too hot to do anything today.' 'Nome is pretty cold this time of year' 'Last Tuesday was a real scorcher.' 'Tomorrow is gonna be chilly.' 'I ca n't go out into the cold . DNI DNI'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Attribute | Core | The temperature feature of the weather. |
| Degree | Core | A modifier expressing the deviation of the Temperature from the norm. 'It's like totally chilly, dude, like, totally.' |
| Place | Core | The Place where it is a certain Temperature . 'Chicago is hot today .' |
| Temperature | Core | A quantity or other characterization of the Temperature of the environment. 'The temperature was 85 F in the shade today' |
| Time | Core | The Time during which an ambient environment has a particular Temperature. |
| Weather | Core | The meteorological conditions which determine the ambient temperature of a locale. 'We get warmer weather this time of year.' |
| Circumstances | Extra-Thematic | Some specification of the circumstances under which the ambient Temperature is as specified. 'It's plenty cool in the shade' |

**Frame relations** (super → sub)

- Inheritance: Temperature → Ambient_temperature

**Lexical units** (9): chilly.a, cold.a, cold.n, cool.a, freezing.a, hot.a, scorcher.n, temperature.n, warm.a

## Ammunition  (frame id 1565)

A piece of Ammunition is a disposable artifact to be fired as a projectile in a weapon with the purpose of causing harm or damage. 'The octagenarian inventor's vest repels armor-piercing bullets. ' 'It is armed with a automatic loaded 105 mm gun firing anti-tank rounds' 'Depleted uranium munitions are primarily used by the US and the UK.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Ammunition | Core | This FE identifies the Ammunition that is designed to have a particular Use. |
| Creator | Peripheral | An individual or individuals that bring the Ammunition into existence. |
| Material | Peripheral | Any indication of what makes up the Ammunition, including components, ingredients, etc. |
| Name | Peripheral | The term used to refer to an Ammunition. |
| Time_of_creation | Peripheral | The time at which an Ammunition comes into existence. |
| Type | Peripheral | An indication of the subtype of Ammunition. |
| Use | Peripheral | The use for which a piece of ammunition is intended. |
| Weapon | Peripheral | The weapon that the Ammunition is used in. 'Ammo for an AK-47 was found in the bedroom .' 'Shotgun shells, unlike simple balls, cannot be reused .' |

**Frame relations** (super → sub)

- Inheritance: Artifact → Ammunition
- Using: Weapon → Ammunition

**Lexical units** (7): ammo.n, ammunition.n, bullet.n, munitions.n, ordnance.n, round.n, shell.n

## Apply_heat  (frame id 236)

A Cook applies heat to Food, where the Temperature_setting of the heat and Duration of application may be specified. A Heating_instrument, generally indicated by a locative phrase, may also be expressed. Some cooking methods involve the use of a Medium (e.g. milk or water) by which heat is transferred to the Food. A less semantically prominent Food or Cook is marked Co-participant. 'Sally fried an egg in butter.' 'Sally fried an egg in a teflon pan.' 'Ellen fried the eggs with chopped tomatoes and garlic.' This frame differs from Cooking_creation in focusing on the process of handling the ingredients, rather than the edible entity that results from the process.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Container | Core | The Container holds the Food to which heat is applied.'Boil the potatoes in a medium-sized pan.'Things that apply the heat directly are Heating_Instruments, e.g. crock-pot, electric skillet. |
| Cook | Core | The Cook applies heat to the Food.'Drew sauteed the garlic in butter.' |
| Food | Core | Food is the entity to which heat is applied by the Cook.'Suzy usually steams the broccoli.'In instructional imperatives, this FE, which would be used for the (missing) object, is tagged CNI:'Cook on low heat for two … |
| Heating_instrument | Core | This FE identifes the entity that directly supplies heat to the Food. 'Jim browned the roast in the oven.' This FE will take precedence over Container when both are expressed in the same constituent. For example: 'Kate … |
| Temperature_setting | Core | This FE identifies the Temperature_setting of the Heating_instrument for the Food. 'He baked the cookies at 350 degrees for 11 minutes.' 'She microwaved the popcorn on high.' 'You can't cook popcorn on low heat!' |
| Beneficiary | Extra-Thematic | THe person for whose benefit the food is cooked. |
| Co-participant | Extra-Thematic | Co-participant is the gramatically less prominent of two foods to which heat is applied by the Cook.' Kate baked the apples with cinnamon.''Joe roasted potatoes with the chicken.' |
| Degree | Peripheral | This FE identifies the Degree to which heat application occurs. |
| Duration | Peripheral | Duration is the amount of Time heat is applied to the Food.'Jim boiled the egg for three minutes.' |
| Manner | Peripheral | Any description of the cooking event which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may indicate … |
| Means | Peripheral | This FE identifies the Means by which heat is applied to Food. 'Kate blanchedthe broccoli by throwing it into a pot of boiling water.' |
| Medium | Extra-Thematic | Medium is the substance through which heat is applied to the Food. 'Bobby fried the potatoes in oil.' |
| Place | Peripheral | This FE identifies the Place where the heat application occurs. 'We baked the cake in the kitchen.' |
| Purpose | Peripheral | This FE identifies the Purpose for which an intentional act is performed.'John baked cookies to show Patti that he was sorry.' |
| Time | Peripheral | This FE identifies the Time at which the heat application occurs. 'Jim roasted the chestnuts in the evening.' |

**Frame relations** (super → sub)

- Causative_of: Apply_heat → Absorb_heat
- Inheritance: Activity → Apply_heat
- Inheritance: Intentionally_affect → Apply_heat
- ReFraming_Mapping: Apply_heat → Soaking
- ReFraming_Mapping: Soaking → Apply_heat
- See_also: Apply_heat → Cooking_creation
- Using: Apply_heat → Cooking_creation

**Lexical units** (40): bake.v, baking.n, barbecue.v, blanch.v, boil.v, boiling.n, braise.v, broil.v, broiling.n, brown.v, char.v, coddle.v, cook.v, cooking.n, deep fry.v, fry.v, frying.n, grill.v, grilling.n, melt.v, melting.n, microwave.v, parboil.v, plank.v, poach.v, roast.v, roasting.n, saute.v, scald.v, scorch.v, sear.v, simmer.v, simmering.n, singe.v, steam.v, steaming.n, stew.v, stewing.n, toast.v, toasting.n

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

## Awareness  (frame id 19)

A Cognizer has a piece of Content in their model of the world. The Content is not necessarily present due to immediate perception, but usually, rather, due to deduction from perceivables. In some cases, the deduction of the Content is implicitly based on confidence in sources of information (believe), in some cases based on logic (think), and in other cases the source of the deduction is deprofiled (know). 'Your boss is aware of your commitment.' '' Note that this frame is undergoing some degree of reconsideration. Many of the targets will be moved to the Opinion frame. That frame indicates that the Cognizer considers something as true, but the Opinion (compare to Content) is not presupposed to be true; rather it is something that is considered a potential point of difference, as in the following: 'I think that you are awesome.' In the uses that will remain in the Awareness frame, however, the Content is presupposed. '' This frame is also distinct from the Certainty frame, in that it does not profile the relationship of the Cognizer to the Content, but rather presupposes it. In Certainty, the Degree of confidence or certainty is expressible as a separate frame element, as in the following: 'She absolutely knew that he would be there .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The Cognizer is the person whose awareness of phenomena is at question. With a target verb or adjective the Cognizer is generally expressed as an External Argument with the Content expressed as an Object or Complement. … |
| Content | Core | The Content is the object of the Cognizer's awareness. Content can be expressed as a direct object or in a PP Complement. 'Your boss is aware of your commitment.' 'The students do not know of your commitment.' 'The … |
| Expressor | Core | Expressor is the body part that reveals the Cognizer's state to the observer. 'Bob's eyes were overly aware' |
| Topic | Core | Some verbs in this frame allow a Topic to be expressed in about-PPs. 'Kim knows about first aid.' However, a number of nouns and adjectives in this frame which cannot take about-phrases allow Topic to be expressed as … |
| Degree | Peripheral | This FE identifies the Degree to which an event occurs. |
| Evidence | Peripheral | The source of awareness or knowledge which can be expressed in a PP Complement: 'The sailors knew from the look of the sky that a storm was coming.' 'I knew from experience that Jo would be late.' |
| Explanation | Extra-Thematic | The reason why or how it came to be that the Cognizer has awareness of the Topic or Content. |
| Manner | Peripheral | This FE identifies the Manner in which the Cognizer knows or thinks something. |
| Paradigm | Extra-Thematic | This frame element identifies the Paradigm which serves as the basis for the Cognizer's awareness. 'The formation of black holes should be understood in astrophysic terms.' |
| Role | Peripheral | Role is the category within which an element of the Content is considered. 'He understood her remark as an insult.' |
| Time | Peripheral | The time interval during which the Cognizer is aware of the Content. 'Yet there is no evidence that Mr. Parrish was cognizant at the time of the signing of the notes that the clauses in issue were present.' |

**Frame relations** (super → sub)

- Inchoative_of: Coming_to_believe → Awareness
- Inheritance: Awareness → Expectation
- Inheritance: Awareness → Grasp
- Inheritance: Mental_activity → Awareness
- Perspective_on: Awareness_situation → Awareness
- ReFraming_Mapping: Awareness → Attention
- ReFraming_Mapping: Awareness → Categorization
- ReFraming_Mapping: Awareness → Coming_up_with
- ReFraming_Mapping: Awareness → Emotion_directed
- ReFraming_Mapping: Awareness → Expertise
- ReFraming_Mapping: Awareness → Opinion
- ReFraming_Mapping: Categorization → Awareness
- See_also: Awareness → Certainty
- See_also: Awareness → Opinion
- Using: Awareness → Certainty
- Using: Awareness → Examination
- Using: Awareness → Fame
- Using: Awareness → Impression
- Using: Awareness → Religious_belief
- Using: Awareness → Remembering_information
- Using: Awareness → Representing
- Using: Awareness → Secrecy_status
- Using: Information → Awareness

**Lexical units** (28): aware.a, awareness.n, believe.v, cognizant.a, comprehend.v, comprehension.n, conceive.v, conception.n, conscious.a, consciousness.n, hunch.n, idea.n, ignorance.n, imagine.v, know.v, knowledge.n, knowledgeable.a, presume.v, presumption.n, reckon.v, supposition.n, suspect.v, suspicion.n, think.v, thought.n, understand.v, understanding.n, unknown.a

## Be_in_agreement_on_action  (frame id 1380)

Two (or more) people (the Parties, also encodable as Party_1 and Party_2) have an agreement. Both sides are construed as having a commitment to an Obligation--the relationship is understood to be symmetrical or reciprocal. Instead of a specific mention of the Obligation, a Topic expression may be used to indicate the domain covered. 'The US and Russia have an agreement to share early warning data on missile launches.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Obligation | Core | An expression of the commitment of the Parties . 'The US and Russia have an agreement to share early warning data on missile launches.' |
| Parties | Core | The group of individuals portrayed as equally involved in having an agreement. 'The US and Russia have an agreement to cooperate in destroying surplus portable anti-aircraft missiles.' |
| Party_1 | Core | The individual or individuals that form the more prominent (i.e. agentive) party of the agreement, as compared with Party_2. That is, Party_1 is generally encoded as the External Argument of verbs, and peripheral FEs … |
| Party_2 | Core | The semantically (and grammatically) less prominent participant (or group of participants) in the agreement. It is generally encoded within a prepositional phrase (e.g. headed by with). 'Mozilla Foundation now has a … |
| Topic | Core | Topic is a description of the domain covered by the agreement. 'Some types of alloy steel have been covered in the expiring trade agreement.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Degree | Extra-Thematic | This frame element selects some gradable attribute and modifies the expected value for it. |
| Descriptor | Extra-Thematic | This FE describes a characteristic or description of the agreement_on_action. |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of a continuous situation (the one denoted by the target) to its end. In many cases, the continuous situation is a dynamic action which is ongoing, while in others … |
| Manner | Peripheral | Any description of the agreement not specified by the other FEs, including particularly salient characteristics of the parties. |
| Medium | Peripheral | As with other frames in the Communication domain, the Medium of communication may be expressed. Medium is the physical entity or channel used to record or negotiate the Obligation. 'The parties have a written agreement … |
| Place | Peripheral | This FE identifies the Place where an agreement was made. 'The Kyoto treaty has so far been relatively ineffectual.' |
| Time | Peripheral | This FE identifies the Time when the agreement was made. 'The missile agreement of 1952 was still in force, however.' |

**Frame relations** (super → sub)

- Inheritance: Be_in_agreement_on_action → Having_commercial_agreement
- Using: Make_agreement_on_action → Be_in_agreement_on_action

**Lexical units** (6): accord.n, agreement.n, convention.n, deal.n, strike.v, treaty.n

## Be_in_agreement_on_assessment  (frame id 1496)

The Cognizers have a similarity (or dissimilarity) in their Opinion. The Cognizers may be expressed separately, with Cognizer_2 being the basis for establishing the Opinion of Cognizer_1. Rather than a specific Opinion, a phenomenon about which a similar or differing Opinion is held, the Topic, may be specified. A specific Opinion may also go unmentioned when the Opinions of the Cognizers are understood as answers to a Question. 'Dr. Gerry and Mr. Pond agree in their impressions.' ' This copyeditor and I mostly see eye to eye on things.' 'I agree with you that everything should be monitored to keep the person from wasting time and protecting the interests of the company.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer_1 | Core | When there is an asymmetry, Cognizer_1 is the individual characterized by their similarity in opinion to Cognizer_2, whose opinion is assumed to be known. Cognizer_1 is often an external argument. |
| Cognizer_2 | Core | When the Cognizers are expressed separately, Cognizer_2 is the one whose opinion is assumed to be known; it serves as a basis for establishing the opinion of Cognizer_1. |
| Cognizers | Core | This FE marks constituents that express the set of Cognizers whose similarity of opinion is at issue. |
| Opinion | Core | A state of affairs believed by the Cognizers. 'We agree that babies should not be dropped from helicopters.' |
| Question | Core | This FE denotes an implicit question in response to which the Cognizers give their Opinions, which are then assessed for their similarity. The Question may concern the identitiy of a particular entity, as in the first … |
| Topic | Core | A phenomenon that the Cognizers are considering with respect to their Opinion. |
| Circumstances | Extra-Thematic | The state-of-affiars under which aggreement occurs (as independent of the act of agreement). |
| Degree | Peripheral | The extent to which the Cognizers are similar in their Opinions. |
| Depictive | Extra-Thematic | This FE is used for any Depictive phrase describing the state of the Cognizers |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the agreement or disagreement logically follows. |
| Manner | Peripheral | This FE is for descriptions of the agreement state not covered by more specific FEs, especially characterizations of the state as a whole or of one of the Cognizers or Cognizer_1. |
| Place | Peripheral | The Place is the general area in which the Cognizers are in agreement or disagreement. |
| Time | Peripheral | This FE identifies the Time when the Cognizers are in agreement or disagreement. |

**Frame relations** (super → sub)

- Inheritance: Similarity → Be_in_agreement_on_assessment
- Using: Be_in_agreement_on_assessment → Point_of_dispute
- Using: Be_in_agreement_on_assessment → Quarreling
- Using: Opinion → Be_in_agreement_on_assessment

**Lexical units** (4): agree.v, agreement.n, concur.v, see eye to eye.v

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

## Being_in_control  (frame id 1800)

A Controlling_entity has control of a Dependent_entity, Dependent_situation, or Dependent_variable. 'She was in control of the empire within two days.' This frame is distinct from Control in that the Controlling_entity is not fully asserted to be currently controlling the Dependent_entity, Dependent_situation, or Dependent_variable, but rather is attentive to it and capable of making the situation correspond to the desired state at any time.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Controlling_entity | Core | A thing or person whose behavior controls a Dependent_entity, Dependent_situation, or Dependent_variable. |
| Dependent_entity | Core | An entity, usually a thing, that is influenced in its behavior by a Controlling_entity. |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Degree | Core-Unexpressed | The Degree to which the Controlling_entity effects the Dependent_entity. |
| Dependent_situation | Core-Unexpressed | A situation whose temporal or other characteristics are influenced by a Controlling_entity. |
| Dependent_variable | Core-Unexpressed | A scalar variable, whose value depends on the behavior of a Controlling_entity. 'Move the slider on the SpeedBar while playing audio or video material to control playback speed.' |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including force (hard, softly), secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may also … |
| Place | Peripheral | The location at which the controlling occurs. |
| Time | Peripheral | The Time at which the controlling occurs. |

**Frame relations** (super → sub)

- Inheritance: Being_in_control → Dominate_competitor
- Inheritance: Control → Being_in_control
- ReFraming_Mapping: Control → Being_in_control
- Using: Being_in_control → Kidnapping

**Lexical units** (9): control.n, control.v, dominate.v, domination.n, manage.v, management.n, manipulate.v, manipulation.n, rule.v

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

## Being_relevant  (frame id 2530)

A Phenomenon is related to some cognitive action, the Endeavor, of a Cognizer. In many LUs, the Cognizer is null-instantiated and implied as being the speaker or another participant of the Endeavor. 'This book is very relevant to my essay.' 'This book is very relevant to my essay.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | A participant in the mental Endeavor to which the Phenomenon is related. This frame element is often null-instantiated and may be inferred from the Endeavor. |
| Endeavor | Core | A cognitive action (eg discussion, decision) performed by the Cognizer to which the Phenomenon is connected in some way. |
| Phenomenon | Core | Something that is profiled in the mind of the Cognizer as being related to mental Endeavors. |
| Degree | Peripheral | A description of how related the Phenomenon is to the Endeavor. |
| Specification | Peripheral | The knowledge or situation that mediates the relevance of the Phenomenon to the Endeavor. 'How does Assad 's family dynamic play into his intransigence ?' |

**Frame relations** (super → sub)

- Inheritance: Cognitive_connection → Being_relevant

**Lexical units** (4): irrelevant.a, pertinent.a, play (into).v, relevant.a

## Being_wet  (frame id 332)

An Item is in a state of wetness with the possibility of the wetting Liquid being mentioned, along with the Degree of wetness. ' The mop is drenched with water from last night's rain.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Item | Core | The Item takes up the Liquid through its pores. ' The mop is drenched with water.' |
| Liquid | Core | The Liquid is a fluid or gas that permeates the Item. It most frequently occurs in a PP Complement headed by with. 'The mop was drenched with water.' |
| Degree | Peripheral | This FE identifies the Degree to which the Item is wet. 'The mop is absolutely drenched.' |
| Explanation | Extra-Thematic | The Explanation brings about the state of wetness, and is usually expressed in a from-prepositional phrase. 'The mop is drenched from the rain.' |
| Subregion | Extra-Thematic | The Subregion describes which part of a larger whole is being affected. 'The mop was drenched on the fringes.' |

**Frame relations** (super → sub)

- Causative_of: Cause_to_be_wet → Being_wet
- Inheritance: Gradable_attributes → Being_wet
- Using: Being_wet → Being_rotted

**Lexical units** (16): clammy.a, damp.a, dewy.a, drenched.a, humid.a, moist.a, moistened.a, saturated.a, soaked.a, soaking.a, sodden.a, soggy.a, sopping.a, sweaty.a, waterlogged.a, wet.a

## Biological_entity  (frame id 2567)

The LUs in this frame refer to biological entities labeled by the FE Organism. An Organism is described as something that can be alive, or have naturally occuring biological processes and functions; however the concept of life is often used metaphorically for non-organic entities which resemble or act as if they have organic life. 'NASA may someday discover a new lifeform from another planet.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Organism | Core | An organic that has naturally occuring bioligical processes and functions. |
| Descriptor | Peripheral | Any characterization of the Organism not covered by other FEs. |
| Origin | Peripheral | The location from which the Organism originated. |

**Frame relations** (super → sub)

- Inheritance: Biological_entity → Animals
- Inheritance: Biological_entity → People
- Inheritance: Biological_entity → Plants
- Inheritance: Entity → Biological_entity
- Using: Biological_entity → Biological_classification
- Using: Biological_entity → Dead_or_alive
- Using: Biological_entity → Gusto

**Lexical units** (4): human.a, life.n, lifeform.n, organism.n

## Boundary  (frame id 329)

This frame contains words that describe a Boundary between two Entities. In many cases, the Boundary is the border between an Entity and some unnamed space, generally conceived of as empty. 'The canyon is the border between the two states.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Boundary | Core | The region which is between the Entities or between the Entity and empty space. |
| Entities | Core | The joint construal of both Entities next to the Boundary. |
| Entity | Core | The entity that has a Boundary. |
| Relative_location | Peripheral | The relative location of the boundary in respect to the Entity or Entities. |

**Frame relations** (super → sub)

- Using: Boundary → Bounded_entity

**Lexical units** (4): border.n, boundary.n, edge.n, line.n

## Buildings  (frame id 173)

This frame contains words which name permanent fixed structures forming an enclosure and providing protection from the elements. 'The baroque church, built in 1635, has a very rich interior' 'The city tour includes the 16th-century monastery of the Transfiguration and Church of Elijah the Prophet' 'An ancient stone church stands amid the fields' 'Jack built his house in the style of the day.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Building | Core | The entity built by the Builder which has some Function. |
| Creator | Extra-Thematic | The Individual that created the Building. |
| Descriptor | Extra-Thematic | A characterization of some property of the Building. |
| Function | Peripheral | The use for which the Building is intended. |
| Material | Extra-Thematic | Any indication of what makes up the Building, including components, ingredients, etc |
| Name | Extra-Thematic | The Name used to refer to the Building. |
| Place | Peripheral | The building's location. |
| Possessor | Extra-Thematic | The person or other legal entity that owns or has possession of the Building. |
| Relative_location | Peripheral | A place that a Building is located with respect to. |
| Time_of_creation | Extra-Thematic | The time at which the Building comes into existence. |
| Type | Peripheral | An indication of the subtype of Building, including architectural style. |

**Frame relations** (super → sub)

- Inheritance: Artifact → Buildings
- Subframe: Buildings → Building_subparts
- Using: Locale_by_use → Buildings

**Lexical units** (104): acropolis.n, airport.n, arena.n, auditorium.n, bar.n, barn.n, barracks.n, basilica.n, blockhouse.n, building.n, bungalow.n, bunker.n, cabin.n, campanile.n, caravan.n, caravanserai.n, castle.n, chalet.n, chateau.n, church.n, citadel.n, city hall.n, condominium.n, conservatory.n, cottage.n, dacha.n, disco.n, discotheque.n, dormitory.n, dwelling.n, farmhouse.n, fort.n, fortification.n, fortress.n, garage.n, gazebo.n, greenhouse.n, hacienda.n, hall.n, hangar.n, high-rise.n, hippodrome.n, home.n, homestead.n, hospital.n, hostel.n, hotel.n, house.n, houseboat.n, housing.n, hovel.n, igloo.n, inn.n, kennel.n, kiosk.n, library.n, lighthouse.n, lodge.n, maisonette.n, mall.n, manor.n, manse.n, mansion.n, monastery.n, mosque.n, motel.n, outbuilding.n, outhouse.n, pagoda.n, palace.n, palazzo.n, pavilion.n, pension.n, penthouse.n, pub.n, pueblo.n, pyramid.n, quarters.n, residence.n, rotunda.n, shack.n, shanty.n, shebang.n, shed.n, shelter.n, skyscraper.n, stable.n, stadium.n, structure.n, supermarket.n, synagogue.n, tabernacle.n, tavern.n, temple.n, tenement.n, tent.n, tepee.n, terminal.n, theater.n, tower.n, triplex.n, villa.n, warehouse.n, wigwam.n

## Businesses  (frame id 365)

A Proprietor owns or runs a Business which provides a Product (which may be goods or services). 'The consumer electronics company Apple has exploded with popularity in recent years.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Business | Core | Business identifies the company or establishment. This may be the target itself or the Business_Name if it is an appositive not set off with commas (i.e. restrictive): 'The electronics firm went bankrupt.' In the … |
| Business_name | Peripheral | The name of the Business when it appears in an appositive set off by commas (non-restrictive): 'My clothing company, Togs, is doing well.' |
| Descriptor | Peripheral | Descriptor indicates other characteristics of the business besides its Product and Proprietor. 'Chris runs a small company in Idaho.' 'I work for a non-profit arts company.' |
| Place | Peripheral | This FE identifies the Place in which the business is located. 'Chris's business in Idaho is thriving.' 'Local companies are looking for more and more Spanish-speaking employees.' |
| Product | Peripheral | Product identifies the product or service provided by the business. 'Josh runs a copier toner business.' |
| Proprietor | Peripheral | Proprietor is the owner or chief participant in the business. 'I worked in Goldberg's legal practice .' 'I didn't want to go into the family business.' |
| Service_provider | Peripheral | When a Business is described in terms of the professionals who work to produce the product or service, use Service_provider. ' John works as an office assistant for a firm of accountants.' |

**Frame relations** (super → sub)

- Using: Commerce_scenario → Businesses

**Lexical units** (14): bank.n, boutique.n, business.n, chain.n, company.n, corporation.n, establishment.n, firm.n, mill.n, operation.n, paper.n, practice.n, shop.n, store.n

## Calendric_unit  (frame id 229)

Words in this frame name the different parts of the calendric cycle, both man-made and natural. The Unit (e.g. Tuesday) specifies some time period as part of a specific larger temporal Whole (Tuesday of next week), or may be resolved to an exact time span by a Relative_time (next Tuesday). 'Jo's mother will visit on this coming Tuesday.' '' Very frequently, the Whole or Relative_time are left out (i.e., DNI), and often should be interpreted as a time period overlapping with the communication, but more generally must be understood from context. So, for example, in the first sentence below, we can imagine that the Whole refers to a year (e.g., 1983) that was already mentioned or established in context. In the second example below, the most likely interpretation is the nearest April, whether in this year or the next, and this interpretation is best indicated by indicating the Relative_time is DNI. 'On April 2 , she finally found her mother . DNI. ' 'I 'll come back in April .DNI' '' Most members of this frame can be used with iterative events, either with a plural Unit (on Tuesdays), or marked with every (every April). 'On Tuesday and Thursday afternoons , we have tea .' In this use, when the Whole is omitted, the Whole should be marked INI. 'On Tuesdays , we have tea . INI ' '' Words of this frame often occur in a non-lexical construction that uses some Calendric_unit expressions to establish when an event occurred. To capture this information, we use the extra-thematic FEs Landmark_period and Trajector_event (see Temporal_collocation) on the second layer, as in the following: 'Last Tuesday she said I 'd have to come back .' 'Last Tuesday she said I 'd have to come back .' We do not use these FEs for cases where the temporal relationship is introduced by an overt word of the Temporal_collocation frame (like on, in, at, before, etc.). Most lexical units of this frame occur in this construction, with or without requiring a Relative_time, while some idiosyncratically do not, so information on the use with the extra-thematic FE Trajector_event is lexically specific. '' There are a number of non-lexical constructions that evoke this frame, including date constructions (the third, May 5), decade constructions (the oughts), year constructions (1975, 24 BCE, 10 AH, year 19, etc.), and time-of-day constructions. Although not annotated in this frame, examples such as the following show that the FEs Unit and Whole are quite appropriate: 'The 4th of April dawned clear and cold .' 'December 11 was when Alix finally left .' 'The 23rd will be snowy . DNI ' 'Nothing much happened in the 90s , did it ? DNI ' As described above for the lexical targets that evoke this frame, some non-lexical versions of the frame may also occur in a non-lexical Temporal_collocation construction: 'No-one has forgotten what happened the 5th of November !' 'No-one has forgotten what happened the 5th of November !' '' Words in this frame figure into a variety of temporal schemas, realized as constructions, primarily cases in which the Calendric_unit serves as a Landmark_period in the Temporal_collocation frame. There are families of constructions in which these words occur, including ones in which weekday names combine with day part names using particular prepositions (e.g. on Wednesday morning, cf. on Wednesday, but in the morning) and ones in which calendric terms fill the slots in multi-word expressions such as N-after-N (e.g. day after day), N-by-N (e.g. week by week), N-to-N (e.g. month to month), etc. More can be found on these in Fillmore (2002). Note, also, the connection between this frame and Frequency, specifically that many iterative adjectives and adverbs are based on calendric terms (e.g. daily, weekly, monthly, etc.).

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Relative_time | Core | Relative_time is used for the word or words that locate the time with respect to an identifiable reference point. 'Jo's mother will visit this coming Tuesday.' |
| Unit | Core | The calendric unit that is denoted. LUs in this frame all denote the Unit. |
| Whole | Core | Whole is used for the larger unit of which the target word names a part. 'Jo fled in the early morning of Sunday December 15.' |
| Count | Peripheral | The number of intervals of the specified type. 'These last two weeks, I just keep getting myself into trouble .' |
| Landmark_period | Extra-Thematic | The time-expression that is used to establish when the Trajector_event occurred. This FE, when present, always occurs on the second layer. 'Turn in your expense reports next April .' This FE is not to be used when the … |
| Name | Peripheral | Name is used for the name of a day (month, etc.). Note that only the word (or words) that is the name is (are) tagged, not the target word. 'Labor Day is just around the corner.' 'January is Black History Month.' |
| Salient_event | Extra-Thematic | An event saliently associated with a particular calendric unit. 'Today was my school's cut day.' 'Republicans have indicated they plan to make Kerry's positions an election year issue.' |
| Trajector_event | Extra-Thematic | An event that is located by the Calendric_unit expression. 'Last November , they selected a new president .' This FE is not to be used when a target of the Temporal_collocation frame explicitly introduces the temporal … |

**Frame relations** (super → sub)

- Inheritance: Location_in_time → Calendric_unit
- See_also: Calendric_unit → Frequency
- See_also: Calendric_unit → Temporal_collocation
- Using: Calendric_unit → Change_event_time

**Lexical units** (63): April.n, August.n, December.n, February.n, Friday.n, January.n, July.n, June.n, March.n, May.n, Monday.n, November.n, October.n, Saturday.n, September.n, Sunday.n, Thursday.n, Tuesday.n, Wednesday.n, afternoon.n, age.n, autumn.n, calendar year.n, century.n, dawn.n, day.n, daybreak.n, decade.n, dusk.n, era.n, eve.n, evening.n, fortnight.n, holiday.n, hour.n, leap year.n, midday.n, midnight.n, millennium.n, minute.n, month.n, morn.n, morning.n, night.n, noon.n, one day.n, quarter.n, rush hour.n, school year.n, second.n, spring.n, summer.n, today.n, tomorrow.n, tonight.n, twilight.n, week.n, weekday.n, weekend.n, weeknight.n, winter.n, year.n, yesterday.n

## Capacity  (frame id 2138)

An Entity has the ability to contain a Theme. 'Our facility seats up to 500 people.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The Entity whose ability to contain items is assessed. 'Our facility seats up to 500 people.' |
| Theme | Core | The Entity has the ability to contain the Theme, often expressed with a quantity. 'Our facility seats up to 500 people.' |
| Circumstances | Extra-Thematic | The Circumstances under which the Entity meets or fails to meet the pre-conditions for containing. |
| Degree | Peripheral | The extent to which the Entity exceeds or falls short of the minimum requirements for holding the items. |
| Depictive | Extra-Thematic | A description of one of the participants, typically the Theme but possibly the Entity. 'Our facilities seat 500 people seated.' |
| Explanation | Extra-Thematic | An entity, event, or state that causes the Entity to be able or unable to hold the items. |
| Purpose | Extra-Thematic | The Purpose of the Entity's specified capacity. 'It seats approximately 180 persons for full silver service.' |
| Status | Extra-Thematic | The status of the capability (e.g., innately, with modifications). |
| Subregion | Extra-Thematic | This FE denotes a sub-part of the Entity which has a particular capacity. 'The two small cars seated only 32 inside.' |
| Time | Peripheral | The Time at which the Entity has or had a certain capacity. |

**Frame relations** (super → sub)

- Inheritance: Capability → Capacity

**Lexical units** (6): feed.v, fit.v, seat.v, serve.v, sleep.v, take.v

## Catastrophe  (frame id 115)

The words in this frame involve an Undesirable_event which affects the Patient negatively. No agent need be involved. '' 'The first calamity was a disastrous trade war with Holland.' 'It is sad to have to make a living by grubbing around in the dirt of a national calamity.' 'The result has been catastrophic.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Patient | Core | The entity that experiences the Undesirable_Event. 'An environmental disaster is just what we need.' 'Should hair loss befall you...' |
| Undesirable_event | Core | The undesirable event which occurs. |
| Cause | Peripheral | The cause of the Undesirable_Event. 'Most counties are prepared for some level of natural disaster.' |
| Circumstances | Extra-Thematic | This FE indicates the Circumstances under which a warning applies. (Proper only to betide.) |
| Degree | Peripheral | This FE identifies the Degree to which event occurs. |
| Manner | Peripheral | Manner of performing an action |
| Place | Peripheral | Where the Undesirable_Event takes place. |
| Time | Peripheral | When the Undesirable_Event occurs. |

**Frame relations** (super → sub)

- ReFraming_Mapping: Undergoing → Catastrophe
- Using: Eventive_affecting → Catastrophe

**Lexical units** (21): accident.n, apocalypse.n, befall.v, betide.v, calamitous.a, calamity.n, casualty.n, cataclysm.n, catastrophe.n, catastrophic.a, crisis.n, debacle.n, disaster.n, disastrous.a, incident.n, mischance.n, misfortune.n, mishap.n, suffer.v, tragedy.n, victim.n

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

## Cause_change  (frame id 683)

An Agent or Cause causes an Entity to change, either in its category membership or in terms of the value of an Attribute. In the former case, an Initial_category and a Final_category may be expressed, in the latter case an Initial_value and a Final_value can be specified. 'Our storylines follows the saga outlined by the Ultima Series, but we have modified it in order to make our writing more cohesive.' 'I don't think you can turn that rabbit into a hat.' 'How can a guy that changed his name from Bob Craft to Jack Ass declare anyone defamed his character?' ' At this juncture, a new development changed the political situation on the island.' 'She had at some time earlier completely changed her clothing and appearance and now stood in front of me dressed like a garden gnome.' 'Hence, when (Hg 0 ) is converted to Hg 2+ , it can be rapidly taken up in rain water, snow, or adsorbed onto small particles' 'Hence, when (Hg 0 ) is converted to Hg 2+ , it can be rapidly taken up in rain water, snow, or adsorbed onto small particles'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The sentient entity that effects a change in the Entity. 'The system administrator changed the value from 'KDE' to 'GNOME', and then restarted the system.' |
| Entity | Core | The abstract or concrete thing or situation that the Agent causes to change. 'The recent terrorist attacks had changed the political climate.' |
| Final_category | Core | The category that the Entity belongs to after it has undergone the change. 'The radical message of the cross transformed Saul of Tarsus and changed him from a persecutor of Christians to a tender believer.' |
| Final_value | Core | The value that the Attribute assumes as a result of the change that the Entity is caused to undergo. 'We changed the size from 8 1/2x11 to a larger 11 x 17 and gave it a complete graphical makeover. ' |
| Initial_category | Core | The category of which the Entity is a member before the Agent causes a change. 'Her time with the Healer Craft has changed her from a shy, nervous young girl into a confident (almost) young woman' |
| Initial_value | Core | The value that the Attribute has before the change takes place. 'My dad changed his hair color from red to blue today.' |
| Attribute | Core-Unexpressed | A characteristic of the Entity for which a value can be assigned or determined by calculation, measurement , or observation. 'We changed the price from $1.26 to $1.27 per pint.' |
| Cause | Core-Unexpressed | An event that causes a change in the Entity. 'Major technological innovations changed the social and economic conditions.' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Containing_event | Extra-Thematic | This FE denotes an event that occurs or state of affairs that holds at a time that includes the time during which the event or state of affairs reported by the target occurs and of which it is taken to be a part. |
| Degree | Extra-Thematic | The extent to which the initial and final categories or values differ from each other. 'We significantly changed its appearance during this time. ' |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of a continuous situation (the one denoted by the target) to its end. In many cases, the continuous situation is a dynamic action which is ongoing, while in others … |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. |
| Explanation | Extra-Thematic | A state of affairs that the Agent is responding to in bringing about the change in the Entity. 'I didn't change its name because I think it has already got used to it.' |
| Manner | Peripheral | Any description of the event causing the change of the Entity which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, loudly), and … |
| Means | Peripheral | An intentional action performed by the Agent (or event resulting from the Cause) that produces a change in the Entity. 'Ling said he had transformed the car by putting slicks on.' |
| Period_of_iterations | Extra-Thematic | The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | The location where the change of the Entity is caused. 'In his own room he had modified nothing.' |
| Purpose | Peripheral | An action that the Agent intends to accomplish by effecting a change in the Entity. 'His real name is Jerry Rivers, but he changed it in order to sound more ethnic and appealing' |
| Re-encoding | Extra-Thematic | This FE presents the current frame as an integral part of a larger conceptualization expressed by another frame. |
| Role | Extra-Thematic | The particular role that the Agent plays in the Cause_change event. |
| Time | Peripheral | The time at which the change of the Entity is caused. 'He changed it after David Bowie told him that only twerps have the same first and last name.' |

**Frame relations** (super → sub)

- Causative_of: Cause_change → Undergo_change
- Inheritance: Cause_change → Change_event_duration
- Inheritance: Cause_change → Change_event_time
- Inheritance: Cause_change → Exchange_currency
- Inheritance: Transitive_action → Cause_change
- ReFraming_Mapping: Reshaping → Cause_change
- Using: Cause_change → Adjusting
- Using: Cause_change → Reforming_a_system

**Lexical units** (16): alter.v, alteration.n, change.v, conversion.n, convert.v, deform.v, make.v, modification.n, modify.v, reshape.v, shift.v, transform.v, transformation.n, turn.v, variation.n, vary.v

## Cause_change_of_position_on_a_scale  (frame id 96)

This frame consists of words that indicate that an Agent or a Cause affects the position of an Item on some scale (the Attribute) to change it from an initial value (Value_1) to an end value (Value_2). The direction of the change (Path) can be encoded as well as the magnitude of the change (Difference). The rate of change of the value (Speed) can optionally be indicated as well as a second scale (Co_Variable), which the values are correlated with. '' 'The company is raising the final dividend from 4.34p to 4.57p, to boost the total by 5.3 percent to 6.36p.' 'Similarly, a consumer boom will encourage the authorities to increase interest rates in order to keep money supply on target.' 'United Way of Central Indiana adds value to your investment.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The person who causes an entity (Item) to change its positon on a scale with respect to some property (Variable). |
| Attribute | Core | The scale along which the Item ranges in value. 'They increased the price of oil.' |
| Cause | Core | The force that causes the change. 'The rain increased the river's flow rate to an astonishing million gallons per second.' |
| Item | Core | The entity whose position along a scale is being changed. 'Oil prices were raised yesterday.' |
| Co-variable | Extra-Thematic | The Co-Variable is the scale that the (dependent ) Variable is measured against. 'We raise the temperature with the pressure' |
| Difference | Peripheral | The distance between the orginial value (Value-1) and the final value (Value-2) of the entity on the scale (Variable). 'Coke raised the price of their soda by 2%.' |
| Manner | Peripheral | Any description of the Agent changing the value of an Attribute which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may … |
| Means | Peripheral | An act performed by the Agent that brings about the change in the position of the Item on the scale. 'They increase the price of diamonds by withholding a sizable portion of the supply.' |
| Path | Peripheral | Any expression that says something about the movement of the entity (Item) along the scale between its initial (Value-1) and its final position (Value-2). 'They moved up the price of oil.' |
| Place | Peripheral | The location where the Agent changes the value of an Attribute. 'As a result, they raised prices in Peoria.' |
| Purpose | Extra-Thematic | The purpose for which an intentional act is performed. 'John flattered her to receive a raise.' |
| Speed | Peripheral | The rate at which the entity's positon on the scale changes. 'Ford slowly raised the price of their best-selling model.' |
| Time | Peripheral | When the event occurs. |
| Value_1 | Peripheral | The initial value of the entity (Item) along the scale. |
| Value_2 | Peripheral | The final position on the scale that the entity (Item) assumes. |

**Frame relations** (super → sub)

- Causative_of: Cause_change_of_position_on_a_scale → Change_position_on_a_scale
- Inheritance: Cause_change_of_position_on_a_scale → Cause_proliferation_in_number
- Inheritance: Transitive_action → Cause_change_of_position_on_a_scale
- ReFraming_Mapping: Cause_expansion → Cause_change_of_position_on_a_scale

**Lexical units** (26): add.v, crank.v, curtail.v, cut.n, cut.v, decrease.v, development.n, diminish.v, double.v, drop.v, enhance.v, growth.n, increase.v, knock down.v, lift.v, lower.v, move.v, promote.v, push.n, push.v, raise.v, reduce.v, reduction.n, slash.v, step up.v, swell.v

## Cause_change_of_strength  (frame id 1781)

An Agent causes a Patient to be more strong, often resulting in something that is more secure and safe. 'Local Serbs are strengthening their grip on a narrow corridor along the Sava River between two large Serbian areas.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent fortifies the Patient. |
| Patient | Core | The Patient is the entity that is being made stronger. |
| Cause | Core-Unexpressed | An event which causes the Patient to become stronger. |
| Circumstances | Extra-Thematic | The Circumstances of the world at the time of the event (which do not bear directly on the event itself). |
| Containing_event | Extra-Thematic | This FE denotes an event that occurs or state of affairs that holds at a time that includes the time during which the event or state of affairs reported by the target occurs and of which |
| Degree | Extra-Thematic | This frame element selects some gradable attribute and modifies the expected value for it. |
| Depictive | Extra-Thematic | Depictive phrase describing the actor of an action |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. |
| Manner | Peripheral | Any description of the intentional act which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may indicate … |
| Means | Peripheral | An act performed by an Agent that enables them to act upon the Patient. |
| Place | Peripheral | The location at which the Agent fortifies the Patient. |
| Result | Extra-Thematic | The resultant state of the action. |
| Time | Peripheral | The time at which the Agent makes the Patient stronger. |

**Frame relations** (super → sub)

- Inheritance: Cause_change_of_strength → Change_resistance
- Inheritance: Transitive_action → Cause_change_of_strength
- Using: Cause_change_of_strength → Supporting

**Lexical units** (5): beef up.v, fortify.v, reinforce.v, strengthen.v, weaken.v

## Cause_harm  (frame id 112)

The words in this frame describe situations in which an Agent or a Cause injures a Victim. The Body_part of the Victim which is most directly affected may also be mentioned in the place of the Victim. In such cases, the Victim is often indicated as a genitive modifier of the Body_part, in which case the Victim FE is indicated on a second FE layer. '' 'Rod saw his father beating his mother.' 'In the end Wormtongue is fed up with being beaten so he cuts Saruman's throat to free himself.' 'A mother stabbed to death by her husband made a secret will stating that he must never be allowed to care for their son.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | Agent is the person causing the Victim's injury. 'Jolosa, who broke a rival player 's jaw, was told to model his play on the England striker.' 'Someone bashed him on the back of the head with a heavy smooth object.' … |
| Body_part | Core | The Body_part identifies the location on the body where the bodily injury takes place. 'Someone bashed him on the back of the head with a heavy smooth object.' 'Jolosa, who broke a rival player 's jaw , was told to … |
| Cause | Core | The Cause marks expressions that indicate some non-intentional, typically non-human, force that inflicts harm on the Victim 'A falling rock crushed my ankle.' |
| Victim | Core | The Victim is the being or entity that is injured. If the Victim is included in the phrase indicating Body_part, the Victim FE is tagged on a second FE layer (see 3rd example). 'Someone bashed him on the back of the … |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the Cause_harm event and any of its participants. |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the Cause_harm event) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in … |
| Containing_event | Extra-Thematic | This FE identifies the event in which the harm is caused. |
| Degree | Peripheral | Degree is the degree to which the Agent causes harm to the Victim. 'She wanted to slap him hard for his change of mood.' 'Fox spun around and slapped him, harder than necessary.' |
| Depictive | Extra-Thematic | Depictive identifies any Depictive phrase describing the actor of an action. 'Indeed, Henry V used to burn them alive.' |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of the Cause_harm event to its end. |
| Explanation | Extra-Thematic | A fact or action somehow related to the Victim that the Agent responds to by causing harm to the Victim. 'She wanted to slap him hard for his change of mood.' 'She could easily have slapped her for that remark.' |
| Frequency | Extra-Thematic | How often the Cause_harm event occurs. |
| Instrument | Peripheral | This FE is any object used to cause the injury. 'Someone bashed him on the back of the head with a heavy smooth object.' 'John butted her in the chest with his head.' |
| Iterations | Extra-Thematic | Iterations refers to the number of times the Agent causes harm to the Victim. 'Kim hit Harold with the stick a dozen times.' 'he had slapped his wife across the face a number of times.' |
| Manner | Peripheral | The Manner in which the Agent acts upon the Victim. 'He violently slapped his assailant.' |
| Means | Peripheral | An intentional action performed by the Agent that accomplishes the action indicated by the target. 'Rachael injured her friend by closing the car door on his left hand.' |
| Particular_iteration | Extra-Thematic | This FE indicates that the Cause_harm event is conceived as embedded within an iterated series of similar events or states. |
| Period_of_iterations | Extra-Thematic | The length of time from when the Cause_harm event began to be repeated to when it stopped. |
| Place | Peripheral | Place identifies the place where the harm causing event occurs. 'Boys are punched at school for payback ' |
| Purpose | Extra-Thematic | Purpose identifies the purpose for which a harm-causing action is carried out. |
| Re-encoding | Extra-Thematic | A description of the harm event which significantly displays a different aspect. 'Then she elbowed me -- a serious affront to my sensibilities !' |
| Result | Extra-Thematic | Result identifies the result of the Agent's action. 'Riot police in Nairobi clubbed four women unconscious on March 3.' 'A battered wife who burned her brutal husband to death was freed from jail yesterday.' 'Claire … |
| Subregion_bodypart | Extra-Thematic | The Subregion_bodypart defines the precise location on the Body_part which is harmed. 'Martha's legs were chopped off at the knees.' |
| Time | Peripheral | Time identifies the time when the harm-causing event occurs. 'Riot police in Nairobi clubbed four women unconscious on March 3.' |

**Frame relations** (super → sub)

- Inheritance: Cause_bodily_experience → Cause_harm
- Inheritance: Cause_harm → Corporal_punishment
- ReFraming_Mapping: Cause_harm → Cause_impact
- ReFraming_Mapping: Cause_harm → Corporal_punishment
- ReFraming_Mapping: Death → Cause_harm
- Using: Cause_harm → Abusing
- Using: Cause_harm → Terrorism
- Using: Cause_harm → Toxic_substance
- Using: Cause_harm → Violence
- Using: Experience_bodily_harm → Cause_harm

**Lexical units** (72): bash.v, batter.v, bayonet.v, beat up.v, beat.v, belt.v, biff.v, bludgeon.v, boil.v, break.v, bruise.v, buffet.v, burn.v, butt.v, cane.v, chop.v, claw.v, clout.v, club.v, crack.v, crush.v, cudgel.v, cuff.v, cut.v, drug.v, elbow.v, electrocute.v, electrocution.n, flagellate.v, flog.v, fracture.v, gash.v, hammer.v, hit.v, horsewhip.v, hurt.v, impale.v, injure.v, jab.v, kick.v, knee.v, knife.v, knock.v, lash.v, maim.v, maul.v, mutilate.v, pelt.v, poison.v, poisoning.n, pummel.v, punch.v, run through.v, slap.v, slice.v, smack.v, smash.v, spear.v, squash.v, stab.v, sting.v, stone.v, strike.n, strike.v, swipe.v, thwack.v, torture.v, transfix.v, twist.v, welt.v, whip.v, wound.v

## Cause_motion  (frame id 55)

An Agent causes a Theme to move from a Source, along a Path, to a Goal. Different members of the frame emphasize the trajectory to different degrees, and a given instance of the frame will usually leave some of the Source, Path and/or Goal implicit. The completion of motion is not required (unlike the Placing frame, see below), although individual sentences annotated with this frame may emphasize the Goal. '' This frame is very broad and contains several different kinds of words that refer to causing motion. Some words in this frame do not emphasize the Manner/Means of causing the motion (transfer.v, move.v). For many of the others (cast.v, throw.v, chuck.v, etc.), the Agent has control of the Theme only at the Source of motion, and does not experience overall motion. For others (e.g. drag.v, push.v, shove.v, etc.) the Agent has control of the Theme throughout the motion; for these words, the Theme is resistant to motion due to some friction with the surface along which they move. 'She threw her shoes into the dryer .' 'The mechanic dragged the jack out from under the car .' 'We will move the sofa out of the room through the french doors, down the stairs, and onto the sidewalk .' '' '' This frame is used in a very large number of productive metaphors, not all of which can be outlined here. The most salient types include causing an entity, construed as a Theme, to change state from an initial state (Source) via an intermediate state (Path) to a final state (Goal): 'Hillary was catapulted to stardom and his life has never been the same since . CNI' 'She felt as though flung from health to illness and back by the day , by the hour .' 'Once our parents are dead , we are catapulted into becoming the older generation ourselves . CNI' 'Croquet was pushed out by tennis .' '' A particularly divergent subtype casts changing someone's intentions as changing their location: 'Democratsforced the Senate into a rare closed door session .' 'He nudged Mrs Thatcher towards acceptance of a unified Germany .' '' Another subtype is specifically about causing a change in quantity (the Theme) through some sequence of values (Source, Path, and Goal): 'Bonus payments would be handed out for pushing up voting levels CNI .' '' Another type, with many subtypes, involves causing an action or state (construed as a Theme) to have an effect on another person or location or conceptual domain. In such cases, theGoal is used for the final affected domain, and Source for initial affected domain, Path for an intermediate affected domain, and Distance for degree of difference between original application of the action and final: 'Jake had been hurling these same insults at her now for years' 'One can not press this argument too far .' 'She shoved the thought to the very back of her mind .' 'She flung him a savage little smile .' All of the foregoing metaphorical uses are annotated in this frame and marked "Metaphor", since they seem to be semantically motivated and not lexically idiosyncratic. '' '' This frame contrasts with the following frames which talk about an Agent changing a Theme's position with respect to a landmark (either Source or Goal): '' In Placing, the figure (Theme) is profiled as the object, and ends up on the ground (Goal). The focus is on the final stage of motion, in which the Theme ends up at the Goal, and usually stably remains there. 'Joyce placed the flowers onto the bed.' '' In Filling, the ground (Goal) is profiled as the object, and the figure (Theme) ends up on the ground (Goal). 'John filled the box with old toys.' '' In Removing, the figure (Theme) is profiled, and is removed from the ground (Source). 'Jennifer removed the flowers from the bed.' '' In Emptying, the ground (Source) is profiled and the figure (Theme) is removed from it. 'Jason emptied the box of the old toys .' '' Words of this frame also differ from the words of the Bringing frame in that they are more general: either the Agent has a momentary interaction with the Theme that causes its motion, unlike the continuous causation of Bringing, or the Agent continuously acts on the Theme, but there is no supporting object that helps with the motion like the Carrier of the Bringing frame.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the one whose action causes the motion of a Theme. The Agent is generally realized as the External Argument. 'Pat threw the china at the wall.' |
| Area | Core | The FE Area is used for expressions which describe a general area in which motion takes place when the motion is understood to be irregular or not to consist of a single, linear path. Locative setting adjuncts may also … |
| Cause | Core | Cause marks expressions that indicate some non-intentional, typically non-human, force that causes the Theme to be set in motion. 'The storm tossed the sailor from the boat' |
| Goal | Core | The FE Goal is the point at which the Theme ends up as a result of the motion. 'Kim threw the cat into the garden.' |
| Initial_state | Core | A previous state that the Theme was in before the beginning of its motion. 'Paul pulled Fran upright from her sitting position.' |
| Path | Core | The FE Path is any description of a trajectory of motion which is neither a Source nor Goal. 'I pushed the trolley along the street.' |
| Result | Core | A resultant state that the Theme is in at the end of its motion. 'The fireman dragged the injured driver clear' |
| Source | Core | The FE Source is the starting point of motion. 'Pat dragged the box out of the cupboard.' |
| Theme | Core | The FE Theme is generally an NP Object. 'Pat threw the china at the wall.' |
| Degree | Extra-Thematic | Degree to which event occurs |
| Depictive | Extra-Thematic | The state of a participant during the action 'We pushed the cart around, gleeful.' |
| Distance | Peripheral | The FE Distance is any expression characterizing the extent of motion of the Theme. 'Pat threw the Javelin 50 meters.' |
| Duration | Peripheral | The amount of time that the action requires. |
| Explanation | Extra-Thematic | This FE denotes a proposition from which the main clause logically follows. |
| Handle | Extra-Thematic | The Agent's manipulation of the Theme may be further specified as being localized to some part of the Theme, a Handle. The Handle is usually expressed as a PP |
| Instrument | Peripheral | An entity saliently involved in the transmission of force from an Agent to a Theme. It may be the Agent's bodypart, or some kind of device. 'When passing a basketball, you should throw with bath hands.' |
| Manner | Peripheral | The FE Manner is any expression which describes a property of the motion of the Theme which is not directly related to the trajectory of motion. Descriptions of steadiness, grace, and other things count as Manner … |
| Means | Peripheral | The FE Means indicates the action that is taken that results in the motion of the Theme |
| Place | Peripheral | The Place is the general area that provides a setting for a specific motion (with Source, Path, or Goal). |
| Subregion | Extra-Thematic | Subregion identifies the part of the Theme that makes contact with the resulting location. When Subregion is expressed, there usually is no Goal expressed. 'The horse pitched the rider on his head' |
| Time | Peripheral | The time at which the motion of the Theme occurs. 'We shoved half of the cargo overboard on the 29th.' |

**Frame relations** (super → sub)

- Causative_of: Cause_motion → Motion
- Inheritance: Cause_motion → Cause_fluidic_motion
- Inheritance: Cause_motion → Passing
- Inheritance: Cause_motion → Shoot_projectiles
- Inheritance: Transitive_action → Cause_motion
- Metaphor: Cause_motion → Manipulate_into_doing
- ReFraming_Mapping: Cause_motion → Bringing
- See_also: Cause_motion → Bringing
- See_also: Cause_motion → Emptying
- See_also: Cause_motion → Filling
- See_also: Cause_motion → Placing
- See_also: Cause_motion → Removing
- See_also: Manipulation → Cause_motion
- Subframe: Cause_motion → Placing
- Subframe: Cause_motion → Removing
- Using: Cause_motion → Bringing
- Using: Cause_motion → Excreting
- Using: Cause_motion → Gathering_up
- Using: Cause_motion → Ingestion

**Lexical units** (42): attract.v, cast.v, catapult.v, chuck.v, drag.v, draw.v, drive.v, drop.v, fling.v, force.v, haul.v, hit.v, hurl.v, impel.v, jerk.v, knock.v, launch.v, lift.v, move.v, nudge.v, pitch.v, press.v, propel.v, pull.v, punt.v, push.v, rake.v, roll.v, run.v, scoot.v, shove.v, slam.v, slide.v, stick.v, throw.v, thrust.v, toss.v, transfer.v, tug.v, wrench.v, wrest.v, yank.v

## Cause_temperature_change  (frame id 334)

In this frame, an Agent changes the temperature of an Item. A Temperature_goal can specify the desired temperature. A Temperature_change can also be indicated. The Temperature_start indicates the initial temperature. 'Margaret Anne chilled the salad to 30 degrees.' 'Heat the water 30 degrees.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent performs the intentional act which changes the temperature of the Item. 'Ryan reheated the pasta in the microwave.' |
| Cause | Core | An animate or inanimate entity, a force, or event that changes the temperature. Volitionality is not a necessary characteristic of Causes. 'The sun warmed the house.' |
| Hot_Cold_source | Core | The Hot_Cold_source is the source of the heat or coolness. 'We chilled the drinks on ice.' |
| Item | Core | The Item undergoes the temperature change. 'Ryan reheated the pasta in the microwave.' |
| Circumstances | Extra-Thematic | This FE identifies the Circumstances at which the temperature change occurs. 'Bill cooled the jello at room temperature.' |
| Container | Peripheral | This FE identifies the Container that holds the Item whose temperature is being changed. 'Heat the potatoes in a medium-sized pan.' |
| Degree | Peripheral | The degree to which the Item approaches (an implicit) Temperature_goal, which is often construed to be the ambient temperature. 'You'll probably have to wait a while to warm your legs up completely.' |
| Depictive | Extra-Thematic | This FE identifies the Depictive phrase describing the Agent or Item. |
| Duration | Peripheral | The length of time for which the Agent changes the temperature of the Item. 'Refrigerate the cookie dough for an hour before baking.' |
| Instrument | Peripheral | This FE identifies the Instrument with which the Agent changes the temperature of the Item. |
| Manner | Peripheral | This FE identifies the Manner in which the Agent changes the temperature of the Item. |
| Means | Peripheral | This FE identifies the Means by which the Agent changes the temperature of the Item. |
| Place | Peripheral | This FE identifies the Place where the Agent changes the temperature of the Item. |
| Purpose | Extra-Thematic | This FE identifies the Purpose for which the Agent changes the temperature of the Item and what the Agent hopes to accomplish. |
| Result | Extra-Thematic | Result is the resultant state of the Agent changing the temperature of the Item. |
| Subregion | Extra-Thematic | The Subregion describes which part of a larger whole is being affected. 'The mousse was chilled around the edges.' |
| Temperature_change | Peripheral | The Temperature_change is the amount of difference between the intial and goal temperatures. |
| Temperature_goal | Peripheral | The Temperature_goal is the temperature to which the Agent is heating or cooling the Item. 'Heat the syrup to 180 degrees.' |
| Temperature_start | Peripheral | Temperature_start is the initial temperature of the Item. 'Heat the sugar water mixture from room temperature until it reaches 180 degrees.' |
| Time | Peripheral | This FE identifies the Time when the Agent changes the temperature of the Item. |

**Frame relations** (super → sub)

- Causative_of: Cause_temperature_change → Change_of_temperature
- Inheritance: Transitive_action → Cause_temperature_change
- ReFraming_Mapping: Cause_temperature_change → Change_of_temperature

**Lexical units** (10): chill.v, cool down.v, cool.v, heat up.v, heat.v, overheat.v, refrigerate.v, reheat.v, warm up.v, warm.v

## Cause_to_be_wet  (frame id 309)

An Agent causes a Patient to be wet with a Liquid. In this frame, the Liquid can be a liquid or gas. Patients are porous objects, but not hollow (like containers). 'Jo soaked the dog with water.' 'Ellen wet the sponge with water.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is a volitional animate being who causes the Patient to become wet. 'Hannah drenched the cat with anti-flea ointment.' |
| Cause | Core | An animate or inanimate entity, a force, or event that produces the state of wetness. 'The sprinklers drenched me.' |
| Liquid | Core | The Liquid is a fluid or gas that permeates or covers the Patient. It most frequently occurs in a PP Complement headed by with. 'Jo soaked the dog with water.' |
| Patient | Core | The Patient takes up the Liquid through its pores or has the Liquid covering its surface. 'Ellen wet the sponge with water.' |
| Degree | Peripheral | Degree to which the Agent wets the Patient. 'Ryan doused the fire with water until it stopped smoldering.' |
| Explanation | Extra-Thematic | This FE describes the reason for the state of the Cause_to_be_wet event. |
| Instrument | Peripheral | This FE identifies the Instrument with which an Agent intentionally wets the Patient. 'Colin doused the burning pot with a fire extinguisher.' |
| Manner | Peripheral | This FE identifies the Manner or way in which the Agent wets the Patient. |
| Means | Peripheral | This FE identifies the Means by which an the Agent wets the Patient |
| Place | Peripheral | This FE identifies the Place where the Agent wets the Patient. |
| Purpose | Extra-Thematic | This FE identifies the Purpose for which the Agent wets the Patient and what the Agent hopes to accomplish. |
| Subregion | Extra-Thematic | The Subregion describes which part of a larger whole is being affected. 'The cloth was wetted around the edges.' |
| Time | Peripheral | This FE identifies the Time when the Agent wets the Patient. |

**Frame relations** (super → sub)

- Causative_of: Cause_to_be_wet → Being_wet
- Inheritance: Transitive_action → Cause_to_be_wet

**Lexical units** (12): dampen.v, douse.v, drench.v, humidify.v, hydrate.v, moisten.v, moisturize.v, saturate.v, soak.v, sop.v, souse.v, wet.v

## Cause_to_end  (frame id 1149)

An Agent or Cause causes a Process or State to end. 'Bush may lift sanctions on his own, despite opposition.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The individual who causes the Process or State to end. |
| Cause | Core | An event that causes the Process or State to end. 'That move ended her political career, she said in a 1994 Times Union interview.' |
| Process | Core | A Process which is ended by the Agent or Cause. |
| State | Core | A State which is ended by the Agent or Cause. 'We should end poverty.' |
| Degree | Peripheral | The Degree to which the Process or State is brought to an end. |
| Depictive | Extra-Thematic | Depictive phrase describing the actor of the event that causes the Process or State to end. |
| Explanation | Extra-Thematic | The Explanation for why the Process or State is ended. |
| Manner | Peripheral | The Manner of causing the Process or State to end. |
| Means | Peripheral | An action of the Agent that causes the Process or State to end. |
| Place | Peripheral | The location where the Process or State is caused to end. 'They ended their relationship in the same coffeehouse where it started.' |
| Time | Peripheral | The Time when the Process or State is ended. |

**Frame relations** (super → sub)

- Causative_of: Cause_to_end → Process_end
- Inheritance: Transitive_action → Cause_to_end

**Lexical units** (7): abort.v, arrest.v, do away with.v, end.v, lift.v, lifting.n, put an end to.v

## Cause_to_move_in_place  (frame id 276)

An Agent causes a Theme to move with respect to a certain Fixed_location, generally with a certain Periodicity, without undergoing unbounded translational motion or significant alteration of configuration/shape. 'Paul shook the remote control frantically.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent performs the intentional act. |
| Bodypart_of_agent | Core | This FE identifies the part of the Agent's body being used to manipulate the Theme. 'Kim twirled the glass in his fingers.' |
| Cause | Core | Cause identifies the non-agentive force that causes the motion in place. 'The wind vibrated the string.' |
| Theme | Core | Theme identifies the object involved in motion. |
| Angle | Peripheral | Angle identifies the amount that the Theme turns. 'Spin the dial a quarter turn.' |
| Degree | Peripheral | Degree to which event occurs |
| Direction | Peripheral | This frame element is used for all path-like expressions, that express the Direction of the swinging, vibrating or rotating. |
| Duration | Peripheral | The amount of time for which a state holds or a process is ongoing. |
| Explanation | Extra-Thematic | This FE identifies the Explanation for which an event occurs. |
| Fixed_location | Peripheral | The point or set of points that define the limits of motion for the Theme. For spinning motions, it is the axis, for vibrating it is a boundary, for swinging it is a point. 'She twirled around him several times.' … |
| Instrument | Peripheral | This FE identifies the Instrument with which an intentional act is performed. |
| Locus | Extra-Thematic | The Agent's manipulation of an Theme may be further specified as being localized to some part of the Theme, a Locus. This FE is usually expressed as a PP Complement. 'Pat squeezed Jo by the hand.' |
| Manner | Peripheral | Manner of performing an action |
| Means | Peripheral | The Means is the way in which the motion in place is instigated. |
| Periodicity | Peripheral | The number of times the Theme returns to a state in a given duration. 'It turns at 1000 rpms.' |
| Place | Peripheral | This FE identifies the Place where the event occurs. |
| Purpose | Extra-Thematic | This FE identifies the Purpose for which an intentional act is performed. |
| Result | Extra-Thematic | This FE identifies the Result of an event. |
| Time | Peripheral | This FE identifies the Time when the event occurs. |

**Frame relations** (super → sub)

- Causative_of: Cause_to_move_in_place → Moving_in_place
- Inheritance: Transitive_action → Cause_to_move_in_place
- ReFraming_Mapping: Cause_to_move_in_place → Moving_in_place
- Using: Activity_ongoing → Cause_to_move_in_place
- Using: Manipulation → Cause_to_move_in_place

**Lexical units** (16): jiggle.v, juggle.v, rock.v, roll.v, rotate.v, seesaw.v, shake.v, spin.v, squeeze.v, swing.v, swirl.v, turn.v, twirl.v, vibrate.v, wave.v, wiggle.v

## Cause_to_start  (frame id 381)

A Cause, animate or inanimate, causes a process, the Effect, to begin. 'The murder of Sergei Kirov set off a chain of events that culminated in the Great Terror of the 1930s.' 'Space email sparked astronaut jealousy.' 'A crime surge in a former coal town prompted a crackdown on illegal immigrants'.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cause | Core | An animate or inanimate entity, a force, or event that produces an effect. Volitionality is not a necessary characteristic of Causes. 'The programme sparked a public outcry.' |
| Effect | Core | This Frame Element marks expressions that indicate the process that the Cause initiates. 'Few things spark the wrath of the British like food additives.' |
| Circumstances | Extra-Thematic | The state of the world at the time when the Cause produces the Effect. |
| Co-timed_event | Extra-Thematic | This FE identifies the first Co-timed_event of the started Effect. |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the target operates (often denoted by words such as "officially," "formally," "technically," etc.). |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Containing_event | Extra-Thematic | This FE denotes an event that occurs or state of affairs that holds at a time that includes the time during which the event or state of affairs reported by the target occurs and of which it is taken to be a part. |
| Depictive | Extra-Thematic | This FE identifies the Depictive phrase describing the actor or undergoer of an action. |
| Event_description | Extra-Thematic | This FE applies to appraisals of the event, typically a judgment of its expectedness |
| Explanation | Extra-Thematic | The reason why or the way in which the Cause causes the Effect. |
| Manner | Peripheral | The way in which the Cause causes the Effect. |
| Means | Peripheral | The Means is the way in which the Cause causes the process to begin. |
| Medium | Peripheral | Medium is the physical or abstract setting in which the Cause results in the Effect. |
| New_situation | Extra-Thematic | A consecutive event to the starting of the Effect. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. In addition, most … |
| Place | Peripheral | This FE identifies the Place where the Effect occurs. 'In Obscurania, the release of the movie sparked protests.' |
| Purpose | Extra-Thematic | To what end the Cause caused the Effect. |
| Time | Peripheral | This FE is for the Time when causing to start occurs |

**Frame relations** (super → sub)

- Causative_of: Cause_to_start → Process_start
- Inheritance: Causation → Cause_to_start
- ReFraming_Mapping: Activity_start → Cause_to_start
- Using: Cause_to_start → Launch_process

**Lexical units** (21): actuate.v, arouse.v, bring about.v, call forth.v, create.v, elicit.v, engender.v, excite.v, generate.v, incite.v, instigate.v, kindle.v, motivate.v, produce.v, prompt.v, provoke.v, set off.v, spark.v, stimulate.v, stir up.v, trigger.v

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

## Change_event_time  (frame id 691)

In this frame, an Agent or Cause changes the timing of an Event. The Event will then take place at the Destination_time or with respect to a Destination_event. This can be done with by certain Means, in a certain Manner or to a certain Degree. 'The rain delayed the baseball game.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the animate entity which brings about the change in time of the Event. 'The umpire postponed the game.' |
| Cause | Core | The Cause is the non-sentient force which brings about the change of time for the Event. 'The rain delayed the baseball game.' |
| Event | Core | The Event is the occurrence which changes time. 'The opening of the musical was delayed.' |
| Degree | Peripheral | The Degree is the extent to which the time change takes place. |
| Destination_event | Peripheral | The Destination_event is the occasion which the timing of the Event occurs with respect to. 'Consumers should postpone purchasing a new car until their credit rating is acceptable.' |
| Destination_time | Peripheral | The Destination_time is the time at which the Event actually occurs. 'The king is postponing the festival until July.' |
| Explanation | Extra-Thematic | The Explanation is the reason or explanation for why the Event occurs at a different time. |
| Interval | Peripheral | The Interval between the Landmark_time and the Destination_time may be expressed. 'The lanch will be delayed for two months.' |
| Landmark_time | Peripheral | The Landmark_time is when the Event was originally intended to take place. 'The driving test was postponed from July to September.' |
| Manner | Peripheral | The Manner is the way in which the time change takes place. 'My mother thoughtlessly delayed my salon appointment.' |
| Means | Peripheral | The Means describe the way in which the time change is accomplished. 'The mayor delayed the ribbon-cutting ceremony by pretending to be ill.' |
| Place | Peripheral | The location at which the expected time of the Event changes. |
| Purpose | Peripheral | The state-of-affairs that the Agent intends to bring about by changing the time the Event will take place. |
| Time | Peripheral | The time at which the delay occurred. |

**Frame relations** (super → sub)

- Inheritance: Cause_change → Change_event_time
- ReFraming_Mapping: Change_event_time → Scheduling
- ReFraming_Mapping: Relative_time → Change_event_time
- Using: Calendric_unit → Change_event_time
- Using: Change_event_time → Holding_off_on
- Using: Change_event_time → Waiting
- Using: Scheduling → Change_event_time

**Lexical units** (13): advance.v, defer.v, delay [duration].n, delay.n, delay.v, hold over.v, hold up.v, move back.v, move up.v, postpone.v, put off.v, put over.v, reschedule.v

## Change_of_temperature  (frame id 797)

In this frame, the temperature of an Item changes. An Initial_temperature, Final_temperature, or Temperature_change can also be indicated. 'The house had cooled off by a few more degrees by midnight, and we finally managed to eat a bite.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Item | Core | The entity whose temperature changes. |
| Temperature | Core | The scalar property that the Item possesses. This FE is rarely expressed. 'The raw fish that is to be eaten as sushi has to be meticulously prepared and must first be chilled in temperature to exactly above freezing … |
| Cause | Peripheral | An event or state-of-affairs that leads to the change in temperature of the Item. |
| Circumstances | Extra-Thematic | This FE identifies the Circumstances under which the temperature change occurs |
| Container | Peripheral | This FE identifies the Container that holds the Item whose temperature is being changed. |
| Degree | Peripheral | The degree to which the change in temperature takes place. |
| Depictive | Extra-Thematic | The state of the Item during the temperature change. |
| Duration | Peripheral | The span of time in which the Item is changing temperature. |
| Final_temperature | Peripheral | The temperature of the Item after the event. |
| Hot_cold_source | Peripheral | The Hot_cold_source is the source of the heat or coolness |
| Initial_temperature | Peripheral | The temperature that the Item has prior to the event. |
| Manner | Peripheral | The manner in which the Item changes temperature. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Place | Peripheral | The location at which the Item changes temperature. |
| Result | Peripheral | The state of the Item that results from the temperature change. |
| Subregion | Extra-Thematic | A portion of the Item which is affected by the temperature change. |
| Temperature_change | Peripheral | The amount of difference between the Initial_temperature and the Final_temperature of the Item. |
| Time | Peripheral | The time at which the change in temperature occurs. |

**Frame relations** (super → sub)

- Causative_of: Cause_temperature_change → Change_of_temperature
- Inchoative_of: Change_of_temperature → Temperature
- Inheritance: Change_position_on_a_scale → Change_of_temperature
- ReFraming_Mapping: Cause_temperature_change → Change_of_temperature

**Lexical units** (7): chill.v, cool off.v, cool.v, heat.v, refrigerate.v, reheat.v, warm.v

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

## Chemical_potency  (frame id 2724)

This frame contains words that describe how potent a chemical is.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Chemical_entity | Core | The entity for which potency is being evaluated. |
| Degree | Core | A modifier expressing the deviation of the potency from the norm expressed by the target LU. |
| Circumstances | Extra-Thematic | Some specification of the circumstances under which the Chemical_entity has the ascribed potency. |
| Place | Extra-Thematic | The location where the Chemical_entity has the ascribed potency. |
| Time | Extra-Thematic | The time during which the Chemical_entity is in the state of having a particular potency. |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Chemical_potency

**Lexical units** (3): potent.a, stiff.a, strong.a

## Clothing  (frame id 134)

This frame refers to clothing and its characteristics, including anything that people conventionally wear. The Wearer wears a Garment that has a certain Style, is made of a certain Material, and can be otherwise characterized by a Descriptor. In some cases, the Body_location (where the garment is worn) and Subregion of the clothing may also be specified. 'Claudia dressed in a dark green cotton DRESS clasped round her slender waist with a broad yellow belt , drank a cup of coffee and opened her neglected post .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Garment | Core | This FE identifes the clothing worn. 'Mike wore a new leather jacket.' |
| Body_location | Peripheral | Body_location identifies the place on the body where the clothing is worn. 'Hannah draped a shawl elegantly over her shoulders.' |
| Creator | Peripheral | The individual who created the Garment. 'She 's wearing a Ralph Lauren dress.' |
| Descriptor | Peripheral | This FE identifes any description of the clothing besides Style and Material. 'Mike wore a new black leather jacket.' Note that each modifer of the target gets its own FE (and, hence, its own GF and PT). |
| Material | Peripheral | This FE identifes the material from which the clothing is made. 'Mike wore a new leather jacket.' |
| Name | Peripheral | The name given to a specific Garment. Note this is not the name of a general class of clothing items, but rather an individual item. This is accordingly VERY RARE. '' |
| Style | Peripheral | This FE identifes the design, or cut, of the clothing. 'Mike wore a tailored leather jacket.' |
| Subregion | Peripheral | This FE identifies a part of the clothing. 'Mike wore a leather jacket with fringes.' |
| Time_of_creation | Peripheral | The time at which the Creator makes the Garment. 'The bikinis of the 1940's are fairly similar.' |
| Use | Peripheral | This FE identifes the Use for which a Garment is worn or was made. 'Mike wore a new riding jacket.' |
| Wearer | Peripheral | The Wearer is the person wearing the clothes, or for whom the clothes are intended. 'Mike wore a new leather jacket.' |

**Frame relations** (super → sub)

- Inheritance: Artifact → Clothing
- ReFraming_Mapping: Clothing → Armor
- Using: Closure → Clothing
- Using: Clothing → Clothing_parts
- Using: Clothing → Dressing
- Using: Clothing → Undressing
- Using: Clothing → Wearing

**Lexical units** (163): abaya.n, alb.n, apparel.n, apron.n, attire.n, ballgown.n, bathrobe.n, bikini.n, blazer.n, blouse.n, bodice.n, boot.n, bow-tie.n, bra.n, brassiere.n, breeches.n, briefs.n, buskin.n, camisole.n, cape.n, cardigan.n, chasuble.n, chemise.n, cloak.n, clog.n, clothes.n, clothing.n, coat.n, cope.n, corset.n, cossie.n, costume.n, cottons.n, coverall.n, cowl.n, cravat.n, crinoline.n, culottes.n, cummerbund.n, doublet.n, dress.n, ensemble.n, ermines.n, finery.n, fishnet.n, flannels.n, flip-flops.n, footwear.n, frock.n, g-string.n, galosh.n, garb.n, garment.n, garter.n, gauntlet.n, get-up.n, glove.n, gown.n, greatcoat.n, gumboot.n, hose.n, hosiery.n, jacket.n, jeans.n, jerkin.n, jodhpurs.n, jumper.n, jumpsuit.n, kaftan.n, kilt.n, kimono.n, knickers.n, leggings.n, legwarmers.n, lingerie.n, livery.n, miniskirt.n, mitt.n, mitten.n, motley.n, muff.n, muslins.n, neckerchief.n, necktie.n, neckwear.n, nightdress.n, nightgown.n, nightie.n, nightwear.n, one-piece.n, outfit.n, overall.n, overcoat.n, pallium.n, panties.n, pants.n, pantyhose.n, parka.n, petticoat.n, pinafore.n, polo-neck.n, poncho.n, pullover.n, pyjama.n, rags.n, raiment.n, raincoat.n, regalia.n, robe.n, sandal.n, sari.n, sarong.n, satins.n, scarf.n, shawl.n, shift.n, shirt.n, shoe.n, shorts.n, silks.n, skirt.n, slip.n, slipper.n, smock.n, sneaker.n, sock.n, stiletto.n, stocking.n, stole.n, suit.n, sundress.n, surplice.n, sweater.n, sweatpants.n, sweatshirt.n, swimsuit.n, t-shirt.n, tatters.n, teddy.n, tie.n, tights.n, tippet.n, togs.n, tracksuit.n, trousers.n, tunic.n, tutu.n, tweeds.n, two-piece.n, underclothes.n, underclothing.n, undergarment.n, underwear.n, undies.n, uniform.n, vest.n, vestment.n, waistcoat.n, wellington.n, welly.n, windbreaker.n, windcheater.n, wrap.n

## Cogitation  (frame id 22)

A person, the Cognizer, thinks about a Topic over a period of time. What is thought about may be a course of action that the person might take, or something more general. 'The men were silently mulling over the proposition of committing an assassination'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | With a target verb, the Cognizer is usually expressed as an External Argument, with the Topic appearing as an Object NP, a gerundive verbal Complement, or a PP. 'Pat considered a career change.' 'The employees … |
| Topic | Core | With a target verb, the Topic is usually expressed as an Object NP, a gerundive verbal complement, or a PP. 'Pat considered a career change.' 'The employees contemplated going on strike.' 'Everyone thought about the … |
| Degree | Extra-Thematic | The FE Degree indicates the degree to which the cognizing occurs. |
| Depictive | Extra-Thematic | Depictive phrase describing the actor of an action |
| Manner | Peripheral | The FE Manner indicates the way in which the cognizing is being done. |
| Means | Peripheral | An intentional action performed by the Cognizer that makes them able to cogitate. |
| Medium | Extra-Thematic | The physical or abstract setting in which the Cognizer considers the Topic. 'Over the telephone, Frank pondered telling Maria about the fire.' |
| Purpose | Peripheral | The state-of-affairs that the Cognizer is trying to bring about by thinking. |
| Result | Extra-Thematic | Result of an event |
| Time | Peripheral | The time at which the Cognizer considers the Topic. |

**Frame relations** (super → sub)

- Inheritance: Cogitation → Assessing
- Inheritance: Cogitation → Emotion_active
- Inheritance: Cogitation → Memorization
- Using: Cogitation → Remembering_experience
- Using: Cogitation → Research
- Using: Mental_activity → Cogitation

**Lexical units** (20): brood.v, consider.v, consideration.n, contemplate.v, contemplation.n, deliberate.v, deliberation.n, dwell.v, give thought.idio, meditate.v, meditation.n, mull over.v, muse.v, ponder.v, reflect.v, reflection.n, ruminate.v, think.v, thought.n, wonder.v

## Colonization  (frame id 1794)

A group of Colonists from a Homeland migrate to and proceed to settle in a New_area. The New_area then becomes their permanent home. The New_area and Homeland are in some way construed as being part of the same organization or system. In the case of (people from) nation-states colonizing other areas, the colony and nation-state are considered a single political entity. In the extended sense of living things in general colonizing or settling a new area, the original Homeland must still inhabited by some of the same group. In this sense Colonization is distinct from migration or exodus. 'In the 7th century BC, Phoenicians colonized the eastern section of Libya.' 'In the 7th century BC, Phoenicians colonized the eastern section of Libya.' 'Finns colonized the land from the south some 2,000 to 4,000 years ago' 'If a colony from Britain was established in that large tract of Country, and if we were at war with Holland or Spain, we might very powerfully annoy either state from our new settlement.' This frame also includes metaphorical uses involving animals or plants, or abstract domains such as ideas. 'Deciduous trees such as red alder subsequently colonized the logged area.' 'Conservatives don't get what the left gets, which is that the left has already colonized and converted whole university departments.' 'As the years progressed and adaptations occurred new species and subspecies began to populate the islands.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Colonists | Core | A group of people who move together to an area outside their Homeland for the purpose of settling. 'Spain settled the northern areas of Mexico through the use of missions, civil settlements, and presidios. ' Often the … |
| Homeland | Core | The Homeland is where the Colonists are originally from. |
| New_area | Core | The Colonists move to the New_area, inhabiting it and (in the case of nation-states) extending the control of the Homeland. 'Norse invaders in the 900s colonized the North Midlands more densely than any other part of … |
| Degree | Extra-Thematic | The extent to which the group of Colonists spreads across or inhabits the New_area. 'In the reign of Elizabeth, the English strove to thoroughly colonize Ireland, which they had originally invaded in the twelfth … |
| Descriptor | Extra-Thematic | A characteristic of the Colonists, Homeland, or New_area. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the colonization event logically follows. |
| Purpose | Peripheral | The purpose for which the colonizing is done. 'Humans in the future may end up colonizing outer space in order to survive.' |
| Time | Peripheral | The time at which the colonizing takes place. 'The English colonized the islands in 1632.' |

**Frame relations** (super → sub)

- Using: Residence → Colonization

**Lexical units** (10): colonist.n, colonize.v, colony.n, people.v, populate.v, repopulate.v, settle.v, settlement [act].n, settlement [entity].n, settler.n

## Commerce_pay  (frame id 180)

This frame involves Buyers paying Money for Goods. In this frame the Money is the direct object, and is mapped to the theme of the transfer. 'I paid her $50 for a video game.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Buyer | Core | The Buyer has the Money and wants the Goods. 'Gem paid fifty dollars for a shirt' |
| Goods | Core | The FE Goods is anything (including labor or time, for example) which is exchanged for Money in a transaction. 'Kim paid fifty dollars for the shirt' |
| Money | Core | Money is the thing given in exchange for Goods in a transaction. 'Pat paid 14 dollars for a movie ticket.' |
| Rate | Core | In some cases, price or payment is described per unit of Goods. 'The manager pays the paper boys five dollars an hour. ' |
| Seller | Core | The Seller has the Goods and wants the Money. 'The landlord is paid $700 a month by the tenants for the apartment. ' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. 'Worker 's compensation payments alone in cases … |
| Explanation | Extra-Thematic | The Explanation for which an event occurs. |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. 'A good tenant pays her rent regularly' |
| Manner | Peripheral | Any description of the paying event which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may also indicate salient … |
| Means | Peripheral | The Means by which a commercial transaction occurs. Abby bought the car with cash. Robin paid for the car by check. |
| Place | Peripheral | Where the event takes place. |
| Purpose | Peripheral | The Purpose for which an intentional act is performed. |
| Time | Peripheral | When the event occurs. |
| Unit | Peripheral | This FE is any unit in which goods or services can be measured. Generally, it occurs in a by-PP. 'Bob pays for peppers by the pound. ' |

**Frame relations** (super → sub)

- Inheritance: Giving → Commerce_pay
- Perspective_on: Commerce_money-transfer → Commerce_pay
- ReFraming_Mapping: Commerce_scenario → Commerce_pay
- Using: Commerce_pay → Earnings_and_losses

**Lexical units** (6): disburse.v, disbursement.n, pay.v, payer.n, payment.n, shell out.v

## Communicate_categorization  (frame id 796)

A Speaker communicates a message stating an Item's membership in a Category, i.e., asserts that the Item has the defining characteristics of the Category. Alternatively, the message is conceived as communicated by a Medium. 'He depicted his involvement as merely peripheral.' 'The first half of the book portrays Bragg's mother as a beautiful and heartbroken woman'.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Category | Core | The class of entities with characteristics that match those of the Item according to the portrayal of the Speaker. |
| Item | Core | The entity that the Speaker portrays as belonging to a Category. |
| Medium | Core | The piece of text in which a Speaker communicates their categorization of the Item. 'However, "A Brief History of Medicine" characterizes influenza as the most deadly plague, overall.' |
| Speaker | Core | The individual that communicates the message concerning the Category of an Item. |
| Circumstances | Extra-Thematic | The Circumstances under which the categorization is made. |
| Criteria | Peripheral | The characteristics of an Item that fit the defining characteristics of a Category, and thus serve as the basis of the Speakers characterization of the Item . |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of a continuous situation (the one denoted by the target) to its end. In many cases, the continuous situation is a dynamic action which is ongoing, while in others … |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, loudly), and general descriptions comparing … |
| Means | Peripheral | An action taken by the Speaker through which they communicate that the Item fits into a particular Category. |
| Place | Peripheral | The location at which the Speaker characterizes the Item |
| Time | Peripheral | The point in time at which the Speaker makes a characterization of the Item. |

**Frame relations** (super → sub)

- ReFraming_Mapping: Categorization → Communicate_categorization
- Using: Categorization → Communicate_categorization

**Lexical units** (17): cast.v, characterization.n, characterize.v, define.v, definition.n, depict.v, depiction.n, describe.v, description.n, make out to be.v, paint.v, portray.v, redefine.v, redefinition.n, represent.v, representation.n, treat.v

## Communication_noise  (frame id 39)

This frame contains words for types of noise which can be used to characterize verbal communication. It inherits from Communication (possibly more specifically Communication_manner) and the Sound_emission frame (which simply characterizes basic sounds of whatever source, including those made by animals and inanimate objects). As such, it involves a Speaker who produces noise and thus communicates a Message to an Addressee. '' '"Don't treat me as a child!" she cried scornfully.' 'A writer in the Town Planning Review trumpeted that train-sheds were now obsolete.' 'You know he yelled at Aunt Lou yesterday, because he slipped on that mat in the hall.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Message | Core | Message has a number of different realizations in this frame, including that-clauses, direct quotes, infinitival complements, for-to phrases, and NP Objects. 'Kim whined that it wasn't fair.' '"Get moving!" Jess … |
| Speaker | Core | Speaker is the sentient entity that delivers the Message. 'Kim whined that it wasn't fair.' |
| Topic | Core | Topic occurs in PP Complements, usually headed by about. 'Kim howled about the unfairness of it all.' |
| Voice | Core | The Voice describes the Speaker's utterance or other message-encoded production. 'John's voice bellowed for her to be quiet.' |
| Addressee | Peripheral | The Addressee refers to the one toward whom the Communication_noise is directed. Addressee generally occurs in to or at PPs. 'Kim whined to Jess that it wasn't fair.' 'Jess screamed at Kim to be quiet.' |
| Back | Extra-Thematic | This FE indicates that the communication act denoted by the target is in response to an earlier communication act in which the roles of Speaker and Addressee were reversed. This is conceptually akin to the … |
| Degree | Peripheral | Degree to which event occurs |
| Depictive | Extra-Thematic | This FE identifies the state of the Speaker during the communication. '"Get outta here!" he barked unflinching.' |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the main clause (headed by the target) logically follows. This often means that the Explanation causes the target's proposition, but not in all cases. |
| Internal_cause | Extra-Thematic | The Communication_noise may be prompted by either some outside phenomenon or occurrence, or by an Internal_cause, the Speaker's mental or emotional state. Internal_cause is expressed in a PP Complement. 'Kim growled at … |
| Manner | Peripheral | Manner describes the manner or style in which the Communication_noise is delivered. '"Huh!" he grunted disbelievingly.' '`"Long , dark hair" he murmured thoughtfully.' |
| Means | Peripheral | The Means by which the Speaker communicates. |
| Medium | Peripheral | Medium is used for a physical entity or channel that transmits the Message. It is normally expressed as a PP Complement headed by on or in. 'Pat screamed something in Spanish.' |
| Place | Peripheral | This FE identifies the Place where an event occurs. |
| Time | Peripheral | This FE identifies the Time where the Communication noise event occurs. |

**Frame relations** (super → sub)

- Inheritance: Communication → Communication_noise
- Using: Make_noise → Communication_noise

**Lexical units** (59): babble.n, bark.v, bawl.v, bellow.v, bleat.v, bray.v, burble.v, cackle.v, chirp.v, chirrup.v, chuckle.v, cluck.v, coo.v, croak.v, croon.v, crow.v, cry.v, drone.v, gasp.v, grate.v, groan.v, growl.v, grunt.v, gurgle.v, hiss.v, hoot.v, howl.v, moan.v, murmur.v, purr.v, rap.v, rasp.v, rattle.v, roar.v, rumble.v, scream.v, screech.v, shriek.v, shrill.v, snarl.v, snort.v, splutter.v, sputter.v, squawk.v, squeak.v, squeal.v, thunder.v, titter.v, trill.v, trumpet.v, twitter.v, wail.v, warble.v, wheeze.v, whimper.v, whine.v, whoop.v, yell.v, yelp.v

## Compatibility  (frame id 360)

Item-1 and Item-2 are compatible with each other if they can exist or function together in some context without problems, conflict, or other undesirable situation. The set of Item-1 and Item-2 may be expressed jointly as Items. The Degree to which the Items are compatible may also be indicated, as may be a Parameter along whose lines the Items are compatible. ' Make sure your site is compatible with any browser.' 'Our software applications are compatible. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Item_1 | Core | The Frame Element Item_1 marks the grammatically more prominent of the two entities, i.e.the subject in active clauses, when they are expressed separately. 'That technology turned out not to be compatible with the … |
| Item_2 | Core | The Frame Element Item_2 marks the grammatically less prominent of the Items when they are expressed separately. 'My computer is not compatible with my new printer. ' |
| Items | Core | This FE is used when the Items are expressed jointly in a phrase, either a plural or a coordinated NP. 'Your socks don't match.' ' Creationism and Evolutionary Theory don't jibe.' |
| Parameter | Core | This Frame Element is used for expressions that indicate a Parameter or respect in which the Items are said to be compatible, not in conflict. 'The two applications are compatible in their essential features.' |
| Degree | Peripheral | This Frame Element is used for expressions that indicate the extent to which two Items are compatible. 'These devices are absolutely compatible.' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Compatibility

**Lexical units** (26): accord.v, agree.v, at variance.a, biocompatible.a, clash.v, cohere.v, compatibility.n, compatible.a, comport.v, conflict.v, conflicting.a, congruent.a, congruous.a, consistent.a, consonant.a, dovetail.v, fly in the face of.v, go.v, harmonize.v, harmony.n, incompatibility.n, incompatible.a, jibe.v, match.v, rhyme.v, square.v

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

## Compliance  (frame id 117)

This frame concerns Acts and State_of_Affairs for which Protagonists are responsible and which either follow or violate some set of rules or Norms. '' 'A lot of people suspect that blocking savers' access to their money violates the new constitution's explicit ban on compulsory loans to the government.' 'Not that by adhering to the subject-before-predicate principle, the translator of the above extract has had to ignore the principle of end-weight.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Act | Core | This FE identifies the Act that is judged to be in or out of compliance with the Norms. 'Jo's violation of the no trespassing law came as a surprise.' |
| Norm | Core | This FE identifies the rules or Norms that ought to guide a person's behavior. 'John violated the law by not paying taxes.' |
| Protagonist | Core | The Protagonist's behavior is in or out of compliance with norms. 'Jo violated the no trespassing law.' |
| State_of_affairs | Core | A State_of_affairs may violate a law or rule. 'Their pricing policy violated inter-governmental agreements.' |
| Degree | Peripheral | This FE identifies the Degree to which the compliance ocurrs. |
| Depictive | Extra-Thematic | Depictive identifies any description of the Actor or Undergoer. |
| Explanation | Extra-Thematic | The Explanation for complying with the Norm. 'He submitted to the will of the king because he had no other choice.' |
| Judge | Peripheral | The individual whose point of view is taken in assigning the judgment denoted by the target. |
| Manner | Peripheral | This FE identifies the Manner in which the compliance occurs. 'Jo complied with the law willingly.' |
| Means | Peripheral | This FE identifies the Means by which the compliance is (or is not) accomplished. 'He complied with the decree by firing the employees.' |
| Result | Extra-Thematic | This FE identifies the Result of compliance. |
| Time | Peripheral | This FE identifies the Time when the act of compliance or non-compliance occurs. |

**Frame relations** (super → sub)

- Inheritance: Satisfying → Compliance
- Inheritance: Social_behavior_evaluation → Compliance
- ReFraming_Mapping: Compliance → Giving_in
- Using: Compliance → Legality
- Using: Compliance → Strictness
- Using: Obligation_scenario → Compliance

**Lexical units** (35): (in/out of) line.n, abide (by).v, adhere.v, adherence.n, breach.n, breach.v, break.v, by-pass.v, circumvent.v, compliance.n, compliant.a, comply.v, conform.v, conformity.n, contrary.a, contravene.v, contravention.n, disobey.v, flout.v, follow.v, honor.v, in accordance.a, keep.v, lawless.a, noncompliance.n, obedient.a, obey.v, observance.n, observant.a, observe.v, play by the rules.v, transgress.v, transgression.n, violate.v, violation.n

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

## Connecting_architecture  (frame id 1025)

An entity is integrated into a building as a Part of a (possibly unexpressed) Whole which may refer to the whole building or merely to a sub-part of the building. The Part itself connects locations within the building to each other, Connected_locations. If a particular point of view is adopted in the context of real or imagined motion, then one of the locations can be construed as Goal and the other as Source. 'It was of great interest to me to see the star signs of Taurus the Bull and Leo the Lion on the staircase to the upper Palace.' 'All visitors may use the elevator between the Main Level and the Upper Level instead of the main staircase' 'The window into the garden was open.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Part | Core | A Part of a larger architectural unit, the Whole. 'Could you open the door for me, please?' |
| Connected_locations | Peripheral | Two or more named locations that are connected by the architectural Part. ' Security in the hallway between the jail and the Court Building needs to be improved.' |
| Creator | Peripheral | The Individual who creates the Part. 'If a caprenter's door is shoddy, is it always his fault?' |
| Descriptor | Peripheral | A property relating to the Part. 'People may give you weird looks as you struggle up the steps with your suitcase instead of using the slow escalator.' |
| Direction | Peripheral | The Direction is the direction or directions the Part of connecting architecture runs. 'Please take the east west stairs down to the lower floor' |
| Goal | Peripheral | The Goal is one of the Connected_locations treated as a goal 'Finally they corner us as we reach the escalator to the first floor.' |
| Material | Peripheral | Any indication of what makes up the Part, including components, ingredients, etc. 'The house has an oak door' |
| Orientation | Peripheral | This is a property of the Part that situates the Part within the Whole. 'We can let you in through the back door.' |
| Source | Peripheral | The Source is one of the Connected_locations treated as source. 'Does door from basement to living quarters have an adequate lock operated from living quarters side?' |
| Whole | Peripheral | An architectural unit which includes the Part. 'The kitchen door came off its hinges' |

**Frame relations** (super → sub)

- Inheritance: Architectural_part → Connecting_architecture

**Lexical units** (11): corridor.n, door.n, elevator.n, escalator.n, gate.n, hallway.n, lift.n, staircase.n, stairs.n, step.n, window.n

## Conquering  (frame id 2021)

This frame describes a Theme losing its autonomy and perhaps sustaining material damage as the result of a successful invasion on the behalf of a Conqueror. 'The Spaniards conquered the Incas with both the Cross and the arquebus' 'He said that the aim had been the takeover of the Soviet government by "advocates of swift privatization"' 'The Romans fell to the Goths in 410 AD.' 'Bright Star campaign forces captured the garrison town of Kajo Kaji'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Conqueror | Core | The Conqueror is the entity that overtakes the Theme. 'The Achaemenid monarch Cambyses conquered Egypt in the year 525 BC' |
| Theme | Core | The Theme is the land, government, and its people that is seized by the Conqueror. 'Britain had an opportunity to conquer Europe.' |
| Degree | Peripheral | This FE describes the intensity and extent of the conquering event. 'Britain had been ` completely conquered and immediately thrown away '' |
| Depictive | Extra-Thematic | This FE describes a participant of the state of affairs introduced by the target as being in some state during the action. |
| Frequency | Extra-Thematic | Frequency is the number of times the Conquering event occurs per some unit of time. |
| Instrument | Peripheral | The tool used by the Conqueror to seize the Theme. 'The army will conquer the far-away lands with the most sophisticated weapons ever made.' |
| Manner | Peripheral | The manner in which the Conqueror takes over the Theme. 'He violently captured the castles of La Haye , Preuilly and Champigny' |
| Means | Peripheral | The action by which the conquering event is made possible through the efforts of the Conqueror. 'They captured the haunted castle by bombarding it with low-energy x-rays.' |
| Place | Peripheral | The location where the Conqueror takes over the Theme. 'On Planet Earth, humans prefer to conquer those lands whose acquistion offers some economic benefit or advantage.' |
| Purpose | Extra-Thematic | The reason why the Conqueror seized the Theme. 'Rome initially conquered lands in order to enrich itself.' |
| Time | Peripheral | The Time at which the Conqueror seizes the Theme. 'China 's 1997 takeover would push over 10 per cent of the population out of the colony'. |

**Frame relations** (super → sub)

- Precedes: Invading → Conquering
- Subframe: Invasion_scenario → Conquering

**Lexical units** (7): capture.v, conquer.v, fall.v, overcome.v, reduce.v, take.v, takeover.n

## Containers  (frame id 78)

This frame covers entities which are prototypically conceived of and created to fulfill the function of containing--i.e. Containers that contain objects or substances, the Contents. This can be expressed as a complement , and includes potential or intended contents. A Container may also have an Owner, a current Relative_location, Material from which it is constructed, a method of Construction, and a Type. Note the connection between words in this frame and those in the Filling, Emptying, and Fullness frames. 'a bag of popcorn' 'underwear drawer' 'Chuck's suitcase' 'the suitcase in Chuck's office' 'straw basket' 'woven basket' 'Erlenmeyer flask'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Container | Core | Container is an object which is conventionally used as a container. Target words in this frame are tagged with this frame element. 'John carried a bucket.' |
| Construction | Peripheral | Construction indicates the action (or causer) which creates the Container. 'fired urns.' |
| Contents | Peripheral | Contents is the object(s)/stuff contained in the Container. |
| Descriptor | Peripheral | The Descriptor describes some aspect of the Container. 'He put everything into a really really huge briefcase' |
| Material | Peripheral | Material identifies the material of which the Container is made. 'straw basket' |
| Owner | Peripheral | Owner identifies the owner of the Container. 'Chuck's suitcase' |
| Part | Peripheral | This FE identifies a Part of the Container. 'screw top bottle' |
| Relative_location | Peripheral | Relative_location is the location of the Container. 'The wallet in his pocket was full of photos of his family.' |
| Type | Peripheral | Type designates the type of Container. Often the Type labels part of a multi-word or compound word target. 'Erlenmeyer flask' 'TABLESPOON' |
| Use | Peripheral | Use identifies the purpose for which an artifact is constructed and the activity with which it is associated, or the Contents protypically contained in the Container. 'watering can' 'wine glass' |

**Frame relations** (super → sub)

- Using: Bounded_entity → Containers
- Using: Containing → Containers

**Lexical units** (119): amphora.n, ampule.n, ashtray.n, backpack.n, bag.n, barrel.n, basin.n, basket.n, beaker.n, bin.n, bottle.n, bowl.n, box.n, briefcase.n, bucket.n, can.n, canister.n, canteen.n, carafe.n, carryall.n, cart.n, carton.n, cartridge.n, case.n, cask.n, casket.n, casserole.n, cauldron.n, censer.n, chalice.n, chest of drawers.n, chest.n, coffer.n, coffin.n, container.n, cooler.n, crate.n, creamer.n, crock.n, crucible.n, cruet.n, cup.n, cuspidor.n, cylinder.n, decanter.n, dish.n, dispenser.n, drawer.n, drum.n, duffel bag.n, empty.n, envelope.n, etui.n, flagon.n, flask.n, folder.n, glass.n, goblet.n, goldfish bowl.a, grail.n, hamper.n, handbag.n, haversack.n, hopper.n, hot-water bottle.n, jar.n, jeroboam.n, jigger.n, jug.n, keg.n, knapsack.n, ladle.n, locker.n, magnum.n, mailer.n, mug.n, overnighter.n, pack.n, pail.n, pannier.n, pipette.n, planter.n, pot [cooking].n, pot.n, pouch.n, punch bowl.n, purse.n, ramekin.n, reservoir.n, reticule.n, rucksack.n, sack.n, safe.n, salver.n, samovar.n, sarcophagus.n, satchel.n, snifter.n, spittoon.n, spoon.n, stein.n, suitcase.n, tank.n, teaspoon.n, thermos.n, tin.n, toilet bowl.n, tub.n, tumbler.n, tun.n, tureen.n, urn.n, valise.n, vase.n, vat.n, vial.n, vivarium.n, wallet.n, wine bottle.n

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

## Control  (frame id 1799)

A Controlling_entity, Controlling_situation, or Controlling_variable control a Dependent_entity, Dependent_situation, or Dependent_variable. The latter, dependent, element or some aspect of it is not just influenced, but determined by the controlling element. 'Can you control the robot?' 'Although you may not be able to control every situation, you can control your reaction.' 'Students do not have control over the temperature of the heating water.' 'Everyone knows that the price of oil controls the price of asphalt.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Controlling_entity | Core | A thing or person whose behavior controls a Dependent_entity, Dependent_situation, or Dependent_variable. |
| Dependent_entity | Core | An entity, usually a thing, that is influenced in its behavior by a Controlling_entity or an Controlling_situation. |
| Controlling_situation | Core-Unexpressed | A situation whose temporal or other characteristics control a Dependent_entity, Dependent_situation, or Dependent_variable. |
| Controlling_variable | Core-Unexpressed | A scalar variable (with unspecified value) which has an effect on the Dependent_entity, Dependent_situation, or Dependent_variable. |
| Degree | Core-Unexpressed | The Degree to which the Controlling element affects the Dependent element. |
| Dependent_situation | Core-Unexpressed | A situation whose temporal or other characteristics are influenced by a Controlling_entity, Controlling_situation, or Controlling_variable. |
| Dependent_variable | Core-Unexpressed | A scalar variable, whose value depends on the behavior of a Controlling_entity, a Controlling_situation, or a Controlling_variable. 'Move the slider on the SpeedBar while playing audio or video material to control … |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including force (hard, softly), secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may also … |
| Place | Peripheral | The location at which the controlling occurs. |
| Time | Peripheral | The Time at which the controlling occurs. |

**Frame relations** (super → sub)

- Inheritance: Control → Being_in_control
- Inheritance: Objective_influence → Control
- ReFraming_Mapping: Control → Being_in_control

**Lexical units** (7): command.n, command.v, control.n, control.v, determine.v, regulate.v, regulation.n

## Controller_object  (frame id 2654)

This frame contains items which, when manipulated, alter the function of some device, internal or external. 'This button makes the radio turn on.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Control | Core | This FE identifies the entity or substance that is designed to have a particular Use. This is often an incorporated FE. |
| Controlled_entity | Peripheral | The entity which the Control controls. 'The radio knob was broken.' |
| Creator | Extra-Thematic | An individual or individuals that bring the Control into existence. |
| Material | Extra-Thematic | Any indication of what makes up the Control, including components, ingredients, etc. |
| Name | Extra-Thematic | The term used to refer to an Control. |
| Time_of_creation | Extra-Thematic | The time at which an Control comes into existence. |
| Type | Extra-Thematic | An indication of the subtype of Artifact. 'Flip the three-way switch.' |
| Use | Peripheral | The use for which an control is intended. 'knob for volume control.' |

**Frame relations** (super → sub)

- Inheritance: Artifact → Controller_object

**Lexical units** (6): board.n, button.n, control.n, knob.n, switch.n, switchboard.n

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

## Dead_or_alive  (frame id 310)

A Protagonist is in the dynamic, maintained state of being alive or has exited this state. 'Frank's dead body was apalling.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Figure | Core | This FE identifies the Figure or form being described by the target. 'Frank's dead body was apalling.' |
| Protagonist | Core | Protagonist identifies the being or entity that is dead or alive. 'Frank was dead.' |
| Degree | Peripheral | This FE identifies the Degree to which a Protagonist is dead or alive. |
| Explanation | Extra-Thematic | Explanation identifies any object or event that brings about the death of the Protagonist. 'Within hours, Frank was dead of exposure.' |
| Time | Peripheral | The time in which the Protagonist is dead or alive. |

**Frame relations** (super → sub)

- Inchoative_of: Death → Dead_or_alive
- Inheritance: Dead_or_alive → Subsisting
- Inheritance: State → Dead_or_alive
- Subframe: Cycle_of_life_and_death → Dead_or_alive
- Using: Biological_entity → Dead_or_alive
- Using: Dead_or_alive → Resurrection

**Lexical units** (14): alive.a, dead.a, dead.n, deceased.a, dirt nap.n, late.a, life.n, lifeless.a, live.v, living.a, living.n, nonliving.a, undead.a, undead.n

## Death  (frame id 53)

The words in this frame describe the death of a Protagonist. A Cause of death may also be expressed obliquely. '' 'The machine was not switched off, but Mr. Lavelle died of natural causes, police said.' 'To avenge the death of a son is not hasty work, if he is to be honored.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Protagonist | Core | The FE Protagonist is the being or entity that dies. With verbs in this frame, the Protagonist is the External Argument. 'The goldfish died.' |
| Containing_event | Extra-Thematic | This FE identifies the larger event in which the Protagonist dies, i.e. changes from living to dead. 'The pilot died in the crash' |
| Degree | Peripheral | Some measure of the event, generally frequency. 'You know, I wouldn't want to live in a Shakespearian play; people die in them a lot.' |
| Depictive | Extra-Thematic | The FE Depictive denotes the state of the Protagonist as the death occurred. 'I think he died happy.' |
| Explanation | Extra-Thematic | The FE Explanation expresses any object or eventuality that brings about the Protagonist's death. 'The cat died of old age.' 'The children perished from hunger.' |
| Maleficiary | Extra-Thematic | An individual negatively affected by the death of the Protagonist. 'Aww man, my dog died on me.' |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including force (hard, softly), secondary effects (quietly, loudly), and general descriptions comparing events (the same way). 'He died horribly; … |
| Place | Peripheral | The FE Place indicates where the death takes place. 'Your father passed away in his hospital bed.' |
| Result | Extra-Thematic | The FE Result indicates what occurs as the result of the death of the Protagonist. 'If we don't find something soon, we'll all starve to death.' |
| Time | Peripheral | The FE Time denotes when the dying or killing occurs. 'Your father passed away about four minutes ago.' 'He sadly passed away in 1962 because of severe cerebrovascular disease.' |

**Frame relations** (super → sub)

- Causative_of: Killing → Death
- Inchoative_of: Death → Dead_or_alive
- Inheritance: Ceasing_to_be → Death
- Precedes: Being_born → Death
- Precedes: Dying → Death
- Precedes: Giving_birth → Death
- ReFraming_Mapping: Death → Cause_harm
- ReFraming_Mapping: Death → Offenses
- ReFraming_Mapping: Killing → Death
- Subframe: Cycle_of_life_and_death → Death

**Lexical units** (20): asphyxiate.v, croak it.v, croak.v, death.n, decease.v, demise.n, die.v, drown.v, end.n, expire.v, kick the bucket.v, mortal.a, mortality.n, pass away.v, perish.v, starvation.n, starve.v, suffocate.v, suffocation.n, terminator.n

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

## Degree  (frame id 2001)

LUs in this frame modify a gradable attribute and describe intensities at the extreme positions on a scale. 'She is very brave.' 'It is that simple!' 'The feuds are so vicious because the stakes are so low.' 'The plant is totally red without the slightest hint of green.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Gradable_attribute | Core |  |

**Frame relations** (super → sub)

- See_also: Hedging → Degree
- Using: Importance → Degree

**Lexical units** (21): a little bit.adv, a little.adv, a lot.adv, as hell.adv, crystal (clear).n, dirt (poor).n, far.adv, fully.adv, great.a, heavily.adv, in part.adv, kind of.adv, particular.a, so.adv, somewhat.adv, sopping (wet).a, stone (cold).n, that.adv, totally.adv, very.adv, way.adv

## Deny_or_grant_permission  (frame id 520)

In this frame, an Authority allows a Protagonist to know (in some way) that they may or may not engage in an Action. For lexical units of this frame marked with the semantic type "Negative", e.g., authorize.v, the Authority has the power to tell the Protagonist not to do something, but does not do so. It is assumed that if the Protagonist engages in the Action without permission, then the Authority will punish the Protagonist in some way, at least with disapproval; if the Authority grants permission, however, the Authority is agreeing not to impose a punishment on the Protagonist for performing the Action. 'The police officer forbid me from turning around .' ' My mother okayed me to go to the movies with Simon . ' ' The teacher gave the children permission to eat their lunch outside. ' 'The Church had sanctioned for recital after Mass a special prayer to St. Michael.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Action | Core | The Action is what the Protagonist seeks to do, but is ordered not to. |
| Authority | Core | The Authority orders the Protagonist to not engage in a particular Action. |
| Protagonist | Core | The Protagonist wants to engage in an Action, but is ordered not to by the Authority. |
| Allowed_category | Extra-Thematic | A category that the Action fits into, which dictates the Action's being permitted (in accord with some implicit Principle.) 'The transfer was sanctioned as a "necessary precaution".' |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Degree | Extra-Thematic | This frame element selects some gradable attribute and modifies the expected value for it. |
| Depictive | Extra-Thematic | A description of the Authority or the Protagonist while they are involved in the action. 'He granted permission fully aware of her crime .' |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. There are two somewhat distinct subgroups of sentence modifiers that cover this function. First, it applies to appraisals of … |
| Explanation | Extra-Thematic | This FE denotes a proposition from which the main clause (headed by the target) logically follows. |
| Frequency | Extra-Thematic | How often the event occurs. |
| Manner | Extra-Thematic | A holistic description of the event (the same way), or a description of the Authority that also affects the overall event (carefully). |
| Means | Peripheral | The action performed by an Authority that brings about the Denying or Granting Permission. |
| Period_of_iterations | Extra-Thematic | The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | The Place is where the denial of permission occurs. |
| Purpose | Extra-Thematic | The Purpose is what the Authority hopes to accomplish by denying permission. |
| Time | Peripheral | The Time is when the denying of permission occurs. |

**Frame relations** (super → sub)

- Metaphor: Preventing_or_letting → Deny_or_grant_permission
- ReFraming_Mapping: Deny_or_grant_permission → Preventing_or_letting
- Using: Communication → Deny_or_grant_permission

**Lexical units** (22): approval.n, approve.v, authorize.v, clear.v, disallow.v, forbid.v, greenlight.v, leave.n, mandate.n, okay.v, outlaw.v, permission.n, permit.v, prohibit.v, prohibition.n, restrict.v, sanction [allow].v, suffer.v, the go ahead.n, the go-ahead.n, the green light.n, the okay.n

## Desirability  (frame id 354)

This frame concerns an Evaluee being judged for its quality, i.e. how much it would probably be liked. In many cases, the Evaluee is implicitly judged good or bad relative to other instances of its type. The Evaluee's desirability is determined by one or more Parameters, which are scalar properties of the Evaluee. The evaluation may also explicitly be relativized to a set of Circumstances, a Comparison_set of entities that belong to the same class as the Evaluee, or an Affected_party. The Degree of goodness or badness may also be expressed. Note: With some targets, desirability is conventionally aligned with quantity, i.e., GOOD is MORE. 'The view was astonishing.' 'On clear days, the view was excellent.' 'The book is astounding in its scope.' 'The games have been awful for the team.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Evaluee | Core | The Evaluee is being judged for its quality. ' He gave me another lame excuse.' |
| Affected_party | Extra-Thematic | The Affected_party indicates entities that benefit or suffer from the good or bad quality of the Evaluee. 'The season was splendid for the team.' |
| Circumstances | Extra-Thematic | Circumstances marks expressions that indicate a set of conditions under which the quality of the Evaluee is being judged. 'It's a great game when it rains.' |
| Comparison_set | Extra-Thematic | This FE marks expressions that indicate what class of things or events the Evaluee is being judged against. 'The standard of living is poor compared to other Western industrialized countries.' |
| Degree | Peripheral | This FE identifies the Degree to which the Evaluee is judged good or bad. ' Smithers was doing an absolutely splendid job.' |
| Depictive | Extra-Thematic | The Frame Element Depictive encodes a state that the Evaluee is in and which does not represent a temporary or hypothetical set of Circumstances. 'The aerial view is superb with its view of the harbour.' |
| Parameter | Core-Unexpressed | This FE marks expressions that denote a scalar property of the Evaluee with respect to which the Evaluee is judged. 'The Beaujolais Nouveau is dazzling in freshness.' |

**Frame relations** (super → sub)

- Inheritance: Desirability → Aesthetics
- Inheritance: Desirability → Desirable_event
- Inheritance: Desirability → Popularity
- Inheritance: Desirability → Social_desirability
- Inheritance: Gradable_attributes → Desirability
- ReFraming_Mapping: Desirability → Expertise
- ReFraming_Mapping: Desirability → Usefulness
- ReFraming_Mapping: Expertise → Desirability
- Using: Desirability → Grooming
- Using: Desirability → Preferred_alternative_scenario
- Using: Desirability → Thriving
- Using: Experiencer_focus → Desirability

**Lexical units** (77): amazing.a, appalling.a, astonishing.a, astounding.a, atrocious.a, average.a, awesome.a, awful.a, bad.a, best thing since sliced bread.n, cool.a, crap.n, crappy.a, decent.a, desirable.a, dreadful.a, excellence.n, excellent.a, execrable.a, extraordinary.a, fabulous.a, fair.a, fantastic.a, fine.a, first-rate.a, garbage.n, gem.n, gold.n, good.a, great.a, horrible.a, idyllic.a, incredible.a, inferior.a, junk.n, killer.a, lame.a, lamer.n, magnificent.a, marvellous.a, mediocre.a, miserable.a, nasty.a, okay.a, outstanding.a, pathetic.a, pitiful.a, poor.a, popular.a, rock.v, rotten.a, second-rate.a, sensational.a, shit.n, shitty.a, so-so.a, splendid.a, standout.n, stupendous.a, substandard.a, suck.v, super.a, superb.a, superlative.a, sweet.a, terrible.a, terrific.a, third-rate.a, tip-top.a, tolerable.a, top-notch.a, tremendous.a, uncool.a, unfortunate.a, well.adv, wonderful.a, worthless.a

## Difficulty  (frame id 375)

An Experiencer has an easy or difficult time carrying out an Activity. The ease or difficulty associated with the Activity seems to often be associated with a prominent participant. However, we consider this impression to be due to the syntax and pragmatics of the relevant sentence constructions and employ no special FE for such participants. The Degree of ease or difficulty is often specified as well as a set of Circumstances. A Parameter may be mentioned that indicates in which respect the Activity is judged to be easy or difficult. '' Unmarked LUs of this frame indicate that something is easy, while LUs of this frame that mean the opposite of easy are marked with the semantic type "Negative", as in difficult.a, arduous.a, and a bitch.n. '(1) John is easy to please.' '(2) It is easy to get Alex annoyed.' '(3) Smithers is very tough for me to please.' '(4) VWs are easy to repair.' '(5) The dating of western sculpture is difficult.' '(6) In that kind of wind the course is physically very tricky.' '(7) The last question on the exam was hard. ' '(8) The last one was a hard question to answer. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | This Frame Element marks expressions indicating the Activity that the Experiencer finds difficult or easy. In many cases, the relevant Activity has to be inferred from the context. 'The climb was difficult.' 'That … |
| Experiencer | Core | This Frame Element marks expressions that indicate which person judges carrying out the Activity to be easy or difficult. 'The geology question on the exam was hard for me.' |
| Circumstances | Extra-Thematic | This Frame Element marks expressions that indicate a set of conditions in which the Activity is being experienced and which influence the Experiencer's perception of how easy or difficult the Activity is. 'In this … |
| Degree | Peripheral | This Frame Element marks expressions that indicate the Degree of difficulty that the Experiencer has in carrying out the Activity. ' Charlie is very tough for Lulu to please.' |
| Parameter | Peripheral | This FE marks expressions that indicate a respect in which the Activity is judged easy or difficult to carry out by the Experiencer. 'The problem involves a mathematically difficult Fourier transformation.' |
| Standard | Peripheral | The experience of the Activity by the Experiencer may be compared to a Standard situation, which may be evoked either as an event or state, or by reference to a salient participant. 'Man, running on hilly bike paths of … |
| Time | Peripheral | The time at which the Activity takes place. |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Difficulty
- Using: Hindering → Difficulty

**Lexical units** (26): a bastard.n, a bitch.n, a breeze.n, a cinch.n, a doddle.n, a pain in the neck.n, a pain.n, a piece of cake.n, a snap.n, a walk in the park.n, arduous.a, challenge.n, challenging.a, child's play.n, difficult.a, difficulty.n, ease.n, easy.a, hard.a, impossible.a, like taking candy from a baby.adv, near thing.a, no picnic.n, tough.a, tricky.a, trivial.a

## Distributed_position  (frame id 76)

This frame involves a static (primarily spatial) relationship between a Location and a Theme, in which the Theme is located in many or all subregions of the Location, and is thus construable as covering it. The Time when the covering configuration holds, and the Subregion of the Location that is involved may, optionally, be indicated. 'By Summer, weeds dotted the field .' 'The papers around my office were too messy .' Prepositional and verb targets of this frame differ in the ways they can participate in forming sentences; one of the most important differences is that prepositions may modify the entire sentence to describe the event (the Theme) as distributed over the Location. 'Puddles were rippling all over the roof .' Some members of this frame specifically indicate that the configuration is attractive or unattractive; this is indicated by the semantic types Positive_judgement and Negative_judgement respectively. Some of the non-verb LUs of the frame (esp. around.prep) refer to multiple possible positions that might be occupied by a single Theme, often accompanied by "somewhere": 'I hope my wallet is around here (somewhere) .' These same LUs may refer a vague sequence of locations occupied by a single Theme: 'I kept walking around my apartment .' All or virtually all of the verbs used statically in this frame can also occur in the frame Filling, producing pairs such as the following: 'Filling: Pat covered the table with flowers.' 'Distributed_position: Flowers covered the table.' '' Please note: adorned, covered, etc are in the Abounding_with frame because of the point of view shift. '' 'The tree was studded all over with soft dark fruit.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Location | Core | Location is the entity or area with respect to which the Theme's spatial arrangement is described. This frame element generally occurs as an NP Object.'Thick varnish coated the beautiful wood.' |
| Theme | Core | The Theme in this frame is the object which is described as standing in some spatial relation to a particular Location. Theme typically occurs as the External Argument or, with passives, as a PP Complement headed by … |
| Deixis | Extra-Thematic | An indication of how the locative phrase relates to the grounding of the speech situation, either locating it near (here) or far (there, yonder). Fillers of this FE are restricted to this closed class of items. 'The … |
| Region_quantification | Extra-Thematic | A description of how much of a potential profiled region actually has (or is expected to have) a Theme in it. It is normally filled by closed-class items like 'all', 'somewhere', 'nowhere', etc. 'All around the town, … |
| Subregion | Extra-Thematic | The part of the Location which contains or is covered by the Theme. 'Bulletholes covered the windshield on the right side.' |
| Temporal_profile | Extra-Thematic | A description of how the access path to the Location interacts with time. This FE is filled only by the closed class adverbial back.adv (which indicates that the position was occupied by the Theme before). While this … |
| Time | Peripheral | The time at which the Theme occupies the Location. 'By 1950, factories dotted the adjacent countryside.' |

**Frame relations** (super → sub)

- Inheritance: Locative_relation → Distributed_position
- Perspective_on: Distributed_abundance → Distributed_position
- See_also: Distributed_position → Abounding_with
- See_also: Distributed_position → Filling
- See_also: Surrounding → Distributed_position

**Lexical units** (23): across.prep, adorn.v, all over.prep, around.prep, blanket.v, cloak.v, coat.v, cover.v, deck.v, decorate.v, dot.v, encrust.v, envelop.v, festoon.v, fill.v, film.v, garnish.v, line.v, litter.v, over.prep, pave.v, stud.v, wreathe.v

## Documents  (frame id 560)

Words in the frame refer to any Document that has a legal status or conventional social significance. Some Documents empower the Bearer of the Document to execute the Right. Others indicate the Obligation of the Bearer. Still others show the identity or Status of the Bearer. 'They got their marriage licence from Canada.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Bearer | Core | The holder of the document. 'My visa will expire next month.' |
| Document | Core | Document is the piece of paper that has the legal status. 'The police need a search warrant to enter his house.' |
| Issuer | Core | The authority that issues the document. 'US consulate issued a Visa to Ms. Yang to travel to San Francisco.' |
| Obligation | Core | Obligation is the obligation that is imposed on the Bearer of the Document. 'They were all under subpoena to appear in court.' |
| Right | Core | Right is the right of the Bearer of the Document that is authorized by the Document. 'Raymond has a fishing licence.' |
| Status | Core | Status is the state of the Bearer of the Document indicated by the Document. 'The couple just got their marriage certificate.' |
| Descriptor | Extra-Thematic | Descriptor covers any characterization or description of the target that is not covered by another more specific FE. |
| Medium | Peripheral | The language the Document is written in, or a specification of the kind of object that instantiates it. 'We only need an electronic confirmation.' |
| Specification | Extra-Thematic | A Specification is a condition that applies to the Rights and/or Obligations described in the Document. 'Before you get your driver's liscense, you need to carry your temporary driving permit when you drive. ' |

**Frame relations** (super → sub)

- Inheritance: Text → Documents
- Using: Documents → Terms_of_agreement
- Using: Obligation_scenario → Documents

**Lexical units** (35): accord.n, affidavit.n, agreement.n, authorization.n, brief.n, business card.n, certificate.n, charter.n, confirmation.n, contract.n, contractual.a, deed.n, deposition.n, diploma.n, document.n, finding.n, identification.n, lease.n, license.n, opinion.n, orders.n, papers.n, passport.n, permit.n, ruling.n, subpoena.n, summons.n, testament.n, testimony.n, title.n, treaty.n, visa.n, warrant.n, will.n, writ.n

## Dominate_competitor  (frame id 1796)

An Agent, by virtue of strength or forcefulness, controls, rules, or strongly influences some Patient in some Situation. 'The fireballing righthander looked poised to dominate the Yankees yet again, striking out seven straight batters during one stretch'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent controls the Patient by being forceful and possibly aggressive. |
| Patient | Core | The Patient is trying to gain control of a situation, but ends up being subject to the control and influence of the Agent. |
| Degree | Peripheral | The Degree to which the Agent dominates the Patient. |
| Duration | Peripheral | The period of time over which the domination occurs. 'For England and France, domination over their colonies during the colonial period was mainly a cultural obligation.' |
| Manner | Peripheral | A description of the event as a whole, or of any of the participants that does not fit any of the other more specific Frame Elements. 'He managed to be dominant over most of the rest of the staff, in a good way.' |
| Place | Peripheral | The place where the domination occurs. 'Women tend to dominatemen at home and at Church.' |
| Situation | Peripheral | The Situation within which the Agent is able to gain control over the Patient (thus excluding them from controlling the Situation). |
| Time | Peripheral | The time when the domination takes place. 'Their role models might have dominated women in the past; they may not have understood the concept of equality.' |

**Frame relations** (super → sub)

- Inheritance: Being_in_control → Dominate_competitor
- Perspective_on: Domination → Dominate_competitor

**Lexical units** (4): dominant.a, dominate.v, domination.n, strongman.n

## Dominate_situation  (frame id 1795)

An Agent acts so as to be the strongest force, or most important causal factor in some Situation, to the exclusion of other competing actors. 'York dominated the game as they held the ball on offense almost the entire 70 minutes.' 'Is there a future for Unix in a market increasingly dominated by Microsoft?' 'Walz dominated the debate so completely it was almost embarrassing.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the most forceful and pivotal factor in the situation. |
| Situation | Core | The Situation is primarily affected by the Agent, in particular how it develops or concludes. |
| Degree | Peripheral | The Degree to which the Agent dominates the Situation. |
| Duration | Peripheral | The period of time over which the domination occurs. 'Dinosaurs were vertebrate animals that dominated the terrestrial ecosystem for over 160 million years.' |
| Manner | Peripheral | A description of the event as a whole, or of any of the participants that does not fit any of the other more specific Frame Elements. 'Most predict that the top teams from last year to ruthlessly dominate the league.' |
| Place | Peripheral | The location where the domination takes place. 'Indeed, in all Latin America, United States corporations dominated the key sectors of the economy.' |
| Time | Peripheral | The Time when the Agent is dominant. 'As discussed above, Ford dominated the market in the 1920s, then left the business to create production capacity for the Model A.' |

**Frame relations** (super → sub)

- Perspective_on: Domination → Dominate_situation
- Using: First_rank → Dominate_situation

**Lexical units** (5): dominant.a, dominate.v, domination.n, predominate.v, rule.v

## Duplication  (frame id 11)

This frame involves a Creator making a duplicate, the Copy, of some Original entity. A Source, the location of the Original, and Goal, the location of the Copy, may be expressed. 'The teacher copied the problem onto the blackboard.' ' His handouts were poorly photocopied by his assistantfrom my originals .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Copy | Core | The Copy produced by the Creator is frequently not expressed. However, when Copy does occur, it is usually expressed as the External Argument of verbs: 'The results replicate those of an earlier study.' |
| Creator | Core | The Creator produces the Copy based on the Original. It is normally expressed as an External Argument. 'Pat photocopied the article.' |
| Original | Core | The Original is the entity which is copied. With verbs it is frequently expressed as an NP Object:'Pat photocopied the article.' |
| Characterization | Extra-Thematic | This FE designates the character of the medium in which a Copy is made. Usually, it is expressed as PP-in or AP. 'They sold a million copies in hardback.' 'Opposite is Pilinsky's wood-engraved copy.' 'The margins are … |
| Co-participant | Extra-Thematic | An entity that participates in much the same way as another participant (Creator, Copy, or Original), although it is characterized as being less focal to the action. 'Copy my list along with yours .' |
| Degree | Peripheral | Degree to which event occurs. |
| Depictive | Extra-Thematic | This FE identifies any Depictive phrase that describes a primary participant, either the Creator or the Copy/ Original. 'Such leaflets have to be duplicated en masse.' 'She did the copying unaware of the fact that John … |
| Duration | Extra-Thematic | The amount of time for which a state holds or a process is ongoing. |
| Explanation | Extra-Thematic | The Explanation for which an intentional act is performed. |
| Fidelity | Peripheral | The way in which the Copy matches or does not match the Original. 'I made a half-size copy.' |
| Frequency | Extra-Thematic | The Frequency is the frequency with which the Original is copied. 'The scribes copied the scripture every 80 years.' |
| Goal | Extra-Thematic | The Goal is the location to which material is copied. Unlike the FE Goal in other frames, there is no actual movement of any entity to this location. Goal is usually expressed as a PP Complement: 'Copy the file onto … |
| Instrument | Peripheral | The Instrument with which an intentional act is performed. |
| Iterations | Extra-Thematic | The Iterations is the number of times the Original is copied. 'Jim copied the book 300 times.' |
| Manner | Peripheral | Manner of performing an action |
| Means | Peripheral | An intentional action performed by the Creator that lets them bring about the duplication. |
| Place | Peripheral | Where the event takes Place. |
| Purpose | Peripheral | The Purpose for which an intentional act is performed. |
| Result | Extra-Thematic | Result of an event |
| Source | Peripheral | The Source is the location from which material is copied, i.e. the location of the Original. Unlike the FE Source in other domains and frames, there is no actual movement of either Copy or Original from this location. … |
| Time | Peripheral | When the event occurs. |

**Frame relations** (super → sub)

- Inheritance: Duplication → Forging
- Inheritance: Intentionally_create → Duplication

**Lexical units** (14): clone.n, clone.v, copy.n, copy.v, duplicate.n, duplicate.v, duplication.n, photocopy.n, photocopy.v, reduplicate.v, replica.n, replicate.v, reproduce.v, run off.v

## Duration_description  (frame id 79)

An event or state (here termed an Eventuality) or time-Period is described in terms of the Degree to which its duration diverges from a standard. As is usual for gradable attributes, the standard of comparison is normally based on the expected duration for the type of Eventuality or Period. (In conjunction with the comparative construction, the standard may also be based upon an explicit value.) '' 'After a lengthy discussion with the Foreign Minister, Mr. Qian Qichen, they met the Prime Minister.' '' 'The lengthy period which most party leaders have already spent in Parliament before gaining office certainly gives them time to acquire suitable skills.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Eventuality | Core | A situation, action or event whose duration is being described. The Eventuality occurs as the External Argument if the adjective is used predicatively, or as the modified noun if the adjective is used attributively: … |
| Period | Core | Sometimes these adjectives describe simply a period of time, rather than an event or state. The Period almost invariably occurs as the modified noun with an attributive adjective: We waited for only a short time. Use … |
| Degree | Peripheral | Degree to which event occurs |

**Frame relations** (super → sub)

- Inheritance: Measurable_attributes → Duration_description
- Perspective_on: Duration_scenario → Duration_description
- Using: Duration_description → Taking_time

**Lexical units** (17): abiding.a, brief.a, chronic.a, enduring.a, ephemeral.a, eternal.a, extended.a, interim.a, lasting.a, lengthy.a, long.a, momentary.a, perpetual.a, persistent.a, rapid.a, short.a, sustained.a

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

## Emitting  (frame id 359)

In this frame a Source_emitter discharges its Emission along a Path or to a Goal. ' (1) The factory exudes toxic fumes from three large chimneys.' The Sub-source is only present when the actual Source_emitter is also given or is present in a possessive. ' (2) Light is emitted from the tower . ' ' (3) Noxious odors are emitted from his feet . ' In (3) we would tag 'his' as Source_emitter on a second layer because the inalienable possession on the Sub-source indicates the Source_emitter

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Emission | Core | The Emissions are discharged out of the Source_emitter . |
| Source_emitter | Core | The Source_emitter is the item from which the Emission are discharged. |
| Area | Peripheral | The Area is used for expressions which describe a general area in which emission takes place when the motion is understood to be irregular or not to consist of a single, linear path. |
| Carrier | Peripheral | This is the means of conveyance of the Emission. ' The acorn seeds are excreted in the feces of squirrels . ' |
| Degree | Peripheral | Degree to which emission occurs |
| Depictive | Extra-Thematic | Depictive phrase describing the the state of the Emission or Source_emitter. |
| Distance | Peripheral | This FE is an expression characterizing the extent of motion of the Emission |
| Duration | Peripheral | The amount of time for which the Source_emitter emits the Emission. |
| Explanation | Extra-Thematic | The Explanation for which the Source_emitter emits the Emission |
| Form | Extra-Thematic | The Form is the state in which the Emission is emitted. ' The signal is emitted as radio waves . ' |
| Goal | Peripheral | This FE is the point at which the Emission ends up as a result of the motion. |
| Manner | Peripheral | This FE identifies the Manner in which the Source_emitter emits the Emission |
| Means | Peripheral | The Means by which the Source_emitter emits. |
| Path | Peripheral | This FE is a description of a trajectory of motion which is neither a Source_emitter or Sub_source nor Goal. |
| Speed | Peripheral | The rate at which emission occurs. |
| Sub-source | Extra-Thematic | The Sub-source is the subregion of the Source_emitter which emits the Emission. |
| Time | Peripheral | This FE identifies the Time when the Source_emitter emits the Emission. |

**Frame relations** (super → sub)

- Causative_of: Emitting → Emanating

**Lexical units** (10): discharge.v, emanate.v, emit.v, excrete.v, exhale.v, exude.v, give off.v, radiate.v, secrete.v, void.v

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

## Endangering  (frame id 631)

An Agent or Cause is responsible for placing a Valued_entity at risk. Endangering_act, Place, Time, Reason, and Circumstance may also be specified. 'His actions have imperiled his immortal soul!' 'I admit that I endangered you all by attracting the killer's notice.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The sentient entity which causes the risk to the Valued_entity. |
| Cause | Core | An (non-sentient) entity or state of affairs that leads to the peril to the Valued_entity. |
| Valued_entity | Core | The entity which may be negatively impacted as a result of the emperilment. |
| Endangering_act | Peripheral | The specific event or state of affairs brought about by the Agent or Cause which endangers the Valued_entity. 'The snow endangered not only the mission but also our lives by slowing us down.' 'His actions imperiled his … |
| Manner | Peripheral | The Manner describes an aspect of the endangering act that is not directly related to the cause, intermediate action, or entity involved. 'Members of the underground club would frequently endanger the lives of others … |
| Place | Peripheral | The location where the Valued_entity is put in danger. |
| Time | Peripheral | The time when the Valued_entity is put in danger. |

**Frame relations** (super → sub)

- Causative_of: Endangering → Being_at_risk
- Inheritance: Transitive_action → Endangering

**Lexical units** (4): endanger.v, endangerment.n, imperil.v, jeopardise.v

## Endeavor_failure  (frame id 2622)

Some individual or group ceases to be able to sustain an Endeavor (a long-term activity involving economic interaction with the public, often a business venture). Unlike Business_failure and Locale_closure, the Endeavor need not refer to an organization or business tied to a specific location or locations. 'Exxon went under.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Endeavor | Core | The Endeavor is rendered unable to continue its regular operations. 'His small business failed.' |
| Circumstances | Extra-Thematic | The Circumstances that caused failure. Compared to Explanation, this describes situations or environments that lead to failure, not a specific reason for failure. 'Shops often close down amid political or economic … |
| Containing_event | Extra-Thematic | The Containing_event is an event within which the failure occurs. 'Businesses in the Congo failed during the civil war.' |
| Degree | Peripheral | The degree to which the Endeavor fails. |
| Depictive | Extra-Thematic | A Depictive describes something about the Endeavor. 'The business, unable to maintain appeal in the E.U., closed its doors in 2003.' |
| Explanation | Extra-Thematic | The Explanation is named as one of the causes of failure. 'The local McDonalds shut down in 2008 because the owner died.' |
| Manner | Peripheral | The Manner describes the way in which the Endeavor failed. 'Because of its lack of funding, the website quickly flopped.' |
| Means | Peripheral | The means by which the Endeavor fails. |
| Place | Peripheral | The Place of the failing Endeavor. 'The hot dog stand on 4th avenue flopped.' |
| Time | Peripheral | The Time of the failure. 'Her campaign failed in 2008 but found much more support in 2012.' |

**Frame relations** (super → sub)

- Inheritance: Endeavor_failure → Business_closure
- Inheritance: Success_or_failure → Endeavor_failure
- See_also: Endeavor_failure → Business_closure
- See_also: Endeavor_failure → Locale_closure

**Lexical units** (6): collapse.v, fail.v, flop.v, fold.v, go bust.v, go under.v

## Enforcing  (frame id 1813)

An Agent acts to ensure that a Rule (often a constraint on behavior) is being followed. The Agent's action is according to a general plan for Rules (such that implicit in the Rule is the affordance to certain entities to ensure that the Rule is followed). The Rule may be specified for the Duration for which it is in effect. 'Why don't we enforce the 20000 gun laws currently on the books across the nation?' 'Computer systems can ruthlessly enforce rules and standards indefinitely.' 'Can a landlord enforce rules upon tenants?'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent, often an institution, governmental organization, or arm thereof, puts into effect (i.e., enforces) a Rule. 'Can a landlord enforce rules upon tenants?' |
| Medium | Core | This FE describes the medium through which the rule was enforced. It may occur in the same syntactic position as the Agent. 'The rules will be enforced by a new computer system that tracks people's movements.' |
| Rule | Core | The Rule is the set of constrants on behavior that the Agent implements (i.e., forces others to obey or face consequences). 'Employers should strictly enforce a prohibition against use of any substance that may affect … |
| Circumstances | Extra-Thematic | The state-of-affairs under which the Agent puts the Rule into effect. |
| Degree | Extra-Thematic | This FE describes how fully the Rule was enforced. |
| Duration | Peripheral | The length of time for which the Rule is or is not in effect. 'The coat-and-tie dress code for the Plimsoll Club in the World Trade Center was strictly enforced for years.' |
| Explanation | Extra-Thematic | A cause, reason, or other explanation for the enforcing of the Rule. |
| Focal_participant | Extra-Thematic | The individual or group who is obligated to follow the Rule. 'Can a landlord enforce rules upon tenants?' |
| Manner | Peripheral | The Manner describes some state of the Agent, or provides additional characterization of the event. 'The coat-and-tie dress code for the Plimsoll Club in the World Trade Center was strictly enforced for years.' |
| Means | Peripheral | The Means is an intermediate action done by the Agent in order to enforce the Rule. 'Since 1961 the church has enforced it by "disfellowshipping" or expelling un-repentant members who wilfully accept prohibited blood … |
| Outcome | Extra-Thematic | The Outcome is the failure or success of enforcing the rule. |
| Place | Peripheral | The Place at which the Rule is or is not enforced. 'For this reason they enforced the settlement system in America just as strictly as in Germany.' |
| Purpose | Peripheral | This FE identifies the Purpose for which the Agent enforces the Rule. |
| Time | Peripheral | The Time at which the Agent enforces the Rule. 'That particular regulation was only enforced in 1920.' |

**Frame relations** (super → sub)

- Inheritance: Execute_plan → Enforcing
- Using: Being_in_effect → Enforcing

**Lexical units** (2): enforce.v, enforcement.n

## Escaping  (frame id 273)

A Self-moving Escapee departs from an Undesirable_location. 'Benjamin escaped from Germany.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Escapee | Core | The Escapee manages to leave the Undesirable_location. 'Benjamin escaped from Germany.' |
| Undesirable_location | Core | The Undesirable_location is where the Escapee begins. 'Benjamin escaped from Germany.' |
| Degree | Peripheral | This FE identifies the (abstract) nearness of the Escapee to being caught in the Undesirable_location. 'Benjamin's narrow escape from Germany left him fearful.' |
| Depictive | Extra-Thematic | Depictive identifies a word or phrase describing a participant of an action. 'Benjamin escaped unscathed.' |
| Distance | Peripheral | The distance along a path away from the Undesirable_location that the Escapee travels. 'She escaped a few feet away, then looked back at him coldly.' |
| Explanation | Extra-Thematic | The situation that explains why the (instance of) the event occurred. 'We flew the coop 'cuz we knew pappy was coming home .' |
| Goal | Peripheral | Goal identifies any expression which tells where the Escapee ends up, or would end up, as a result of the motion. 'Benjamin escaped to the United States.' |
| Manner | Peripheral | Manner is used for any expression which describes a property of motion which is not directly related to the trajectory of motion, including descriptions of steadiness, grace, means of motion, etc. 'Benjamin escaped … |
| Means | Peripheral | covers any act performed by the Escapee brings about the escape. 'Benjamin escaped from Germany by bribing the border guards.' |
| Path | Peripheral | Path describes the trajectory of motion of the Escapee. 'Benjmain escaped from Germany along the southern border.' |
| Place | Peripheral | This FE identifies the Place where the Escaping occurs. |
| Purpose | Peripheral | This FE identifies the Purpose for which the escaping takes place. 'Benjamin escaped from Germany to rsave his life.' |
| Speed | Peripheral | Speed idenitifies the rate at which the escaping occurs. 'Benjmain speedily escaped from Germany.' |
| Time | Peripheral | This FE identifies the Time when the escaping occurs. |
| Vehicle | Peripheral | Vehicle identifies the means of conveyance by which the Escapee leaves the Undesirable_location. 'Benjamin escaped in a lorrie.' |

**Frame relations** (super → sub)

- Inheritance: Departing → Escaping
- ReFraming_Mapping: Avoiding → Escaping
- ReFraming_Mapping: Cotheme → Escaping
- ReFraming_Mapping: Escaping → Fleeing
- ReFraming_Mapping: Removing → Escaping
- ReFraming_Mapping: Self_motion → Escaping

**Lexical units** (9): bust out.v, escape.v, evacuate.v, evacuation.n, fly the coop.v, get free.v, get loose.v, get out.v, scarper.v

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

## Event  (frame id 187)

An Event takes place at a Place and Time. 'Big earthquakes only happen along plate boundaries. INI ' 'The party will take place on Sunday in the all-you-can-eat buffet.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Place | Core | Where the event takes place. |
| Time | Core | When the event occurs. |
| Duration | Extra-Thematic | How long the Event takes place. |
| Event | Core-Unexpressed | Name of the event which occurs. |
| Explanation | Extra-Thematic | The Explanation for which an event occurs. |
| Frequency | Extra-Thematic | How often the Event occurs. 'Stuff like this happens every day at 3:00pm.' |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), force (hard, softly), secondary effects (quietly, loudly), and general … |
| Timespan | Extra-Thematic | The period within which an Event has occurred. 'It was the largest food fight to occur since the time Jimmy's mom packed him extra Sloppy Joes.' 'From 1992 to 2014, my amazing birthday celebration has happened 22 times.' |

**Frame relations** (super → sub)

- Inheritance: Event → Birth_scenario
- Inheritance: Event → Change_of_consistency
- Inheritance: Event → Change_position_on_a_scale
- Inheritance: Event → Coincidence
- Inheritance: Event → Come_together
- Inheritance: Event → Coming_to_be
- Inheritance: Event → Coming_to_believe
- Inheritance: Event → Emergency
- Inheritance: Event → Eventive_affecting
- Inheritance: Event → Experience_bodily_harm
- Inheritance: Event → Getting
- Inheritance: Event → Go_into_shape
- Inheritance: Event → Intentionally_act
- Inheritance: Event → Losing_someone
- Inheritance: Event → Misdeed
- Inheritance: Event → Motion
- Inheritance: Event → Objective_influence
- Inheritance: Event → Process_end
- Inheritance: Event → Process_pause
- Inheritance: Event → Process_resume
- Inheritance: Event → Process_start
- Inheritance: Event → Process_stop
- Inheritance: Event → Rotting
- Inheritance: Event → Transition_to_state
- Inheritance: Event → Traversing
- Inheritance: Event → Undergoing
- Inheritance: Event → Waking_up
- Precedes: Event → Event_endstate
- Precedes: Event_initial_state → Event
- Subframe: Dynamic_situation_scenario → Event
- Using: Event → Frequency
- Using: Event → Hindering
- Using: Event → Locale_by_event
- Using: Event → Manner
- Using: Event → Participation
- Using: Event → Preventing_or_letting
- Using: Event → Temporal_pattern

**Lexical units** (9): development.n, episode.n, event.n, go on.v, happen.v, incident.n, occur.v, take place.v, transpire.v

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

## Existence  (frame id 660)

An Entity is declared to exist, generally irrespective of its position or even the possibility of its position being specified. Time, Duration, Inherent_purpose, and State may also be mentioned. This frame is to be contrasted with Presence, which describes the existence of an Entity in a particular (and salient) spacio-temporal context, and which also entails the presence of an observer who can detect the existence of the Entity in that context. 'Finally, Poland ceased to exist as a state for hundreds of years.' 'Such laws exist to prevent exactly this kind of fraud.' 'There IS a Santa Claus!'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | Some entity, abstract or concrete, which is stated to exist. |
| Circumstances | Extra-Thematic | Circumstances marks expressions that indicate a set of conditions under which the Entity is declared to exist |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Depictive | Extra-Thematic | This FE describes a participant of the state of affairs introduced by the target as being in some state during the action. |
| Duration | Extra-Thematic | The period during which the Entity exists. |
| Explanation | Extra-Thematic | A situation, force, or entity which brings about the existence of the Entity. |
| Inherent_purpose | Extra-Thematic | The reason why the Entity exists. Generally, this is more specifically the reason why the Entity was made. |
| Place | Peripheral | Where the Entity exists. |
| State | Extra-Thematic | The condition that the Entity exists in. 'Natural electricity exists in many forms: in storms, solar wind, and nerve impulses.' |
| Time | Peripheral | A time at which the entity is in existence. |
| Viewpoint | Extra-Thematic | The perspective of an individual who judges whether they consider the Entity (or further state of affairs) to exist or not. 'For him, there 's just too much drink in the world.' |

**Frame relations** (super → sub)

- Inchoative_of: Coming_to_be → Existence
- Inheritance: Existence → Circumscribed_existence
- Inheritance: State → Existence
- Precedes: Coming_to_be → Existence
- Precedes: Existence → Ceasing_to_be
- See_also: Existence → Presence
- Subframe: Cycle_of_existence_scenario → Existence
- Using: Existence → Have_associated
- Using: Existence → Locative_relation

**Lexical units** (5): exist.v, existence.n, real.a, remain.v, there be.v

## Expansion  (frame id 725)

An Item changes its physical size. The Size_change of an Item may be explicitly indicated or characterized in terms of Initial_size and/or Result_size. In the default case, expansion is along all dimensions, but sometimes the Dimension of expansion is incorporated or made explicit. '' This frame does not specify whether the Item gains mass or substance along with the change in size, and thus includes words that specify an increase in substance (grow.v) along with those that deny an increase in substance (stretch.v) and those that are unspecified (expand.v). 'The pile of leaves had shrunk by about half after the first haul.' 'The jeans stretched a little.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Item | Core | This FE identifies the Item whose size changes. 'Joan's new sweater shrank to a size that might fit a doll.' |
| Co-variable | Peripheral | Co_variable is the quantity that varies commensurately with the size of the Item, usually construed to be causally linked to the size. 'The snake's belly expanded with each mouse it ate.' |
| Degree | Peripheral | This FE identifies the Degree to which the expansion occurs. 'Joan's new sweater had shrunk completely.' |
| Dimension | Peripheral | Change of size may be limited to or described in terms of a single Dimension. 'The wall grew in height.' 'The piglet had grown 6 inches in length.' |
| Duration | Peripheral | This FE identifies the Duration of time that the expansion takes. 'The piglet had grown 6 inches over two months.' |
| Goal | Peripheral | Where the Iteam ends up due to Expansion. |
| Group | Peripheral | This FE identifies the Group in which an Item changes size. 'Tails lengthened 10% among rats more than 3 days old.' |
| Initial_size | Peripheral | Initial_size is used for the size of the Item before any change occurs. It is rarely expressed without Result_size also being explicit. Initial_size generally occurs in a PP-from Complement. 'The glacier shrank from … |
| Manner | Peripheral | This FE is used for any description of the Manner of the expansion including force (hard, softly), secondary effects (quietly, loudly), and general descriptions comparing events (the same way). |
| Path | Peripheral | Path is used for any expression that gives information about points on the scale of size that the Item traverses between the starting and ending point of its movement. 'The muscle tissue contracts down to less than … |
| Rate | Peripheral | This FE identifies the Rate of change of the value. 'The balloon inflates about 2 cubic cm a minute.' |
| Result_size | Peripheral | Result_size is the size that the Item has after the event. It is typically expressed in a PP Complement headed by to. 'The trees grow to 25 feet.' |
| Size_change | Peripheral | This FE identifies the Size_change of an Item. 'A 2-3cm expansion in width is required.' |
| Time | Peripheral | This FE identifies the Time when the expansion occurs. |

**Frame relations** (super → sub)

- Causative_of: Cause_expansion → Expansion
- ReFraming_Mapping: Cause_expansion → Expansion
- Using: Expansion → Dough_rising

**Lexical units** (16): contract.v, contraction.n, dilate.v, enlarge.v, enlargement.n, expand.v, expansion.n, explosive.a, extension.n, grow.v, inflate.v, lengthen.v, shrink.v, spread.v, stretch.v, swell.v

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

## Expensiveness  (frame id 83)

A Payer gives up (or potentially gives up) the use of an Asset (generally money) in order to achieve an Intended_event. This event is often more specifically described as gaining possession of some Goods or receiving a Service. In the majority of cases, the Payer is described generically (INI), and the situation depicted answers the question of how much of an Asset would have to be given up to receive the Goods or bring about the Intended_event. 'It 'll cost Sandra's parents fifty grand a year for her to attend that school. ' 'That book would cost you more than twenty dollars to bind in a local book bindery.' 'Stamps used to cost only five cents. INI' 'The cost of a trip to a resort or spa varies by region, dependent primarily on weather, not local economic conditions. INI' 'Well, it 'll cost you.' 'For you, thirty bucks is practically free. DNI'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Asset | Core | The price of or payment made for the Goods. 'The painting was cheap at $600.' '$600 is exorbitant for that painting!' |
| Goods | Core | The FE Goods is the item(s) whose price is being assessed. Goods is usually an External Argument: 'These paintings are very pricey. ' |
| Intended_event | Core | The event that the Payer brings about by deploying the Asset. 'Attending summer school is expensive.' |
| Payer | Core | The person whose Asset is given up in order to achieve an Intended_event. This FE is often expressed as INI. 'A holiday in Europe is very expensive for me.' 'Europe is not cheap. INI' |
| Degree | Peripheral | This FE identifies the Degree to which Goods are cheap or expensive. |
| Origin | Peripheral | The place where a transaction would take place, generally where Goods and services are created or sold. 'Shirts are cheap at K-Mart.' |
| Rate | Peripheral | The amount of an Asset relative to some measure of the Goods |
| Time | Peripheral | The time when a transaction takes place. 'No, they've got a special on; it's really cheap there on Tuesdays' |

**Frame relations** (super → sub)

- ReFraming_Mapping: Commerce_scenario → Expensiveness
- Using: Abounding_with → Expensiveness
- Using: Commerce_scenario → Expensiveness

**Lexical units** (16): affordability.n, affordable.a, cheap.a, cost.n, cost.v, costly.a, exorbitant.a, expense.n, expensive.a, free.a, inexpensive.a, low-cost.a, low-priced.a, overpriced.a, pricey.a, set back.v

## Experiencer_focus  (frame id 48)

The words in this frame describe an Experiencer's emotions with respect to some Content. A Reason for the emotion may also be expressed. Although the Content may refer to an actual, current state of affairs, quite often it refers to a general situation which causes the emotion. ' My enjoyment of the movie was considerably impaired by the seven-foot guy sitting in front of me. ' ' Smithers takes great pleasure in collecting matchboxes.' ' Sergio derives great pleasure from smoking.' ' Smoking gives me extreme pleasure.' With certain verbs, the Circumstances can be expressed in a finite clausal or wh- complement which may optionally be preceded by a Null NP Object: 'I hate it when you do that.' Note: This is not how it is currently tagged.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Content | Core | Content is what the Experiencer's feelings or experiences are directed towards or based upon. The Content differs from a stimulus because the Content is not construed as being direcly responsible for causing the … |
| Event | Core | The Event is the occasion or happening that Experiencers in a certain emotional state participate in. ' It felt pretty awkward to partake in such a nervous ceremony.' Here we know that the ceremony was filled with … |
| Experiencer | Core | The Experiencer experiences the emotion or other internal state. |
| Topic | Core | The Topic is the area about which the Experiencer has the particular experience. ' Mr. Whiskers was upset about his cat treats.' |
| Circumstances | Extra-Thematic | The Circumstances FE encodes the circumstances or conditions under which the Experiencer experiences the emotion. Unlike Content it does not give the specific content of the emotion, but the Content can often be … |
| Degree | Peripheral | The Degree to which the experience occurs. |
| Explanation | Extra-Thematic | The Explanation is the explanation for why an Experiencer experiences the particular emotion. ' People love giant pandas because they look like teddy bears.' |
| Expressor | Core-Unexpressed | The Frame Element Expressor marks expressions that indicate a body part, gesture or other expression of the Experiencer that reflect his or her emotional state. They describe a presentation of the experience or emotion … |
| Manner | Peripheral | Manner of performing an action |
| Parameter | Extra-Thematic | The Parameter is a domain in which the Experiencer experiences the Content. 'Very few physical science students stressed the intellectual enjoyment of the degree course. ' |
| State | Core-Unexpressed | The State is the abstract noun that describes a more lasting experience by the Experiencer. 'Tracy was in an irritated mood. ' |
| Time | Peripheral | The time at which the Experiencer is in the specified emotional state. 'Last year, Bob was still interested in the young Republicans.' |

**Frame relations** (super → sub)

- Causative_of: Cause_emotion → Experiencer_focus
- Inheritance: Experiencer_focus → Desiring
- Inheritance: Experiencer_focus → Mental_stimulus_exp_focus
- Perspective_on: Emotions → Experiencer_focus
- ReFraming_Mapping: Emotion_directed → Experiencer_focus
- ReFraming_Mapping: Experiencer_focus → Desiring
- ReFraming_Mapping: Experiencer_focus → Emotion_directed
- ReFraming_Mapping: Experiencer_focus → Fear
- ReFraming_Mapping: Experiencer_focus → Feeling
- Using: Experiencer_focus → Desirability
- Using: Experiencer_focus → Tolerating

**Lexical units** (67): abhor.v, abhorrence.n, abominate.v, adoration.n, adore.v, agape.a, antipathy.n, apprehensive.a, calm.a, comfort.n, compassion.n, cool.a, delight.v, despair.v, desperation.n, despise.v, detest.v, detestation.n, discomfort.n, dislike.n, dislike.v, dissatisfied.a, dread.v, easy.a, empathy.n, envy.n, envy.v, fazed.a, fear.v, fed up.a, feverish.a, feverishly.adv, fond.a, fulfilled.a, fulfillment.n, grieve.v, happily.adv, hate.v, hatred.n, interested.a, intimidated.a, irritated.a, like.v, loathe.v, loathing.n, love.v, mourn.v, nervous.a, nettled.a, pity.n, pity.v, pleasure.n, regret.n, regret.v, relish.n, resent.v, resentment.n, rue.v, rueful.a, satisfaction.n, satisfied.a, solace.n, taken.a, unfazed.a, upset.a, worked up.a, worried.a

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

## Experimentation  (frame id 2683)

An Experimenter conducts an Experiment based on a Hypothesis. This Experiment contains a Control_group or Control_group_member which is compared with a Treatment_group or Treated_individual in order to determine the Result. '' 'Johann's experiment proved the new drug was effective in treating the disease.' 'Jacob placed the control group under a strong light for 20 hours each day.' 'Rolf tested his hypothesis in Vienna in 1973.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Control_group | Core | The group of entities in the Experiment which have not been treated and are compared to the Treatment_group or Treated_individual. '' 'The control in George's experiment consisted of 17 mice.' |
| Control_group_member | Core | An individual entity of the Experiment which is left untreated and then compared with the Treatment_group or the Treated_individual. '' |
| Experiment | Core | The test or Experiment conducted by the Experimenter using a Control_group and a Treatment_group. '' 'Jeff's experimentshowed the drug to be harmful to human health.' |
| Experimenter | Core | The Experimenter is the individual conducting the Experiment. 'Justin's experiment turned out to be rather successful.' 'The professor performed an interesting experiment for the class. ' |
| Hypothesis | Core | The Hypothesis is a conjecture as to the result of an Experiment. The Experiment takes place in order to prove the Hypothesis as correct or incorrect. 'Katrina tested her hypothesis yesterday afternoon. ' |
| Subjects | Core | In this frame Control_group and Treatment_group can be combined and expressed as Subjects. This FE can also be used for a generic individual on whom the Experiment is being conducted (see second example). 'They were … |
| Topic | Core | The Topic is the subject that the Experiment is studying. 'Jimmy conducted an experiment on tropical plants in non-tropical environments.' |
| Treated_individual | Core | An individual subject that receives treatment and is then compared to the Control_group or Controlled_individual. 'One rat's treatment caused it to outlive the rats of the control group.' |
| Treatment_group | Core | A group of subjects that receive Treatment and are compared to the Control_group or Controlled_individuals. '' 'The experiment's rats who received a dose of the drug every hour did not live to see the next day. DNI' |
| Descriptor | Peripheral | A Descriptor identifies a characteristic or description of the Experiment or the Subjects not captured by any other frame element. 'Mica's clever study was conducted in 2011.' |
| Duration | Peripheral | The amount of time the Experiment lasts. 'The six week long study was published in a prominent scientific journal.' |
| Instrument | Peripheral | A tool used in conducting the Experiment. Usually expressed by a with-PP. 'Silke experimented with chemical insecticides. ' |
| Phenomenon | Peripheral | A property that belongs to either the Control_group or the Treatment_group. Usually expressed by a PP. 'The control for the problem of imprecise sensing is currently being monitored. ' |
| Place | Peripheral | The Place in which the Experiment is conducted. |
| Result | Peripheral | The Result depicts the outcome of the Experiment. 'The experiment proves the new drug is effective treating the disease.' |
| Time | Peripheral | The Time at which the Experimenter conducts the Experiment. |

**Frame relations** (super → sub)

- Using: Scrutiny → Experimentation

**Lexical units** (9): control group.n, control.n, experiment.n, experiment.v, hypothesis.n, study.n, subject.n, test.v, treatment.n

## Expertise  (frame id 136)

This frame concerns people's knowledge or skill in certain domains. It does not concern acquaintance or familiarity with people. With adjectives as targets in this frame, we annotate on two FE layers. 'FE Layer-1: He is an experienced programmer.' 'FE Layer-2: He is an experienced programmer.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Behavior_product | Core | A product of behavior that shows the Protagonist's skill or lack of skill. 'A skillful advertising campaign persuaded voters that his opponent was soft on crime.' |
| Focal_participant | Core | This frame element can only occur in place of a skill expression. It refers to the prototypical patient in an action involving the Protagonist. For instance, in the following sentence the children are experts at some … |
| Knowledge | Core | The area of knowledge (as opposed to a practical skill) in which the Protagonist 's experience is assessed. |
| Protagonist | Core | The person whose expertise is assessed. |
| Role | Core | This frame element denotes a role in which the protagonist has developed his expertise. 'His prowess as a surgeon is impressive.' In many cases, the Role noun secondarily evokes the Skill that is at issue. |
| Skill | Core | Skill identifies the Protagonist's talent or ability to do things with one's hand or body. |
| Degree | Peripheral | Degree to which event occurs |
| Judge | Peripheral | The individual whose point of view is taken in assigning the judgment denoted by the target. |
| Manner | Peripheral | The Manner give further description of the way in which the Protagonist exhibits their skill or lack of skill. |
| Time | Peripheral | The Time when the Protagonist has the expertise. |

**Frame relations** (super → sub)

- Inheritance: Social_behavior_evaluation → Expertise
- ReFraming_Mapping: Awareness → Expertise
- ReFraming_Mapping: Bungling → Expertise
- ReFraming_Mapping: Desirability → Expertise
- ReFraming_Mapping: Expertise → Desirability
- ReFraming_Mapping: Mental_property → Expertise
- Using: Result_of_attempt_scenario → Expertise

**Lexical units** (73): ace.a, ace.n, adept.a, adept.n, adeptness.n, amateur.a, amateur.n, awful.a, bad.a, buff.n, competence.n, competent.a, connoisseur.n, conversance.n, conversant.a, crack.a, dreadful.a, excel.v, excellent.a, experience.n, experienced.a, expert.a, expert.n, expertise.n, familiar.a, fantastic.a, good.a, great.a, guru.n, incompetence.n, incompetent.a, incredible.a, inept.a, ineptitude.n, ineptness.n, inexperienced.a, inexpert.a, know-how.n, knowledgeable.a, lay.a, layman.n, master.a, master.n, mastery.n, maven.n, mediocre.a, new (to).a, novice.n, outstanding.a, pro.n, proficiency.n, proficient.a, prowess.n, skilful.a, skill.n, skilled.a, so-so.a, specialist.n, splendid.a, strong.a, stupendous.a, superb.a, superlative.a, terrible.a, terrific.a, tremendous.a, versed.a, virtuosity.n, virtuoso.n, well-versed.a, whiz.n, wizard.n, wonderful.a

## Explaining_the_facts  (frame id 1462)

A Question about the reason or cause of a known State_of_affairs is presented as being answered by the existence of a particular Fact. The exact chain of reasoning, including the answer itself, of which the Fact is a part is not specified. Contrast this frame with the Evidence frame which casts a Support (a fact) as providing Evidence for, or conclusively proving, the Proposition (another proposed fact). Thus, there is no open question in the Evidence frame. 'Ruby's orange vest marked with the words "service dog" accounts for why the 3-year-old goes along.' 'The nation's history explains why the current conflict succumbs to, and yet simultaneously transcends, the stereotype.' 'Then that I exist is explained by A and B having come together.' ' Lack of potential for improvement in the immediate future accounts for the low number of returnees into South Ossetia, even for the Ossetian ethnic group.' 'That explains it.' 'Somehow this explains why Apple is always the last man to get the technology.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Fact | Core | A Fact which can be connected by a chain of reasoning to the State_of_affairs. 'This fact alone explains the Sun/climate anomaly.' |
| Question | Core | An open proposition concerning the cause of the State_of_affairs. 'The fact that this remained in Pandora's box explains why men have hope.' '' |
| State_of_affairs | Core | A Fact whose cause is under consideration. 'Do increased proinsulin concentrations explain the excess risk of coronary heart disease in diabetic and prediabetic subjects?' |
| Concessive | Extra-Thematic | The state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the Concessive. |
| Degree | Peripheral | This FE identifies how much of the State_of_affairs is explained by the Fact. 'This, in my opinion, partially accounts for why Anakin became a ghost.' |
| Manner | Peripheral | This FE indicates salient characteristics of the Fact considered as an explanation. 'Current life-history theory would readily explain the small males in B if juvenile male mortality were higher than that of females , … |
| Means | Peripheral | An intermediate logical step that justifies the relationship between the Fact and the State_of_affairs. 'This gives an explanation for the observation by identifying it as an instance of general pattern' |
| Viewpoint | Extra-Thematic | The perspective of an individual who judges whether they consider the Fact an explanation for the State_of_affairs. 'To her, this explains things, and we therefore need not discuss it any longer. ' |

**Frame relations** (super → sub)

- Using: Evidence → Explaining_the_facts

**Lexical units** (3): account.v, explain.v, explanation.n

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

## Fluidic_motion  (frame id 345)

In this frame a Fluid moves from a Source to a Goal along a Path or within an Area. ' The blood spurted from the wound. ''The water gushed into the house . '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Area | Core | Area is the setting in which the Fluid's movement takes place on an unspecified Path. 'The Thames River flows throughout England.' |
| Fluid | Core | The Fluid is the entity that changes location and moves in a fluidic way. |
| Goal | Core | Goal is the location the Fluid ends up. |
| Path | Core | The Path is the trajectory along which the Fluid moves. |
| Source | Core | The Source is the location the Fluid occupies initially. |
| Configuration | Extra-Thematic | The Configuration encodes information about the amount, arrangement, and unitization of the flow. 'The water cascaded in torrents' . 'The water cascades in large volumes.' |
| Depictive | Extra-Thematic | This FE identifies the Depictive phrase describing the Fluid throughout the action. |
| Distance | Peripheral | This FE describes the phsyical extent of the motion of the Fluid. |
| Duration | Peripheral | The amount of time for which the Fluid moves. |
| Explanation | Extra-Thematic | The Explanation is the reason for the fluidic motion. 'It flowed from the sheer weight of water above it.' |
| Manner | Peripheral | The Manner in which the Fluid flows. |
| Place | Peripheral | The Place describes the location of the motion which has a specified Source, Path or Goal. 'At Oregon Caves, a stream runs through the dining room.' |
| Result | Extra-Thematic | This FE identifies the result of the Fluid moving. |
| Speed | Peripheral | This is the rate at which the Fluid flows. |
| Time | Peripheral | The Time when the Fluid flows. |

**Frame relations** (super → sub)

- Causative_of: Cause_fluidic_motion → Fluidic_motion
- Inheritance: Motion → Fluidic_motion
- ReFraming_Mapping: Make_noise → Fluidic_motion
- Using: Fluidic_motion → Breathing

**Lexical units** (28): bubble.v, cascade.v, course.v, dribble.v, drip.v, flow.v, gush.v, hiss.v, jet.v, leak.v, ooze.v, percolate.v, pump.v, purl.v, run.v, rush.v, seep.v, soak.v, spew.v, spill.v, splash.v, splatter.v, spout.v, spray.v, spurt.v, squirt.v, stream.v, trickle.v

## Food  (frame id 277)

This frame contains words referring to items of food. 'Specialties include deep fried shredded beef , duck , prawn dishes and hand-made noodles.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Food | Core |  |
| Constituent_parts | Peripheral | A part of the Food. 'You'd be surprised, but it was hard to eat a banana with such a thick peel.' |
| Descriptor | Peripheral | This FE indicates a characteristic or description of the food. ' She drinks low-fat milk' |
| Type | Peripheral | This FE identifies a particular Type of the food item. ' cooking apple' 'Granny Smith apple.' |

**Frame relations** (super → sub)

- Inheritance: Physical_entity → Food
- Using: Food → Tasting
- Using: Ingestion → Food

**Lexical units** (71): MRE.n, almond.n, apple.n, banana.n, basil.n, beef.n, beer.n, berry.n, biscuit.n, bread.n, butter.n, cabbage.n, cake.n, carrot.n, cereal.n, cheese.n, cheesecake.n, chicken.n, chocolate.n, coffee.n, cookie.n, cracker.n, croissant.n, date.n, dressing.n, egg.n, fat.n, fish.n, food.n, fruit.n, herb.n, honey.n, juice.n, ketchup.n, lamb.n, lasagne.n, lettuce.n, lobster.n, mayonnaise.n, meat.n, milk.n, noodle.n, nut.n, oil.n, pancake.n, pasta.n, pastry.n, pea.n, peanut.n, pepper.n, potato.n, poultry.n, roll.n, salmon.n, sauce.n, shellfish.n, shrimp.n, soup.n, spice.n, stew.n, sugar.n, sweet.n, sweetener.n, tea.n, tuna.n, turkey.n, veal.n, vegetable.n, vinaigrette.n, vinegar.n, water.n

## Gesture  (frame id 36)

The words in this frame have to do with non-verbal communication. Topic is not normally expressed with these words. This seems to be related to the absence of a verbal code in cases of gestural communication. Topic can be viewed as a partial characterization of a Message, but such partial characterization is either difficult or irrelevant in the absence of a verbal code. 'I gestured with my hand for him to come over.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Addressee | Core | This is the person to whom a non-verbal Message is communicated. It may be expressed as an NP Object or as a PP Complement: The teacher gestured us into the room. The teacher gestured to us to enter the room. |
| Body_part | Core | The Body_part is the specific body part of the Communicator which gestures. |
| Communicator | Core | This is the sentient entity that communicates a Message non-verbally. It is normally expressed as an External Argument: The teacher gestured us into the room. |
| Indicated_entity | Core | The Indicated_entity is the entity which the Communicator is pointing out to the Addressee as meaningful. |
| Message | Core | This is the content of non-verbal communication. It may be expressed as a that-clause Complement, a to-marked infinitive VP Complement, or a directional PP Complement: The teacher gestured that it was time to leave. … |
| Instrument | Peripheral | An Instrument that the Communicator uses to gesture to the Addressee together. |
| Manner | Peripheral | Manner of performing an action |
| Means | Peripheral | An act performed by the Communicator that results in the successful transfer of a Message. 'He signalled John to fold by touching his ear and leaning back.' |
| Place | Peripheral | The Place is where the gesturing occurs. |
| Time | Peripheral | When the gesturing occus. |

**Frame relations** (super → sub)

- Inheritance: Communication → Gesture

**Lexical units** (8): beckon.v, gesticulate.v, gesture.v, motion.v, nod.v, signal.n, signal.v, wave.v

## Give_impression  (frame id 67)

In this class of perception words, a Phenomenon, typically expressed as External Argument, and its perceptual characteristics are given some description. This may be a Characterization describing purely perceptual properties, an Appraisal (i.e. positive or negative judgment) or an Inference about some non-perceptual property based on the Perceiver_passive's perception. '' 'There's a hamburger bar open, and it smells real good.' 'What we drank then tasted like sulphur and ox blood.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Appraisal | Core | Appraisal is the positive or negative judgement given to the Phenomenon.'Kim's hair feels nice.''That trumpet sounds dreadful.' |
| Characterization | Core | Characterization is the subjective description (of the Perceiver_passive ) of the Phenomenon.'Kim's new furniture looks sort of bluish.''The violins sounded as if they were in pain.''The city smelled like rotting … |
| Inference | Core | Inference expresses some property of the Phenomenon that is not a direct feature of the particular sensory modality (if any), but rather is based on perception within that modality.'Pat sounds devastated by the bad … |
| Phenomenon | Core | The Phenomenon is typically the External Argument of the verbs in this frame.'The soup tasted very salty.' |
| Body_part | Peripheral | Body_part expressions are not common in this frame, but may occur with the verb "feel" (the only verb in this frame that does not lexically encode the Body_part involved in perception) or occasionally (and redundantly) … |
| Circumstances | Extra-Thematic | The physical or abstract Circumstances that determine the appearance of the Phenomenon. 'The people I work with seem to either hate their jobs, or like them, depending on my mood.' |
| Degree | Peripheral | The extent to which a Phenomenon gives the impression that a certain Characterization or Inference holds. 'John looks like his father a bit.' |
| Frequency | Extra-Thematic | How often the Phenomenon has the Appraisal, Characterization, or Phenomenon. |
| Ground | Peripheral | Ground is the perceptual background against which the Phenomenon is experienced (or not experienced) by the Perceiver_passive.'The painting looks great against the new wallpaper.' |
| Location_of_protagonist | Extra-Thematic | Location_of_protagonist identifies the position of the Perceiver_passive during the act of perception. Typically it is expressed in a PP-from.'The house looks deceptively small from the outside.' |
| Path | Peripheral | This frame element, usually expressed in a PP, is used for all path-like expressions, except those indicating the Location_of_perceiver (see above), that describe how the Perceiver_passive's attention is directed … |
| Perceiver_passive | Peripheral | The Perceiver_passive experiences some perception without necessarily intending to, but makes a judgment about the Phenomenon. The Perceiver_passive generally occurs in a PP Complement.'The milk smells bad to me.' |
| State | Extra-Thematic | This FE identifies expressions that predicate something of the Phenomenon, providing some information about its State while the Perceiver_passive experiences it.'Pat looks great dressed in red.''The meat tastes … |

**Frame relations** (super → sub)

- Inheritance: Perception → Give_impression
- Using: Give_impression → Chemical-sense_description
- Using: Give_impression → Want_suspect

**Lexical units** (9): appear.v, feel.v, look.v, reek.v, seem.v, smell.v, sound.v, stink.v, taste.v

## Giving  (frame id 139)

A Donor transfers a Theme from a Donor to a Recipient. This frame includes only actions that are initiated by the Donor (the one that starts out owning the Theme). Sentences (even metaphorical ones) must meet the following entailments: the Donor first has possession of the Theme. Following the transfer the Donor no longer has the Theme and the Recipient does. 'Barney gave the beer to Moe.' '$300 was endowed to the university to build a new performing arts building.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Donor | Core | The person that begins in possession of the Theme and causes it to be in the possession of the Recipient . |
| Recipient | Core | The entity that ends up in possession of the Theme. |
| Theme | Core | The object that changes ownership. |
| Circumstances | Extra-Thematic | The Circumstances are the conditions under which the Theme is given. 'I give my services free of charge.' |
| Depictive | Extra-Thematic | A description of the Donor, Recipient, or Theme given independently of the giving event per se. |
| Explanation | Extra-Thematic | The Explanation for which the Donor gives the Theme to the Recipient. |
| Imposed_purpose | Extra-Thematic | The Recipient's intended purpose for the Theme. 'Please give this list to the secretary for entry into the client database.' |
| Manner | Peripheral | The Manner is the manner in which the Donor gives the Theme to the Recipient. |
| Means | Peripheral | The Means by which the Donor gives the Theme to the Recipient. |
| Period_of_iterations | Extra-Thematic | The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | The Place where the Donor gives the Theme to the Recipient. |
| Purpose | Peripheral | The Purpose for which the Donor gives the Theme to the Recipient. |
| Time | Peripheral | The Time is when the Donor gives the Theme to the Recipient. |

**Frame relations** (super → sub)

- Inheritance: Giving → Commerce_pay
- Inheritance: Giving → Commerce_sell
- Inheritance: Giving → Lending
- Inheritance: Giving → Submitting_documents
- Inheritance: Giving → Supply
- Inheritance: Giving → Surrendering_possession
- Inheritance: Intentionally_act → Giving
- Inheritance: Lose_possession → Giving
- Perspective_on: Transfer → Giving
- Precedes: Giving → Post_giving
- Precedes: Pre_giving → Giving
- Subframe: Giving_scenario → Giving
- Using: Giving → Conferring_benefit
- Using: Giving → Offering

**Lexical units** (26): advance.v, bequeath.v, bequest.n, charity.n, confer (upon).v, contribute.v, contribution.n, donate.v, donation.n, donor.n, endow.v, fob off.v, foist.v, gift.n, gift.v, give out.v, give.v, hand in.v, hand out.v, hand over.v, hand.v, leave.v, pass out.v, treat.v, volunteer.v, will.v

## Gizmo  (frame id 106)

This frame contains general words denoting equipment where the Use or purpose is not specified by the lexeme but (typically) by a separate expression. The words are described with respect to the Use for which the item is used or its typical User. 'coffee machine' 'dentist's equipment'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Gizmo | Core | The complex artifact with a particular use. |
| Descriptor | Extra-Thematic | A characteristic of the Gizmo. |
| Power_source | Peripheral | The Frame Element Power_source marks expressions that indicate how a device is powered. ' We use gas appliances in our kitchen' |
| Use | Peripheral | This FE identifies the prototypical Use of a tool or device. 'coffee machine' 'device for making soap bubbles' |
| User | Peripheral | User identifies the person who (typically) uses a particular tool. ' This drawer is used for storage of dentist's equipment' |

**Frame relations** (super → sub)

- Using: Artifact → Gizmo
- Using: Gizmo → Being_in_operation

**Lexical units** (20): apparatus.n, appliance.n, centrifuge.n, contraption.n, core.n, device.n, equipment.n, gadget.n, gear.n, implement.n, instrument.n, level.n, machine.n, mechanical.a, player.n, range.n, system.n, technology.n, tool.n, utensil.n

## Grasp  (frame id 979)

A Cognizer possesses knowledge about the workings, significance, or meaning of an idea or object, which we call Phenomenon, and is able to make predictions about the behavior or occurrence of the Phenomenon. The Phenomenon may be incorporated into the wider knowledge structure via categorization, which can be indicated by the mention of a Category. The Cognizer may possess knowledge only in part and this may be expressed in a Completeness expression. The Cognizer may also be realized as a cognitive-emotional Faculty that is conceived of as having understanding. Note that the knowledge may have been acquired either from instruction or from the Cognizer's own experimentation, observation, or mental operations. Words in this frame are frequently used metonymically to denote the transition into the state described above. 'I figured this out last week and now I really understand it.' 'My father failed to comprehend that his explanations were based as much upon faith as mine' 'The draughtsman must fully comprehend what he is drawing' 'Nobody seems to have explained this to her, but finally she understands DNI' 'I realized I had not properly understood my own needs' 'The mind is often unable to comprehend the significance of what it perceives.' 'Our sensations are in some sense to be understood in terms of a set of stimulation levels (spiking frequencies) in the appropriate sensory pathways. CNI'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The sentient animate being who acquires new knowledge. 'Sue grasped the essentials right away' |
| Faculty | Core | A part of a person's cognitive-emotional faculties that is said to acquire knowledge. 'My heart grasped that reality immediately.' 'Man has understood something only when he has grasped it with his heart' |
| Phenomenon | Core | A state of affairs or dynamic system whose internal make-up and working the Cognizer comes to assimilate into their knowledge structure. 'You must grasp the complex relationship of all these subjects to each other' |
| Category | Peripheral | This frame element expresses a general type or class of which the Phenomenon is considered an instance by the Cognizer, allowing them to make predictions about the qualities, occurrence, or behavior of the Phenomenon. … |
| Completeness | Peripheral | The extent to which the Cognizer has incorporated the workings and significance of a Phenomenon into their knowledge structure. 'To comprehend fully the distinction between task and process it is necessary to … |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Evidence | Peripheral | Evidence marks expressions that indicate the source of the Cognizer's knowledge. 'The reason for this effect is easiest to understand from a picture.' |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously) and general descriptions comparing events (the same way). It may also … |
| Reference_point | Peripheral | A mental concept or domain to which the Cognizer relates their new knowledge. 'Unless one posits an inherent human tendency to comprehend the world in binary terms, one has to look for more sociological explanations.' |
| Time | Peripheral | This FE indicates the when the Cognizer asssimilates the new knowledge. 'Yesterday the students finally grasped the meaning of the equation' |

**Frame relations** (super → sub)

- Inheritance: Awareness → Grasp

**Lexical units** (14): apprehend.v, comprehend.v, comprehensible.a, fathom.v, follow.v, get.v, grasp.n, grasp.v, graspable.a, incomprehensible.a, intelligible.a, see.v, understand.v, unintelligible.a

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

## Health_response  (frame id 52)

A Protagonist is sensitive to a Trigger, which has the potential to cause some kind of reaction in the Protagonist. '' 'Mr. Clinton and his wife Hillary are allergic to cats.' 'On top of this, he has allergies to oats and dust and is a finicky feeder.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Protagonist | Core | The Protagonist occurs as the External Argument of the targets in this frame. The Protagonist represents the one exhibiting the response to the Trigger. 'Pat's allergy to dairy products is severe.' 'Young children are … |
| Trigger | Core | The Trigger most commonly occurs in a PP Complement headed by to. The Trigger is that substance or element which causes a health response in the Protagonist. 'Some people are very sensitive to chemicals in the … |
| Body_part | Peripheral | The Body_part identifies the part of the body that is responding to the Trigger. 'Diabetics may have increased vascular sensitivity to angiotensin II' |
| Degree | Peripheral | The Degree describes the extent to which the health response occurs. 'Jake is extremely allergic to codeine.' 'Grass and clover seeds need fairly warm conditions for germination and are more sensitive to drought or … |
| Manner | Peripheral | Manner describes the way (or style) in which the Protagonist Health_response manifests itself. 'Different socio-economic groups , age-groups , ethnic groups , genders have different needs for medical services because … |

**Frame relations** (super → sub)

- Inheritance: Inclination → Health_response
- Using: Response → Health_response

**Lexical units** (6): allergic.a, allergy.n, sensitive.a, sensitivity.n, susceptibility.n, susceptible.a

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

## Idiosyncrasy  (frame id 982)

A certain Idiosyncrasy belongs to an Entity distinguishing it from other entities. 'If you have 32 totally idiosyncratic meanings for a term in a class, everyone will be very confused when they talk! DNI' 'The art of change-ringing is peculiar to the English'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The Entity that has a certain distinguishing Idiosyncrasy. 'This bird is unique to England' |
| Idiosyncrasy | Core | An entity or characteristic belonging to the Entity. 'Paul has an idiosyncratic tendency to go barefoot at all times.' |
| Degree | Peripheral | The extent to which the Idiosyncrasy differs from the norm. 'Was this behavior completely idiosyncratic?' |

**Frame relations** (super → sub)

- Inheritance: Relation → Idiosyncrasy
- See_also: Typicality → Idiosyncrasy

**Lexical units** (10): certain.a, idiosyncrasy.n, idiosyncratic.a, oddity.n, particular.a, peculiar.a, peculiarity.n, uncanny.a, unique.a, weird.a

## Importance  (frame id 407)

A Factor affects the outcome of an Undertaking, which can be a goal-oriented activity or the maintenance of a desirable state, the work in a Field, or something portrayed as affecting an Interested_party. A Reason may be given for the importance of the Factor. The Degree of importance may also be specified. 'Temperature is the most critical factor in successful storage.' ' Timing will be critical.' 'Heathcliff is more important to me than myself . ' ' 1992 was of great importance to the business community. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Factor | Core | Factor is used for the concrete or abstract entity whose importance is assessed. ' Being sure they are buying fresh food is important to most people.' |
| Field | Core | A Factor may be generally important to the people or the activities in a field of endeavour. ' A successful GATT round is important for the world economy. ' |
| Interested_party | Core | Interested_party identifies the people who are affected by a particular Factor. ' Being sure they are buying fresh food is important to most people.' |
| Undertaking | Core | The Undertaking is a process or state or field of activity in which the Interested_party has a stake. 'Temperature is the most critical factor in successful storage.' |
| Degree | Peripheral | This FE marks expressions that indicate the Degree to which the Factor is important to the Undertaking. ' 1992 is of great importance to the business community. ' |
| Explanation | Extra-Thematic | This FE identifies the Explanation for which the Factor is important to the Undertaking. 'It 's critical to get it right because there are situations where if you don't, they will withhold some commission..' |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. A Frequency expression answers the question how often. |
| Place | Extra-Thematic | The location at which the Factor is important. |
| Time | Extra-Thematic | The Time at which the Factor is important to the Undertaking. |

**Frame relations** (super → sub)

- Using: Importance → Degree
- Using: Importance → Emphasizing
- Using: Importance → Historic_event
- Using: Importance → Individual_history

**Lexical units** (23): acute.a, considerable.a, count.v, critical.a, crucial.a, decisive.a, epic.a, fundamental.a, import.n, importance.n, important.a, instrumental.a, key.a, landmark.n, main.a, major.a, pivotal.a, priority.n, serious.a, seriously.adv, significance.n, significant.a, vital.a

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

## Intentionally_create  (frame id 280)

The Creator creates a new entity, the Created_entity, possibly out of Components. 'The Libyans were generating arms for export.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Created_entity | Core | This FE identifies the entity that the Agent intentionally creates. 'They were generating grenades for export.' |
| Creator | Core | The Creator creates a created entity. |
| Co-participant | Extra-Thematic | A secondary agent with whom the Creator intentionally creates the Created_entity. 'Emily set up the business with the former president of Intersoft, Inc.' |
| Components | Extra-Thematic | This FE identifies the Components that are attached together to form a Created_entity. 'He made a jungle gym out of iron bars.' |
| Depictive | Extra-Thematic | This FE identifies a depictive phrase describing the actor or undergoer of an action. |
| Instrument | Peripheral | This FE identifies the instrument with which an Agent intentionally creates a Created_entitiy. |
| Manner | Peripheral | Any description of the creation event which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may indicate … |
| Means | Peripheral | This FE identifies the Means by which a Creator intentionally creates a new entity. |
| Place | Peripheral | This FE identifies the place ehere the Agent intentionally creates the new entity. |
| Purpose | Peripheral | This FE identifies the purpose for which an Agent intentionally creates a new entity. |
| Role | Extra-Thematic | The role of Created_entity. 'This particular book was created as an introductory text.' |
| Time | Peripheral | This FE identifes the Time when an Agent intentionally creates a new entity. |

**Frame relations** (super → sub)

- Inheritance: Creating → Intentionally_create
- Inheritance: Intentionally_act → Intentionally_create
- Inheritance: Intentionally_create → Achieving_first
- Inheritance: Intentionally_create → Building
- Inheritance: Intentionally_create → Cooking_creation
- Inheritance: Intentionally_create → Create_physical_artwork
- Inheritance: Intentionally_create → Duplication
- Inheritance: Intentionally_create → Knot_creation
- Inheritance: Intentionally_create → Manufacturing
- Inheritance: Intentionally_create → Text_creation
- Inheritance: Intentionally_create → Translating
- ReFraming_Mapping: Intentionally_create → Creating

**Lexical units** (15): create.v, creation.n, develop.v, development.n, establish.v, establishment.n, found.v, generate.v, generation.n, make.v, produce.v, production.n, set up.v, synthesis.n, synthesise.v

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

## Leadership  (frame id 73)

These are words referring to control by a Leader over a particular entity or group (the Governed) or an Activity. The frame contains both nouns referring to a title or position (e.g. director, king, president), and verbs describing the action of leadership (e.g. rule, reign). With verbs, it is possible to mention the Role played by the Leader (often a name of a leading position, e.g., king) 'Sebek em hat was a Leader of Priests. ca. 1780 BC' 'In 1789 Fletcher Christian led the mutiny on HMS Bounty' 'Louis XIV ruled over his people as king for the longest period of any European monarch.' Compare to: Appellations.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | The Leader directs the Activity. 'The captain's cousin led the mutiny.' 'John Cage is one of the leaders of the minimalist music movement.' |
| Governed | Core | The entity whose actions or beliefs the Leader directs in the context of a joint activity or movement. This entity can be a political body, a person, or a group of people. 'Cyprus Turks turn against their leader' … |
| Leader | Core | The Leader is the one who has the role of leading. With verbs, and with predicate nominals linking an individual to a Role, the Leader is usually the External Argument: 'King Hussein ruled Jordan.' 'Hussein was King of … |
| Role | Core | The role played by the Leader in a given situation, often an official title; incorporated in most noun LUsin this frame. When expressed separately from the target, Role usually occurs in a PP Complement headed by as. … |
| Degree | Peripheral | The Degree to which leadership is asserted. |
| Depictive | Extra-Thematic | Depictive refers to that which describes one of the participants in the leadership relationship. 'He led them for a thousand years, strong, bold, and deathless.' |
| Descriptor | Peripheral | The Descriptor is a temporary condition of the Leader. 'A nervous governor stepped up to the lectern to give his speech.' |
| Domain | Extra-Thematic | The relevant Domain within which the Leader rules. This includes a specification of a country that the Leader serves (Iranian officials) or any other organizations that the Leader acts as part of (congressional … |
| Duration | Peripheral | Leadership by any particular individual is frequently limited in time, which is noted here as Duration. Duration usually occurs in a PP Complement. 'She reigned for 3 years.' |
| Manner | Peripheral | Manner refers to the style/way in which the leadership is asserted. 'Alternative and orthodox practitioners reign harmoniously side by side.' |
| Means | Peripheral | Means identifies act(s) performed by the Leader through which leadership is maintained. 'He ruled by sheer brutality and intimidation.' 'Napolean reigned by the grace of God and the will of the people.' |
| Place | Peripheral | The locale from which the Leader leads the Governed or the Activity. 'He ruled the west from his palace in Milan.' |
| Time | Peripheral | Time refers to the point in time that the leadership took place. 'The general led his troops into battle on June 22, 1883.' |
| Type | Peripheral | This FE indicates what subtype of the general category the Leader belongs to. |

**Frame relations** (super → sub)

- Causative_of: Change_of_leadership → Leadership
- See_also: Appellations → Leadership
- Using: Leadership → Political_locales

**Lexical units** (106): CEO.n, administer.v, administration.n, authority.n, baron.n, bishop.n, boss.n, caliph.n, captain.n, chair.v, chairman.n, chairperson.n, charge.n, chief executive officer.n, chief.n, chieftain.n, command.n, command.v, commandant.n, commander.n, commissioner.n, congressman.n, congresswoman.n, crown prince.n, despot.n, dictator.n, diplomat.n, director general.n, director.n, doyen.n, doyenne.n, drug lord.n, duchess.n, emperor.n, empress.n, executive.n, general.n, govern.v, government.n, governor.n, head.n, head.v, headmaster.n, high-priest.n, imam.n, kaiser.n, khan.n, khedive.n, king.n, lawmaker.n, lead.v, leader.n, leadership.n, legislator.n, legislature.n, maharaja.n, major general.a, mayor.n, minister.n, mogul.n, monarch.n, officer.n, official.n, overlord.n, pasha.n, power [govt].n, power [rule].n, premier.n, preside.v, president [non-political].n, president [political].n, presidential.a, prime minister.n, prince.n, principal.n, queen.n, rector.n, regime.n, reign.v, representative.n, rule.n, rule.v, ruler.n, run.v, satrap.n, secretary.n, senate.n, shah.n, sheik.n, sovereign.n, spearhead.v, state.n, sultan.n, superintendent.n, supervisor.n, suzerain.n, tsar.n, tsarina.n, tyrant.n, vice-captain.n, vice-chairman.n, vice-president [non-political].n, vice-president [political].n, vice-principal.n, viceroy.n, vizier.n

## Legal_rulings  (frame id 2076)

An Authority with the power to make decisions hands down a Finding over a question presented in a formal or informal Case. 'The judge ruled yesterday that the revisions were not adequate. DNI' 'A high court in London ruled on the case that a vulture fund can extract more than $20 million from Zambia for a debt.' 'In the California case, a judge ruled Oct. 12 that Tendler must pay the bloggers' legal fees.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Authority | Core | The Authority (which may be the jury, judge, magistrate or court) decides on the Finding. 'The US International Trade Commission ruled that a 1987 anti-dumping tariff against frozen concentrated orange juice from … |
| Case | Core | This FE describes the question on which the Authority gives a Finding. 'US Supreme Court ruled on flag salutes in public schools today.' |
| Defendant | Core | The person about whom the Authority passes a judgment or Finding. 'They held judgment upon me as a convicted traitress.' |
| Finding | Core | This FE identifies the outcome of the Authority's deliberation or consideration. 'Miss Mahmod's father ruled that she would never marry him.' |
| Circumstances | Extra-Thematic | The Circumstances under which the ruling was reached. |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the ruling event operates (often denoted by words such as "officially," "formally," "technically," etc.). |
| Duration | Extra-Thematic | The amount of time that a Finding holds. |
| Explanation | Extra-Thematic | The Explanation for the Finding. |
| Legal_basis | Peripheral | This FE indicates the basis in law of a Finding. |
| Manner | Peripheral | This FE identifies the Manner in which the Authority acts. |
| Means | Peripheral | This FE identifies an action that the Authority performs in order to return the verdict. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. In addition, most … |
| Place | Peripheral | Where the Finding takes place. |
| Purpose | Peripheral | This FE identifies the purpose why the Authority returns a particular Finding. |
| Re-encoding | Peripheral | This FE presents the current frame as an integral part of a larger conceptualization expressed by another frame. The frame expressed by the target typically corresponds to a Means action within the frame expressed by … |
| Time | Peripheral | When the Authority gives his Finding. |

**Frame relations** (super → sub)

- Inheritance: Intentionally_act → Legal_rulings
- Inheritance: Legal_rulings → Verdict
- Using: Communication → Legal_rulings

**Lexical units** (6): adjudicate.v, decree.v, deem.v, judge.v, judgment.n, rule.v

## Level_of_force_exertion  (frame id 1563)

An Exerter, Action, or Force is capable of exerting or does exert a physical force at a level specified by the target. That physical force may cause deformation or breakage of, or simply motion in the receiving entity. The receiving entity is conceptually present (even if remotely), but is usually not lexically explicit. This frame covers both individual-level/static uses ("a STRONG person") as well as stage-level/dynamic uses ("a STRONG push"). However, the durative, individual-level meaning appears more frequently in the data and seems more basic. 'Eugenie loved the sea and was a strong swimmer.' 'Spartacus dealt the Roman soldier a mighty blow.' 'A powerful force tore off the tree's branches.' Exerter, Action, and Force belong to a Core set. '' There are several productive metaphors covered by this frame. The first and most common is one in which social influence or control is conceptualized as the physical exertion of force. The social influence/control is more specifically a propensity to cause change in social realms such as the economic, political, militaristic, cultural, or intimate: 'There were theoretical limits to the power of the king.' 'Voters in the South have a strong incentive to keep such Democrats in office.' Another similar metaphor is one in which psychological influence or control is understood as the physical exertion of force. The psychological influence/control includes the emotional as well: 'Poetic words in a text can be given more emotive power by using melisma.' 'He was a forceful speaker.' A third metaphor involves the amount of an entity construed as the physical force exertion of said entity. Depending on context, amount could be volume, etc. (“STRONGEST critics”; “MIGHTY uproar”). '' Two related physical force dynamic frames are Level_of_force_resistance and Dynamism. This frame is distinguished from the Level_of_force_resistance frame in that it describes the level of force exertion instead of the level of resistance, and also in that there are three categories of Core FE available to the target (i.e Exerter, Action, or Force), whereas in Level_of_force_resistance there are only two Core FEs (i.e. Resisting_entity and Opposing_force). Of the latter frame's FEs, Opposing_force specifies the thing that the main entity resists to a level desginated by the target. Its parallel in Level_of_force_exertion is implied but backgrounded to the extent that it rarely appears as explicit lexical material; thus there is no corresponding Core FE. This frame differs from Dynamism with regard to individual-level cases; targets here express the FE's capability. In contrast, Dynamism targets express the FE's tendency. For example, "a STRONG person" is generally construed as a person who is capable of strength, while "an ENERGETIC person" (energetic.a from the Dynamism frame) is construed as a person who tends to be energetic. However, there is overlap between the two frames in stage-level cases - "a STRONG push" and "an ENERGETIC push" seem rather comparable.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Action | Core | The Action that can or does exert a force of the level specified by the target. 'She gave him a playful, weak punch in the arm.' |
| Exerter | Core | The Exerter that can or does exert a force of the level specified by the target. 'Salesmen touted the power of the engine's motor.' |
| Force | Core | The Force that can or does exert a force of the level specified by the target. 'No one should underestimate the mighty strength of the dung beetle.' |
| Circumstances | Extra-Thematic | The Circumstances under which the Exerter, Action, or Force can or does exert a force. 'The winds were strongest during the hurricane.' |
| Degree | Peripheral | The Degree to which the Exerter, Action, or Force can or does exert a force. 'After being in space for six months, his muscles were extremely weak.' Where Degree is expressed by a comparative or superlative form of the … |
| Descriptor | Peripheral | This FE describes the force exertion of the Exerter, Action, or Force. 'Henry's longstanding powerlessness against the school bully made him fearful and withdrawn.' |
| Domain | Peripheral | The Domain is the field in which the Exerter, Action, or Force can or does exert its force. 'The U.S. possesses great military strength.' |
| Place | Peripheral | The location where the Exerter, Action, or Force can or does exert its force. 'Muhammad Ali's force in the ring was indisputable.' |
| Time | Peripheral | The Time during which the Exerter, Action, or Force can or does exert its force. 'My quads feel particularly weak after 100 squats.' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Level_of_force_exertion
- ReFraming_Mapping: Dynamism → Level_of_force_exertion
- ReFraming_Mapping: Level_of_force_exertion → Capability
- See_also: Level_of_force_exertion → Dynamism
- See_also: Level_of_force_exertion → Level_of_force_resistance
- Using: Causation → Level_of_force_exertion

**Lexical units** (11): force.n, forceful.a, might.n, mighty.a, power.n, powerful.a, powerless.a, strength.n, strong.a, weak.a, weakness.n

## Likelihood  (frame id 114)

This frame is concerned with the likelihood of a Hypothetical_event occurring. The Hypothetical_event is its only core frame element. 'It is likely that he'll arrive late.' Notice that in the case where a noun phrase is the subject of the Support Verb, that NP is also tagged as Hypothetical_event. 'He is likely to arrive late.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Hypothetical_event | Core | The state of affairs or occurrence whose likelihood is assessed. 'Rain is fairly unlikely today, I think.' |
| Circumstances | Extra-Thematic | The Circumstances under which the Hypothetical_event is likely. 'A positive placebo effect is more likely when both patient and physician believe that therapeutic benefit will result.' |
| Degree | Peripheral | Degree to which event occurs 'There is a high probability that it will rain today.' |
| Explanation | Extra-Thematic | This FE expresses a reason the speaker has for making judgment about the likelihood of an event. 'There is a high chance of rain because of the stormfront.' |
| Place | Peripheral | Where the event takes place. 'There is a high chance of rain in Seattle.' |
| Time | Peripheral | When the event occurs. 'There is a high chance of rain today.' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Likelihood
- Inheritance: Likelihood → Run_risk
- ReFraming_Mapping: Certainty → Likelihood
- Using: Likelihood → Capability
- Using: Likelihood → Luck

**Lexical units** (31): assured.a, bound.a, can.v, certain.a, certainly.adv, certainty.n, chance.n, guaranteed.a, impossible.a, improbability.n, liable.a, likelihood.n, likely.a, likely.adv, long.a, may.v, might.v, must.v, possibility.n, possible.a, possibly.adv, probability.n, probable.a, probably.adv, prone.a, sure.a, surely.adv, tend.v, undoubtedly.adv, unlikely.a, would.v

## Limitation  (frame id 2715)

An Entity that would be expected to have a characteristic to a certain degree (typically based on comparison to other entities of the same type) instead has a more limited degree of that characteristic. 'The limitations on the theory's applicability made it unpopular in its time.' 'Are there any undocumented limitations on the use of this machine?'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The Entity would normally be expected to have a set of possibilites, but instead exhibits only certain possibilites, or exhibits them on fewer situations than expected. 'Our technology has limits we didn't expect.' |
| Degree | Peripheral | The Degree to which the Entity is limited. 'There are strong limits on its usefulness.' |

**Frame relations** (super → sub)

- Causative_of: Limiting → Limitation
- Using: Limiting → Limitation

**Lexical units** (2): limit.n, limitation.n

## Linguistic_meaning  (frame id 406)

A linguistic Form has a particular Meaning, possibly restricted to a particular Context. Some linguistic Forms, nouns and nominal expressions, also can refer to an object in the real or an imagined world, a Referent. '"Unicorn" denotes a mythological horse with a horn on its head.' 'In art, the word "oeuvre" means "the collected works of an artist."'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Form | Core | Form is the formal pole of a linguistic sign. |
| Meaning | Core | Meaning is the sense of a linguistic Form. |
| Referent | Core | Referent identifies an object in the real (or a hypothetical) world that a linguistic expression is used to talk about. |
| Degree | Extra-Thematic | This frame element selects some gradable attribute of the Form and modifies the expected value for it. |
| Textual_location | Extra-Thematic | The FE Textual_location is used for expressions that indicate under which semantic, collocational, pragmatic or other circumstances a Form has a particular Meaning. |

**Frame relations** (super → sub)

- Using: Linguistic_meaning → Word_relations
- Using: Simple_name → Linguistic_meaning

**Lexical units** (15): ambiguous.a, denotation.n, denote.v, designate.v, extension.n, intension.n, mean.v, meaning.n, monosemous.a, non-referential.a, polysemous.a, reading.n, referential.a, sense.n, vague.a

## Locale_by_collocation  (frame id 2626)

A Profiled_region is identified as being the region where an Entity is located. 'State your location.' 'I can't get a lock on their position.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The entity is located at the Profiled_region. 'If you sign up for this new service, we can get a fix on your phone's location if you lose it or it is stolen.' |
| Profiled_region | Core | The region where the Entity is located. 'If you sign up for this new service, we can get a fix on your phone's location if you lose it or it is stolen.' |
| Constituent_parts | Extra-Thematic | Salient parts that make up a Profiled_region. |
| Container_possessor | Extra-Thematic | The location that the Profiled_region is a part of. |
| Descriptor | Extra-Thematic | The Descriptor is a temporary condition of the Profiled_region. |
| Formational_cause | Extra-Thematic | This FE indicates the action (or causer) which brings the features of the Profiled_region about. This FE should also include words that indicate that there was no salient formation. |
| Inherent_purpose | Extra-Thematic | The activity that is carried out in the Profiled_region. |
| Related_event | Extra-Thematic | An event related to the Profiled_region in some way other than (1) Formational_cause (which is a separate FE) or an intended use (which would place the instance in Locale_by_use), or (3) a defining event (which would … |
| Relative_location | Peripheral | A place that a Profiled_region is located with respect to. 'Once you have indicated your location next to a shopping mall, you can access the full array of our services on your mobile device.' |
| Time | Peripheral | The Time at which the Entity is at the Profiled_region. 'Any updates on his current location?' |

**Frame relations** (super → sub)

- Inheritance: Locale_by_collocation → Locale_by_event
- Inheritance: Relational_location → Locale_by_collocation

**Lexical units** (2): location.n, position.n

## Locative_relation  (frame id 199)

A Figure is located relative to a Ground location. 'The cat is on the mat.' 'The kitchen, with its breakfast / snack bar, adjoins on one side while the dining area adjoins on the other side. DNI' 'The president's plane landed in Washington.' This frame is used for LUs that do not belong in daughter frames, either because they are too general to have any particular image schema associated with them (e.g., here.adv), or because we do not (yet) have a specific frame with the correct image schema (e.g., inland.a). Prepositions, adverbs, and spatial adjectives that act as targets in this frame and its descendants cooccur with a number of constructions that may supply extra information and should be annotated as extrathematic frame elements. The location of the Figure may be further specified by its Distance from the Ground along a vector implied by the targets image schema, or the Direction in which the Figure lies from a reference location (generally, the deictic center). In cases where both seem to cooccur, the Distance actually modifies the Direction, as seen in the following example: 'This pup was lying abandoned, 350 feet down at the bottom of an Arizona canyon.' There is no sense in which the Distance is measured using the schema for at.prep ('350 feet at the bottom of the canyon' doesn't mean the right thing at all); rather the distance is measured using the schema for down.adv, and is thus considered a modifier of the Direction FE. In some very specific situations, prepositions, adjectives, and nouns can be used with a copula to describe the whole Profiled_region where a Figure is or could be, as in the following: 'Inside my wallet is where I put it .' 'Outside your blind date's door seems like the worst place in the world .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Figure | Core | The Figure is perceived as located relative to a certain Ground location. The figure can be an entity or an event. 'The cat is on the mat.' |
| Ground | Core | The Ground serves as a basis for describing the location of the Figure. 'The cat is on the mat.' |
| Profiled_region | Core | The region within which a Figure might be found. This FE is exclusive of Figure, and is a reconstrual that is not possible with verb lexical units. 'Next to the kitchen is the best place to locate your garage .' |
| Accessibility | Extra-Thematic | An indication of how accessible the Figure is to some participant in the speech context (either the speaker or the addressee, or some other highly salient viewpoint in a narrative). This FE normally describes … |
| Deixis | Extra-Thematic | An indication of how the locative phrase relates to the grounding of the speech situation, either locating it near (here) or far (there, yonder), or specifically separated from the speech context by distance or a … |
| Direction | Extra-Thematic | This FE identifies the Direction from a reference location (generally, the deictic center) of a path to the Figure. This FE is filled by one of a closed class of adverbs: up, down, out (meaning 'beyond the boundary … |
| Directness | Extra-Thematic | An indication of how closely the position of Figure matches the prototype expected from the image schema associated with the target. This FE is normally filled by closed-class, dedicated adverbs like right, straight, … |
| Distance | Extra-Thematic | This FE identifies the Distance between the Figure and the Ground. This FE requires an image schema with a vector that extends from the Ground, or a subpart of the Ground, in some direction, and the Distance is … |
| Figures | Core-Unexpressed | The Figures are items which mutually serve to identify the location of the other items. |
| Region_quantification | Extra-Thematic | A description of how much of a potential profiled region actually has (or is expected to have) a Figure in it. It is normally filled by closed-class items like 'all', 'somewhere', 'nowhere', etc. 'I think it 's … |
| Temporal_profile | Extra-Thematic | A description of how the access path to the Ground interacts with time. This FE is filled only by the closed class of adverbials back.adv (which indicates that the position was occupied by the Figure before) and on.adv … |
| Time | Peripheral | The period of time during which the locative relation between Figure and Ground obtains. 'He was in Athens on Friday.' |

**Frame relations** (super → sub)

- Inheritance: Basis_for_attribute → Locative_relation
- Inheritance: Locative_relation → Abounding_with
- Inheritance: Locative_relation → Adjacency
- Inheritance: Locative_relation → Containing
- Inheritance: Locative_relation → Directional_locative_relation
- Inheritance: Locative_relation → Distributed_position
- Inheritance: Locative_relation → Expected_location_of_person
- Inheritance: Locative_relation → Goal
- Inheritance: Locative_relation → Gradable_proximity
- Inheritance: Locative_relation → Interior_profile_relation
- Inheritance: Locative_relation → Location_on_path
- Inheritance: Locative_relation → Non-gradable_proximity
- Inheritance: Locative_relation → Spatial_co-location
- Inheritance: Locative_relation → Spatial_contact
- Inheritance: Locative_relation → Within_distance
- Inheritance: State → Locative_relation
- Perspective_on: Locative_scenario → Locative_relation
- ReFraming_Mapping: Locative_relation → Adjacency
- ReFraming_Mapping: Locative_relation → Interior_profile_relation
- ReFraming_Mapping: Locative_relation → Non-gradable_proximity
- ReFraming_Mapping: Locative_relation → Spatial_contact
- Using: Existence → Locative_relation
- Using: Locative_relation → Being_located
- Using: Locative_relation → Path_shape
- Using: Locative_relation → Relational_natural_features

**Lexical units** (39): above-ground.a, all over.prep, along.prep, astride.prep, at.prep, athwart.prep, beyond.prep, border.v, bracket.v, distant.a, down.prep, elsewhere.adv, everywhere.adv, here.adv, inland.a, mainland.n, meet.v, near.prep, north.prep, northeast.prep, northwest.prep, offshore.a, out.prep, outlying.a, over.prep, past.prep, south.prep, southeast.prep, southwest.prep, surrounding.a, there.adv, throughout.prep, to.prep, ubiquitous.a, underground.a, underground.adv, up.prep, west.prep, where.adv

## Losing  (frame id 2197)

This frame describes a situation in which an Owner loses his or her Possession. The Owner may have failed to keep ownership of their Possession (i.e. robbery or gambling) or may have unintentionally misplaced their Possession. 'I misplaced my watch.' 'He lost his wedding ring while playing cards.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Owner | Core | The original Owner of the Possession. |
| Possession | Core | The object that is possessed by the Owner. |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the event of losing a Possession logically follows. |
| Means | Peripheral | This FE describes how the Owner loses the Possession. |
| Place | Peripheral | The Place where the Possession is lost. |
| Time | Peripheral | The Time when the Possession is lost. |

**Frame relations** (super → sub)

- Inheritance: Losing_track_of_theme → Losing

**Lexical units** (2): lose.v, misplace.v

## Make_agreement_on_action  (frame id 1342)

Two (or more) people (the Parties, also encodable as Party_1 and Party_2) negotiate an agreement. Both sides are construed as making a commitment to assume an Obligation--the process is understood to be symmetrical or reciprocal. Instead of a specific mention of the Obligation, a Topic expression may be used to indicate the domain covered. 'So far , we have agreedto cede 100km of coastline to Kiribati . DNI ' 'At common law, the parties could make an oral agreement to submit a dispute to arbitration and such oral agreement would be valid.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Obligation | Core | An expression of the commitment made by the Parties . 'The US and Russia have agreed to share early warning data on missile launches.' |
| Parties | Core | The group of individuals portrayed as equally involved in making an agreement. 'The US and Russia have agreed to cooperate in destroying surplus portable anti-aircraft missiles.' |
| Party_1 | Core | The individual or individuals that form the more prominent (i.e. agentive) party of the agreement, as compared with Party_2. That is, Party_1 is generally encoded as the External Argument of verbs, and peripheral FEs … |
| Party_2 | Core | The semantically (and grammatically) less prominent participant (or group of participants) in the agreement. It is generally encoded within a prepositional phrase (e.g. headed by with). 'Mozilla Foundation has finally … |
| Topic | Core | Topic is a description of the domain covered. 'Some types of alloy steel have been covered in the expiring trade agreement.' |
| Descriptor | Extra-Thematic | This FE describes a characteristic of the Obligation. |
| Manner | Peripheral | Any description of the act of making an agreement which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may … |
| Medium | Peripheral | As with other frames in the Communication domain, the Medium of communication may be expressed. Medium is the physical entity or channel used to record or negotiate the Obligation. 'The parties made a written agreement … |
| Place | Peripheral | This FE identifies the Place where the Agreement occurs.'The town coucil members reached an agreement at the City Hall plenary session.' |
| Time | Peripheral | This FE identifies the Time where the Agreement occurs.'The town coucil members finally reached an agreement at midnight.' |

**Frame relations** (super → sub)

- Inheritance: Make_agreement_on_action → Make_compromise
- Using: Commitment → Make_agreement_on_action
- Using: Make_agreement_on_action → Be_in_agreement_on_action

**Lexical units** (5): agree.v, agreement.n, deal.n, settle.v, treaty.n

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

## Manufacturing  (frame id 408)

A Producer produces a Product from a Resource for commercial purposes. ' They produced only half of the units after an injunction to follow the environmental policy.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Factory | Core | Factory identifies the particular plant where the Product is manufactured. 'Those machines were manufactured in the Miami plant.' |
| Producer | Core | The person or company that produces the Product. 'General Electric manufactures electronic appliances.' |
| Product | Core | The Product is produced by the Producer. 'The company manufactured T-shirts.' |
| Circumstances | Extra-Thematic | This FE identifies the Circumstances under which the the product was produced. 'They produced only half of the units after an injunction to follow the environmental policy.' |
| Consumer | Peripheral | The Producer produces the Product for the Consumer. 'The toys are made for children.' |
| Depictive | Extra-Thematic | A phrase that describes the state of the Producer or the Product during the manufacturing process. 'They manufactured the goods naked.' |
| Frequency | Extra-Thematic | The number of manufacturing events in a given time period. 'We produce 90 million units every month.' |
| Instrument | Peripheral | This FE identifies the Instrument with which a Producer produces a Product. 'Those lamps were made by machines.' |
| Locus | Extra-Thematic | The Locus is a description of the active zone of the Producer, where the manufacturing most saliently takes place. |
| Manner | Peripheral | This FE identifies the Manner in which a Producer creates a Product. 'Fine furniture is usually made slowly.' |
| Means | Peripheral | This FE identifies the Means by which a Producer creates a Product. 'Cars are manufactured by mass production.' |
| Place | Peripheral | This FE identifies the Place where the Product is manufactured. 'Those leather shoes were made in Italy.' |
| Purpose | Peripheral | This FE identifies the Purpose for which an Producer produces a Product. 'The company will produce more high-tech gadgets to meet the demand of the market.' |
| Resource | Peripheral | Resource is the material that the product is made from. 'Copal varnishes are manufactured from fossilised resins.' |
| Time | Peripheral | This Fe identifies the Time when the product was produced. 'Those cars were produced in 1997.' |

**Frame relations** (super → sub)

- Inheritance: Intentionally_create → Manufacturing
- Precedes: Product_development → Manufacturing
- Subframe: Product_development_scenario → Manufacturing

**Lexical units** (14): assembly line.n, fabricate.v, fabrication.n, industrial.a, make.v, maker.n, manufacture.n, manufacture.v, manufacturer.n, manufacturing.n, produce.v, producer.n, product.n, production.n

## Measurable_attributes  (frame id 965)

An Entity has a particular scalar Attribute with a value exceeding a contextually-specified or generally-understood standard. Except where there is a difference in FEs, we place all adjectives related to measurable quantities in this frame. Note that when an adjective appears with a quantity expression (e.g., 6 feet long), it belongs to the Dimension frame. 'That ladder is really tall.' 'After his back injury, he won't lift heavy boxes.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Degree | Core | A modifier expressing the deviation of the Value from the norm. |
| Entity | Core | The Entity for which a particular gradable Attribute is appropriate and under consideration. |
| Attribute | Core-Unexpressed | The feature of an Entity which is under discussion. |
| Circumstances | Extra-Thematic | Some specification of the circumstances under which the Entity has a particular Value for the Attribute. |
| Time | Extra-Thematic | The Time during which the Entity is in the state of having a particular Value for the Attribute. |
| Value | Core-Unexpressed | A quantity or other characterization of the Entity's state with respect to the Attribute. |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Measurable_attributes
- Inheritance: Measurable_attributes → Age
- Inheritance: Measurable_attributes → Duration_description
- Inheritance: Measurable_attributes → Location_of_light
- Inheritance: Measurable_attributes → Rate_description
- Inheritance: Measurable_attributes → Size
- Inheritance: Measurable_attributes → Sound_level
- Inheritance: Measurable_attributes → Speed_description
- Inheritance: Measurable_attributes → Temperature
- Inheritance: Measurable_attributes → Unemployment_rate
- Perspective_on: Measure_scenario → Measurable_attributes
- ReFraming_Mapping: Dimension → Measurable_attributes
- See_also: Measurable_attributes → Dimension
- Using: Measurable_attributes → Accuracy
- Using: Measurable_attributes → Extreme_value

**Lexical units** (13): big around.a, broad.a, deep.a, heavy.a, high.a, light [weight].a, long.a, low.a, narrow.a, short.a, tall.a, thick.a, thin.a

## Measure_duration  (frame id 224)

This frame contains (transparent ) nouns that are Units of measurement for time. The frame elements are Count, Unit and Process. 'The final total was 606, scored in only 10 hours of excellent batsmanship.' In this frame, we will NOT annotate deictic, calendric uses of nouns like week, month, etc. as in "next week, this month, in the 21st century".

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Count | Core | The number of Units of the measured entity.'The ads had been absorbed into her brain during many hours of television watching.' |
| Process | Core | The activity or state that takes place during the period of time under discussion.'He had to listen to almost two hours of complaints.' |
| Unit | Core | The standardized quantity in terms of which other quantities are measured.'Seven hours of torrential rain reduced the pitch to a lake.' |
| Agent | Extra-Thematic | The Agent either brings about or is the most involved in the Process. |

**Frame relations** (super → sub)

- Inheritance: Measures → Measure_duration
- Perspective_on: Duration_scenario → Measure_duration

**Lexical units** (14): a while.n, century.n, day.n, decade.n, fortnight.n, hour.n, millennium.n, minute.n, month.n, nanosecond.n, second.n, time.n, week.n, year.n

## Medical_professionals  (frame id 255)

This frame includes words that name medical professionals and is closely related to the Medical_specialties frame. The FE Type characterizing a Professional's sub-specialty may also be expressed. 'Ralph is a paediatrician.' 'Paediatric oncologists treat children with leukemia.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Professional | Core | This FE identifies the medical Professional. 'Paediatric oncologists treat children with leukemia.' |
| Affliction | Peripheral | The particular disorder that the medical Professional treats. Most words in the frame inherently indicate this information. 'Cardiac gerontologists can make more money in a year than I 'll see in my life !' |
| Age | Peripheral | The length of time the Professional has been alive. |
| Body_system | Peripheral | The part of the body that the medical Professional treats. This is usually indicated by the Lexical Unit itself. '' |
| Compensation | Peripheral | The payment that the Professional recieves for working. |
| Contract_basis | Peripheral | The Contract_basis describes the conditions of employment with respect to permanency, hours per time period, or payment basis. |
| Employer | Peripheral | The Employer gives compensation to the Professional for working. |
| Ethnicity | Peripheral | The Ethnicity is the religious, racial, national, socio-economic or cultural group to which the Professional belongs. |
| Origin | Peripheral | The Origin is the place where the Professional was born or lived a salient part of her or his life. |
| Place_of_employment | Peripheral | The place where the Professional works. |
| Rank | Peripheral | Rank is the position in a hierarchy that the Professional occupies within an organization. |
| Type | Peripheral | This FE identifies the Type of medical professional. 'Paediatric oncologists treat children with leukemia.' |

**Frame relations** (super → sub)

- Inheritance: People_by_vocation → Medical_professionals
- Using: Medical_interaction_scenario → Medical_professionals

**Lexical units** (37): allergist.n, anesthesiologist.n, cardiologist.n, chiropractor.n, dermatologist.n, doctor.n, endocrinologist.n, family practitioner.n, gastroenterologist.n, gerontologist.n, gynaecologist.n, homeopathist.n, immunologist.n, midwife.n, neonatologist.n, nephrologist.n, neurologist.n, nurse.n, obstetrician.n, oncologist.n, ophthalmologist.n, orthopaedist.n, pediatrician.n, physician.n, proctologist.n, psychiatrist.n, psychoanalyst.n, psychologist.n, psychotherapist.n, radiation oncologist.n, radiologist.n, rheumatologist.n, shaman.n, speech therapist.n, surgeon.n, therapist.n, urologist.n

## Membership  (frame id 1026)

A Member is semi-permanently part of a socially constructed Group. 'Victor is part of the Red Crescent'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Group | Core | A set of people standing in a semi-permanent relationship together. |
| Member | Core | The person who belongs to a Group. 'Two members of the Red Cross were here about a donation ' |
| Manner | Peripheral | Any description of the inclusion event which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). |
| Place | Peripheral | The location where the membership relationship holds. |
| Standing | Peripheral | An indication of the Member's status within the Group. 'Bill is a full member of the Elks.' |
| Time | Peripheral | The time at which the Member is a member of the Group. |

**Frame relations** (super → sub)

- Inchoative_of: Becoming_a_member → Membership
- Inheritance: Be_subset_of → Membership
- Using: Membership → Exclude_member
- Using: Membership → Member_of_military

**Lexical units** (6): associated.a, belong.v, member.n, membership [status].n, membership.n, part.n

## Morality_evaluation  (frame id 370)

In this frame an Evaluee is described by a (usually implicit) Judge with respect to the morality or rightness of his or her Behavior. 'That was very righteous of you to help him.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Behavior | Core | The assessment of the Evaluee is based on his or her Behavior. 'Accepting that money was immoral of Lindsay.' |
| Evaluee | Core | This is the person whose Behavior is being judged with respect to its morality. 'It was honorable of Jackie to give up the position.' |
| Expressor | Core | The Expressor is the body part or action by a body part which is the basis of the evaluation of morality. 'His face twisted into an evil grin' |
| Degree | Peripheral | The Degree to which the evaluation holds. |
| Judge | Peripheral | The individual whose point of view is taken in assigning the judgment denoted by the target. 'Timothy McVeigh was, in my opinion, an evil and horrible man.' |

**Frame relations** (super → sub)

- Inheritance: Social_behavior_evaluation → Morality_evaluation
- ReFraming_Mapping: Morality_evaluation → People_by_morality
- Using: Morality_evaluation → Legality
- Using: Morality_evaluation → Misdeed
- Using: Morality_evaluation → People_by_morality

**Lexical units** (39): bad.a, base.a, corrupt.a, dark.a, decent.a, degenerate.a, depraved.a, depravity.n, dishonorable.a, ethical.a, evil.a, felonious.a, foul.a, good.a, heinous.a, high-minded.a, honorable.a, immoral.a, improper.a, iniquitous.a, insidious.a, low-minded.a, low.a, miscreant.a, moral.a, nefarious.a, reprobate.a, right.a, righteous.a, sinful.a, stand-up.a, unethical.a, unscrupulous.a, upstanding.a, vile.a, villainous.a, virtuous.a, wicked.a, wrong.a

## Natural_features  (frame id 191)

The Locale is a geographical location as defined by shape. This frame includes natural geographic features, including land/ice forms and bodies of water. ' We climbed up the rock cliff.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Locale | Core | A stable bounded area. It is typically the designation of the nouns of Locale-derived frames. |
| Constituent_parts | Peripheral | Salient parts of the Locale. 'We drove through a mossy dell.' |
| Container_possessor | Extra-Thematic | The location that the Locale is a part of. 'John spent several years wandering the mountains of Romania.' |
| Descriptor | Extra-Thematic | Any description, characteristic, or property of the Locale which is not covered by more specific FEs. 'That 's a long way down on such a steep cliff.' |
| Formational_cause | Extra-Thematic | Indicates the action (or causer) which brings the features of the Locale about. ' There is a glacial valley near here.'' There is a impact valley near here.' |
| Name | Extra-Thematic | This FE is used for the Names of Locales. 'Lake Constance' 'Pike's Peak' 'The Indonesian archipelago' |
| Relative_location | Peripheral | A place that a Locale is located with respect to. 'All the mountains in America are small.' |
| Type | Extra-Thematic | The Type is the subtype of natural feature. |

**Frame relations** (super → sub)

- Inheritance: Locale → Natural_features
- Inheritance: Natural_features → Relational_natural_features

**Lexical units** (115): archipelago.n, atoll.n, bar.n, bay.n, bayou.n, beach.n, beck.n, berg.n, brook.n, burn.n, butte.n, canyon.n, cascade.n, cataract.n, cave.n, cavern.n, cay.n, channel.n, cirque.n, cliff.n, clough.n, coastal.a, continent.n, continental.a, coombe.n, cordillera.n, corrie.n, cove.n, crag.n, crater.n, creek.n, crevasse.n, dale.n, declivity.n, defile.n, dell.n, depression.n, dingle.n, dune.n, eyot.n, falls.n, fell.n, fjord.n, floe.n, gap.n, glacier.n, glen.n, graben.n, gulch.n, gulf.n, gully.n, guyot.n, headland.n, height.n, hill.n, hillock.n, hollow.n, hummock.n, iceberg.n, inlet.n, island.n, isle.n, islet.n, isthmus.n, key.n, knoll.n, lagoon.n, lake.n, land.n, loch.n, massif.n, mesa.n, moraine.n, mount.n, mountain.n, ocean.n, outcrop.n, pass.n, peak.n, peninsula.n, plateau.n, pond.n, pool.n, range [grazing].n, range.n, rapids.n, ravine.n, reef.n, ridge.n, rill.n, river.n, rugged.a, sandbank.n, sandbar.n, sandspit.n, sea.n, seamount.n, shelf.n, shoal.n, skerry.n, slough.n, sound.n, spring.n, strait.n, strand.n, stream.n, tarn.n, tor.n, vale.n, valley.n, volcano.n, wash.n, water.n, waterfall.n, watershed.n

## Needing  (frame id 1375)

The speaker believes that some state of affairs or entity (the Requirement) must be present in order to cause some other dependent state of affairs to occur (the Dependent). In the typical case, the Cognizer desires the occurrence of the Dependent and so also desires the obtainment or occurrence of the Requirement. 'I need one more bolt. DNI' 'I need one more nail to finish building the cabinet.' 'In order to complete the treaty, the United States will require several more diplomats.' 'He needs everyone to leave his office to finish his work.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The Cognizer requires or believes he/she requires the Requirement to hold so that the Dependent will occur. |
| Consequences | Core | An undesirable state-of-affairs that results if the Requirement is not met. 'He needs to focus on his schoolwork, or he's not going to pass the third grade.' |
| Dependent | Core | The state-of-affairs which cannot hold without the Requirement. |
| Requirement | Core | The entity or state-of-affairs that must be present or obtain in order for the Dependent to obtain. |
| Circumstances | Extra-Thematic | Some specification of the conditions under which the Requirement is likely to be needed. |
| Degree | Peripheral | The extent to which the Dependent depends on the presence of the Requirement. |
| Explanation | Extra-Thematic | The reason why the Cognizer needs the Requirement. |
| Frequency | Extra-Thematic | This frame element is defined as the number of times the Cognizer has a need per some unit of time. |
| Iterations | Extra-Thematic | The frame element Iterations is used for expressions that indicate the number of times an event or state (of the kind denoted by the target in its clause) has taken place or held. |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. |
| Place | Peripheral | The location of the Cognizer when he/she requires the Requirement. 'Over at Merv's house they need three more cement trucks to finish the job.' |
| Time | Peripheral | The Time at which the Cognizer requires the Requirement. 'I need that book now!' |

**Frame relations** (super → sub)

- Using: Desiring → Needing
- Using: Have_as_requirement → Needing
- Using: Needing → Reliance

**Lexical units** (3): need.n, need.v, require.v

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

## Notification_of_charges  (frame id 129)

The judge or other court officer (the Authority) informs the Accused of the Charges against him/her, i.e. the alleged actions and the relevant laws. '' 'The board has been accused by the federal court of making decisions based on narrow agendas and meddling where it shouldn't.' 'The police charged a young nurse with four murders.' Compare to: Citing.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Accused | Core | The person being charged with an offense against the law. |
| Arraign_authority | Core | The judge or other authority of the court in which the accused person is arraigned. |
| Charges | Core | The crime with which the Accused is charged |
| Containing_event | Extra-Thematic | The larger event which contains the Notification of Charges event. 'Seven people have been indicted in the seven-year investigation.' |
| Place | Peripheral | Where the event takes place. |
| Time | Peripheral | When the event occurs. |

**Frame relations** (super → sub)

- Precedes: Notification_of_charges → Entering_of_plea
- See_also: Citing → Notification_of_charges
- Subframe: Arraignment → Notification_of_charges
- Using: Communication → Notification_of_charges

**Lexical units** (5): accuse.v, charge.n, charge.v, indict.v, indictment.n

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

## Offering  (frame id 2239)

An Offerer indicates that he or she is able and willing to give a Theme to a Potential_recipient. In the absence of further qualifications, it is often understood that the Potential_recipient accepts the Theme. 'The host graciously offered us food and drink.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Offerer | Core | The person that begins in possession of the Theme and offers it to the Potential_recipient . |
| Potential_recipient | Core | The entity that ends up in possession of the Theme. |
| Theme | Core | The object which is offered for transfer. |
| Circumstances | Extra-Thematic | The Circumstances are the conditions under which the Theme is offered. 'I offer my services free of charge.' |
| Depictive | Extra-Thematic | A description of the Offerer, Potential_recipient, or Theme given independently of the giving event per se. |
| Explanation | Extra-Thematic | The Explanation for which the Offerer offers the Theme to the Potential_recipient. |
| Imposed_purpose | Extra-Thematic | The Potential_recipient's intended purpose for the Theme. 'Plesae offer a list of people for potential promotion.' |
| Manner | Peripheral | The Manner is the manner in which the Offerer offers the Theme to the Potential_recipient. |
| Means | Peripheral | The Means by which the Offerer offers the Theme to the Potential_recipient. |
| Period_of_iterations | Extra-Thematic | The length of time from when the offer began to be repeated to when it stopped. |
| Place | Peripheral | The Place where the Offerer offers the Theme to the Potential_recipient. |
| Purpose | Peripheral | The Purpose for which the Offerer offers the Theme to the Potential_recipient. |
| Time | Peripheral | The Time is when the Offerer offers the Theme to the Potential_recipient. |

**Frame relations** (super → sub)

- Using: Giving → Offering

**Lexical units** (4): extend.v, offer.v, proffer.v, serve.v

## Operational_testing  (frame id 1301)

A Tester uses a concrete or conceptual Product in order to determine either whether it works or to find out how well or in which manner it works. The Tester may have particular Unwanted_characteristics in mind that they are specifically looking for. The operational test may also be carried out under a particular set of Circumstances that are typically relevant to the functioning of the Product. 'Sun has (hopefully) already tested it for compliance.' 'The Velcro hook and loop closure system has been tested under wet conditions and retains its holding power after 10,000 open and close functions. CNI INI' 'Roe revisited the compound and tested it as a mosquito repellent.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Desired_state_of_affairs | Core | The desirable state of affairs which the Tester hopes to find to obtain when using the Product. 'Test-Driven Development requires you to set an expectation of a result and then test that the result is achieved.' |
| Product | Core | The entity that the Tester uses to ascertain whether it is intact. |
| Purpose | Core | An action that the Tester intends to accomplish subjecting the Product to a test of its functioning. 'Once you have copied your site and have tested it to make sure it works normally, you're ready to pull out the … |
| Tested_property | Core | A variable of behavior of the Product which is specifically evaluated. ' ILCSO staff have tested the behavior of the ILCSO-standard version of WebVoyage with several browsers.' |
| Tester | Core | The person who uses the Product to see if it is intact or to ascertain its characteristics during operation. 'I just wish we could have tested the car with a manual gearbox, instead of the five-speed automatic' |
| Unwanted_characteristics | Core | An entity or property whose presence would impair the acceptability or usefulness of the Product. 'To ensure that the remedy is complete, nCipher have fully reviewed the software and tested it for similar errors.' |
| Circumstances | Extra-Thematic | The FE Circumstances is used for circumstances that obtain during the test procedure. These are typically relevant to how the Product functions. 'We tested the drive using the generic drivers of the OS.' |
| Degree | Peripheral | This FE identifies the extent to which the Tester examines the Product. |
| Duration | Peripheral | The length of the time period during which the Tester continuously or repeatedly operates the Product to determine its operational characteristics. 'Before launching BioCheck, we tested the system for a year in … |
| Function | Peripheral | A use to which the Product is put . 'If you have HTML files from another source and you can't first read them into Microsoft Word, you can try the process, but I haven't tested it for that use. ' |
| Location_of_protagonist | Extra-Thematic | This FE is the position of the Tester during the act of testing. Typically, it is expressed in a from-PP. |
| Manner | Peripheral | This FE identifies the Manner in which the Tester uses the Product in order to evaluate its functioning. 'Engineers carefully tested the fields of view to make sure that security personnel would be able to view all … |
| Means | Peripheral | This FE is used for a Means action which the Tester carries out in testing the Product. 'How we tested the Radeon 9700 Pro video-card.' |
| Period_of_iterations | Extra-Thematic | The length of time from when the testing event began to be repeated to when it stopped. 'This approach has been tested since 2001.' |
| Place | Peripheral | The location in which the test is carried out. 'We tested the product in California first.' |
| Result | Extra-Thematic | The Result of the Operational_testing. |
| Time | Peripheral | The Time when the Tester uses the Product to evaluate its functioning. |

**Frame relations** (super → sub)

- Using: Operating_a_system → Operational_testing

**Lexical units** (10): crash-test.v, flight test.n, flight test.v, flight-test.v, flight-testing.n, test.n, test.v, testing.n, trial.n, try out.v

## Opinion  (frame id 1412)

A Cognizer holds a particular Opinion, which may be portrayed as being about a particular Topic. 'John thinks that it looks better back .' 'Well, my opinion about that is none of your business. ' 'What 's your take on the recent oil crisis ?' 'Your view of Smithers as an excellent secretary is not shared by the rest of the UN.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The Cognizer is the person whose Opinion is in question. 'My take is that Johnson will not actually make it to the last round .' 'Everyone is entitled to their opinion .' |
| Opinion | Core | The Cognizer's way of thinking, which is not necessarily generally accepted, and which is generally dependent on the Cognizer's point of view. 'My take is that it is a version of the Macbeth story - what happens when … |
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Constancy | Peripheral | The level of firmness with which the Cognizer holds an opinion. It refers to the amount of convincing that they would need to change their mind. 'I really think that you should reconsider.' |
| Domain | Extra-Thematic | The aspects of the Opinion (and its Topic, if any) which are under consideration. 'We seemed to have two quite different moral views about this situation.' 'Noone could take seriously Dr. Furst's ill-advised medical … |
| Evidence | Extra-Thematic | The events or states-of-affairs that form the basis for the Cognizer's Opinion. 'From what I've seen so far, my opinion is that it won't really matter.' |
| Manner | Peripheral | Any description of how the Cognizer holds an opinion which is not covered by more specific FEs, including secondary effects (quiet(ly)), and general descriptions comparing events (the same way). In addition, it may … |
| Role | Extra-Thematic | Role describes the presuppositional terms of the Opinion by placing the Topic or the Cognizer of the Opinion into a category. 'My opinion of her as a brother isn't important anymore.' 'Your take on it as a political … |
| Time | Peripheral | The Time at which the Cognizer has the Opinion. |
| Topic | Extra-Thematic | A phenomenon that the Cognizer is considering with respect to their Opinion. Note that this extra-thematic frame element occurs freely with nouns, but only in very restricted contexts with verbs. 'My opinion about that … |

**Frame relations** (super → sub)

- ReFraming_Mapping: Awareness → Opinion
- See_also: Awareness → Opinion
- Using: Opinion → Be_in_agreement_on_assessment
- Using: Opinion → Taking_sides

**Lexical units** (15): belief.n, believe.v, believer.n, expect.v, feel.v, figure.v, hold.v, opinion.n, sense.n, subscribe.v, subscriber.n, suppose.v, take.n, think.v, view.n

## Part_ordered_segments  (frame id 331)

In this frame a Part is part of a larger Whole comprised of parts that are ordered. The Parts can be ordered temporally (first to last and vice versa) or vertically (down to up and vice versa). The Part can be modified by the Part_prop or the number of the part can be given by Ordinality. '' ' I sat through the first interminable act of the play . ' ' Tess finished a dissertation chapter . ' 'The first level of rock consisted of sediment from the Neolithic period.' 'The last layer of sediment was also the thickest.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Ordinality | Core | This is the number of the sequence of Parts.' I sat through the first interminable act of the play . ' |
| Part | Core | A part of a larger Whole. ' I sat through the first interminable act of the play . ' |
| Whole | Core | An undivided entity having all its Parts. ' I sat through the first interminable act of the play . ' |
| Part_prop | Peripheral | A property relating to the Part of a Whole. ' I sat through the first interminable act of the play . ' |

**Frame relations** (super → sub)

- Inheritance: Part_whole → Part_ordered_segments

**Lexical units** (6): act.n, book.n, chapter.n, inning.n, layer.n, level.n

## Part_whole  (frame id 140)

This frame is concerned with nouns denoting a part or parts of a Whole entity . The Part is not defined relative to the Whole's orientation, center, or edge and is not ordered. We also annotate properties of the Part, e.g. relating to its size. 'Kim forgot a large part of the story.' 'Abby ate only the top half of the cake.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Part | Core | A Part of a larger Whole.'Sergey had half of the pizza for breakfast.' |
| Whole | Core | An undivided entity having all its Parts. 'Sergey had half of the pizza for breakfast.' |
| Name | Extra-Thematic | A label applied to a Part of a Whole in order to identify the Part within some System. |
| Orientation | Extra-Thematic | This is a property of the Part that determines the portion of the Part. 'Abby ate only the top half of the cake . ' |
| Part_prop | Extra-Thematic | A property relating to the Part of a Whole.'Sue painted a big section of the room.' |
| System | Extra-Thematic | A system of organization of the Parts within the Whole, of which a Part is identified with a Name . |

**Frame relations** (super → sub)

- Inheritance: Part_piece → Part_whole
- Inheritance: Part_whole → Part_edge
- Inheritance: Part_whole → Part_inner_outer
- Inheritance: Part_whole → Part_ordered_segments
- Inheritance: Part_whole → Part_orientational
- Inheritance: Part_whole → Rest
- Inheritance: Part_whole → Shaped_part
- Inheritance: Part_whole → Temporary_group
- Inheritance: Part_whole → Vehicle_subpart
- Using: Part_whole → Completeness
- Using: Part_whole → Inclusion

**Lexical units** (13): development.n, eighth.n, fifth.n, fragment.n, half.n, hundredth.n, part.n, portion.n, quarter.n, section.n, segment.n, tenth.n, third.n

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

## People_by_religion  (frame id 1021)

This frame contains words for individuals, i.e. humans, with respect to their Religion. The Religion is generally incorporated, but with some lexical units it is specified separately. 'The bells call the faithful to evensong DNI' 'A 90-year-old Baptist claims to have seen God personally in his backyard.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Person | Core | The Person is the human being. |
| Religion | Core | The religious belief system that the Person follows. |
| Age | Peripheral | The Age is the length of time the Person has been alive. |
| Descriptor | Peripheral | The Descriptor is a temporary condition of the Person. |
| Ethnicity | Peripheral | The Ethnicity is the racial, national, socio-economic or cultural group to which the Person belongs. |
| Origin | Peripheral | The Origin is the place where the Person was born or lived a salient part of her or his life. |
| Persistent_characteristic | Peripheral | The Persistent_characteristic is a physiological characteristic or personality trait of the Person which is conceived of as persisting over time. |

**Frame relations** (super → sub)

- Inheritance: People → People_by_religion
- Using: Religious_belief → People_by_religion

**Lexical units** (10): baptist.n, buddhist.n, christian.n, faithful.n, infidel.n, jew.n, mormon.n, muslim.n, pagan.n, zealot.n

## Perception_experience  (frame id 70)

This frame contains perception words whose Perceivers have perceptual experiences that they do not necessarily intend to. For this reason we call the Perceiver role Perceiver_passive. Comparing the Perception_experience frame to the Perception_active frame, we note that for some modalities there are different lexical items in each frame. For instance, whereas Perception_experience has see, Perception_active has look at. For other sense modalities, we find the same lexical items in both frames. To illustrate, consider the verb smell where I smell something rotten exemplifies its Perception_experience use and Smell this to see if it's fresh exemplifies its Perception_active sense. This frame also includes words which are not specific to any sense modality, including detect, perceive, perception, sense. '' 'Abashed, realising that he had overheard her conversation with Victoria, Sheeley didn't try to make excuses.' 'She smelled the wine on Paul's breath, and bade him to sit down.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Body_part | Core | The Body_part is the location on the Perceiver_passive's body where the perceptual experience takes place. It is typically expressed in a PP. 'Marlow felt something cold and hard against the back of his neck.' This … |
| Perceiver_passive | Core | This FE is the being who has a perceptual experience, not necessarily on purpose. It is typically expressed as an External Argument. 'The waiter smelled something foul in the kitchen.' |
| Phenomenon | Core | This FE is the entity or phenomenon that the perceiver experiences with his or her senses. It is typically expressed as Object with verbs. 'The waiter smelled something foul in the kitchen.' 'I saw the baker prepare … |
| Circumstances | Extra-Thematic | A situation which pertains during the event. This frame element is primarily used to highlight the event denoted by the target against a (potentially partially) causal or concessive background state-of-affairs. |
| Concessive | Extra-Thematic | This FE signifies that the state-of-affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state-of-affairs would be expected given the state-of-affairs in the … |
| Contrastive_context | Extra-Thematic | An element of the discourse that serves to contextualize the Phenomenon, with which it is directly related (i.e. filling a frame-element role of the Phenomenon or vice-versa). It contrasts with other contextually … |
| Degree | Peripheral | The Degree indicates the degree to which the Perception is experienced. 'A nightmare creature, barely perceived in the swirling dense smoke, was beating at the flames coming from its own body.' 'Older people perceive … |
| Depictive | Extra-Thematic | The State indicates predicate expressions that apply to the Phenomenon, providing some information about the state it is in while the Perceiver_passive experiences it. 'The detective saw the suspect fleeing.' 'Pat saw … |
| Direction | Peripheral | This frame element is used for all path-like expressions, except those indicating the location of the perceiver (see above), that describe how the perceiver's attention is directed during the act of perception. 'The … |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of a continuous situation (the one denoted by the target) to its end. |
| Frequency | Extra-Thematic | An expression of how often the event occurs. |
| Ground | Peripheral | The Ground is the perceptual background against which the Phenomenon is experienced (or not experienced) by the Perceiver_passive. It can be distinguished from locative postnominal modifiers of the Phenomenon in … |
| Location_of_protagonist | Extra-Thematic | This FE identifies the Location_of_protagonist during the perceptual experience. It is typically expressed in a from-PP. 'The witnesses saw the robbery from the their car.' |
| Manner | Peripheral | Manner expressions may be of lexicographic interest if they describe properties of perception as such: clearly, loudly, etc. 'Pat heard the shot clearly.' |
| Means | Peripheral | The action whereby the Perceiver perceives. 'He saw it by looking out the window.' |
| Obscuring_medium | Peripheral | The Obscuring_medium is the medium through which the Phenomenon makes itself perceivable to the Perceiver_passive. This is similar to the Direction, but occurs in the opposite direction and implies a movement of the … |
| Place | Peripheral | The general location within which the act of perception takes place. |
| State | Peripheral | State is the location, activity, or other characteristic of the Phenomenon. 'I saw the baker baking his special peanut butter pie'. 'I overheard the cat in the cupboard'. 'I heard fear in his voice'. |
| Time | Peripheral | The Time at which the Perceiver_passive or the Body_part perceives the Phenomenon. |

**Frame relations** (super → sub)

- Causative_of: Cause_to_perceive → Perception_experience
- Inheritance: Perception → Perception_experience
- Inheritance: Perception_experience → Punctual_perception
- ReFraming_Mapping: Hearsay → Perception_experience
- See_also: Perception_active → Perception_experience
- Using: Perception_experience → Eclipse
- Using: Perception_experience → Perception_body

**Lexical units** (13): detect.v, experience.n, experience.v, feel.v, hear.v, overhear.v, perceive.v, perception.n, see.v, sense.v, smell.v, taste.v, witness.v

## Placing  (frame id 62)

Generally without overall (translational) motion, an Agent places a Theme at a location, the Goal, which is profiled. In this frame, the Theme is under the control of the Agent/Cause at the time of its arrival at the Goal. 'David placed his briefcase on the floor.' This frame differs from Filling in that it focuses on the Theme rather than the effect on the Goal entity. It differs from Removing in focusing on the Goal rather than the Source of motion for the Theme.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the person (or other force) that causes the Theme to move. 'The waiter placed the food on the table.' |
| Cause | Core | 'Grass , which is sown with clover , provides rich pasture for cattle in summer and the clover is another plant which puts nitrogen into the soil .' |
| Goal | Core | The FE Goal is the location where the Theme ends up. This FE is profiled by words in this frame. 'The waiter placed the food on the table.' |
| Theme | Core | The Theme is the object that changes location during the Placing. 'The waiter placed the food on the table.' |
| Area | Peripheral | The Area is the setting into which the Theme is placed. 'She emptied a wash basket full of towels and deposited them around the house.' |
| Beneficiary | Extra-Thematic | This extrathematic FE applies to participants that derive a benefit from the occurrence of the event specified by the target predicate. Further, the target predicate should involve some sort of Agent that intends that … |
| Cotheme | Extra-Thematic | This is the second moving object, expressed as a direct object or an oblique. 'Pat lay the trophy on the mantle along with her portrait. ' |
| Degree | Extra-Thematic | The Degree indicates the degree to which the placing occurs. |
| Depictive | Extra-Thematic | This FE identifies any Depictive phrase describing the Agent or Theme of the placing. 'I put the dishes into the cabinet unwashed.' |
| Distance | Peripheral | This FE is any expression which characterizes the extent of motion. 'I plunged my hands wrist deep in the fragrant herbs and rubbed the dry fragments between the fingertips' |
| Duration | Extra-Thematic | The Duration is the amount of time for which the Theme is to stay in the Goal location. 'If you place it there for extended periods, your monitor may suffer permanent damage.' |
| Explanation | Extra-Thematic | The Explanation indicates why the Placing occurs. |
| Manner | Peripheral | Any expression which describes a property of the placing action which is not directly related to the trajectory of the Theme's motion expresses the frame element Manner. Descriptions of speed, steadiness, grace, means … |
| Means | Peripheral | The Means is an act whereby the Agent achieves the placing of the Theme. 'The Egyptians set it in place by simple levering.' |
| Path | Peripheral | Any description of a trajectory of motion which is neither a Source nor a Goal expresses the frame element Path. In this frame, Path expressions almost always have a via-sense. 'The mail carrier stuck the letters … |
| Place | Peripheral | The Place indicates where the Placing occurs. |
| Purpose | Extra-Thematic | An action that the Agent intends to accomplish by perform the placing action. 'They put the vase in a box to protect it during transportation.' |
| Result | Extra-Thematic | This FE identifies the Result of the Placing. |
| Source | Peripheral | The Source is the initial location of the Theme, before it changes location. 'Her mother shelved the cans from the countertop.' |
| Speed | Peripheral | The Speed is the rate at which Placing occurs. 'Smithers put his book down quickly and turned around.' |
| Time | Peripheral | Time is when the Placing occurs 'Smithers had placed the table there the night before.' |

**Frame relations** (super → sub)

- Inheritance: Placing → Burying
- Inheritance: Placing → Dispersal
- Inheritance: Transitive_action → Placing
- Perspective_on: Placing_scenario → Placing
- Precedes: Removing → Placing
- ReFraming_Mapping: Placing → Arranging
- ReFraming_Mapping: Placing → Assigned_location
- ReFraming_Mapping: Placing → Attaching
- ReFraming_Mapping: Placing → Bringing
- ReFraming_Mapping: Placing → Cause_fluidic_motion
- ReFraming_Mapping: Placing → Dispersal
- ReFraming_Mapping: Placing → Planting
- See_also: Cause_motion → Placing
- See_also: Placing → Filling
- See_also: Placing → Removing
- Subframe: Cause_motion → Placing
- Using: Motion → Placing
- Using: Placing → Arranging
- Using: Placing → Dressing
- Using: Placing → Dunking
- Using: Placing → Installing
- Using: Placing → Storing

**Lexical units** (69): archive.v, arrange.v, bag.v, bestow.v, billet.v, bin.v, bottle.v, box.v, brush.v, cage.v, cram.v, crate.v, dab.v, daub.v, deposit.v, drape.v, drizzle.v, dust.v, embed.v, emplace.v, enclose.v, file.v, gag.v, garage.v, hang.v, heap.v, immerse.v, implant.v, implanted.a, inject.v, insert.v, insertion.n, jam.v, lay.v, lean.v, load.v, lodge.v, pack.v, package.v, park.v, perch.v, pile.v, place.v, placement.n, plant.v, plunge.v, pocket.v, position.v, pot.v, put.v, rest.v, rub.v, set.v, sheathe.v, shelve.v, shoulder.v, shower.v, sit.v, situate.v, smear.v, stable.v, stand.v, stash.v, stick.v, stow.v, stuff.v, tuck.v, warehouse.v, wrap.v

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

## Position_on_a_scale  (frame id 95)

This frame contains words that describe an Item's static position on a scale with respect to some property Variable. '' 'Dried fruits are especially high in fibre, as are pulses.' 'Despite the fact that the local land was rich in silver, by 1865 most of the mining traffic through Las Vegas was of propectors headed to California or Northern Nevada in search of gold.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Item | Core | Item identifies the entity whose scalar property is specified. 'Bacon is high in fat.' |
| Variable | Core | Variable is the scalar property that the Item possesses. Soda is high in sugar. |
| Degree | Peripheral | This FE identifies the Degree to which the scalar property of an Item holds with respect to some Variable. 'Bacon is very high in fat.' |
| Domain | Peripheral | Domain describes the set of Items for which the Variable 's position is determined. 'Interest rates are high in West Germany.' |
| Value | Core-Unexpressed | The Value is the position or range of positions on the scale that the Item occupies. This is normally implicit in the LU. 'This car is high in price.' |

**Frame relations** (super → sub)

- Inchoative_of: Change_position_on_a_scale → Position_on_a_scale
- Inheritance: Gradable_attributes → Position_on_a_scale
- Inheritance: Position_on_a_scale → Evaluative_comparison
- Inheritance: Position_on_a_scale → Sufficiency
- Inheritance: Position_on_a_scale → Surpassing
- Inheritance: Position_on_a_scale → Used_up
- ReFraming_Mapping: Position_on_a_scale → Delimitation_of_diversity
- Using: Position_on_a_scale → Delimitation_of_diversity
- Using: Position_on_a_scale → Probability

**Lexical units** (10): advanced.a, deficient.a, high.a, lacking.a, low.a, medium.a, moderate.a, poor.a, rich.a, through the roof.adv

## Possession  (frame id 118)

An Owner has (or lacks) a Possession. '' 'The river's part of my manor, but of course it also belongs to the River Police.' 'It's a nuisance having to abandon my belongings, though.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Owner | Core | The entity that owns a posession. |
| Possession | Core | The thing which is owned by the Owner. Ex.: I have twenty bucks. (This does not include bodyparts or medical conditions, but does include intellectual property, etc.) |
| Depictive | Extra-Thematic | State of the Owner or Possession. |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of a continuous situation (the one denoted by the target) to its end. In many cases, the continuous situation is a dynamic action which is ongoing, while in others … |
| Explanation | Extra-Thematic | The reason for which the Owner has the Possession. |
| Manner | Peripheral | The way that the Owner possesses the Possession. |
| Time | Peripheral | This FE indicates the Time interval during which the Owner has a possession. |

**Frame relations** (super → sub)

- Inchoative_of: Getting → Possession
- Inheritance: Possession → Post_getting
- Inheritance: Possession → Post_lose_possession
- Inheritance: Possession → Post_transfer
- Inheritance: Possession → Pre_getting
- Inheritance: Possession → Pre_lose_possession
- Inheritance: Possession → Pre_transfer
- Inheritance: Possession → Retaining
- Using: Possession → Capital_stock
- Using: Possession → Change_of_quantity_of_possession
- Using: Possession → Locale_by_ownership
- Using: Possession → Prevent_or_allow_possession
- Using: Possession → Sacrificing_for
- Using: Possession → Wealthiness

**Lexical units** (23): assets.n, belong.v, belongings.n, custody.n, effects.n, got.v, have got.v, have.v, lack.n, lack.v, lacking.a, own.v, owner.n, ownership.n, possess.v, possession [definite noun].n, possession [of goods].n, possession.n, possessor.n, property.n, want.n, want.v, wanting.a

## Possibility  (frame id 2120)

A Possible_event is deemed to have all pre-conditions satisfied; in other words, it has some probability of occurrence, if some (generally implicit) further Condition pertains. The Condition, whether overt or implicit, often concerns the decision of an agent to attempt to bring the Possible_event about. The primary implication is that certain other aspects of the situation that might have been expected to prevent the Possible_event, usually lack of capability or permission, do not pertain. 'You ca n't burn glass . INI' 'You can have two more if you want .' 'This sense of lack can never be satisfied .' 'We just ca n't stand it anymore . INI' This frame is confusable with the Capability frame, which specifically involves an Agent who is presented as needing only the decision to perform an Action in order to successfully perform the Action.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Circumstances | Extra-Thematic | The Circumstances under which the preconditions of the Possible_event are met. 'In this weather, an experienced pilot can still manage to fly 500 miles.' |
| Condition | Core-Unexpressed | The state-of-affairs that does not hold, but if it did, the Possible_event would occur. 'If he wants , he can have all the fishsticks .' |
| Explanation | Extra-Thematic | An entity, event, or state that brings about the possibility of the Possible_event. |
| Possible_event | Core-Unexpressed | The Possible_event has met its preconditions, and will occur if some further Condition holds. |
| Time | Peripheral | The time at which the Possible_event can occur. 'You can come in now.' |

**Frame relations** (super → sub)

- Inheritance: Possibility → Capability
- See_also: Possibility → Capability

**Lexical units** (4): can.v, could.v, may.v, might.v

## Posture  (frame id 18)

An Agent supports their body in a particular Location. The LUs of the frame convey which body part is the Point_of_contact where the Agent is supported, what orientation the body is in, and some overall arrangement of the limbs (especially the legs) and the torso. 'He knelt down, hand on heart .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the individual whose body is in a particular posture. The Agent FE is generally expressed as the external argument of verbs: 'Kim was kneeling by the window.' |
| Location | Core | A description of the position of the Agent. The Location of the Agent is frequently expressed and generally occurs as a PP Complement: 'Kim was kneeling by the window.' |
| Point_of_contact | Core | The part of the body that provides support to the Agent's body in the posture. 'I stood on my heels and looked out the window' |
| Degree | Peripheral | Degree to which event occurs |
| Dependent_state | Extra-Thematic | A state of the Agent which crucially depends on their posture. 'She sat upright' |
| Depictive | Extra-Thematic | The Agent's state throughout the time they are in a particular posture. |
| Duration | Peripheral | The length of time for which the Agent holds the posture. ' I could have stood there all afternoon' |
| Manner | Peripheral | Any description of the event which is not covered by more specific FEs, including secondary effects (quietly, loudly), and general descriptions comparing events (the same way). In addition, it may indicate salient … |
| Purpose | Extra-Thematic | The Purpose for which the Agent holds the posture. ' Joel sat on the porch to watch the traffic go by' |
| Time | Peripheral | This FE indicates the Time interval during which the Agent held a certain posture. ' Yesterday evening he was sitting in his armchair as usual' |

**Frame relations** (super → sub)

- Causative_of: Change_posture → Posture
- Inheritance: State → Posture
- ReFraming_Mapping: Posture → Change_posture

**Lexical units** (25): bend.v, bent.a, cower.v, crouch.v, crouched.a, huddle.v, huddled.a, hunch.v, hunched.a, kneel.v, lean.v, lie.v, position.n, posture.n, seated.a, shrink.v, sit.v, slouch.v, slouched.a, sprawl.v, sprawled.a, squat.v, stance.n, stand.v, stoop.v

## Precariousness  (frame id 2703)

A Theme has the potential of falling from its current Location, which would likely result in damage. 'Now, balanced easily and firmly, he stood on the ledge outside in the slight, chill breeze.' 'A ball will sit there perfectly balanced on a jet of water (or air).' ' Joey teetered into him sometimes, losing his balance from extreme exhaustion. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Theme | Core | A valuable entity which might fall and be damaged. |
| Dangerous_entity | Core-Unexpressed | An entity which may cause the Theme to fall. |
| Degree | Peripheral | A modifier expressing the deviation of the actual level of precariousness from the expected value given the Theme and the state indicated by the target itself. |
| Depictive | Extra-Thematic | This FE describes the Theme as being in some state during the action. |
| Domain | Extra-Thematic | The Domain in which the Theme has a degree of precariousness. Usable only in metaphorical sentences. |
| Duration | Extra-Thematic | Duration denotes the length of time from the beginning of a continuous situation (the one denoted by the target) to its end. In many cases, the continuous situation is a dynamic action which is ongoing, while in others … |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the state of precariousness of the Theme logically follows. |
| Falling_event | Core-Unexpressed | The event of falling, incorporated in the LUs of this frame. |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. A Frequency expression answers the question how often. |
| Location | Peripheral | The location where the Theme is supported. |
| Manner | Extra-Thematic | Any description of the holistic properties of the balancing situation. |
| Place | Peripheral | A particular location in which the Theme is at risk of falling. Frequently, it is to be inferred that the characteristics of the location put the Theme in danger. |
| Result | Extra-Thematic | An event or state that results from the instability of the Theme. |
| Situation | Extra-Thematic | The Situation under which the Theme is safe or unsafe from falling. Most expressions of Time and Place also express the Situation and should be labeled as such on the 2nd FE layer. |
| Time | Peripheral | The time period during which the Theme is in danger of falling. |

**Frame relations** (super → sub)

- Inheritance: Being_at_risk → Precariousness
- Using: Motion_directional → Precariousness

**Lexical units** (8): balanced.a, instability.n, stability.n, stable.a, steady.a, teeter.v, unstable.a, unsteady.a

## Predicament  (frame id 300)

An Experiencer is in an undesirable Situation, whose Explanation may also be expressed. 'The insurers ended up in the bind of having to pay 15 years' taxes.' 'He was in a bit of a pickle and make no mistake!' 'What a mess we 're in now!'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Experiencer | Core | The Experiencer is in an undesirable Situation. 'The insurers ended up in a bind.' |
| Situation | Core | This FE identifies the undesirable Situation the Experiencer is in. 'They found themselves in a quite a fix.' 'The company was definitely in dire straits from the dollar's inflation.' |
| Domain | Extra-Thematic | The Domain in which the Experiencer has the problem. |
| Explanation | Extra-Thematic | This FE identifies the Explanation of the Situation. 'We 're in this mess from paying too little attention to quality control.' |
| Place | Peripheral | The location where the Situation occurs. 'The trouble in America is only going to get worse.' |
| Time | Peripheral | Thiis FE identifies the Time when the Situation is in effect. 'Yesterday's predicament was a little too exciting.' |

**Frame relations** (super → sub)

- Inheritance: State_of_entity → Predicament
- Using: Emotions → Predicament

**Lexical units** (12): bind.n, fix.n, jam.n, mess.n, misfortune.n, pickle.n, pinch.n, plight.n, predicament.n, problem.n, scrape.n, trouble.n

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

## Preventing_or_letting  (frame id 516)

A Potential_hindrance or an Agent (via their actions) keeps an Event from taking place, or despite the possibility of prevent the Event, do not do so. Lexical units which indicate that the event is not prevented, e.g. allow.v, are marked with the semantic type "Negative". Some lexical units, like avert and avoid indicate that the Potential_hindrance or Agent would have been affected if the Event occurred. ' Rain prevented the ball game from taking place.' ' He could have stopped the riot .' ' The government narrowly averted a coup . ' 'She allowed more than a few mistakes to happen .' 'Technology has permitted firms to link together more closely.' 'Unlike DOS , Windows lets you get on with something else when sending a fax.' 'Liberalization allows easier entry into particular markets .' 'Mesh allows the water to circulate normally through the aquarium.' '' Unlike in the Thwarting frame, the Potential_hindrance or Agent does not directly prevent the actions of an individual, but rather affects the world in such a way that an Event cannot occur.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the sentient being which keeps the Event from happening. |
| Event | Core | The Event is prevented from occurring by the Preventing_cause or the Agent. |
| Potential_hindrance | Core | The Potential_hindrance is the force which keeps the Event from happening, or does not. |
| Allowed_category | Extra-Thematic | A category that the Event fits into, which dictates the Event's being permitted or prevented (in accord with some implicit Principle.) 'The transfer was sanctioned as a "necessary precaution".' |
| Circumstances | Extra-Thematic | A situation that accompanies the preventing or allowing. |
| Degree | Extra-Thematic | This frame element selects some gradable attribute and modifies the expected value for it. |
| Depictive | Extra-Thematic | A description of the Agent or an entity of the Event while they are involved in the action. |
| Event_description | Extra-Thematic | In general, this FE is used for phrases that describe the clause of the target as a whole. There are two somewhat distinct subgroups of sentence modifiers that cover this function. First, it applies to appraisals of … |
| Explanation | Extra-Thematic | This FE denotes a proposition from which the main clause (headed by the target) logically follows. |
| Frequency | Extra-Thematic | How often the event occurs. |
| Manner | Extra-Thematic | Any description of details of the event that influence the overall understanding and impression, such as the attitude of an Agent (casually) or the overall nature of the event (the same way). |
| Means | Extra-Thematic | The action performed by an Agent that brings about the prevention or allowing. |
| Period_of_iterations | Extra-Thematic | The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | The Place is where the Potential_hindrance or Agent keeps the Event from taking place. |
| Purpose | Extra-Thematic | The situation that the Agent hopes to bring about with their action. |
| Time | Peripheral | The Time is when the Potential_hindrance or Agent keeps the Event from taking place. |

**Frame relations** (super → sub)

- Inheritance: Preventing_or_letting → Prevent_or_allow_possession
- Inheritance: Preventing_or_letting → Self_control
- Inheritance: Preventing_or_letting → Thwarting
- Metaphor: Preventing_or_letting → Deny_or_grant_permission
- Perspective_on: Causation_scenario → Preventing_or_letting
- ReFraming_Mapping: Deny_or_grant_permission → Preventing_or_letting
- ReFraming_Mapping: Thwarting → Preventing_or_letting
- Using: Event → Preventing_or_letting
- Using: Preventing_or_letting → Level_of_force_resistance

**Lexical units** (24): allow.v, avert.v, avoid.v, check.v, enable.v, enablement.n, forestall.v, frustrate.v, keep (from).v, let.v, nip in the bud.v, obviate.v, permit.v, preclude.v, preempt.v, preemption.n, preemptive.a, prevent.v, prevention.n, prohibit.v, stave off.v, stop.v, stopping.n, upset.v

## Process_continue  (frame id 145)

An Event continues at a certain Place through Time. (Note that often when 'continue.v' occurs with definite time points, it denotes Resumption, which is out of frame here.) NB: Refer to Process frame. '' 'Pyongyang agreed to suspend its withdrawal while talks continued with Washington.' 'Missions and different plans proceed according to Islamic law provision.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Circumstances | Extra-Thematic | Circumstances describe the state of the world (at a particular time and place) which is specifically independent of the event itself and any of its participants. |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Depictive | Extra-Thematic | Depictive phrase about the state of a focal participant. 'The rain continued unabated.' |
| Duration | Peripheral | This FE identifies the Duration of time over which the Event is ongoing. |
| Event | Core-Unexpressed | Name of the Event which is continuing. |
| Explanation | Extra-Thematic | The Explanation for which the Event occurs. |
| Manner | Peripheral | Manner in which the Event is continuing. |
| Next_subevent | Extra-Thematic | The Next_subevent of the overall Event.'The meeting continued with a discussion...' |
| Place | Peripheral | Where the Event takes place. |
| Time | Peripheral | When the Event occurs. |

**Frame relations** (super → sub)

- Causative_of: Cause_to_continue → Process_continue
- Inchoative_of: Process_start → Process_continue
- Inheritance: Process_continue → Activity_ongoing
- Inheritance: Process_continue → Sleep
- Perspective_on: Delimited_state_scenario → Process_continue
- Precedes: Process_continue → Process_end
- Precedes: Process_continue → Process_pause
- Precedes: Process_continue → Process_stop
- Precedes: Process_resume → Process_continue
- Precedes: Process_start → Process_continue
- Subframe: Process → Process_continue

**Lexical units** (9): continue.v, drag on.v, go on.v, on.adv, ongoing.a, persist.v, persistence.n, proceed.v, underway.a

## Process_end  (frame id 232)

A Process comes to an end. 'The project came to a close.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Process | Core | Name of the event which occurs.'Let the carnage end.' |
| Degree | Peripheral | Degree to which the event occurs. |
| Depictive | Extra-Thematic | Depictive phrase describing the actor of the event. |
| Duration | Extra-Thematic | The amount of time it takes for the Process to end. |
| Explanation | Extra-Thematic | The Explanation for which the event ends. |
| Final_subevent | Extra-Thematic | The Final_subevent of an event.'The peace march ended with a prayer.' |
| Frequency | Extra-Thematic | The number of times that the event is repeated. 'Twice the peace march ended with a prayer.' |
| Manner | Peripheral | Manner of performing the event. |
| Place | Peripheral | Where the event takes place. |
| Result | Extra-Thematic | Result for the event. |
| Time | Peripheral | When the event ends. |

**Frame relations** (super → sub)

- Causative_of: Cause_to_end → Process_end
- Inheritance: Event → Process_end
- Inheritance: Process_end → Activity_finish
- Precedes: Process_continue → Process_end
- Precedes: Process_end → Process_completed_state
- Subframe: Process → Process_end

**Lexical units** (12): come to a close.v, come to a end.v, conclude.v, draw to a close.v, draw to a end.v, end [cessation].n, end [final-subevent].n, end.n, end.v, final.a, finale.n, pass.v

## Process_start  (frame id 133)

An Event begins at a certain Time and Place. Reason may also be indicated. NB: Refer to Event frame. 'The project began.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Depictive | Extra-Thematic | Depictive phrase describing the actor of an action. |
| Duration | Extra-Thematic | The period of time for which the Process is ongoing after it has started. 'In three instances, violence erupted for brief periods.' |
| Event | Core-Unexpressed | Name of the Event which occurs. ' The crying began after sunset.' |
| Explanation | Extra-Thematic | The Explanation for which an Event occurs. |
| Frequency | Extra-Thematic | The number of times that the specified type of Event begins. 'Clashes broke out twice because Kenneth had been arrested.' |
| Initial_subevent | Extra-Thematic | The Initial_subevent of the Event.'The service began with a prayer.' |
| Manner | Peripheral | Manner in which an action is performed. |
| Place | Peripheral | Where the Event takes place. |
| Result | Extra-Thematic | Result of the Event. |
| Time | Peripheral | When the Event occurs. |

**Frame relations** (super → sub)

- Causative_of: Cause_to_start → Process_start
- Inchoative_of: Process_start → Process_continue
- Inheritance: Event → Process_start
- Inheritance: Process_start → Activity_start
- Inheritance: Process_start → Come_into_effect
- Precedes: Process_initial_state → Process_start
- Precedes: Process_start → Process_continue
- See_also: Transition_to_a_situation → Process_start
- Subframe: Process → Process_start

**Lexical units** (10): begin.v, break out.v, commence.v, commencement.n, erupt.v, eruption.n, incipient.a, nascent.a, onset.n, start.v

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

## Project  (frame id 1158)

An Agent, which may be an individual or group, is engaged in a complex Activity. A larger Goal which motivates the Agent carrying out the Activity may be indicated. Instead of a particular Activity, a Field of endeavor may be indicated. The project may also have a Name and the Time when as well as the Place where it is ongoing may be specified. 'The New Car Assessment Program (NCAP) is dedicated to helping the public buy a safer car.' 'The school will continue with its project to end all violence related to racism, xenophobia and intolerance.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | What the Agent (an individual or the members of an organization) are dedicated to doing. 'The New Car Assessment Program (NCAP) is dedicated to helping the public buy a safer car. ' |
| Agent | Core | The individual or organization that carries out the project. 'The DOE Human Genome Program also has developed high-throughput approaches to identifying is-regulatory sequences in the human and other genomes' |
| Field | Core | An area of human endeavor, typically scientifc in nature, in which the Agent's Activity falls. 'Several projects in computational linguistics have recently stalled due to lack of funding .' |
| Goal | Core | The larger aim that the Agent is pursuing by carrying out certain coordinated measures. 'The program to analyze the composition of Titan's sludge is nearly complete.' |
| Project | Core | The ongoing plan of action which allows the Agent to pursue the Activity. |
| Salient_entity | Core | An entity (abstract or concrete) which is involved in an implicit Activity. 'Iran has vowed to continue its nuclear program and is demanding that sanctions against it should be lifted .' 'The DOE Human Genome Program … |
| Co-participant | Extra-Thematic | Co-participant is an entity that participates in a coordinated way in the Activity of the project as the Agent. 'It turned out that the company was doing a program with a local Arab-American communal group.' |
| Descriptor | Extra-Thematic | This FE is used to describe a characteristic of the Project. |
| Duration | Peripheral | The length of time over which the project is lasts or is slated to last. 'The government has initiated yet another seven-year program.' |
| Manner | Peripheral | A description of the manner in which the Agent performs the Activity associated with the program. |
| Name | Peripheral | A name given to the project for identification. 'Our agency is responsible for administering the WIC Program' |
| Place | Peripheral | The location where a Project is pursued. |
| Time | Peripheral | The time at which the Project is ongoing. |

**Frame relations** (super → sub)

- Using: Purpose → Project

**Lexical units** (4): plan.n, program.n, project.n, scheme.n

## Proportional_quantity  (frame id 1923)

The Denoted_quantity is (generally) an imprecise characterization of the quantity of Individuals or a Mass, made with reference to a relatively easily and precisely imaginable Reference_quantity. 'It took about three hours, but we 're done now.' 'But there were barely 300 in the whole district. DNI' 'Put in right around a pinch and a half. DNI ' 'She waited a good second before knocking.' 'She waited a good second before knocking.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Denoted_quantity | Core | The quantity denoted by phrases headed by the Target. |
| Individuals | Core | A collection of entities, either quantifiable physical beings (e.g. toads) or quantifiable units whether physical or not (e.g. dollars). |
| Mass | Core | A substance that is being quantified. |
| Reference_quantity | Core | A relatively precise quantity in some oft-used form that is used as the basis for defining the Denoted_quantity. |
| Degree | Peripheral | This frame element selects some gradable attribute and modifies the expected value for it. |
| Q_prop | Extra-Thematic | A property of the Denoted_quantity. |

**Frame relations** (super → sub)

- See_also: Hedging → Proportional_quantity

**Lexical units** (26): a good.a, about.prep, almost.prep, approximately.adv, around.prep, at least.adv, at most.adv, barely.adv, circa.prep, close (to).a, exactly.adv, in neighborhood (of).prep, little.art, minimum.n, most.art, much.art, nearly.adv, odd.a, or so.adv, over.prep, precisely.adv, roughly.adv, some.art, thereabouts.adv, tops.n, under.prep

## Protecting  (frame id 1631)

Some Protection prevents a Danger from harming an Asset. 'The rubber on her sneakers protected her from the mud.' 'The coral reefs shielded the coastline from the worst of the waves.' 'A growing number of sustainable farmers are preserving agricultural variety and protecting biodiversity by raising ?heritage? or ?heirloom? varieties.' 'The man responsible for this entire ordeal cowardly shielded himself from justice with the little boy's struggling body.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Asset | Core | Something desirable possessed by or directly associated with the Protection which might be lost or damaged. 'Almost 10 years later, that agreement insulated Microsoft from liability on copyright claims over the … |
| Danger | Core | A situation that could damage the Asset. 'Other nations tended to muffle or modulate their occasional annoyance with the country that was their shield against the Soviet threat.' |
| Protection | Core | The person, entity, or action that prevents harm to an Asset. 'The tabloid's deal with the woman shielded Schwarzenegger.' |
| Beneficiary | Extra-Thematic | FN: This extra-thematic FE applies to participants that derive a benefit from the protecting event. |
| Degree | Extra-Thematic | This frame element selects some gradable attribute and modifies the expected value for it. |
| Depictive | Extra-Thematic | FN: This FE describes a participant of the state of affairs introduced by the target as being in some state during the action. |
| Descriptor | Extra-Thematic | A description or characteristic of the Protection. |
| Duration | Extra-Thematic | FN: This FE denotes the length of time in which the Asset is protected. |
| Event_description | Extra-Thematic | Tthis FE is used for phrases that describe the protecting event as a whole. It applies to appraisals of the event, typically a judgment of its expectedness. The notion of appraisal requires a factive portrayal of the … |
| Explanation | Extra-Thematic | The Explanation denotes a proposition from which the act of protecting logically follows. |
| Instrument | Peripheral | An entity directed by a volitional agent acting as a Protection which interacts with an undergoer to accomplish the security of the Asset from harm by the Danger. 'Your Brake Pads Parts order is encrypted and … |
| Manner | Peripheral | Any description of the protecting event (or state) which is not covered by more specific FEs, including force (hard, softly), secondary effects (quietly, loudly), and general descriptions comparing events (the same … |
| Means | Peripheral | An event involving the Protection that removes the Asset from potential harm through the Danger. 'Jackson secured the flank by timely charging the enemy and driving him back.' |
| Place | Peripheral | The place where the Danger threatened the Asset. 'To make his way on a foreign soil, he needed different guardians from those that protected him in his own birthplace .' |
| Time | Peripheral | The time when the Danger threatens. 'Regardless of the distribution media, USPTO information is safeguarded before, during, and after dissemination from improper access and modification.' |

**Frame relations** (super → sub)

- Using: Protecting → Armor
- Using: Run_risk → Protecting

**Lexical units** (14): bulwark.n, cover.n, guard.v, insulate.v, protect.v, protection [entity].n, protection [event].n, safeguard.n, safeguard.v, secure.v, shelter.n, shelter.v, shield.n, shield.v

## Quantified_mass  (frame id 189)

This frame contains transparent nouns (and some adjectives) denoting quantities of a Mass or of Individuals. As opposed to aggregate words such as group, set, these Quantity do not have a status as Wholes on their own. 'He found them in the deluge of papers on his desk.' Initially, at least, we have annotated both Quantity of Masses and of Individuals in this frame, though we may split the frame along these lines later on.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Individuals | Core | A collection of entities. 'A number of concerned citizens have raised objections.' |
| Mass | Core | A substance that is being quantified. 'A modicum of seepage on the floor is to be expected.' |
| Quantity | Core | The Quantity-denoting Target word. 'I had a heap of troubles.' |
| Degree | Peripheral | This frame element selects some gradable attribute and modifies the expected value for it. |
| Q_prop | Peripheral | A property of the Quantity. 'John bought a large heap of old National Geograhics at the flea market.' |

**Frame relations** (super → sub)

- Perspective_on: Measure_scenario → Quantified_mass
- See_also: Quantified_mass → Quantity

**Lexical units** (58): a bit.n, a few.art, a little.n, a lot.n, abundance.n, all.a, amount.n, any.a, avalanche.n, billions.n, both.a, deal.n, degree.n, deluge.n, dose.n, dozens.n, fair.a, few.a, few.n, flood.n, handful.n, heap.n, hundreds.n, load.n, many.a, many.n, mass.n, measure.n, millions.n, mite.n, modicum.n, mountain.n, multiple.a, myriad.n, no.a, number.n, numerous.a, oodles.n, ounce.n, pile.n, pinch.n, plethora.n, quantity.n, raft.n, scads.n, scores.n, several.a, several.n, shitload.n, smattering.n, stream.n, thousands.n, ton.n, torrent.n, touch.n, trace.n, trickle.n, wave.n

## Rate_quantification  (frame id 2425)

An Event occurs that can be characterized by a given Rate. The Rate is a ratio of how much a particular quantity changes over time. Degree compares the the given Rate with a standard or expected rate for a similar Event. The Agent is a participant in the event who is responsible for the Rate. '' 'We compared the evolutionary rates of the two different species of monkey.' 'Graduation rates have not gone up in the last decade.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | A participant in the Event who is responsible for the indicated Rate. 'The mating rate of cats has dropped dramatically.' |
| Event | Core | The Event that occurs at a certain Rate. 'Production rates have risen in the last year.' |
| Rate | Core | How much a particular salient quantity involved in an Event changes over time. 'His heart rate quickened.' |
| Degree | Peripheral | Degree compares the given rate for the standard or familiar rate for a given Event. |
| Descriptor | Peripheral | Any characterization of the Rate that is not covered by another more specific FE. 'This camera is capable of shooting at high speeds.' |
| Type | Peripheral | A name of the Rate of or description of the particular category the Rate belongs to. 'His heart rate was unusually fast.' |

**Frame relations** (super → sub)

- Inheritance: Relational_quantity → Rate_quantification

**Lexical units** (1): rate.n

## Reason  (frame id 514)

A volitional Agent is responding to a State_of_affairs by performing some Action. 'And was that your reason for becoming an actor ?' 'But Giles is the reason that I am here .' 'Oh my reason for including it was Section fifty four A.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Action | Core | The action that the Agent performs in response to a State_of_Affairs. ' I find that all my reasons for postponing giving birth still apply ' |
| Agent | Core | The person who responds to a State_of_Affairs by performing some Action. 'Those are my reasons , " said Toby . ' |
| State_of_affairs | Core | The eventuality that motivates the Agent"s performing a particular Action in response to it. ' My reason is that our cities are now designed round the motor car' |

**Frame relations** (super → sub)

- Using: Intentionally_act → Reason
- Using: Reason → Deserving

**Lexical units** (5): basis.n, motivation.n, motive.n, reason.n, why.n

## Records  (frame id 2680)

A Record that contains a permanent account of Data. This Record may be maintained by a Recorder for a certain Entity. '' 'The bank's books were not accurate.' 'He made notes of the subject's responses in the journal by the desk.' 'She kept a record of how many times Steven had asked her for money.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Record | Core | The Record is the entity in which events or accounts are permanently recorded. 'She kept a record of how many times he asked to borrow money.' |
| Data | Peripheral | The Data is the information which is recorded in the Record. It is often expressed as a prepositional phrase. 'Andy kept a log of the girls he had dated.' 'His assistant maintained the records of customer payments.' |
| Descriptor | Peripheral | A characteristic of the Record. 'Moria's bank kept detailed books.' |
| Entity | Peripheral | The Entity is the person or institution for which the Record is maintained. 'She keeps the books for the advertising firm.' 'The bank's records were not ready for the unexpected audit.' |
| Material | Peripheral | What a Record is made of (if applicable). |
| Medium | Peripheral | The Medium is the language in which a Record is composed, or the physical medium (radio, ink) in which it is distributed. |
| Place | Peripheral | The region where the Record is sold, circulated, or otherwise popular |
| Recorder | Peripheral | The Recorder is the person who records the Data in the Record. 'Shirley's log of her favorite eateries grew every day.' |
| Time_of_creation | Peripheral | The Time at which the Record was created. |
| Title | Peripheral | The Title of a Record. |
| Topic | Peripheral | Topic is what the Record is about. |
| Type | Extra-Thematic | The Type refers to the kind of Record being kept. 'Molly was in charge of the finacial records at the small law firm.' |
| Use | Peripheral | The use for which the Record was produced; its purpose. |

**Frame relations** (super → sub)

- Inheritance: Text → Records

**Lexical units** (5): book.n, journal.n, log.n, record.n, recording.n

## Relative_time  (frame id 81)

These words relate to the relative ordering of two events or times. There are two major types of relations evoked by the words of this frame. '' Some of the words (e.g. follow.v, antecedent.a, previous.a) describe the (definitively) stative relationship between two events (the Landmark_occasion and the Focal_occasion). This first type will be moved to the Time_vector frame. 'After she arrived , she laid out her papers on the desk.' 'The following morning, she tried to figure out what it meant . DNI' '' Others (e.g. belated.a, early.a) refer to the change or deviation of an event from the Landmark_occasion (which is expected or usual at a particular time) to the Focal_occasion (which occurs at a different time). Quite often, a Focal_participant who is saliently involved in the Focal_occasion stands in for the occasion. 'My flight is early by 20 minutes.' 'I 'm late for my departure !'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Focal_occasion | Core | The Focal_occasion is the event which is being located in time with respect to some other event: The Focal_occasion is profiled, in contrast to the Landmark_occasion, which is backgrounded. 'Hours of eating and … |
| Focal_participant | Core | The Focal_participant is the participant in the Focal_occasion which is profiled as being in a relation of relative time to the Landmark_occasion. 'We were late for dinner.' |
| Landmark_occasion | Core | The Landmark_occasion is the event with respect to which the Focal_occasion is located. 'Hours of eating and drinking followed the wedding ceremony.' |
| Degree | Peripheral | Degree to which event occurs |
| Explanation | Extra-Thematic | This FE is used for the Explanation or explanation for the Focal_occasion being early or late. |
| Interval | Peripheral | Frequently, the Interval between the Reference and Focal Occasions is expressed: The article in the Times closely followed the singer's announcement that he was retiring. |
| Manner | Peripheral | Manner of performing an action |

**Frame relations** (super → sub)

- Inheritance: Relation → Relative_time
- ReFraming_Mapping: Relative_time → Change_event_time
- ReFraming_Mapping: Relative_time → Temporal_collocation
- See_also: Relative_time → Time_vector

**Lexical units** (39): after.prep, ahead.adv, antecedent.a, as.adv, behind.adv, belated.a, come on heels.v, coming.a, early.a, erstwhile.a, follow.v, following.a, in parallel.a, last.a, late [at night].a, late.a, later.adv, latest.a, next.a, on time.adv, overdue.a, past.a, precede.v, preceding.a, predate.v, premature.a, previous.a, prior.a, punctual.a, punctuality.n, punctually.adv, recent.a, sooner rather than later.adv, sooner.adv, subsequent.a, subsequently.adv, succeed.v, tardy.a, while.c

## Reliance  (frame id 901)

A Protagonist needs a Means action performed for their Benefit. The relevant Means action is often evoked only by reference to an Intermediary who performs it. Also, if the Protagonist performs the Means action themselves, the Instrument that they use may be referred to in place of the Means Note that when one of the three interrelated FEs Means, Instrument and Intermediary is realized overtly, the other two are blocked from overt realization as clause-level arguments of the target.'' When the Protagonist is a sentient being, it is implied that they put their trust in the Intermediary to help in the achievement of the Benefit. The extent to which the Protagonist is dependent on an Intermediary or Instrument can be indicated in a Degree phrase.'' A set of Circumstances in which the Protagonist's need for the Benefit arises, may also be specified. '' The difference between the Benefit that the Means action provides and the Purpose that the Protagonist has is very subtle. For our purposes we will assume that one can form a predication from Benefit and Means on the one hand, and Protagonist and Purpose on the other, but that they cannot be intermingled (cf. examples (7) and (8) below). With for-PPs such as in (6) it is not clear which FE they instantiate, Benefit or Purpose. We will arbitrarily call them Benefit'' '(1) I rely on you to see that my name is not sullied.' '(2) The system can rely entirely on coaxial cable or entirely on optical fibre, just as a tree and branch network can be based on either technology .' '(3) The Tories had got him into this and he relied on them to get him out.' '(4) I knew we could rely on you. DNI ' '(5) To get the economy moving he will rely on repairing the infrastructure of America' '(6) Later , when the Northern Ireland Office was established , it relied heavily on it for the information on which it based security and political activities.' '(7) She would have to rely on his help to get through the fight in one piece. -- She got through the fight in one piece/*His help got through the fight in one piece' '(8) I rely on his help to get me through a long season -- His help got me through a long season/*I got me through a long season ' '(9) We rely on your helping us ' ' (10) You can rely on him when the chips are down to inspire the troops'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Benefit | Core | An action or state that the Means action brings about and from which the Protagonist profits. 'He still relies on me to do the head work' |
| Instrument | Core | An object that the Protagonist uses to realize a Benefit. 'I hate having to rely on my car to get where I want to go' |
| Intermediary | Core | The person or thing that performs a Means action to the Benefit of the Protagonist. 'We rely on you for feedback and input' |
| Means | Core | An action performed either by the Protagonist or an Intermediary that has a Benefit for the Protagonist attached to it. 'We rely on your response' |
| Protagonist | Core | The person or thing whose needs are served by the Means action. ' I rely on this walking stick to get me around' |
| Purpose | Core | An action or state that the Protagonist wants to bring about. It is more or less the Benefit viewed in relation to the Protagonist rather than the Means. 'The user will quickly begin to rely on the pills to cope with … |
| Circumstances | Extra-Thematic | The conditions when the Protagonist needs to rely on an Instrument or Intermediary. 'We have to fully rely on him when times get a little rough' |
| Degree | Peripheral | The extent to which the achievement of the Benefit depends on the Means action. ' He knows I rely entirely on him to point out all my blunders and spelling mistakes.' |

**Frame relations** (super → sub)

- Using: Contingency → Reliance
- Using: Needing → Reliance

**Lexical units** (6): count.v, depend.v, dependence.n, dependency.n, reliance.n, rely.v

## Religious_belief  (frame id 1019)

A Believer has faith in a piece of Content or an Element which fits into a religious belief system made up of many articles of faith. The Content is not necessarily tied to direct sensory experience. The system of beliefs may be enshrined by the members of a social group 'Do Muslims believe in the virgin birth of Jesus?' 'Muslims believe in only One God, the same God that Jews and Christians believe in, but some of the ideas about the nature of God are different' 'Muslims believe that the month of Ramadan is the holiest month of the year'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Believer | Core | The Believer is the person whose religious beliefs are in question. |
| Content | Core | The Content is the object of the Believer's religious conviction. Content can be expressed as a finite clause or in a in-PP Complement. ' A Christian believes that Jesus of Nazareth was a prophet. ' |
| Element | Core | A predefined, fixed idea to which reference is made throughout the belief system. 'I believe in Jesus' 'To Clark, who infinitely believes in angels and celebrating the holidays with loved ones, Christmas means kids and … |
| Role | Core | Role is a function that an Element of the faith is believed to serve. 'If a person believes in Jesus as his Saviour, he can he baptized.' |
| Degree | Peripheral | This FE identifies the Degree to which the Believer is convinced of the usefulness and validity of their religious beliefs . 'Christ the King Presbyterian Church therefore believes fervently in Christian civilization' |
| Manner | Peripheral | This FE identifies the Manner in which the Believer knows or thinks something. 'All we have to do is believe in Jesus like a child and confess him' |

**Frame relations** (super → sub)

- Using: Awareness → Religious_belief
- Using: Religious_belief → People_by_religion

**Lexical units** (4): belief.n, believe.v, faith.n, faithful.n

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

## Required_event  (frame id 1381)

Unless a particular Required_situation obtains, Negative_consequences will follow. Alternatively, the Required_situation is required to achieve a Purpose (which avoids Negative_consequences). A set of Circumstances may be specified under which the requirement holds. 'You must turn in your test by 5 p.m.' 'You better have that fixed by tomorrow or else we'll fire you.' 'The book needs to be shorter to sell to such a young audience.' Most, but not all, LUs of this frame are usable in a context that implies a duty or responsibility, concepts related to the Being_obligated frame. However, our analysis is that such interpretations are due to contextual pragmatic strengthening--in other words, a duty is a frequently salient type of purpose that has negative consequences if not achieved.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Required_situation | Core | The state-of-affairs which prevents Negative_consequences. |
| Circumstances | Extra-Thematic | The FE Circumstances encodes a setting, often temporal or spatial, within which the requirement holds. |
| Degree | Peripheral | The degree to which the Required_situation is necessary. The Degree may either imply a modification of the direness of the Negative_consequences, the probability of the Negative_consequences (if the Required_situation … |
| Explanation | Extra-Thematic | The reason why the Required_situation is necessary. ' I do realize his pitch needed to be wide-ranging because of the differences between folks in the room .' |
| Negative_consequences | Peripheral | An event or state of affairs that results if the required Required_situation does not occur and which impacts some deprofiled entity in a way that the speaker finds undesirable. |
| Place | Peripheral | The location within which the Required_situation is required. 'In California , seatbelts must be fastened at all times .' |
| Purpose | Peripheral | The event or state of affairs that is achieved by bringing about the Required_situation and which entails the non-occurrance of Negative_consequences. |
| Time | Peripheral | The period during which the Required_situation is necessary to prevent negative consequences. 'He was told that when he got back , his column needed a serious rethink .' |

**Frame relations** (super → sub)

- Inheritance: Required_event → Obligation_scenario
- Perspective_on: Preferred_alternative_scenario → Required_event
- ReFraming_Mapping: Being_obligated → Required_event
- ReFraming_Mapping: Required_event → Desirable_event
- See_also: Required_event → Being_obligated
- Using: Being_necessary → Required_event
- Using: Required_event → Deserving
- Using: Required_event → Desirable_event

**Lexical units** (13): be supposed (to).v, best.v, better.v, got to.v, gotta.v, had better.v, hafta.v, have to.v, must.v, need.v, ought to.v, oughta.v, shall.v

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

## Resolve_problem  (frame id 1523)

An Agent resolves an outstanding Problem by finding its solution, explanation, answer, etc. Alternatively, some non-agentive Cause may resolve the Problem. The Means, Degree, Time and Place may also be expressed. 'As it turns out, putting all of my eggs in one basket completely solved all of my problems.' 'Students finally worked through all of the difficult problems by working together.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent finds the solution or explanation to the outstanding mystery or Problem. 'If we have not been able to resolve a problem to your satisfaction, please email us.' |
| Cause | Core | The Cause is the non-Agentive event or state of affairs that brings about the resolution of the Problem. 'First, the Tripartite Agreement of 1979 actually solved the only significant friction between the two countries.' |
| Problem | Core | The Problem is the predicament or mystery that is resolved. 'Likewise, once the students worked through the problem and obtained their results, their next assignment would be to publish these to the web.' |
| Beneficiary | Extra-Thematic | This FE applies to participants that derive a benefit from the resolution of a Problem . 'I wanted you to believe that I was as grateful as you that the baby had died and solved the problem for us of concealing the … |
| Circumstances | Extra-Thematic | Some specification of the circumstances under which the Problem is resolved. 'Such issues can only be resolved at local level .' |
| Co-participant | Extra-Thematic | A person who participates in resolving a Problem along with the Agent. |
| Containing_event | Extra-Thematic | The Containing_event denotes an event or state of affairs that occurs or holds at a time that includes the time during which the resolution of the Problem occurs. 'There are tricky design and methodological issues … |
| Degree | Peripheral | The Degree to which the Agent or Cause resolves the problem. 'Our plan, I believe, wil completely resolve all outstanding questions.' |
| Duration | Peripheral | This FE identifies the length of time taken to resolve a Problem . The government resolved the beach ball crisis in just 22 hours. |
| Frequency | Extra-Thematic | Frequency describes how often the Agent or Cause resolves this problem. 'Unfortunately , when such influences are considered as explanations of the results of free-running experiments , the following problems have … |
| Instrument | Peripheral | The Instrument is an entity used for resolving the Problem . 'Using modern computers , many practical elastic and other problems may be solved by manipulation of this matrix .' |
| Manner | Peripheral | Any description of the resolution, such as secondary effects ( quietly ) or comparisons of events ( the same way ). In agentive cases, Manner may also describe salient characteristics of the Agent which affect the … |
| Means | Peripheral | The Means is an intermediate action taken by the Agent in order to resolve the Problem. 'I fixed the floorplate issue by shaving off the excess stock around the floorplate that was keeping it from closing' |
| Medium | Peripheral | This FE identifies the physical or abstract setting in which the Problem is resolved. |
| Outcome | Extra-Thematic | The Outcome is the failure or success of resolving a Problem . 'This issue must have been raised before and BSM would presumably be gratified to see the situation successfully resolved , once and for all .' |
| Place | Peripheral | This FE indicates the location at which the Problem is resolved. 'A group of international scientists solved the fundamental particle hierarchy question at an underground accelerator.' |
| Purpose | Peripheral | The state of affairs that the Agent is trying to bring about by solving the Problem in the specified way. |
| Resultant_situation | Extra-Thematic | The Resultant_situation is any situation which arises as a result of resolving a Problem . 'The question was : could the situation be resolved by improving the integration of the thought and design processes , so that … |
| Role | Extra-Thematic | Role is used for the capacity in which the Agent resolves a Problem or the role of the Problem in being resolved, and is expressed in as-PPs. |
| Time | Peripheral | This FE indicates the Time at which the Problem is resolved. |

**Frame relations** (super → sub)

- Inheritance: Intentionally_act → Resolve_problem
- Precedes: Confronting_problem → Resolve_problem
- ReFraming_Mapping: Resolve_problem → Speak_on_topic

**Lexical units** (13): address.v, answer.n, clear up.v, correct.v, deal.v, do something about.v, fix.v, get a handle.v, handle.v, resolve.v, result.n, solve.v, work through.v

## Retaining  (frame id 2800)

In this frame an Agent continues to possess a Theme for a Duration of time. '' 'In her heart she must retain bitterness against those who had killed him.' 'I kept the iPhone Sally gave me.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The person who has possession of the Theme. 'At all times the Saxon government held on to its insistently practiced political tradition. ' |
| Theme | Core | The entity which the Agent possesses for a Duration. 'Once you've got a War Bond, hang on to it for the full ten years of its life.' |
| Duration | Peripheral | The amount of time for which the Agent is in possession of the Theme. 'The man who hates his life will keep it for eternal life.' |
| Manner | Peripheral | The way the Agent retains possession of the Theme. 'I knew these gifts were not meant to be kept selfishly.' |
| Means | Peripheral | The means by which the Agent retains the Theme. 'If Britian had focused on India, could it have retained it by force?' |
| Place | Peripheral | The location where the Agent keeps the Theme. 'He will retain in his heart the memory of the vast Holocaust.' |
| Time | Peripheral | The time at which the Agent has possession of the Theme. 'Margerite held on to the key on Wednesday until I returned to pick it up.' |

**Frame relations** (super → sub)

- Inheritance: Activity_ongoing → Retaining
- Inheritance: Possession → Retaining

**Lexical units** (4): hang on to.v, hold on to.v, keep.v, retain.v

## Risky_situation  (frame id 1762)

A particular Situation is likely (or unlikely) to result in a harmful event befalling an Asset. The Situation may be a state, an activity, or some focal entity that must be inferred to be part of some larger Situation involving both it and the Asset. Although the idea of a harmful event is crucial to the understanding of this frame, it is not expressible as an argument of the LUs in this frame. 'Is climate change dangerous for mankind?' 'Customers can make complaints about unsafe products.' 'The primary risk is to our infrastructure.' See the Run_risk frame for discussion on differentiation regarding the noun risk.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Asset | Core | Something judged to be desirable or valuable which might be lost or damaged. 'Honey is not safe for babies.' |
| Dangerous_entity | Core | A concrete or abstract entity which may come to cause the loss of, or damage to the Asset. 'That man is a risk!' |
| Situation | Core | The Situation which may lead to a harmful event. 'Most people agree, going over 100mph is unsafe.' |
| Circumstances | Peripheral | The Circumstances in which an Asset is at risk. |
| Degree | Peripheral | A modifier expressing the deviation of the actual level of security from the expected value given the Situation and the state indicated by the target itself. 'Rogue nations are our greatest threat.' |
| Domain | Extra-Thematic | The Domain in which the Situation is safe. 'All of our websites are educationally safe.' |
| Frequency | Extra-Thematic | How often the Asset encounters the Risky_situation. |
| Place | Peripheral | A particular location for which the Situation is safe. Frequently, it is to be inferred that the characteristics of the location make various Situations safe or unsafe. |
| Time | Peripheral | The time period during which the Situation has the specified level of safety. |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Risky_situation
- Perspective_on: Risk_scenario → Risky_situation
- ReFraming_Mapping: Run_risk → Risky_situation
- See_also: Run_risk → Risky_situation

**Lexical units** (10): danger.n, dangerous.a, risk.n, riskily.adv, risky.a, safe.a, safely.adv, threat.n, unsafe.a, warm.a

## Robbery  (frame id 99)

These are words describing situations in which a Perpetrator wrongs a Victim by taking something (Goods) from them. In some cases, the Source location from which the Goods were taken is used to metonymically refer to the Victim. The robbery can be done in a particular Manner (for example, forcefully) and via a specific Means (for example, by threatening the Victim). 'Half of the team held up the tellers while the others were stationed to report the arrival of police.' As opposed to Theft, Robbery focuses on the harm to the Victim and on the Source location from which the Goods have been removed, rather than the Goods themselves.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Perpetrator | Core | The Perpetrator is the person (or other agent) that takes the Goods away by force or threats. 'Leslie robbed Kim of her watch.' |
| Source | Core | Source is the initial location of the goods, before they change location. 'Leslie and Kim robbed a bank' This FE is realized in compound nouns as follows: 'bank robbery' |
| Victim | Core | The Victim is the person (or other sentient being or group) that owns the Goods before they are taken away by the Perpetrator. 'Leslie robbed Kim of her watch.' |
| Co-participant | Extra-Thematic | Co-participant denotes a person that participates in a coordinated way in robbery event as the primary protagonist, the Perpetrator. |
| Explanation | Extra-Thematic | The state of affairs that the Perpetrator has in mind which leads to the decision to commit the robbery. 'Listen, I just mug people 'cause I got mouths to feed -- nothing personal.' |
| Frequency | Extra-Thematic | The number of times a robbery event occurs. ' An Agoura Jills cigar store was robbed twice last week' |
| Goods | Peripheral | The Goods are anything (including labor, time, or legal rights) that can be taken away. 'Leslie robbed John of his watch.' |
| Manner | Peripheral | The Manner describes the way in which the Robbery took place. 'He was known for committing violent muggings on schoolchildren' |
| Means | Peripheral | The Means indicates the means by which the Robbery takes place. 'John mugged his victim by holding a toy gun to his head.' |
| Place | Peripheral | The Place is where the Robbery occurs. 'They robbed a bank in North Berkeley.' |
| Purpose | Peripheral | The action that the Perpetrator is trying to accomplish by the robbery. 'They used to rob folks just to see the expression on their faces.' |
| Time | Peripheral | The Time indicates when the Robbery occurs. 'They ROBBED a bank in North Berkeley last May.' |

**Frame relations** (super → sub)

- Inheritance: Committing_crime → Robbery
- Using: Theft → Robbery

**Lexical units** (13): hold up.v, hold-up.n, mug.v, mugger.n, mugging.n, ransack.v, rifle.v, rob blind.v, rob.v, robber.n, robbery.n, stick up.v, stick-up.n

## Self_control  (frame id 2651)

An Agent actively (yet not always with success) attempts to keep themselves from participating in an Event. The Agent is usually pushed to the Event because of an internal urge. '' 'He couldn't help but peek.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent who tries to keep an Event from taking place. |
| Event | Core | The Event is the action or state of affairs that the Agent wishes to prevent. |
| Degree | Peripheral | This frame element selects some gradable attribute and modifies the expected value for it. |
| Place | Peripheral | The Place is where the Agent attempts to prevent the Event from taking place. |
| Time | Peripheral | The Time is when the Agent prevents the Event from taking place. |

**Frame relations** (super → sub)

- Inheritance: Preventing_or_letting → Self_control

**Lexical units** (12): (can't) help.v, hold back.v, refrain.v, repress.v, repression.n, resist.v, resistance.n, resistant.a, restrain.v, restraint.n, suppress.v, suppression.n

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

## Size  (frame id 2282)

The size of an Entity is assessed in terms of the Degree by which it deviates from the norm. The size generally refers to the amount of three-dimensional space that is occupied by the Entity, not primarily to its weight, density, or length, which is why it is peculiar to refer to a bullet as "large", even if it is heavy, unless it actually has larger dimensions than usual, or to a rope as "big", even if it is long, unless its other, cross-sectional dimensions are also significant. 'I own a very small home.' 'Where is my little notebook?' 'That dog is huge!' '' There are an enormous number of productive metaphors that involve this frame as the source domain; two of the most frequent metaphors come from the target domains of quantity/amount and importance. 'He gave me a small sum of money.' 'The novel was a substantial achievement.' '' Subcases of the quantity/amount and importance metaphors are also prominent. These involve cases describing the extent of an action's, event's, or person's effect ("his influence on her work was massive"), as well as those related to events ("big party"), similarity ("gigantic difference"), communication ("giant misunderstanding"), and emotions ("great joy", "little joys"). Other productive metaphors include those dealing with groups (in terms of their number of members, net worth, importance to the economy, i.e. "giant electronics company") and those describing sound volume ("in a tiny voice", "the enormous thundering of her heart"). '' The target domain of fame, by contrast, occurs in a non-productive metaphor, found especially with big.a and huge.a. Maturity and age also occur in non-productive metaphors ("big boy", "little baby").

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The thing whose size is being considered. 'I had a big dinner.' |
| Degree | Peripheral | The extent to which the size of the Entity deviates from the norm. 'I had a really big dinner.' |
| Dimension | Core-Unexpressed | The feature of an (actual or possible) Entity that is measured. In literal examples, it essentially must be size, or a word equivalent to size such as bulk. 'The particles were smaller in size than expected .' 'Her … |
| Standard | Peripheral | The size of the Entity may be compared to the size of a Standard. 'You 're tall for a Swede.' |
| Subregion | Extra-Thematic | This FE denotes a specific subregion being sized. |

**Frame relations** (super → sub)

- Inheritance: Measurable_attributes → Size
- ReFraming_Mapping: Dimension → Size

**Lexical units** (36): Brobdingnagian.a, Lilliputian.a, ample.a, big.a, bitty.a, bulky.a, capacious.a, colossal.a, enormous.a, giant.a, gigantic.a, grand.a, great.a, huge.a, humongous.a, immeasurable.a, immense.a, infinitesimal.a, jumbo.a, large.a, little.a, massive.a, medium-sized.a, medium.a, mid-size.a, mini.a, miniature.a, miniscule.a, petite.a, puny.a, sizable.a, small.a, substantial.a, tiny.a, voluminous.a, wee.a

## Sleep  (frame id 264)

The Sleeper stays in an altered state of consciousness with greatly reduced external awareness. 'We slept.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Sleeper | Core | The entity that is sleeping. |
| Degree | Extra-Thematic | The degree to which the Sleeper is asleep. |
| Duration | Peripheral | This FE identifies the Duration of time for which a state holds or a process is ongoing. |
| Manner | Peripheral | Any description of the sleeping event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, noisily), and general descriptions … |
| Place | Peripheral | Where the event takes place. |
| Time | Peripheral | This FE identifies the Time when the sleep occurs. |

**Frame relations** (super → sub)

- Inheritance: Process_continue → Sleep
- Precedes: Fall_asleep → Sleep
- Precedes: Sleep → Waking_up
- Subframe: Sleep_wake_cycle → Sleep

**Lexical units** (25): asleep.a, catnap.n, catnap.v, doze.n, doze.v, drowse.n, drowse.v, forty winks.n, hibernate.v, hibernation.n, kip.n, kip.v, nap.n, nap.v, out like a light.a, out.a, shut-eye.n, sleep [event].n, sleep [quantity].n, sleep.v, slumber.n, slumber.v, snooze.n, snooze.v, unconscious.a

## Soaking_up  (frame id 2032)

An Item becomes filled with a Substance as a result of movement of liquid into visible or invisible interstices in the Item. 'Paper and board absorb moisture in the winter.' 'A stable soil soaks up water.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Item | Core | The Item is the absorbant friendly thing that takes in the Substance. |
| Substance | Core | The Substance is the material that is taken in by the Item. |
| Degree | Peripheral | Degree describes the extent to which a particular absorption event deviates from the norm. |
| Duration | Peripheral | For what length of time the Item is imbued with Substance. |
| Manner | Peripheral | The way in which the Item soaks in the Substance. |
| Place | Peripheral | The location where the Item takes in Substance. |
| Time | Peripheral | When the Item takes in Substance. |

**Frame relations** (super → sub)

- Causative_of: Soaking → Soaking_up

**Lexical units** (3): absorb.v, soak up.v, sponge.v

## Social_event  (frame id 125)

A Social_event occurs at which Attendees are present to conduct a social function or joint activity. The Social_event is often a party or celebration, in which case it is possible to express someone who is being honored (the Honoree) or its function may be to celebrate an Occasion at which Attendees are present. Often, a specific Attendee, the Host, provides a venue for people to gather. 'Sue threw a party for Bob's birthday.' 'Who will host the Olympic games in eight years?'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Attendee | Core | Attendee is used for the people who come to the Social_event. 'The whole group attended the party.' |
| Beneficiary | Extra-Thematic | The person for whom the Social_event is held. 'I threw a party for Josef.' |
| Degree | Peripheral | This FE identifies the Degree to which the Social_event occurs. |
| Descriptor | Extra-Thematic | A characteristic of the social_event. |
| Duration | Peripheral | This FE identifies the Duration of time for which the Social_event is ongoing. |
| Frequency | Extra-Thematic | This FE describes how often the Social_event occurs. |
| Host | Extra-Thematic | The Host is the person or organization that hosts the Social_event. In cases where an individual stands in for an organization, the host may be marked twice. 'Ron threw a party.' 'President Reagan hosted a state … |
| Manner | Peripheral | This FE identifies the Manner in which the Social_event occurs. |
| Name | Extra-Thematic | The Name of the Social_event. |
| Occasion | Extra-Thematic | The Occasion for which the Social_event is held. |
| Period_of_iterations | Extra-Thematic | COD: The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | This FE identifies the Place where the Social_event occurs. |
| Purpose | Extra-Thematic | The reason the Social_event is being held. 'We threw a banquet to raise awareness to our cause.' |
| Refreshment | Extra-Thematic | Refreshment is used for the meal, food or drinks that are served at the Social_event. 'I enjoy a tasteful dinner party.' 'I attended a cocktail party and drank myself silly.' 'First layer: I attended a banquet on … |
| Social_event | Core-Unexpressed | This FE identifies the Social_event itself. 'The department picnic was lots of fun.' |
| Style | Extra-Thematic | This FE identifies the Style of the Social_event and its level of formality, indicating appropriate dress for participants and/or the kind of activities in which they engage. 'Lee hosted a formal party.' 'Abby's garden … |
| Time | Peripheral | This FE identifies the Time when the Social_event occurs. |

**Frame relations** (super → sub)

- Inheritance: Social_event → Social_event_collective
- Inheritance: Social_event → Social_event_individuals
- Using: Eventive_affecting → Social_event

**Lexical units** (25): ball.n, banquet.n, barbecue.n, bash.n, benefit.n, celebration.n, dance.n, dinner-party.n, dinner.n, fair.n, feast.n, festival.n, fete.n, function.n, gala.n, get-together.n, jollification.n, meeting.n, party.n, picnic.n, rave.n, reception.n, shindig.n, social.n, soiree.n

## State_continue  (frame id 1155)

Despite some implication that a State would be interrupted, the Entity remains in the specified State. Note that State includes locative relations. 'Online security remains elusive.' ''

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | A concrete or abstract Entity. |
| Circumstances | Extra-Thematic | The Circumstances under which the State continues. |
| Depictive | Extra-Thematic | This FE describes a participant of the state of affairs introduced by the target as being in some state during the action. |
| Duration | Extra-Thematic | The time period over which the State continues to hold of the Entity. 'Our commitment to high-quality, distinctively Canadian programming has remained constant for more than six decades.' |
| Explanation | Extra-Thematic | The state of affairs that explains why the State persists. 'Simandle ruled that the contract remains in force because the GTMUA accepted $400,000 in connection fees from the trust.' |
| Place | Peripheral | The location where the Entity is in the State. 'Martial law remains in effect in Absurdistan.' |
| State | Core-Unexpressed | The State of an Entity. |
| Time | Peripheral | The Time when the State is found to still persist. 'Financial recovery remains elusive in 2002.' |

**Frame relations** (super → sub)

- Causative_of: Cause_to_continue → State_continue
- Using: State → State_continue
- Using: State_continue → Continued_state_of_affairs

**Lexical units** (3): remain.v, rest.v, stay.v

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

## Store  (frame id 1511)

A Supply of a Resource is kept safe and available for a future Use. The Supply may be under the control of a Possessor. 'Our supply of food is running low.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Possessor | Core | The entity that possesses the Supply. 'In 1997, France's stock of unirradiated civil plutonium increased to 72 tons.' |
| Resource | Core | The goods or commodity that is being stored in a Supply. ' India has made great strides in agriculture and now not only meets it own grain needs but has a sizeable reserve of basic grains, mainly rice and wheat.' |
| Supply | Core | This FE denotes the Supply of Resources. It is incorporated into each LU in this frame. |
| Use | Core | The future Use for the Resource. 'Due to restrictions imposed by our export control, the Japanese have begun to use a portion of their war reserve of petroleum.' |
| Descriptor | Extra-Thematic | A characterization of the Supply itself, rather than the Resource. 'Institutions have focused on Broward County?s dwindling supply of land, continued population growth and elevated income levels.' |

**Frame relations** (super → sub)

- Inheritance: Aggregate → Store
- Inheritance: Store → Cache
- Using: Storing → Store

**Lexical units** (7): cargo.n, inventory.n, reserve.n, stock.n, stockpile.n, store.n, supply.n

## Substance  (frame id 1321)

This frame concerns internally undifferentiated Substances. 'As their gut bacteria ferment cellulose , they generate methane gas , which escapes from the rear ends of the insects.' ' The pipes are leaking noxious gas.' 'Some CH-47 "Bombers" were equipped to roll-out riot control gas or napalm onto Viet Cong bunker complexes from the rear cargo ramp.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Substance | Core | The undifferentiated entity which is presented as having a permanent existence. 'Liquid flowed over the rocks but it was not water.' |
| Constituents | Peripheral | The frame element expresses substances/ingredients that make up the Substance. 'Argon gas is added into the station's air mixture.' |
| Descriptor | Extra-Thematic | A characterization of the Substance. 'The new Chrysler minivans will run on compressed natural gas.' |
| Inherent_purpose | Extra-Thematic | The purpose for which the Substance is intended. 'Supply and placing of filler sand shall be incidental to installation of the paving stones.' |
| Origin | Extra-Thematic | The location that the Substance comes from, including both extraction sites and emission/production sources. 'It retrieves most of the expensively generated heat from flue gases and puts this heat back into the … |
| Type | Peripheral | This FE indicates what subtype of the general category the Substance belongs to. 'Greenhouse gases trap heat and prevent its escape from the atmosphere.' |

**Frame relations** (super → sub)

- Inheritance: Physical_entity → Substance
- Inheritance: Substance → Active_substance

**Lexical units** (26): aluminum.n, atropine.n, calcium.n, cement.n, chemical.n, fertilizer.n, gas.n, glass.n, iron.n, juice.n, liquid.n, material.n, metal.n, methane.n, mud.n, oil.n, ore.n, oxygen.n, paper.n, petroleum.n, plutonium.n, sand.n, solid.n, uranium.n, water.n, yellowcake.n

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

## Supporting  (frame id 2000)

A Supporter assists to strengthen the Supported by lending itself in material aid (or abstract assistance in the case of metaphorical uses). 'The bottom of the wall is supported by the foundation.' 'Many legislators have supported the industry in the past.' 'The revetment layers buttressed the mud-mortared cobblestone core wall.' 'Online gambling can bolster the US economy.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Supported | Core | The Supported is given strength through the assistance of the Supporter. |
| Supporter | Core | The Supporter acts to benefit the Supported by providing additional strength or stability. |
| Degree | Peripheral | The measure to which the Supporter's assistance brings the Supported added strength and support. 'The physical therapist must totally support tthe patient during the exercises.' |
| Duration | Peripheral | The time period during which the Supporter supports the Supported. 'For some seventy years, this judicial fabrication buttressed racial segregation.' |
| Event_description | Extra-Thematic | A clause describing the event as a whole. |
| Explanation | Extra-Thematic | A state-of-affairs from which the accomplishment would be predicted. |
| Instrument | Peripheral | An entity used by the Supporter in service of the Supported's strength by support. 'The troops used their shoulders to support the doors of the keep, as the enemy forces tried to break through.' 'For years, patrons of … |
| Manner | Peripheral | This FE identifies the Manner in which a Supporter supports the Supported. 'The British Government happily buttressed Saddam's appalling oppression of his people'. |
| Means | Peripheral | An action that the Supporter undertakes in service of the Supported's strengthening. 'The foundation supports the building by distributing the load to the ground below.' |
| Place | Peripheral | This FE identifies the Place where the support occurs. 'In England, economic incentives are buttressed by closing certain overdoctored areas from new practices.' |
| Purpose | Peripheral | The situation that the Supporter wishes to bring about by supporting the Supported. 'The porch tower of Saint-Germain-des-Prés is sturdily buttressed to support the weight of its massive bells'. |
| Time | Peripheral | This FE identifies when the support occurs. 'Early in the twentieth century, such economic arguments buttressed the creation of a National Park Service.' |

**Frame relations** (super → sub)

- Inheritance: Assistance → Supporting
- Using: Cause_change_of_strength → Supporting

**Lexical units** (3): bolster.v, buttress.v, support.v

## System  (frame id 1610)

A Complex with a particular Function is formed out of Component_entities. The function may be expressed by reference to a Salient_entity involved in the working of the Complex. 'The body's immune system can be mobilized against cancer. ' 'The sewer system carries wastewater from homes and businesses to the Water Pollution Control Plant for treatment. '

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Complex | Core | The unit formed by the Component_entities. 'The DeKalb County School System cordially invites you to attend the Ground Breaking Ceremony for Peachtree Middle School.' |
| Component_entities | Core | The entities that function together as a unit. 'The people of Bangkok had the opportunity to experience the long awaited underground train system.' |
| Function | Core | The activity that the Complex entity performs by virtue of its Component_entities interacting. 'These cells form part of the immune system and help to prevent the body from getting diseases .' |
| Salient_entity | Core | The kind of entity that the Complex operates on as part of its Function. 'The lifespan of a central sewage system is about 80 years.' |
| Descriptor | Extra-Thematic | Any characterization or evaluation of the Complex. 'Kwame Kilpatrick is taking a hard look at Detroit's highly inefficient bus system.' |
| Possessor | Extra-Thematic | A person or organization that possesses or owns the Complex or a larger entity of which the Complex itself is a part. 'China's transportation system has undergone profound changes in recent years.' |

**Frame relations** (super → sub)

- Inheritance: Set_of_interrelated_entities → System

**Lexical units** (3): cascade.n, complex.n, system.n

## Taking  (frame id 410)

An Agent removes a Theme from a Source so that the it is in the Agent's possession. 'Milton took the can of beer out of the refrigerator.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The person who takes possession of the Theme. 'Milton took the can of beer out of the refrigerator.' |
| Source | Core | The location of the Theme prior to the taking. 'Milton took the can of beer out of the refrigerator.' |
| Theme | Core | The Agent takes possession of the Theme. 'Milton took the can of beer out of the refrigerator.' |
| Containing_event | Extra-Thematic | The larger event which contains the Taking event. 'These weapons were seized in a police raid'. |
| Explanation | Extra-Thematic | The Explanation for the taking. 'Milton took the champagne out of the ice because it was getting too cold.' |
| Manner | Peripheral | The Manner of the taking. 'Milton stealthily took the can of beer out of the refrigerator.' |
| Means | Peripheral | The intermediate action taken by the Agent to take the Theme. 'Milton took the can of beer from John by distracting him with a shiny nickel'. |
| Place | Peripheral | Where the taking takes place. 'Police seized several tons of marijuana in Berkeley last weekend.' |
| Purpose | Peripheral | The Purpose for the taking. 'Milton took the can of beer out of the refrigerator to make sure no one else took it.' |
| Time | Peripheral | When the taking takes place. 'The government seizure of a suspected dissident's computer last November has increased the tension between citizens and law enforcement.' |

**Frame relations** (super → sub)

- Inheritance: Getting → Taking
- Inheritance: Intentionally_affect → Taking
- Inheritance: Taking → Theft

**Lexical units** (5): commandeer.v, grab.v, seize.v, seizure.n, take.v

## Taking_captive  (frame id 2663)

An Agent begins preventing a Captive from moving despite a tendency or desire on the part of the Captive to do so. 'Authorities recently captured several suspects who were hiding in a remote mountain area.' 'High value target has been quietly and safely secured.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent brings the Captive into custody. 'Authorities recently captured several suspects who were hiding in a remote mountain area.' |
| Captive | Core | The entity which is captured. 'Police have captured three of the suspected bombers after a week-long search.' |
| Cause | Core | The Cause is the non-sentient entity which is responsible for restricting the movement or location of the Captive. |
| Containing_event | Extra-Thematic | The larger event which contains or during which occurs the event of taking the Captive captive. 'The suspects were secured in a large raid conducted by both nations' police forces.' |
| Depictive | Extra-Thematic | The description of one of the participants in the capturing event. 'Make sure they're taken alive!' |
| Explanation | Extra-Thematic | A state of affairs that the Agent is responding to in capturing the Captive. 'She was captured quickly beacuse she was on the department's high priority targets list.' |
| Instrument | Extra-Thematic | The instrument with which the capturing is carried out. |
| Manner | Peripheral | Any description of the event (or state) which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), force (hard, softly), secondary effects (quietly, loudly), and … |
| Means | Peripheral | An intentional action performed by the Agent that accomplishes the action indicated by the target. 'Troops secured the target by entering his compound in small numbers and under the cover of darkness.' |
| Place | Peripheral | This FE identifies the Place where the event occurs. 'Authorities secured the target in a private residence.' |
| Purpose | Peripheral | The purpose for which the Agent takes the Captive into custody. 'These targets were secured to ensure that they would pose no danger during the trial.' |
| Reciprocation | Extra-Thematic | The reason for the confinement. 'He was captured for treason.' |
| Time | Peripheral | When the event occurs. |

**Frame relations** (super → sub)

- Precedes: Taking_captive → Inhibit_movement
- Subframe: Inhibit_motion_scenario → Taking_captive

**Lexical units** (4): capture.n, capture.v, secure.v, take captive.v

## Taking_sides  (frame id 1306)

A Cognizer has a relatively fixed positive or negative point of view towards an Issue. A Side in a debate concerning an Issue or an Action of a Side may stand in for the Issue. The Cognizer's Degree of alignment may also be specified. 'In interviews , it seems like everyone is completely against this expenditure .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Action | Core | An action taken by a Side or a view that the Side takes on an issue which the Cognizer either supports or opposes. |
| Cognizer | Core | The individual that holds an opinion on an Issue or Side. |
| Issue | Core | The matter, usually concerning a course of action, which the Cognizer has a positive or negative opinion about. |
| Side | Core | The party or individual (generally associated with a particular position on an Issue) that the Cognizer has an opinion about. |
| Concessive | Extra-Thematic | This FE signifies that the state of affairs expressed by the main clause (containing the target) occurs or holds, and something other than that state of affairs would be expected given the state of affairs in the … |
| Degree | Peripheral | The Degree to which the Cognizer supports or opposes something. |
| Descriptor | Extra-Thematic | This FE describes the person or element that is taking a side. |
| Explanation | Extra-Thematic | The Explanation is a proposition denoting a state of affairs from which the Cognizer's taking the indicated view on the Issue logically follows. 'Could it be that he sided with them because it was the constitutionaly … |
| Manner | Peripheral | Any description of the Taking_sides which is not covered by more specific FEs, including epistemic modification secondary effects (quietly, loudly), and general descriptions comparing events (the same way). It may also … |
| Particular_iteration | Extra-Thematic | Expressions marked with this extra-thematic FE modify a non-iterative use of the target, and indicate that it is conceived as embedded within an iterated series of similar events or states. In addition, most … |
| Place | Peripheral | The location where the Cognizer takes Sides on an Issue . |
| Time | Peripheral | The time period during which the Cognizer has the indicated point of view towards the Issue. 'Last year she opposed the bill, but changed her mind after she received correspondence supporting the bill. ' |

**Frame relations** (super → sub)

- Using: Desirable_event → Taking_sides
- Using: Opinion → Taking_sides
- Using: Taking_sides → Giving_in
- Using: Taking_sides → Hostile_encounter
- Using: Taking_sides → Partiality
- Using: Taking_sides → Protest

**Lexical units** (18): against.prep, back.v, backing.n, believe (in).v, endorse.v, for.prep, in favor.prep, opponent.n, oppose.v, opposition [act].n, opposition [entity].n, part.n, pro.adv, side.n, side.v, support.v, supporter.n, supportive.a

## Taking_time  (frame id 967)

An Activity takes some Time_length to complete. If an Agent is involved they may stand in metonymically for the Activity. For some LUs (e.g., fast, speedy) the Degree to which the Activity is conceived of as taking less time than usual can be expressed. 'How long will this take?' 'The ride was speedy and often bumpy.' 'Under high-pressure situations, police officers are very fast at reacting to danger.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Activity | Core | The event which requires some Time_length for completion. 'Mona had a speedy recovery.' |
| Agent | Core | The individual who performs the Activity. |
| Degree | Core | A modifier expressing the deviation of the Time_length from the norm. |
| Time_length | Core | The amount of time required for the Activity. 'It'll only take 20 seconds.' |
| Attribute | Peripheral | The durational feature of the Activity. 'In actual experiential time, sorting the beads takes an extremely long time.' |
| Circumstances | Extra-Thematic | Some specification of the Circumstances under which the Activity takes a particular amount of time. 'In the rain, biking to work takes me a lot longer' |
| Duration | Extra-Thematic | Duration is the length of time from the beginning of the Activity to its end. |
| Time | Peripheral | The Time at which the Activity takes place. 'That took an hour last week.' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Taking_time
- Using: Being_necessary → Taking_time
- Using: Duration_description → Taking_time

**Lexical units** (11): fast.a, gradually.adv, in.prep, quick.a, quickly.adv, rapid.a, slow.a, slowly.adv, speedy.a, swift.a, take.v

## Telling  (frame id 750)

A Speaker addresses an Addressee with a Message, which may be indirectly referred to as a Topic. Instead of (or in addition to) a Speaker, a Medium may also be mentioned. 'I told him about the party.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Addressee | Core | The Addressee receives the Message from the Speaker. |
| Medium | Core | This FE is the Medium in which the Message is expressed. |
| Message | Core | The Message is the communication produced by the Speaker. 'The authorities informed me that my brother had been arrested.' 'I told him a bedtime story.' |
| Speaker | Core | The Speaker is the sentient entity that produces the Message. 'Bill told me that he would come to the party.' |
| Topic | Core | The Topic is a general description of the content of the Message. 'Leroy told his mother about his arrest.' |
| Communicative_force | Extra-Thematic | This FE indicates the Communicative_force or authority with which the Message is expressed. This FE is often denoted by words such as "officially," "formally," "technically," etc. 'She has yet to receive official … |
| Descriptor | Extra-Thematic | This FE identifies a characteristic or description of the telling event. |
| Iterations | Extra-Thematic | The FE Iterations is used for expressions that indicate the number of times an event or state (of the kind denoted by the target in its clause) has taken place or held. |
| Manner | Peripheral | The Manner describes the way in which the Speaker delivers the Message. |
| Means | Peripheral | The Means describes the way the Speaker accomplishes the task of giving the Addressee the Message. |
| Place | Peripheral | Place is the location in which the Speaker informs the Addressee of the Message. 'She looked at it for a few moments, thinking of Mark Smeaton and what he had told her on the steps of City Hall.' |
| Time | Peripheral | The Time during which the Speaker informs the Addressee of the Message. 'Even when we had a size problem they informed me right away and everything worked out great.' |

**Frame relations** (super → sub)

- Inheritance: Statement → Telling
- Inheritance: Telling → Suasion
- Inheritance: Telling → Warning
- ReFraming_Mapping: Request → Telling
- ReFraming_Mapping: Statement → Telling

**Lexical units** (11): advise.v, apprise.v, assurance.n, assure.v, brief.v, confide.v, inform.v, let know.v, notification.n, notify.v, tell.v

## Temperature  (frame id 1050)

An Entity has a Temperature characterized by the target. The Temperature is a value of the temperature Attribute. 'The pan is already too hot to touch.' 'The walk-in was freezing, but it was better than hanging out in the kitchen.' '' Note that in this frame, the Entity does not experience the temperature, but is merely described as being in a certain externally verifiable state. Thus 'Open a window; I'm too hot.' is not in frame but rather in Subjective_temperature.

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Attribute | Core | The feature of an Entity which is under discussion. |
| Degree | Core | A modifier expressing the deviation of the Temperature from the norm. |
| Entity | Core | The Entity for which the temperature Attribute is under consideration. 'The soup's too hot.' |
| Temperature | Core | A quantity or other characterization of the Entity's state with respect to the temperature Attribute. 'The skillet had a temperature of 230 F' |
| Circumstances | Extra-Thematic | Some specification of the Circumstances under which the Entity has a particular Temperature. |
| Subregion | Extra-Thematic | A part of the Entity that has the specified Temperature value. 'The pan is hot on the handle' |
| Time | Extra-Thematic | The Time during which the Entity is in the state of having a particular Degree for the temperature Attribute. |

**Frame relations** (super → sub)

- Inchoative_of: Change_of_temperature → Temperature
- Inheritance: Measurable_attributes → Temperature
- Inheritance: Temperature → Ambient_temperature
- Using: Temperature → Heat_potential

**Lexical units** (10): cold.a, cool.a, freezing.a, frigid.a, hot.a, lukewarm.a, scalding.a, temperature.n, tepid.a, warm.a

## Temporal_subregion  (frame id 1470)

A Subpart of a Time_period is picked out. In some cases, the part (as opposed to the entire Time_period) may be described by a Subpart_property. The Time_period may be indicated by an event which takes place during the Time_period. 'I nearly kicked my TV this afternoon after watching the shambolic end of the Austrian Grand-Prix .' 'Jack Yan looks at how the branding profession will be affected in the early 2000s by globalization .' 'The late part of the afternoon is the worst time to get things done .'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Subpart | Core | The part of the Time_period which is profiled. 'The findings mark the beginning of a new age of planetary science, in which "extrasolar" planets can be directly measured and compared.' |
| Time_period | Core | A temporal span conceived of as a whole. 'A zillion copies and clones have been made of this Russian game since it first was released in the mid 80's.' |
| Degree | Extra-Thematic | This frame element selects some gradable attribute and modifies the expected value for it. |
| Subpart_property | Extra-Thematic | Some description which pertains specifically to the Subpart (rather than the Time_period). 'Indeed, the sorry end of the HCI period, with Korea in recession and. in the throes of rampant political turmoil, has led some … |
| Time | Peripheral | This FE indicates the Time that is being referred to. |

**Frame relations** (super → sub)

- Using: Part_orientational → Temporal_subregion

**Lexical units** (13): beginning.n, dawning.n, earlier.a, early.a, end.n, late.a, later.a, mid.a, middle.a, middle.n, outset.n, start.n, turn.n

## Text  (frame id 298)

A Text is an entity that contains linguistic, symbolic information on a Topic, created by an Author at the Time_of_creation. It may be a physical entity that is made of a certain Material etc. It may be constructed for an Honoree. 'It was a good book.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Text | Core | The Text is the entity that contains linguistic information. This an incorporated FE for each LU in this frame. |
| Author | Peripheral | The Author is the person who produced a particular Text. 'I'm glad I bought and read Robbins's book.' |
| Beneficiary | Extra-Thematic | The person for whom the Text is produced. 'The poem for Caitlin was included in an anthology .' |
| Containing_text | Extra-Thematic | This is a text in which the Text is located. 'The last poem in the anthology was horrid.' |
| Descriptor | Extra-Thematic | A characteristic of the Text |
| Genre | Extra-Thematic | The Genre or sub-Genre of the Text. 'She writes only historical fiction.' 'I've got three comedic screenplays on my desk right now!' |
| Material | Extra-Thematic | What a Text is made of (if applicable). 'The library was so old, it was filled with vellum tomes, not a paperback in sight.' |
| Medium | Peripheral | The Medium is the language in which a text is composed, or the physical medium (radio, ink) in which it is distributed. 'Science articles in Greek are difficult to understand for me.' 'It's prudent to pay attention to … |
| Place | Extra-Thematic | The region where the Text is sold, circulated, or otherwise popular. |
| Subpart | Extra-Thematic | The smaller texts that make up the Text. 'He found it in a book of spells.' |
| Time_of_creation | Extra-Thematic | The Time at which the Text was created. 'Jackson's new story is based on a 1980 novel by his father.' 'Poems from the end of that dynasty are known to contain many novel metric structures.' |
| Title | Extra-Thematic | The Title of a Text. 'She read Sassy magazine.' 'Current NOW President Kim Gandy said Friedan's Feminine Mystique book opened women's eyes.' NOTE: when the Title is expressed in an appositive clause, it is labeled as … |
| Topic | Peripheral | Topic is what the Text is about.'I read a book about knitting.' |
| Use | Peripheral | The use for which the text was produced; its purpose. 'She read through the bicycle's construction manual.' |

**Frame relations** (super → sub)

- Inheritance: Artifact → Text
- Inheritance: Text → Documents
- Inheritance: Text → Records
- Using: Text → Law
- Using: Text → Medium
- Using: Text → Reference_text
- Using: Text → Topic
- Using: Text_creation → Text

**Lexical units** (92): account.n, article.n, autobiography.n, ballad.n, benediction.n, biography.n, book.n, booklet.n, brochure.n, bulletin.n, chronicle.n, comedy.n, diary.n, drama.n, edition.n, editorial.n, elegy.n, epic.a, epic.n, epigram.n, epilogue.n, epistle.n, essay.n, eulogy.n, exemplum.n, fable.n, fanzine.n, festschrift.n, fiction.n, grimoire.n, hagiography.n, haiku.n, handbook.n, hardback.n, history.n, imprecation.n, issue.n, journal.n, lay.n, letter.n, life.n, limerick.n, list.n, literature.n, lyric.n, mag.n, magazine.n, manual.n, manuscript.n, material.n, meditation.n, memoir.n, missive.n, monograph.n, mystery.n, newspaper.n, novel.n, novelette.n, novella.n, obituary.n, ode.n, pamphlet.n, paper [article].n, paper [newspaper].n, paperback.n, periodical.n, poem.n, poetry.n, publication.n, record.n, report.n, rhyme.n, saga.n, screenplay.n, script.n, sermon.n, song.n, sonnet.n, speech.n, spellbook.n, tetralogy.n, textbook.n, thriller.n, tome.n, tract.n, tractate.n, tragedy.n, treatise.n, trilogy.n, volume.n, whodunit.n, writings.n

## Thermodynamic_phase  (frame id 2550)

This frame describes the attributes of a thermodynamic Phase of Matter. '' 'The molten stateof the lava.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Matter | Core | The Matter is the physical substance or entity being described in terms of a Phase. |
| Phase | Core | The state of the Matter being described. |

**Frame relations** (super → sub)

- Using: Thermodynamic_phase → Substance_by_phase

**Lexical units** (2): phase.n, state.n

## Time_period_of_action  (frame id 2290)

LUs in this frame denote a period of time in which an Enabled_action becomes possible. The Duration of this time period can be both exact and inexact. An Agent who performs the Enabled_action may be mentioned as well. 'Allow a three-day window for delivery. DNI'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Agent | Core | The Agent is the one who performs the Enabled_action. |
| Duration | Core | A quantity or other characterization of the period of the time in which an Enabled_action is allowed. In this frame, the duration may be exact or inexact. |
| Enabled_action | Core | The action that becomes possible through the existence of the period of time. |
| Whole | Peripheral | The Whole is the larger time period to which target is a part of. |

**Frame relations** (super → sub)

- Inheritance: Timespan → Time_period_of_action
- Using: Alternatives → Time_period_of_action

**Lexical units** (1): window.n

## Topic  (frame id 373)

A stretch of linguistic discourse or a Text that a Communicator produces has a Topic that it is about. 'Chapter 5 discusses the issue of transubstantiation.' 'Smither's essay is about plane spotting.' ' Ostrovsky addresses monetary policy in Chapter 5.' 'This book is mostly about particle physics.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Communicator | Core | The Communicator is the person who has produced a Text on a Topic. 'In his book, Smithers discusses cotton production. ' |
| Text | Core | A set of propositions that is coherent in being about a Topic 'Sue bought a book about Pennsylvania' |
| Topic | Core | The Topic is what a Text is about. |
| Degree | Peripheral | This Frame Element marks expressions that indicate to which Degree the Text is about the Topic 'The article is mostly about yoga techniques' |
| Explanation | Extra-Thematic | The reason for which the Text or Communicator presents the Topic. |
| Manner | Peripheral | This FE marks expressions in which Manner the Topic is treated. 'The book carefully discusses the events leading up to the war' |
| Status | Peripheral | The Frame Element Status is used for expressions that indicate the relative importance of a Topic with respect to the other topics that a Text is about. 'The book is mainly about 19th century sewage systems' ' A … |
| Time | Peripheral | The time at which the Communicator produces Text on a Topic. |

**Frame relations** (super → sub)

- ReFraming_Mapping: Discussion → Topic
- See_also: Spatial_contact → Topic
- Using: Text → Topic

**Lexical units** (16): about.prep, address.v, concern.v, concerning.prep, cover.v, discuss.v, dwell (on).v, on.prep, refer.v, regard.n, regard.v, regarding.prep, subject.n, theme.n, topic.n, treat.v

## Toxic_substance  (frame id 1163)

A Toxic_substance causes death or harm when introduced into or absorbed by a living organism, the Victim. The Toxic_substance may be specified to be produced by or contained in a Toxin_source. The Toxic_substance may affect the Victim as a whole or a particular Body_part (understood here to include organs and other sub-systems). A Degree of harmfulness can be specified and the Toxic_substance may develop its effect only under particular Circumstances. 'The main product , sulphide , is toxic to cells ' 'They are better tolerated and are less toxic in overdose' 'The reason he was close to danger was because an extremely poisonous beetle was crawling down his shoulder.' 'Ingested gliadin and PT-gliadin are toxic to coeliac patients.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Toxic_substance | Core | This FE marks expressions that indicate the substance which potentially causes harm to a Victim. 'Highly toxic pollutants could be safely disposed of by burning them' |
| Toxin_source | Core | A living organism, object or process that produces a Toxic_substance. 'A young man was bitten by a poisonous snake and lives to tell about it.' |
| Victim | Core | The Victim is the being or entity that is capable of being harmed by the Toxic_substance. 'Chocolate can be poisonous for some types of pets.' |
| Body_part | Peripheral | The Body_part defines the part of the Victim's body that is harmed. 'This vitamin taken in excess could be poisonous for the liver' |
| Circumstances | Extra-Thematic | A set of circumstances, often the relative amount of the Toxic_substance that is present, under which the Toxic_substance is specified to have or lack a toxic effect. 'Some metals, such as copper and selenium, are … |
| Degree | Peripheral | Degree is the degree to which the Toxic_substance is harmful to the Victim. |
| Duration | Extra-Thematic | Temporal period for which the substance or source remains toxic to the victim. |
| Explanation | Extra-Thematic | A fact or action that explains why the Toxic_substance has a harmful effect on the Victim . |
| Type | Peripheral | Type identifies the kind or sort of Toxic_substance. |

**Frame relations** (super → sub)

- Using: Cause_harm → Toxic_substance

**Lexical units** (6): poison.n, poisonous.a, toxic.a, toxin.n, venom.n, venomous.a

## Trap  (frame id 2578)

A Deceiver sets up a Trap in order to cause a Victim to have an incorrect understanding about a situation. The Deceiver anticipates that this will lead the Victim to take a course of action (including doing nothing) which causes the Victim harm. 'Setting a trap for your opponents is usually a good strategy.' 'It's a trap!'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Deceiver | Core | The Trap is orchestrated by a Deceiver. |
| Trap | Core | The Trap is a device, strategy, or system designed to mislead and cause harm to a Victim. |
| Victim | Core | The Deceiver intends to mislead and cause harm to the Victim by means of the Trap. |
| Descriptor | Peripheral | A description of the Trap. |

**Frame relations** (super → sub)

- Inheritance: Trap → Prank
- Using: Intentional_deception → Trap

**Lexical units** (2): snare.n, trap.n

## Trust  (frame id 1731)

A Cognizer thinks that the Information given by a particular Source is correct. The specific Content or Topic of the Information may also be described. '' 'I don't trust this information.' 'Nobody will believe you, and people will think you're scum.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Cognizer | Core | The Cognizer is the person who has an opinion about the reliability of a Information_source or the Information from the Information_source. |
| Expressor | Core | An object or action associated with the Cognizer which is so affected by the Cognizer's belief that it reveals the Cognizer's state. 'Her trustworthy eyes revealed that I was in no danger.' |
| Information | Core | The text or speech which the Cognizer has heard and evaluates the truth of. 'America trusted his declaration , to their detriment .' |
| Information_source | Core | The individual that gives Information to the Cognizer. 'Why should we believe him ?' |
| Content | Peripheral | The Content denotes the mental content that the Cognizer is certain or uncertain about. |
| Degree | Peripheral | This FE indicates the Degree to which the Cognizer trusts the Source. |
| Manner | Peripheral | A description of an aspect of the Cognizer that also affects the nature of the trusting, or a general comparison of the state-of-affairs to others. 'She foolishly believed him .' |
| Topic | Peripheral | The Topic is the entity that a Cognizer trusts information about. |

**Frame relations** (super → sub)

- Inheritance: Certainty → Trust

**Lexical units** (10): believe.v, credence.n, credulous.a, faith.n, gullible.a, reliability.n, reliable.a, trust.n, trust.v, trustworthy.a

## Typicality  (frame id 1134)

A State_of_affairs is generally, or with regard to a particular Feature, representative of its class, which may be narrowed to a specific Comparison_set. 'The Elan truly is an unusual car; the first and only Lotus with a front engined/front wheel drive layout, and the first new Lotus to be introduced since 1975.' ' I need a plain, vanilla example that doesn't use PRINT! ' 'How smart is the average drug user/experimenter? ' 'It's not unusual to be loved by anyone, It's not unusual to have fun with anyone,' 'Is lying normal for a child this age, and how can I best handle this situation?'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Feature | Core | A property of the State_of_affairs wherein it differs or is similar to members of a Comparison_set. 'David Hasselhoff's daughters are normal in every way. ' |
| State_of_affairs | Core | The state of affairs which is evaluated with regard to whether it exhibits the essential characteristics of a Comparison_set. ' However I have always loved having an unusual name and I think it's a beautiful name. .' |
| Comparison_set | Peripheral | The set of indviduals, which are of similar kind to the Entity, and to which the Entity is compared. 'It's not unusual for interviewers to look beyond a resume and face-to-face meeting to find the unspoken clues about … |
| Degree | Peripheral | The extent to which the Entity varies from other members of the Comparison_set. 'That is a very unusual bear.' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Typicality
- Perspective_on: Instance → Typicality
- See_also: Typicality → Idiosyncrasy
- Using: Similarity → Typicality

**Lexical units** (13): abnormal.a, average.a, common.a, commonplace.a, conventional.a, curious.a, irregularity.n, normal.a, odd.a, ordinary.a, typically.adv, unusual.a, vanilla.a

## Undergo_change  (frame id 1172)

An Entity changes, either in its category membership, its situation, or in terms of the quality of an Attribute. In the first case, where category membership is changing, an Initial_category and a Final_category may be expressed. In the second case, where a situation as a whole is changing, an Initial_situation and a Final_situation can be present. And in the last case, where some characterization of the Entity is changing, an Initial_quality and a Final_quality can be specified. 'As soon as Tiffany kissed the frog, Tiffany turned into a frog. ' 'He chanted and the rock changed shape, becoming a great double bitted axe.' 'The College has changed markedly over the century since it first opened its doors.' 'If I'm understanding you correctly, you want the switchbar color to change whenever the bot says something?' 'My life instantly changed from an empty life, to a life full of joy and purpose.' 'As you can see, the word WALK changed from red to green rather than have a separate lens for each colour.' 'My feet turned to stone.' 'The promise will turn to ashes if progress is not made.' 'The price changed from $1.26 to $1.27 per pint. DNI' 'At least one relative instruction has changed in size from short to long.' In some cases, the types of perspective are mixed, so that, e.g., an Initial_quality is mixed with a Final_situation; this is usually considered poor style. 'She went from confused to acting completely confident .' This frame is often the target domain of motion metaphors, in which the moving Theme corresponds to the changing Entity, the Source of motion corresponds to the Initial_category, Initial_quality, or Initial_situation and the Goal of motion corresponds to the Final_category, Final_quality, or Final_situation of the Entity. By correspondence with the complex domain of motion, this metaphor introduces several FEs to the target domain of change, such as an Intermediate_state (etc.) from Path, and Tendency_of_change from Direction. 'The nation was crawling towards oblivion.' 'We were walking past almost reasonable and heading right for what-the-bleep.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The concrete or abstract entity that undergoes a change. 'How pleasing to see that Martha has changed now.' |
| Final_category | Core | The type of Entity that results from the change. |
| Initial_category | Core | The category that the Entity belongs to before it undergoes the change. 'The viccar changed from a professional clergyman into an anti-ecclesiastical activist.' |
| Attribute | Core-Unexpressed | A characteristic of the Entity for which a quality can be assigned or determined by calculation, measurement, or observation. 'Test to check if the color changes when you place your mouse over the JavaScript image' |
| Cause | Peripheral | An event or state that causes the change to take place. 'Doctors' practices have changed due to concerns over medical litigation.' |
| Circumstances | Extra-Thematic | The physical or abstract Circumstances under which the change takes place. 'Information may change whenever the US Department of Education issues additional guidance or regulations.' |
| Degree | Peripheral | The extent to which the initial and final categories, situations, or qualities differ from each other. 'Industrial economics has changed a lot during the last two decades' |
| Final_quality | Core-Unexpressed | The quality of the Attribute that results from the change. 'Its color changed from red to blue.' |
| Final_situation | Core-Unexpressed | The Entity's situation that results from the change. 'Tests went from taking three hours to needing less than one .' |
| Frequency | Extra-Thematic | This frame element is defined as the number of times an event occurs per some unit of time. |
| Initial_quality | Core-Unexpressed | The value of the Attribute before the change takes place. 'At that time, my asthma changed from very mild to severe.' |
| Initial_situation | Core-Unexpressed | The situation that the Entity began in. 'She slowly shifted from giving him makework to actually finding he had some skills .' |
| Intermediate_value | Extra-Thematic | A value that the Attribute assumes before the Final_value obtains. 'The slurry was stirred until the color of the suspension changed from red via orange to yellow over a period of two hours.' |
| Manner | Peripheral | Any description of the Change event which is not covered by more specific FEs, including epistemic modification (probably, presumably, mysteriously), secondary effects (quietly, loudly), and general descriptions … |
| Period_of_iterations | Extra-Thematic | The length of time from when the event denoted by the target began to be repeated to when it stopped. |
| Place | Peripheral | The location that the change takes place. |
| Time | Peripheral | The time at which the Entity undergoes the transformation. 'Then she turned into a lizard.' |
| Value_range | Core-Unexpressed | The Initial_value and Final_value taken together as the range through which the Entity changes. The main faith of the church has changed between Orthodox, Protestant and Greek Catholic several times. |

**Frame relations** (super → sub)

- Causative_of: Cause_change → Undergo_change
- Inheritance: Transition_to_state → Undergo_change
- Inheritance: Undergo_change → Improvement_or_decline
- Inheritance: Undergo_change → Nuclear_process
- Inheritance: Undergo_change → Undergo_transformation
- ReFraming_Mapping: Traversing → Undergo_change
- ReFraming_Mapping: Undergo_change → Undergo_transformation
- See_also: Transition_to_state → Undergo_change
- Using: Undergo_change → Progression

**Lexical units** (11): change.n, change.v, changeable.a, go.v, plummet.v, shift.n, shift.v, swing.v, transition.n, turn.v, veer.v

## Usefulness  (frame id 726)

An Entity aids in the successful completion of a Purpose. Its Degree of utility may also be expressed. Some of the lexical units in this frame (e.g. great, good) can only express permanent, generic states of the Entity. 'A box is an ideal storage device.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Entity | Core | The item which is useful for some purpose. |
| Purpose | Core | The kind of task which is promoted by the use or presence of the Entity. |
| Degree | Peripheral | The amount that the presence of the Entity aids in the completion of the (desirable) Purpose. |
| Domain | Extra-Thematic | This Frame Element marks expressions of a Domain or parameter with respect to which the Entity is useful. |
| Time | Peripheral | When the Entity is useful for a Purpose. |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Usefulness
- ReFraming_Mapping: Desirability → Usefulness
- Using: Capability → Usefulness
- Using: Using → Usefulness

**Lexical units** (23): effective.a, excellent.a, fantastic.a, fine.a, good.a, great.a, ideal.a, ineffective.a, marvellous.a, outstanding.a, perfect.a, splendid.a, strong.a, super.a, superb.a, terrific.a, tremendous.a, useful.a, utility.n, valuable.a, value.n, wonderful.a, work.v

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

## Wealthiness  (frame id 85)

A Person or Institution is being described in terms of their wealthiness, in other words the amount of money in their possession. 'Jess is very rich.' 'The university is wealthy.'

**Frame elements**

| FE | core type | definition |
|---|---|---|
| Institution | Core | A group which has (or lacks) possession of some resource. 'The company is bankrupt.' |
| Person | Core | The individual or individuals whose wealthiness is being described. 'Pat and Kim are completely broke at the moment.' |
| Degree | Peripheral | The degree of wealthiness (or poverty) of the Person or Institution. 'The most affluent landowners never pretended there was a democracy.' |
| Type_of_possession | Peripheral | A characterization of the entity (usually money) that the Person (or Institution possesses. 'We are rich in money, but poor Type_of_possession.' |

**Frame relations** (super → sub)

- Inheritance: Gradable_attributes → Wealthiness
- Using: Possession → Wealthiness

**Lexical units** (13): affluent.a, bankrupt.a, broke.a, impoverished.a, needy.a, poor.a, poverty.n, privileged.a, prosperous.a, rich.a, underprivileged.a, wealthy.a, well-off.a

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

