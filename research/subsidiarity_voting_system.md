# Design Note: The Subsidiarity Voting System

**Status:** Speculative design note — raw ideas captured for development, not settled mechanism.
**Epistemic label:** "this should work" (unproven), not "this works."
**Relation to core docs:** Extends and connects several mechanisms already in [`docs/03_mechanisms.md`](../docs/03_mechanisms.md) — §6.3 (Allocation & Voting), §6.7A (Leadership Accountability), §6.9 (Delegation & Agentic Participation), §6.10 (Jurisdiction & Overlap Resolution), §6.13 (Progressive Costs on Concentration). Nothing here should be promoted into §5/§6 until it is decomposed further and its open questions are resolved.

---

## Core Idea in One Sentence

Continuously map the surface of what a populace actually cares about — question by question, at every level of subsidiarity — and separate two distinct powers over that map: a **feedback power** everyone holds (is this going the right way?) and a **selection power** that must be **earned by accumulating delegated trust** rather than spent directly at will.

The system has two halves that reinforce each other:
1. **A sensing layer** that measures preference and preference *intensity* across an open-ended pool of questions, per jurisdiction level.
2. **A power layer** that distributes democratic agency as people become part of society, defaults to delegation over direct spend, and promotes trusted delegates into electors at higher levels.

---

## Decomposition: The Distinct Concerns

These are separate concerns that happen to travel together. Keeping them separate is the point — merging them is how governance systems accrete coupling.

### A. The Opinion Surface — an open-ended question pool

**Purpose:** Build a live map of what the populace cares about, not just how it splits on a fixed ballot.

- The pool of questions is effectively **infinite and open**. Anyone can submit a question — treat it as a free-speech surface, a "question pool" rather than a curated ballot.
- People answer in their **free time**, in whatever quantity they choose. Low participation on a question is itself signal (low salience), not failure — mirrors the engagement-threshold logic in §6.3.
- Each answer captures **more than direction**. At minimum:
  - **Direction** — agree / disagree (and possibly a "false / not important / malformed" escape hatch for junk questions).
  - **Care / importance** — how much do you care about this? How important do you think it is? This is the intensity dimension, and it is the load-bearing one: the goal is to *map the surface* of concern, and a surface needs magnitude, not just sign.
- The output is a **topography of concern**: a map showing where the populace's attention and intensity actually concentrate — which is a prerequisite for routing decisions to the right level (subsidiarity) and for judging whether leadership is moving with or against the grain of what people care about.

