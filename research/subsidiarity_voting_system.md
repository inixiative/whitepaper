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

## Next Steps (before any of this graduates to §6)

- Decompose each concern further and prototype the **opinion-surface** sensing model in isolation — it is the most novel piece and the rest depends on it.
- Reconcile with the existing delegation model (§6.9) and jurisdiction routing (§6.10) rather than duplicating them.
- Run adversarial review specifically on the **re-run exclusion** (G) and the **automatic elector promotion** (E) — both are power-concentration surfaces.
- Resolve the open questions above, or explicitly mark them as experimental parameters for communities to set, consistent with the whitepaper's platform-humility principle.