**Hard parts to flag:**
- Getting an honest **"how important is this?"** signal is genuinely difficult — importance is abstract and people anchor poorly. Needs design work (comparative/forced-tradeoff framing rather than absolute sliders, as §6.3's budget constraint does for magnitude).
- Filtering junk / false / bad-faith questions without becoming a censorship chokepoint. The "free speech question pool" and the "usable signal" goals are in tension.

**Connects to:** §6.3's three-dimensional voting (engagement, direction, magnitude). This is that idea turned into a *continuous sensing instrument* over an open question set, rather than a per-proposal vote.

### B. Levels of Subsidiarity and the Vote-Cost Multiplier

**Purpose:** Map concern *at each level* (neighborhood → city → county → state → national → global, ~6 levels), and structurally bias participation toward the local.

- The opinion surface is mapped **independently at each level of subsidiarity**. What the neighborhood cares about is a different surface from what the nation cares about.
- **Cost asymmetry as an incentive gradient:** votes are **cheap to spend locally** and **incur a multiplier cost at higher levels**. Acting nationally or globally should cost more of your budget than acting in your neighborhood.
  - Effect: people are incentivized to focus their finite budget where they have the most informational access and where their action is cheapest — i.e., locally. This is a *behavioral* implementation of subsidiarity, complementing the *routing* implementation in §6.10.
- Open framing from the source: "who knows" what the exact levels are or how steep the multiplier should be — treat both as experimental parameters.

**Connects to:** §6.10 (subsidiarity routing — routes decisions to the smallest competent scale) and §6.13 (progressive/convex costs on concentration). §6.10 routes *problems* down; this multiplier pushes *people's attention* down. They are complementary levers on the same principle.

**Tension to resolve:** A multiplier that makes higher levels expensive could also *disenfranchise* people on genuinely national/global issues (climate, defense) that are correctly national. The multiplier discourages overreach but must not starve legitimately higher-level concerns. Possibly the multiplier should scale with how *local* the issue actually is, not with the level per se.

### C. Two Registers of Power: Feedback vs. Selection

**Purpose:** Separate "saying whether things are going right" from "choosing who/what runs things." These are different powers and should not be the same token.

- **Feedback power (everyone holds this):** Most of what an ordinary participant's vote does is express **alignment** — are things going the right way? Are outcomes consistent with the goals of society? This is a continuous "is this aligned?" signal laid over the opinion-surface map, not a candidate selection.
- **Selection power (earned, not default):** The power to actually *select* things — participate as an elector in choosing leaders/initiatives — is a distinct, scarcer power that is **earned** (see E) rather than freely spent.

**Why separate them:** it lets the many act as a distributed alignment sensor (cheap, broad, always-on) while concentrating selection authority in those the many have chosen to trust — without collapsing into either pure direct democracy or pure representative democracy.

**Connects to:** §6.7A's "battery" model — leaders maintain power by continuously holding legitimacy. The feedback register is the natural input to that battery: broad alignment feedback continuously charges or drains leadership legitimacy.

### D. Delegation as the Default, Direct Spend as the Exception

**Purpose:** You should *not* be able to just spend your vote directly, all the time. The default posture is delegation.

- Each participant holds a set of votes/powers, one per level of subsidiarity (six levels → roughly six delegable powers), plus possibly distinct *kinds* of vote (see F).
- The expected behavior is to **delegate** these — especially the higher-level ones — to someone whose judgment you trust, rather than spending them yourself. You delegate your next-level-up vote, then the one above that, and so on.
- Direct personal spend is reserved for where you have strong, informed preferences (consistent with §6.9's "participate when you care, delegate otherwise"), and is cheapest locally (see B).

**Connects to:** §6.9 (layered delegation, instantly revocable, publish rationale, bounded chain depth). The new emphasis here is that delegation is the **default expectation at higher levels**, not merely an available convenience — the higher up the subsidiarity ladder, the more the system expects you to delegate rather than act directly.

### E. Earning Elector Status Through Accumulated Delegation

**Purpose:** Turn accumulated trust into graduated, earned authority at the next level up — the mechanism that promotes feedback-holders into selectors.

- When enough people delegate their trust to you — you accumulate a threshold number of delegates — you are **automatically promoted** to participate at the next level of subsidiarity as an actual **elector**: someone who takes part in *selection*, not just alignment feedback.
- This is how democratic power is **imbued as people become part of society**: you start with feedback power; sustained, accumulated trust from others elevates you into selection power at higher levels.
- Promotion is **automatic and threshold-based** — cross the delegate count, gain the seat. No appointment, no election in the classic sense; the delegation graph itself confers the standing.

**Open questions (explicitly unsettled in the source):**
- Does becoming an elector at level N also grant elector standing at **all levels below** N? ("Who knows — that's an unknown question.")
- What is the threshold, and is it absolute or relative to the population at that level?
- Does the promotion decay if delegated trust erodes? (Presumably yes, to stay consistent with continuous accountability, but unspecified.)
- How does this interact with §6.9's **max delegation-chain depth** (currently ~2 levels)? A six-level promotion ladder may need a different chain-depth model, or the two need to be reconciled.

**Connects to:** §6.9.1 (representative matching) for *how* people discover whom to delegate to; §6.7A for the accountability the promoted electors are then subject to.

### F. Divided Vote — distinct kinds of vote, separately delegable

**Purpose:** Not everyone needs or wants the same thing, so a single undifferentiated "vote" is too coarse. Split the vote by function.

- Candidate split from the source: a **rejection vote** (power to reject / withdraw legitimacy — the "is this going wrong?" veto register) versus a **process vote** (power over how things should proceed / be selected).
- Each *kind* of vote can be **delegated independently** — you might delegate your process vote to one trusted person and retain or differently-delegate your rejection vote.

**Connects to:** §6.7A's support/oppose asymmetry (the opposition-premium / opposition-discount ratios). A distinct, separately-delegable rejection vote is a natural home for the "withdraw legitimacy" half of that mechanism.

**Flag:** the exact taxonomy of vote-kinds is unsettled — "rejection" and "process" are the two named so far; there may be more, and they should be discovered by interrogation, not asserted.

### G. Alignment Guardrails and Exclusion

**Purpose:** Ensure leaders who are persistently misaligned are *structurally barred*, not merely voted down — breaking the "trade the second-worst option back and forth" trap.

- The opinion-surface map (A) plus the feedback register (C) yield a continuous read on whether leadership is **moving in the direction the populace actually cares about**.
- **Exclusionary guardrail:** if those in charge are **consistently off-base and moving in the wrong direction** relative to that alignment signal, they **cannot run again**. Persistent misalignment is disqualifying, not just penalizing.
- Intent: prevent the failure mode where a population is stuck alternating between two equally-unaligned options ("the second-worst option, traded back and forth"). Real alignment must gate continued eligibility.

**Connects to:** §6.7A generally (battery-model removal) and §6.7A's accountability sections. The new element is a **hard eligibility bar** driven by sustained misalignment — a step beyond automatic removal, into automatic *ineligibility to re-run*.

**Tension to resolve:** a re-run ban is a powerful exclusion and a capture/abuse surface — who defines "consistently off-base," over what window, and against whose stated goals? This needs the same adversarial scrutiny §6.12 applies to anti-capture mechanisms, or it becomes a tool for removing rivals.

---

## How the Halves Fit Together

```
                 OPINION SURFACE (per subsidiarity level)
   open question pool → {direction, care/importance} → topography of concern
                 │                                        │
                 ▼                                        ▼
         FEEDBACK REGISTER                        ALIGNMENT SIGNAL
   "is this going the right way?"          "are leaders moving with the grain?"
        (everyone holds)                              │
                 │                                     ▼
                 │                            EXCLUSION GUARDRAIL
                 │                    persistent misalignment → cannot re-run
                 ▼
          DELEGATION (default)  ──accumulate delegates──▶  ELECTOR STATUS
     cheap locally, multiplier up          (threshold-based promotion)
       divided by vote-kind                  participate in SELECTION
```

The sensing layer feeds both the everyone-holds feedback power and the earned selection power; delegation is the pump that moves trust up the subsidiarity ladder and converts feedback-holders into electors.

---

## Consolidated Open Questions

Carried directly from the source's own "who knows" markers, plus tensions surfaced above:

1. **Levels:** What are the exact subsidiarity levels, and how steep is the vote-cost multiplier between them?
2. **Multiplier vs. legitimate scale:** How to bias toward local *without* disenfranchising genuinely national/global concerns?
3. **Importance elicitation:** How do you get an honest, comparable "how much do you care?" signal at scale?
4. **Question-pool integrity:** How to keep an open, free-speech question pool while filtering junk/bad-faith questions without a censorship chokepoint?
5. **Elector scope:** Does elector status at level N include all levels below? What's the threshold, and does it decay?
6. **Chain depth reconciliation:** How does a six-level promotion ladder coexist with §6.9's max-chain-depth-2 rule?
7. **Vote-kind taxonomy:** Beyond "rejection" and "process," what other distinct, separately-delegable vote-kinds exist?
8. **Exclusion authority:** Who defines "consistently off-base," over what window, against whose goals — and how is that guardrail itself protected from capture?

---

## Stress Test — Adversarial Analysis

Red-team pass. Each mechanism is attacked on its own terms, then the composite is attacked for emergent failure. The goal is to find the *specific* ways these break, not to list generic Sybil/KYC boilerplate. Verdicts are blunt on purpose.

### A. The Opinion Surface — **fails on agenda-setting and cheap talk**

- **The real power is question-surfacing, and it is unaddressed.** An "infinite open pool" does not democratize the agenda; it makes agenda-setting a flooding contest and hands the actual power to whatever **ranks/surfaces** the questions people see. That ranking function *is* the government. The map is not "what the populace cares about" — it is "what the surfacing algorithm showed them." The most important design decision in the whole sensing layer is the one the note doesn't make.
- **Unbudgeted importance is worthless.** People answer "in their free time, in whatever quantity" — that is **cheap talk**. §6.3's magnitude signal works *only because points are scarce and must be traded off*. Strip the budget and everyone rates everything they touch as important; the "care" dimension — the load-bearing one — collapses into noise. Either the surface inherits §6.3's budget (and then it is just §6.3, not a new instrument) or it measures nothing.
- **The map is of the loud, not the populace.** Answering-in-free-time selects for the retired, the enraged, the ideologically mobilized, the online. Systematic sampling bias, correlated with exactly the political extremity the system claims to filter. A voluntary-response instrument cannot map a population.
- **Manufactured salience.** Because "low participation = low salience" is the filter, any faction that can mobilize participation manufactures the appearance of genuine concern. The topography is sculptable by anyone who can organize a mailing list. And the junk-filter ("false / not important") is itself a brigadable downvote-to-suppress weapon.
- **Verdict:** The sensing layer is the foundation everything else stands on, and it is the softest. It needs a budgeted, sampled (not self-selected), capture-resistant surfacing model before anything built on top of it means anything.

### B. The Vote-Cost Multiplier — **regressive, and backwards on collective action**

- **It taxes exactly the problems that most need higher-level coordination.** Climate, pandemics, defense, monetary policy — the highest-stakes issues are national/global *by nature* because they are collective-action problems no locality can solve. A multiplier that makes higher levels expensive is an **anti-collective-action tax on collective-action problems**. If anything the gradient is backwards: local coordination is already cheap; the subsidy should flow to the hard, higher-level coordination, not away from it.
- **It is plutocratic in vote-budget.** "Higher levels cost more" means national reach is rationed by budget: whoever has the most points (or hoards local ones) buys national influence, and the budget-poor are confined to their neighborhood. It manufactures a class system of political *reach* — the opposite of the anti-plutocracy goal — and does it while wearing subsidiarity's clothing.
- **Jurisdiction-shopping.** If local is cheap, reframe a national push as a thousand coordinated local ones (or vice versa) to dodge the multiplier. The "what level is this issue?" call becomes a gamed chokepoint — and §6.10 already admits that call is unsolved.
- **Verdict:** Sound *intuition* (bias toward the local, where information is best), wrong *instrument*. A flat per-level cost gamed by classification, or a cost that scales with an issue's actual locality rather than its nominal level, are both closer — but this needs redesign, not tuning.

### C. Feedback vs. Selection — **risks being consultative theater**

- **Feedback without a hard coupling to selection is a pressure valve.** Give the many a broad "is this going right?" register while the earned electors hold the actual selection lever, and you have representative democracy plus a satisfaction survey. Unless the feedback signal *mechanically* binds the selectors (charges/drains their standing on a short leash), it launders legitimacy: people feel heard while power sits elsewhere. The note gestures at "feeds the battery" but specifies no binding — an elector class can ignore feedback as long as its delegate count holds (see E).
- **Verdict:** The split is only meaningful if feedback has teeth over selection. As described, the teeth are missing.

### D. Delegation-as-Default — **a concentration engine pointed against subsidiarity**

- **Mandatory-ish delegation pushes trust UP; subsidiarity pushes concern DOWN. They fight.** The system's stated telos is decentralization, but its default posture (delegate, especially at higher levels) is a mechanism for **concentrating** trust upward. This is not a side effect; it is what delegation *is*.
- **Revocability is theater at scale.** "Instantly revocable" is individually true and collectively meaningless: when an elector's power rests on thousands of delegations, no single revocation moves the outcome, so the check never fires (classic collective-action problem). A revocation that changes nothing is not accountability.
- **Delegation is transferable influence, therefore a market, therefore buyable.** Publish-your-rationale (§6.9) does nothing against private side-payments for delegation. Vote-buying reappears as delegation-buying.
- **Verdict:** Delegation is load-bearing for scale but structurally centralizing. Without a hard cap on how much delegated power any node can hold, it is an oligarchy pump.

### E. Earned Elector Status — **the single most dangerous mechanism; an oligarchy generator**

- **It measures popularity and calls it judgment.** Nothing in "accumulate N delegates → auto-promote" measures *judgment*; it measures **delegate count**, which is a popularity/mobilization metric. This is precisely the selection pressure that produces demagogues, machine politicians, and influencers. The note claims the ladder elevates "enough people trust your judgment"; the mechanism elevates whoever is best at *accumulating trust*, which is not the same thing and is often its enemy.
- **Preferential attachment → power law.** Electors get visibility and power, which attracts more delegations, which is more power. Rich-get-richer. The delegate distribution goes heavy-tailed; a handful of super-electors capture most trust. The mechanism whose stated purpose is *distributing* democratic power will, left alone, *concentrate* it.
- **Threshold + automatic promotion = installable by any organized bloc.** A church, union, party, or influencer that can mobilize N delegations installs its own electors. Sybil-resistance (real distinct humans) is necessary but nowhere near sufficient — real people organize. This rebuilds the party machine with extra steps.
- **Direct contradiction with §6.9.** §6.9 caps delegation chains at depth ~2 *specifically to prevent this cascade*. A six-level auto-promotion ladder **is** a deep delegation cascade. The two mechanisms cannot both be true; one has to give.
- **Verdict:** As stated, this manufactures an unaccountable political class. It needs, at minimum: a hard cap on delegated power per node, a decay so standing must be re-earned, a quality gate that is not popularity, and reconciliation with §6.9's depth limit. It may not be salvageable in "automatic promotion" form.

### F. Divided Vote — **multiplies the attack surface; may be a false split**

- **Separately-delegable vote-kinds multiply the delegation markets** — now there is a market per kind — and making the **rejection vote** tradeable is the worst case: concentrated delegated rejection power is a **purge weapon**.
- **The split may be incoherent.** Rejecting X is often just a process-preference for not-X; the two are not cleanly orthogonal. Independent delegation lets your agency self-cancel (reject-delegate to a nihilist, process-delegate to a builder).
- **Complexity is itself the capture surface.** Six levels × multiple vote-kinds × per-kind delegation is enormous cognitive load — the exact thing §6.9 exists to reduce. High load means almost everyone accepts defaults, and **whoever owns the defaults wins**. Added expressiveness that no one can use is power relocated to the parameter-setter.
- **Verdict:** Only justified if a specific, orthogonal decomposition earns its complexity. "Rejection/process" is asserted, not derived; interrogate whether the split is real before paying for it.

### G. Alignment-Based Re-Run Exclusion — **a capturable purge tool that punishes correct-but-unpopular leadership**

- **It self-contradicts §6.7A's own thesis.** §6.7A holds up Lee Kuan Yew — decades governing *against* short-term popular preference — as the model of merit-based tenure. An eligibility bar keyed to "moving with the grain of expressed preference" would have **excluded him**. The mechanism structurally punishes counter-majoritarian courage and selects for pandering. It fights the very section it cross-references.
- **It inherits every flaw of the sensing layer.** "Consistently off-base" is defined against the opinion surface (A). A is capturable via question-surfacing; therefore whoever controls surfacing controls who is branded "misaligned" and thus **barred from running**. This is the most capturable object in the system: control the map → control eligibility → purge rivals under color of accountability.
- **No neutral ground truth for "aligned."** "The goals of society" is either the opinion surface (capturable) or a fixed charter (capturable at authorship). Arrow and value pluralism say there is no coherent societal preference vector to be aligned *to*. The metric is contestable by construction, and once it gates power every faction litigates it.
- **Goodhart, terminally.** The instant an alignment score gates eligibility, it stops measuring alignment and starts measuring "ability to appear aligned near the evaluation window." Window-gaming (align at review, do the necessary-unpopular thing far from it) is trivial.
- **Verdict:** The most dangerous mechanism in the set. A hard exclusion driven by a capturable, gameable, philosophically-incoherent metric is a weapon, not a guardrail. If retained at all it must be (a) driven by *outcome* measures, not expressed-preference alignment, and (b) fenced with §6.12-grade anti-capture scrutiny.

### System-Level — the emergent failures are worse than the parts

- **The capture ratchet A → G → E → A.** Capture question-surfacing (A) → define who is "misaligned" and bar them (G) → your delegates face a thinned field and promote (E) → your electors influence surfacing (A). Each mechanism is a vector alone; **composed, they close into a self-reinforcing loop.** A captured surface doesn't just distort the map — it selects the rulers and purges the opposition. This is the finding that matters most: the mechanisms are individually risky and jointly a ratchet.
- **Net power vector points up, not down.** B and §6.10 push concern *down*; D and E push trust and *formal selection power up*. Formal power (selection, exclusion) lives at the top of the ladder, so the up-flow dominates. The system is **subsidiarist in rhetoric, centralizing in mechanism.**
- **Goodhart on the core instrument.** The opinion surface is the system's one sensor. The system then wires that sensor to real power (electors, exclusion). The moment a measure gates power it ceases to be a measure. The design corrupts its own instrument by using it.
- **Reflexivity.** Publishing "what the populace cares about" changes what the populace cares about (bandwagon, spiral of silence). The sensor perturbs the system it measures; expect herding and manufactured consensus, not a stable map.
- **Complexity is the master vulnerability.** Infinite questions × 6 levels × a multiplier × 2 registers × default delegation × multiple vote-kinds × auto-promotion × exclusion is a system no participant can model — which means power flows to whoever *can*: the parameter-setter, the question-surfacer, the author. This violates §6.15's humility principle directly. Complexity is not neutral; it is anti-democratic, because it relocates power to the meta-level.

### Severity Ranking

| # | Mechanism | Failure | Severity |
|---|-----------|---------|----------|
| 1 | E — auto-promotion | Oligarchy/party-machine generator; measures popularity as judgment; contradicts §6.9 | **Critical — redesign or drop** |
| 2 | G — re-run exclusion | Capturable purge tool; punishes correct-but-unpopular leaders; contradicts §6.7A | **Critical — redesign or drop** |
| 3 | A→G→E loop | Composed capture ratchet | **Critical — emergent** |
| 4 | A — opinion surface | Real power is surfacing (unaddressed); unbudgeted importance is cheap talk; loud ≠ populace | **High — foundation is soft** |
| 5 | B — multiplier | Regressive; taxes collective-action problems backwards | **High — wrong instrument** |
| 6 | D — delegation default | Centralizing; revocability theater; buyable | **Medium-High** |
| 7 | System complexity | Relocates power to parameter-setter; violates §6.15 | **High — cross-cutting** |
| 8 | F — divided vote | Multiplies markets; possibly false split; load | **Medium** |
| 9 | C — feedback/selection | Consultative theater without hard coupling | **Medium** |

### What survives

- **The intuitions survive; most of the mechanisms do not.** Worth keeping: (i) map preference *intensity*, not just direction; (ii) bias participation toward where information is best (local); (iii) make legitimacy continuous, not election-day. All three already live in §6.3/§6.7A/§6.10 in more defensible form.
- **The two mechanisms that are genuinely novel (E auto-promotion, and the A opinion-surface-as-instrument) are also the two most broken.** That is where the design work has to go, or the novelty isn't worth its risk.
- **The exclusion guardrail (G) should probably be inverted:** bar on demonstrated *bad outcomes / abuse*, never on *disagreement with expressed preference* — otherwise it is a machine for punishing the leaders §6.7A says you most want to keep.

## Next Steps (before any of this graduates to §6)

- Decompose each concern further and prototype the **opinion-surface** sensing model in isolation — it is the most novel piece and the rest depends on it.
- Reconcile with the existing delegation model (§6.9) and jurisdiction routing (§6.10) rather than duplicating them.
- Run adversarial review specifically on the **re-run exclusion** (G) and the **automatic elector promotion** (E) — both are power-concentration surfaces.
- Resolve the open questions above, or explicitly mark them as experimental parameters for communities to set, consistent with the whitepaper's platform-humility principle.
