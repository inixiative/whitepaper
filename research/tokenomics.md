# RESEARCH REPORT: Platform Base Token & Store-of-Value Architecture

**Prepared:** July 2026
**Purpose:** Consolidate a design conversation between the architect and Claude into a
self-contained specification an implementer or a follow-on research agent can pick up
without needing the source conversation. This document is a **research/design
artifact**, not whitepaper prose — nothing here should be copied into
`docs/01_diagnosis.md`, `docs/02_specification.md`, or `docs/03_mechanisms.md` without
separate review. Its purpose is to hand off a coherent mechanism design, including its
genuinely unresolved parts, to whoever works on it next.

**Status discipline used throughout this document:** every claim is marked **RULING**
(architect has decided, stated explicitly, don't re-litigate), **READY** (a concrete
mechanism, load-bearing, believed sound, not yet stress-tested by an adversarial
review), **PROPOSED** (a candidate answer to an open question, not yet ratified), or
**OPEN** (a genuine unresolved decision — do not assume an answer and do not silently
pick one while drafting). This distinction is load-bearing for this whole design; do
not flatten it in service of a cleaner-reading document.

---

## 1. The problem this solves

`docs/03_mechanisms.md` §6.12A (~03:2004) already establishes a kWh-backed token as the
platform's transactional "economic lubricant" — elastic supply pegged to real energy
production, deliberately *not* a savings vehicle. §6.12A is explicit that this is only
half a monetary system (03:2058):

> "The kWh system is incomplete without a store of value alongside it... The system
> explicitly recommends holding wealth in a scarce, hard-capped asset (Bitcoin, gold, or
> equivalent) rather than in kWh tokens."

The whitepaper currently punts the store-of-value half to external assets (Bitcoin,
gold). This document is the design work asking: **can the platform supply its own
store-of-value instrument, one that is asset-backed by the platform's own economic
activity rather than an external commodity, without recreating the failure modes
(Cantillon extraction, reflexivity, plutocratic capture) the rest of the whitepaper
spends hundreds of pages diagnosing?**

The design that follows is the second of two attempts at "back money with something
real" — the first being the kWh/energy standard already in the paper. Naming the
lineage matters: the failure modes recur across both attempts, in different clothes.

---

## 2. Where the design landed, in one paragraph

The platform's base token is **not a currency minted against a valuation** — it is an
**asset-backed index fund**: a claim on a pro-rata slice of every tokenized asset on
the platform. It gains value the way a Uniswap LP token does (a cut of every trade
accrues to the pool), not through minting. New tokens enter through **three
simultaneous legs at one Vickrey-cleared price** — external capital, platform
trade-tax revenue, and an ETF-style "creation unit" mint against a real asset actually
entering the basket — never against a self-reported number. The architect then made
two further, explicit reversals on top of this: the platform token is not
economic-only (it also carries governance), and it is not just one instrument among
several (it is also the platform's unit of account — "the dollar"). The result is a
single token that is simultaneously currency, index-fund share, and voting right — a
**deliberate, named linear plutocracy** ("this is the democratic play,
fundamentally"), defended on the grounds that concentrated *accountable* capital
voting directly is better than the status quo of concentrated *unaccountable* capital
voting through custodians (BlackRock/Vanguard/State Street). Whether that
vote-conversion should be linear or dampened is the one major parameter left
genuinely open.

---

## 3. Design lineage (read this before the mechanism — it explains *why*, not just *what*)

Three attempts at the same underlying problem, in order:

1. **Energy-Standard article** (external source, pre-dating this design thread): "back
   money with something real."
2. **kWh token** (§6.12A, already in the whitepaper): answer #1 — back the
   transactional currency with real energy production. Explicitly leaves store-of-value
   unsolved (03:2058, quoted above).
3. **This design** (base/platform token): answer #2 — back a *store-of-value*
   instrument with the actual tokenized assets running on the platform, rather than
   with energy or an external commodity.

The mechanism below evolved through several rounds of proposal → adversarial
stress-test → revision. That history is preserved in-line because the failure modes
found at each step are the reason the current guardrails exist — skipping straight to
"the final design" would drop the reasoning for why each guardrail is there, which the
next person needs in order to know which guardrails are load-bearing vs. incidental.

---

## 4. The base token: asset-backed index, not conjured currency (READY)

**Core claim.** The base token is an index of all individually-tokenized platform
assets — a claim on a pro-rata slice of the basket — not a currency conjured against a
valuation. Some constituents depreciate (most tokenized assets), some appreciate
(trust-fund shares, etc.); net, it behaves like a diversified platform-economy index,
not a hard-capped store of value in the gold/Bitcoin sense. Tokenization's whole point
is liquidity: assets are not locked, and the token itself is generally resellable
(per-asset resale delays are configurable, but the liquid majority is what makes the
index tradeable).

**An earlier version of this idea was explicitly rejected.** The architect first
proposed minting the base token directly against each Vickrey *valuation* — i.e., use
the auction price itself as a mint trigger. This was correctly abandoned: it is a
self-referential mint (the token's supply depends on a price that the token's own
scarcity then influences) and is exactly the reflexivity trap described in §7 below.
The final design routes around this by making the auction a **pricing mechanism**, not
a **minting trigger** — see §6.

**Value accrual mechanism — a trade tax, and it is a proven pattern, not a speculative
one.** "Whenever an asset is sold or traded, you take a part of it; that tax is what
drives the value of the index." This is structurally a Uniswap-style liquidity-pool
token, generalized from crypto trading pairs to tokenized real-world assets: an LP
token is a claim on a pooled basket, every trade pays a fee that accrues into the
pool's value, and holders never need anything *minted* for the token to appreciate —
fee flow does the work. This is a materially stronger "proven at scale, not
speculative" citation than anything currently in §6.12A, and should be cited directly
by name when this gets written up formally.

**Asset-backed via platform co-ownership — and the platform never has to assert a
price.** For real-world assets, the platform itself becomes a part-owner: at a
lifecycle checkpoint, the asset is co-bought, with the Vickrey auction winner taking
one slice and the platform another (an open knob, informally discussed as possibly
under 10%). This is the mechanism's most elegant property: the platform *rides* the
arms-length Vickrey-cleared price rather than running its own valuation. It never
asserts "this is worth X" — it co-invests at the price a real, motivated bidder just
proved. This is also what converts the token from a synthetic claim on trade-tax flow
into a genuinely asset-backed instrument, which is the mechanism that fixes the
closed-end-fund discount problem (§9).

---

## 5. Issuance: the three-way split (READY — the safe-minting answer)

When an asset enters or grows the basket, new tokens are created through **three legs
priced at one shared clearing price**:

1. **External capital.** The Vickrey auction winner injects genuinely new outside
   capital at the cleared price.
2. **Platform trade-tax revenue.** The platform injects its own accumulated
   trading-tax revenue (from §4) at that same price.
3. **The creation-unit mint.** The original asset owner delivers the asset itself in
   exchange for newly minted tokens representing their now-diluted stake in the
   larger pool.

Leg 3 is not "printing against nothing" — it is precisely the **ETF creation-unit
mechanism**: an authorized participant delivers the underlying basket and receives
newly created shares sized so NAV-per-share does not move. Real-world ETFs create and
redeem on the order of trillions of dollars of assets this way, continuously, without
it being considered inflationary, because issuance is always balanced against real
value entering on the other side of the ledger at the same instant.

**The rule that makes this safe, stated precisely:** mint *only* as a creation-unit,
balanced on both sides of the ledger, at that moment, never against a promise, a
self-reported number, or the token's own price. An earlier, stronger version of this
rule ("never mint at all") was too strict — it is the *unbalanced* mint (the platform
conjuring tokens to fund its own buy-in, or minting against a future/promised value)
that is dangerous, not minting per se.

**Consequence: Vickrey integrity becomes the single most load-bearing piece of the
entire design, worth over-engineering relative to everything else.** The cleared price
is no longer just a reporting mark; it is the literal exchange rate determining how
many tokens get created across all three legs simultaneously. An inflated price
doesn't just mis-mark one asset — it over-issues tokens against it and dilutes every
holder in the entire basket, while the platform simultaneously overpays for its own
buy-in slice. Collateral value, platform ownership stake, and issuance rate all
inherit their correctness from one number. Commit-reveal on-chain bidding, staggered
checkpoints, and anti-collusion detection on the bidder pool are worth more
engineering investment than any other part of this stack — see §6.

**A tunable knob against common ownership.** The more of each basket-entry event that
leg 3 (mint) covers, the less of its own capital the platform must spend on leg 2
(direct ownership) to keep growing the basket. "How much does the platform literally
own of everything" is therefore a configurable ratio between the mint slice and the
platform-buy slice, not a fixed structural feature — expose it as a tunable parameter.
This ratio directly affects the common-ownership/referee conflict named in §7.

---

## 6. The Vickrey mechanism: from mint-trigger to honest NAV mark (READY)

A second-price sealed-bid (Vickrey) auction on roughly 10% of an illiquid asset, run at
lifecycle checkpoints, makes the clearing price a *truthful* signal — the dominant
strategy under Vickrey rules is to bid your true value, since you pay the second-highest
bid regardless of your own. This is the same lineage as §5.3's Harberger/Radical
Markets material (03:187), but it corrects Harberger's known perverse incentive: pure
Harberger continuously exposes 100% of an asset to forced sale at your own
self-assessed price, which punishes honesty. Exposing only ~10% at a periodic
checkpoint gives an honest price signal without betting the whole position.

**Under the index reframe, Vickrey is not obsolete — it becomes more necessary,** as
the periodic *marking* function that keeps the fund's NAV honest. This is the identical
problem private equity and venture funds face marking illiquid holdings between
liquidity events — a documented abuse vector, since NAV drives fundraising and fees, so
self-reported marks skew high. The Vickrey checkpoint supplies a periodic, adversarial,
non-self-reported mark, which is exactly what that literature says is missing from the
PE/VC marking process.

**Why smart contracts make this newly possible — a genuine claim, not marketing.**
Classical Vickrey auctions have a trust hole: the auctioneer can lie about what the
second-highest bid actually was. An on-chain commit-reveal scheme (bidders submit
hashed bids, reveal after close, a smart contract computes the second-price outcome
deterministically and verifiably) closes this hole cleanly and is a real "why now"
argument for doing this on a blockchain rather than through a traditional auction
house.

---

## 7. Load-bearing failure modes and their fixes (guardrails — READY, treat all as required, not optional)

Each of these was surfaced adversarially against an earlier version of the design and
should be treated as a required constraint, not a nice-to-have:

- **Reflexivity (Terra/Luna, ~$40B lost in a week).** Any loop where the token being
  priced and the token doing the pricing are the same asset death-spirals. Fix:
  distinguish the safe mint (leg-3 creation-unit: real asset delivered, new tokens
  issued, balanced both sides) from the dangerous mint (the platform conjuring base
  token to fund its own buy-in leg — QE-on-itself). Fund the platform's buy-leg only
  from realized trading-tax revenue, never from minting, so no leg can bootstrap
  another.
- **Thin-reference-price manipulation (LIBOR → SOFR).** A once-off 10% auction with
  massive downstream leverage riding on it has LIBOR's exact shape — a single nudged
  auction here distorts the whole money supply, not one loan. Fix: mark and value
  against a rolling, staggered series of small auctions across many independent
  assets (time-weighted, the same fix that replaced LIBOR with SOFR), never a single
  point-in-time snapshot.
- **Minority/marketability discount, linearly extrapolated.** A non-controlling
  illiquid 10% slice will clear at a discount to true per-unit value; multiplying that
  price by 10 to imply a whole-asset value systematically misprices the whole. Fix for
  any collateral use: a pre-declared haircut / LTV below 100%, the standard lender
  margin against exactly this effect.
- **Closed-end fund vs. ETF (redemption discount).** With no redemption right into the
  basket, expect a persistent 10–20% discount-to-NAV, the way closed-end funds trade
  for years below their stated NAV. See §9 for the chosen answer (burn-on-cash-out).
- **Index-inclusion gaming (the S&P 500 "index pop" effect).** If inclusion in the
  base index is itself valuable (instant liquidity, whole-platform trading volume),
  creators will inflate their marked value right before entry. Fix: inclusion marking
  uses the same staged, multi-checkpoint Vickrey process as ongoing marks, never a
  single self-reported number at entry.
- **Adverse selection / Akerlof lemons in the platform's co-buy.** If the platform
  auto-buys a fixed slice at the cleared price, owners of genuinely appreciating
  assets will keep more of theirs (minimizing what they auction), while owners of
  declining or overhyped assets sell more into the co-buy — the basket quietly tilts
  toward lemons over time. **This makes the co-buy percentage not a free knob** — it
  needs an incentive-compatibility analysis before being set (open decision, §12).
- **Common ownership + referee conflict (Vanguard/BlackRock/State Street; see Azar,
  Schmalz & Tecu on common ownership softening competition).** Owning a slice of every
  asset softens competition among them — and this is *worse* here than for an index
  fund manager, because the platform also runs the voting, sunset reviews, and dispute
  resolution for the same assets it partially owns (common ownership *plus* being the
  referee — the same conflict as an exchange owning its own listings, or a search
  engine ranking its own products). Fix: reuse §4.7's wealth-power firewall pattern on
  the platform's own holdings specifically — cap cumulative platform ownership
  per-asset and per-portfolio, and strip or firewall any governance voting rights
  attached to the platform's own passive stake (owning a sliver of an asset should not
  translate into a vote on that asset's own sunset or dispute).

**Reuse, don't reinvent, on timing/liquidity lag.** Wherever value must be recognized
before it is realized (e.g., crediting against not-yet-verified initiative value), do
not design liquidity-timing from scratch — reuse §6.12A's escrow-buffer pattern
wholesale: pre-credit against fully-escrowed forward collateral, release the escrow as
value verifies, substituting "verified initiative value" for "verified energy
production." This is directly relevant to open decision §12.3 below (recognize value at
proposal-creation vs. only at maturity).

---

## 8. Token structure: three orthogonal instruments, not two (RULING)

An early version of this design proposed a simple economic/governance split for the
base token — modeled on dual-class equity (Google's Class A/B/C structure) and crypto
precedents (MakerDAO's MKR is governance-weighted; Curve's veCRV requires locking to
get vote/boost, kept separate from the liquid economic token). That version made the
base token purely economic, with governance handled by a separate instrument. **This
was superseded** (see §9) for the platform-level token specifically, but the underlying
per-initiative structure survived and is the current ruling:

- **Per-initiative tokens.** Each initiative issues its own token(s) — economic
  and/or governance, per its own configured structure, following §4.23's
  differentiated-cohort-architecture pattern. Voting on that initiative's own
  lifecycle, sunset, or dispute resolution is scoped to that initiative's own token,
  under rules that initiative itself sets.
- **The platform token.** The base/index token from §4–§7 above. Carries
  platform-level governance only — voting on the platform's own rules, parameters,
  fee structure, and the tunable knobs this document exposes (mint/buy ratio,
  haircuts, KYC tiers) — **never** a vote on any individual initiative's internal
  affairs.
- **The separation of powers this produces.** Economic interest in the basket
  (tradeable, carries no vote anywhere) is one right; governance of one initiative
  (that initiative's own token, scoped to it, configurable) is a second; governance of
  the platform itself (the platform token, scoped to the platform, never reaching into
  any single initiative) is a third. Three orthogonal rights, three separate
  instruments or scopes, no instrument doing double duty within an initiative's own
  affairs. This prevents a platform-token holder from ever outvoting an initiative's
  own community on that initiative's own business — a subsidiarity property (ties to
  §4.8, Enforce Subsidiarity) applied to token design.

**A hard regulatory constraint that must be resolved before launch, not after.** A
fungible, freely tradeable token representing a pooled economic interest in a basket,
sold to a broad base, managed by a platform that takes a cut of trades, is close to the
textbook *Howey* fact pattern for a security (investment of money, common enterprise,
expectation of profit from the efforts of others). §6.2 already anticipates
jurisdiction/KYC-tier complexity in the abstract (03:356 area); this document's
specific instrument is the concrete case regulators care about most, and needs an early
legal read, not a launch-time one.

---

## 9. Governance reversal: the platform token reunifies currency and vote (RULING — the central design decision of this document)

This is the single largest revision in the whole design thread, made deliberately and
on reflection, not by accident. It overrides both §8's per-platform economic/governance
split *and* an earlier guardrail (that auctions should clear in an external reference
asset). Preserve this reasoning carefully — it is the part of the design most likely to
draw pushback from a reviewer comparing it against the whitepaper's own
anti-plutocracy machinery (§4.7, §5.3), and it needs to be defended on its actual
merits, not smoothed over.

**Step 1 — the platform's voting token is also the instrument used to buy into
Vickrey auctions.** Capital deployed to win a real-asset auction slice converts
directly into governance power over the whole platform — not an incidental
side-effect requiring a firewall, but the marketplace's literal entry requirement. This
is tighter than an ordinary liquid governance token (where "rich people can also buy
UNI/MKR on the open market" is true but incidental): here, you cannot transact in the
core marketplace *without* holding the governance instrument. Note the feedback loop
this creates: token price and real-asset-auction activity move each other in both
directions, so a governance crisis that depresses the token price makes it cheaper in
real terms to win real-asset auctions — a governance failure could trigger a buying
spree on real collateral at an effective discount. (Where spent tokens go — back to
the seller, burned EIP-1559-style, or to a treasury — changes this dynamic; burning is
the more defensible choice, since it ties scarcer voting weight to genuine platform
throughput rather than to selling activity or an accumulating treasury pile.)

**Step 2 — it is also the universal unit of account ("the dollar" of the platform).**
The same token prices everything on the platform, not just Vickrey slices. This
compounds Step 1: ordinary commerce of any kind now creates constant buy/sell pressure
on the governance instrument, decoupled from anyone's actual interest in voting, and
every contested-governance price swing moves the cost of unrelated transactions. The
standard fix for this — MakerDAO's DAI/MKR precedent, a stable unit-of-account kept
structurally separate from a volatile governance-and-backstop instrument — was raised
and **explicitly rejected**. Recording this so it is not silently re-proposed later:
the rejection is a real design decision, not an oversight.

**Step 3 — the stated justification, and it is a real, well-evidenced problem, not a
rationalization.** *"This is the democratic play, fundamentally... this is a
marketplace and an ETF of all funds — what happens with ETFs is the governance goes to
the ETF owner, and that person plays politics."* The concrete citation for this: Bebchuk
& Hirst's work on the "Big Three" (BlackRock, Vanguard, State Street) documents that
these three firms already cast roughly 25% of votes at S&P 500 companies (projected
toward ~40% within two decades) by holding 5%+ stakes across nearly every major public
company, while spending under $4,500/year in stewardship per $1B held and having zero
engagement with roughly 90% of portfolio companies (2019 figures) — millions of retail
investors effectively hand a proxy decision to a small internal team at three firms,
unaccountable to the actual capital owners. This diagnosis is correct: the failure is
not "capital has influence," it is *unaccountable, opaque, delegated* capital influence
— a custodian playing politics with other people's economic exposure. The design goal
that follows from this (people with real economic exposure vote directly, with no
delegated intermediary) is sound.

**What does not follow, and needs to be stated honestly rather than glossed over:**
unifying currency and vote does not remove concentration — it makes concentration
*accountable and capital-proportional* instead of *custodian-mediated*. That is a
different failure mode (visible plutocracy) from the Big Three's (opaque proxy
capture), not an escape from concentration as such. A real-world alternative that
solves the *actual* stated objection without this trade-off exists and was considered:
BlackRock/Vanguard "pass-through voting" pilots, where the custodian forwards the
actual vote to the underlying holder instead of voting unilaterally. This was
implicitly declined in favor of the unified-token design, and that choice — accountable
concentration over custodian mediation, rather than an attempt to eliminate
concentration itself — should be stated explicitly in any prose version of this
section.

**Step 4 — the final formula.** Voting power equals a function of (a) platform tokens
held plus (b) the value of assets the holder has tokenized on the platform — both
economic-exposure legs feed one combined voting base, held and cast directly, with no
custodian layer. This is not a novel or untested design — it is exactly traditional
joint-stock corporate governance, one-share-one-vote, power proportional to capital at
risk, the default structure of shareholder capitalism for centuries.

**Name what this honestly is.** This is **linear plutocracy**, and it sits in direct,
real tension with machinery the rest of the whitepaper spends hundreds of pages
building: Turchin's wealth-pump/elite-overproduction material, the Gini-danger-zone
content, §4.7's entire wealth-power firewall apparatus ("diminishing returns on
wealth-to-influence conversion," 02:1901–1931), §5.3's quadratic voting (adopted
specifically because linear one-dollar-one-vote lets wealthy interests buy outcomes),
and §2.1A's dynastic-lineage/founder-capital-advantage calculus (01:1799) — now running
*on the platform's own rails* rather than being the thing the platform exists to guard
against. This is not hypocrisy, but it is a real tension that must be named explicitly
in any prose treatment, not discovered later by a critical reader comparing this
section against §4.7/§5.3 and concluding the inconsistency was accidental.

---

## 10. The moral distinction: earned vs. extracted wealth (RULING on the distinction; PROPOSED on the mechanism)

The architect's own resolution to §9's tension, in his own words: *"The issue isn't
that people accumulate wealth, it's that people accumulate wealth through the printing
of money or proximity to banks... it's banking billionaires, billionaires the
government paid to make billionaires — not ones who got there through their own
value."* This maps directly onto §3.11's existing five-money-types framework,
self-applied here: if the platform genuinely has no printer — no central mint, no
privileged banking relationship, wealth entering only by winning open Vickrey auctions
or contributing real assets — then token concentration under this design is
structurally closer to productive/earned money than to Cantillon-extraction or
asset-inflation wealth, which is what the rest of the whitepaper actually diagnoses as
the disease. This substantially defuses §9's tension: linear vote-weight is not
automatically the same disease as fiat one-dollar-one-vote, *because the source of the
wealth is doing the moral work, not the raw fact of concentration.*

**"No printer" does not fully close the loop — two gaps remain, and should be stated
rather than assumed away:**

1. **First-mover / informational-advantage compounding needs no printer at all.**
   Someone who joins early and consistently wins auctions on better information about
   which initiatives will succeed accumulates governance weight through compounding
   advantage untethered from marginal value contributed *today* — this is §2.1A's
   dynastic-lineage calculus, now running *inside* the platform's economy rather than
   against it. A printer-less platform can still grow its own founder-population
   aristocracy purely from time-in-system.
2. **The mint mechanism (§5) is a narrower, private version of the exact vulnerability
   being excluded.** Minting happens against Vickrey-cleared prices; if that auction
   can be gamed, someone receives newly minted tokens against an inflated valuation —
   structurally private Cantillon extraction, wearing an auction instead of a central
   bank. "There's no printer" is only true if Vickrey integrity holds perfectly, which
   makes §6/§7's manipulation-resistance not just important but literally the single
   thing standing between "this platform's wealth is earned" and "this platform
   reinvented the printer with extra steps."

**The size/scale penalty modifier — the architect's own instinct, and the whitepaper
already has the mechanism.** *"You're allowed to be a monopoly, but you have to pay
more — a higher rate the more concentration you have... hard to do without oracles and
anti-Sybil [measures]."* §6.13 (confirmed at 03:2101, "Progressive Costs on
Concentration") is exactly this — Georgist progressive-cost-on-concentration,
generalized past land to wealth, corporate size, and platform monopoly. The practical
obstacle correctly identified: assessing concentration of real-world wealth/asset value
needs external price oracles, which this platform is specifically trying to avoid
depending on.

**The leading proposed fix (not yet ratified — flag explicitly wherever this is
cited).** Apply the discount curve to **voting weight directly**, not to underlying
wealth or asset value: the first N tokens convert to votes at full rate, each
subsequent tranche at a discount. This sidesteps the oracle problem entirely, since
token balance is already on-chain, known, and unforgeable — unlike §6.13's original
wealth-tax framing, no external price feed is needed at all. That leaves only the
Sybil problem (a whale splitting one position across fifty wallets to stay under the
discount threshold), and the whitepaper already has the tool: §6.2 Tier 4
(Vouched/Staked identity, confirmed at 03:381 — "combines social and economic bonds")
as a prerequisite for full voting weight above a concentration threshold. Below
threshold, anonymous participation is fine; above it, enough identity verification to
credibly assert "one actor, not fifty" — the same tradeoff §6.2 already makes explicit
for geographic associations (Tier 3+ required there).

**The coherent full position, pending ratification:** linear-into-earned-wealth is
acceptable *specifically because there is no printer*, provided (1) Vickrey-mechanism
integrity is engineered as the single highest priority in the stack, and (2) a
concentration curve applies to *voting weight itself* (not wealth) via the on-chain,
oracle-free tranche discount above, with §6.2 Tier 4 closing the Sybil gap it opens.

---

## 11. What's actually opposed: cheating and bureaucracy, not concentration itself (RULING — clarifies the target)

A necessary corrective, restated because §9/§10 had begun drifting toward treating
concentration itself as the thing needing justification: *"I'm not against savvy people
being in the market... I'm not against people having power. You need hierarchy, you
need power, you need elites. What I'm against is the cheating and the bad
bureaucracy."* This is not a new position — it **is** §4.7's own founding premise
(02:1633: "governance is fundamentally a Principal-Agent problem"; elites and hierarchy
are assumed necessary, the failure mode is capture, not elite existence per se). The
correct framing, restored: concentration is fine; cheating and bureaucratic capture are
the target — inflation-that-destroys-value (the printer, §3.11) and Cantillon-style
extraction are what is actually opposed, not savvy investors winning fairly.

### 11.1 Ostracism — a no-fault removal valve (READY, new mechanism, distinct from everything above)

Everything built in §4–§10 is fundamentally **cheating-detection machinery** — it works
by trying to define, in advance, exactly what counts as illegitimate accumulation, then
catching violations of that definition (Vickrey-integrity engineering, KYC-tier
Sybil-resistance, the §6.13 concentration curve). Ostracism inverts the premise
entirely.

The actual Athenian procedure: no charge, no trial, no defense, no proof of wrongdoing
required at all. Annually the assembly voted whether to hold one; if so, every citizen
scratched a name on a shard (*ostrakon*); above quorum, whoever accumulated the most
votes was exiled for ten years, citizenship and property both intact, no criminal
record, nothing seized. Purely preemptive — removing someone judged dangerously
prominent (positioning toward tyranny) with zero requirement to demonstrate an actual
bad act.

This is directly parallel to §6.12.4's sortition logic (confirmed at 03:1977: "Can't
capture what you can't predict") — same principle, applied to **removal** instead of
**selection**. Proposed as a §6.12 addition: a periodic, no-fault, community-triggered
mechanism for shedding outsized platform-token concentration or influence, separate
from and complementary to the cheating-detection machinery specified elsewhere in this
document.

**The honest gap this acknowledges.** §2.1A's dynastic-lineage/relative-fitness
argument does not require *any* cheating to produce multi-generational concentration: a
savvy investor who never touches a printer and never games a Vickrey auction, who wins
consistently and compounds that advantage across time and descendants, produces the
same structural entrenchment the whitepaper worries about — through purely legitimate
relative-fitness competition. This does not invalidate §10's earned/extracted
distinction; it means the distinction, even applied perfectly, does not fully close the
loop §2.1A opens. Ostracism is the honest acknowledgment of that residual gap: not a
claim that concentrated power is illegitimate, but a standing community reservation of
the right to say "enough," on its own judgment, without first having to prove the
accumulation was cheated. **Threshold, cadence, and cost-to-invoke are genuinely open**
— see §12.

---

## 12. Second-layer defenses and the redemption mechanism (READY)

### 12.1 Market discipline as an independent check, on top of mechanical anti-manipulation

Even if a single Vickrey auction could be gamed, a bidder who consistently misjudges
true value bleeds capital across repeated rounds and gets selected out over time — the
same self-correction that disciplines mispricing in any repeated market (arbitrageurs
correcting a mispriced asset, bad options-market-makers eventually going bust). This is
a real, distinct defense from the commit-reveal/staggered-checkpoint machinery in §6–§7:
**structural integrity (commit-reveal, staggering) prevents cheap one-shot
manipulation; market discipline prevents sustained mispricing by bad-but-honest
judgment, via ordinary attrition of capital.** Neither alone is sufficient; together
they are a real defense.

**What "eventually corrects" does not cover: governance power exercised during the
window before correction.** The timeframe that matters for §9's linear-plutocracy
design is not the long run — it is what happens with the voting weight a manipulated or
merely optimistic mark *already conferred*, before correction arrives. Win a Vickrey
auction at an inflated mark and the voting weight is live immediately, usable to
approve one's own inclusion terms, vote a sunset review, or vote platform fee/mint
parameters, well before "eventually" reveals the mark was wrong. When correction comes,
the token's *value* shrinks — but the governance decisions already made with that
weight do not unwind. **You cannot claw back a vote.**

The named reason "eventually" is weaker than it sounds: Soros's reflexivity thesis
holds that prices do not just passively converge on an independent fundamental — they
feed back into the fundamentals themselves (an inflated mark is easier to borrow
against, more attractive to the next bidder who anchors on the last price), which is
exactly why bubbles self-sustain for years rather than correcting quickly. Japan's own
1980s asset bubble is the concrete case: equities and real estate stayed inflated
through the decade well past fundamentals, the eventual correction was severe rather
than gentle, and the Nikkei took three decades to reclaim its 1989 peak. "Hard to
maintain permanently" was true; *permanently* is not the timeframe that matters for
governance decisions made *inside* the bubble.

**The fix — cheap, and does not touch the economic mechanism.** A short **vesting
delay on voting power tied to a new high-water mark** — long enough for at least one
more Vickrey checkpoint to confirm the price holds — forces a manipulated or merely
optimistic mark to survive a second independent test before it converts into
governance leverage, not just a first one. The economic side is untouched (tokens are
received and tradeable immediately); only the *voting* consequence of a fresh
high-water mark is delayed until proven durable. This composes cleanly regardless of
how §10's linear-vs-dampened curve question resolves. **Not yet ratified by the
architect — flag as proposed wherever cited** (see §12.4).

### 12.2 Redemption: burn-on-cash-out, not ETF-style basket redemption

§7 flagged an open question: with no redemption right into the basket, expect a
persistent 10–20% discount-to-NAV, the way closed-end funds trade below stated NAV for
years. The chosen answer is narrower than full ETF-style create/redeem, and arguably
cleaner: **per-asset burn-on-realization.** When one constituent asset inside the
basket reaches its own lifecycle conclusion (sold, matured, cashed out), its realized
value flows through to the holders of the tokens that represented that specific asset's
share of the basket, and *those* tokens are burned. Supply contracts in step with real
assets actually exiting, rather than via arbitrageur create/redeem against the
aggregate NAV. This is structurally closer to a bond or trust-certificate redemption at
maturity than to ETF share-creation arbitrage: no continuous two-way convertibility
into the whole basket at will, but a real, non-discretionary payout-and-burn event
whenever any one holding inside the basket completes its own lifecycle — arguably
preferable to full ETF-style redemption given the platform's underlying assets are
individually illiquid.

**Naming collision to resolve before this reaches prose.** The whitepaper already uses
"dividend" for something unrelated: §6.5's persistence-payment structure ("original
proposer collects dividends while policy is active... dividends cease on repeal,"
confirmed 03:899) and the leader/policy dividend-multiplier mechanism (03:551, 03:666,
03:1555) — a compensation stream tied to policy durability, not a fund-share payout.
This document's "dividend tokens" (asset-basket income/payout claims) are a *third*,
distinct instrument that happens to reuse the same word. **Rename before drafting
§6.12B** (e.g. "payout tokens" or "income-share tokens"), or explicitly disambiguate
the two uses in the same section — do not let both stand as unqualified "dividends" in
final prose; a reader will conflate the leader-compensation mechanism with the
fund-payout mechanism.

### 12.3 Recognizing value before it is realized

Open decision, addressed via reuse rather than new design: whether to recognize value
(mint/credit) at proposal-creation against *projected* value (faster, but
speculative/inflationary if the initiative underdelivers) or only at maturity/sunset
against *realized* value (safer, but creates a liquidity lag). §7's reuse of the
§6.12A escrow-buffer pattern (pre-credit against fully-escrowed forward collateral,
release the escrow as value verifies) is what makes the earlier, faster timing safe —
substitute "verified initiative value" for "verified energy production." This is listed
as open in §13 because the specific threshold/schedule for escrow release has not been
designed, only the pattern to reuse.

### 12.4 Status recap for this section

Market discipline (§12.1's first half) and burn-on-cash-out (§12.2) are READY — treat
as settled design. The vesting delay (§12.1's fix) is PROPOSED, not yet ratified. The
recognition-timing question (§12.3) is OPEN.

---

## 13. Two capture mechanisms this design explicitly does NOT solve (RULING — keep distinct, do not collapse)

The architect's own closing instruction on this design thread, worth preserving
verbatim as a discipline: *do not collapse distinct capture mechanisms into one "no
printer, problem solved" claim.* This is the single most important framing to carry
forward.

**What this design specifically excludes, and the concrete disease it is built
against.** In March 2020 the NY Fed hired BlackRock directly, with no open bid, to run
its corporate-bond/ETF purchase programs, with terms letting BlackRock buy its own
iShares ETFs alongside competitors' using the Fed's money, under confidentiality
clauses — BlackRock's own bond ETFs rallied on the announcement before a single bond
was purchased, purely because the firm managing the purchases was positioned to
benefit from them (the same pattern recurred with JPMorgan holding its own QE-eligible
assets in 2008). "Mint against Vickrey-verified real value, no fractional-reserve
layer, no discretionary authority" excludes this by construction: no entity can be
simultaneously *contracted to decide* and *positioned to benefit*, because an
adversarial auction does the pricing, not a hired insider.

**What this design does NOT touch — three separate mechanisms, needing three separate
tools already specified above, not one unified fix:**

1. **First-mover / informational-edge compounding** (§10, gap 1) — needs no printer,
   addressed only partially by ostracism (§11.1) and the concentration curve (§10).
2. **Coalition capture** — a small, organized minority beating a large, diffuse,
   low-engagement majority (§6.9.2's Dictator's Handbook dynamic, confirmed 03:1651).
   Real activist investors swing outcomes with single-digit stakes today because most
   holders never vote at all — and this gets *easier*, not harder, as a platform
   scales, since rational apathy in the median holder grows with size. The protective
   machinery already specified elsewhere in the whitepaper is §6.3.2's engagement
   minimums / plurality thresholds (confirmed 03:482) — requiring genuine broad
   participation for a vote to count, not plurality among whoever showed up. **"The
   platform will get big enough that concentration smooths out" is not a safe
   assumption** — the Big Three's S&P 500 voting share *rose* toward ~25% (projected
   ~40%) *while* the market they operate in grew enormously, because
   concentration-producing forces (capital efficiency at scale, compounding
   structural advantage) scale right along with the platform.
3. **Relative-fitness dynasty-building** (§2.1A, §11.1's honest gap) — purely legitimate
   compounding advantage across generations, addressed only by ostracism as a
   last-resort valve, not prevented structurally.

**A caution against a specific rhetorical failure mode.** "The winners are cheating" is
true of winners who arrived via bailout, bank proximity, or a hired seat inside a
central-bank purchasing program — provably, per the BlackRock/Fed case above. It is
*not* automatically true of every market winner, and collapsing all winners into one
undifferentiated class is the exact move that would let a critic dismiss this
platform's own Vickrey winners as illegitimate just for having won. Keep "winners" a
differentiated category in any prose treatment, including when that is rhetorically
inconvenient — this is what stops the whitepaper's own anti-elite argument from
sliding into anti-market cynicism.

**The honest landing point on how good this gets, stated precisely rather than
implied.** *"I don't think there are perfect solutions. I think there is volatility.
Markets do make mistakes, but if we can make them more honest, that's a step in the
right direction."* This is not a retreat — it is a category shift in what is being
claimed. The design was never claiming to eliminate concentration, capture, or bad
governance decisions, only to make the *inputs* to those outcomes more honest than what
exists today (opaque proxy voting by unaccountable managers, discretionary
central-bank printing with no real-time market check, valuation marks nobody can
contest). A system that fails openly — a bad bet made in public, priced by a
contestable auction, correctable at the next checkpoint — is a genuine improvement over
a system that fails opaquely, even though neither fails at zero rate. This is not a new
position for the whitepaper: it is §6.15's own stated philosophy (confirmed at
03:2366/03:2376 — no optimal governance system exists; Gall's Law, complex systems that
work evolve from simple systems that worked).

**The one-sentence test, worth using as a candidate epigraph for the whole mechanism:**
*"Anyone can bid, it's open, it's public, but you can't just will money into existence
to make that bid — that's the problem now."* Everything in §4–§13 is scaffolding in
service of exactly one property: participation is open to anyone, and the bid must be
backed by something actually earned or produced, not conjured. The single test
distinguishing this design from 2008/2020: can the winning bidder trace their capital
back to value someone else freely paid for, or back to a phone call with a regulator.

---

## 14. A third capture mechanism, named but not yet mechanism-designed: schmoozing-gated capital access

Distinct from both diagnoses in §13 (printer-proximity and dynasty-building): *"Right
now you often need to play ball — cozy up with the other managerialists to get
funding, to have your company play with others."* This is a barrier to *entry* into the
Vickrey/fund-creation process itself, not a distortion of the auction once someone is
already participating — access to capital gated by social proximity to existing
gatekeepers (gestures toward Bourdieu's cultural capital, and to 01:1191's existing
material on managerialism), rather than by demonstrated competence or a legitimate
track record.

**A stated design goal, not yet a mechanism:** the platform's onboarding / fund-creation
flow should provide a genuinely open path to running a Vickrey-eligible fund or
initiative that does not require pre-existing social capital or insider relationships
— a guided, structured process any competent operator can enter on the merits of their
proposal, rather than one gated by who they know. This is explicitly a companion
problem to operator-competence vetting (how does the platform verify someone can
actually run a fund well, as distinct from verifying they have capital or social
proof) — and the two need to be solved together, since a purely open door without any
competence signal reintroduces exactly the kind of unvetted-capital risk the rest of
this document works hard to exclude via Vickrey and KYC-tier machinery. **No concrete
mechanism has been designed for either half of this — this is a scoped problem
statement for future work, not a proposal.**

---

## 15. External precedents and citations to use directly

- **Vickrey (second-price sealed-bid) auctions** — dominant-strategy truthful bidding;
  the core price-discovery primitive throughout §6–§7.
- **ETF creation-unit mechanism** — the precedent for why leg-3 minting (§5) is not
  inflationary; trillions of dollars of real-world ETF assets are created/redeemed this
  way continuously.
- **Uniswap LP tokens / AMM trade-fee accrual** — the precedent for value accrual via
  trade tax rather than minting (§4); a proven-at-scale mechanism, not a speculative
  one.
- **MakerDAO (DAI/MKR)**, **Curve (veCRV)**, **dual-class equity (Google A/B/C)** — the
  standard capital-without-control precedents considered and, for the platform token
  specifically, explicitly departed from in §9 (kept, however, for per-initiative
  tokens per §8).
- **Terra/Luna collapse (~$40B in a week)** — the concrete reflexivity failure case
  motivating the leg-3-only minting rule (§5, §7).
- **LIBOR → SOFR transition** — the concrete thin-reference-price manipulation case
  motivating staggered, rolling-window marking rather than single-point auctions (§7).
- **Akerlof's "market for lemons" / adverse selection** — motivates the
  incentive-compatibility caution on the platform's co-buy percentage (§7).
- **Azar, Schmalz & Tecu on common ownership** — motivates the referee-conflict
  guardrail on the platform's own passive holdings (§7).
- **Bebchuk & Hirst on the "Big Three"** — the direct empirical citation for §9's
  stated justification and §13's "scale doesn't dissolve capture" correction.
- **BlackRock/Fed 2020 corporate-bond purchase program; JPMorgan/2008 QE-eligible
  holdings** — the concrete Cantillon-proximity cases this design is built to exclude
  by construction (§13).
- **Soros's reflexivity thesis** — motivates the vesting-delay proposal (§12.1);
  Japan's 1980s asset bubble is the concrete illustrative case.
- **Athenian ostracism** — the direct historical precedent for §11.1's no-fault removal
  mechanism.
- **Bourdieu's cultural capital** — background citation for §14's schmoozing-gated
  access problem.
- **Michael Spence, "Job Market Signaling" (1973)** — relevant to operator-competence
  vetting (§14's open half): the formal economics of costly signals separating types
  under asymmetric information, directly applicable to why a staked/track-record
  requirement would work where schmoozing fails as a competence signal.
- **Randy Farmer, *Building Web Reputation Systems*** (with earlier "Lessons of
  LucasFilm's Habitat," co-authored with Chip Morningstar) — relevant background for
  operator-reputation and rubric-design questions likely to arise once §14 gets a
  mechanism; not yet applied to any specific decision in this document.

---

## 16. Internal whitepaper anchors (verified against the current docs — cite these directly)

| Anchor | Confirms |
|---|---|
| §6.12A, 03:2004–2069 (esp. 03:2058) | kWh token is the transactional lubricant; a *separate store of value is required* — the gap this whole document fills |
| §5.3, 03:187 | Radical Markets / Harberger taxes — the Vickrey/partial-exposure lineage |
| §4.7, 02:1633, 02:1901–1931 | Governance-as-principal-agent-problem; wealth-power firewalls; diminishing returns on wealth-to-influence conversion |
| §2.1A, 01:1799 | Dynastic-lineage / founder-capital-advantage calculus |
| §3.11 | Five money types — the earned/extracted distinction in §10 |
| §6.13, 03:2101 | Progressive Costs on Concentration — the size/scale penalty precedent |
| §6.2, 03:356, 03:381 | KYC tiers, incl. Tier 4 (Vouched/Staked) — closes the Sybil gap on the concentration curve |
| §6.12.4, 03:1977 | Sortition ("Can't capture what you can't predict") — the direct precedent for ostracism-as-removal |
| §6.9.2, 03:1651 | Dictator's Handbook — small organized coalitions beating diffuse majorities |
| §6.3.2, 03:482 | Engagement minimums / plurality thresholds — the actual defense against coalition capture |
| §6.15, 03:2366, 03:2376 | Platform Philosophy: Humility and Experimentation; Gall's Law |
| §6.5, 03:899, 03:551, 03:666, 03:1555 | Existing "dividend" usage — naming collision to resolve before §6.12B drafting |
| §4.23 | Differentiated cohort architecture — the per-initiative token-structure precedent |
| §4.8 | Enforce Subsidiarity — the initiative/platform governance-scope separation |
| 01:1191 | Managerialism — background for §14's schmoozing-gated-access problem |

---

## 17. Open decisions — do not guess these, resolve or escalate them

These are genuinely undecided. Do not silently pick an answer while drafting §6.12B or
implementing; either bring each back to the architect for a ruling, or if implementing
under time pressure, implement behind a clearly-named configuration parameter and flag
the default choice explicitly as provisional.

1. **Vote-weight conversion curve (§9, §10).** Linear (simple, honest, matches the
   architect's literal wording, but is the plutocracy the rest of the document
   diagnoses as the disease) vs. convex/logarithmic dampening (keeps a single
   instrument, applies the paper's own §4.7 diminishing-returns principle to this
   specific conversion, adds a structural brake on Big-Three-style compounding
   concentration). This blocks writing §6.12B's governance-weight formula.
2. **The vesting-delay proposal (§12.1).** Ratify, reject, or modify the
   "voting power delayed one checkpoint past a fresh high-water mark" mechanism.
3. **Mint/buy ratio and co-buy percentage (§5, §7).** Both flagged as needing an
   incentive-compatibility analysis before being set, not just picked as round
   numbers (the adverse-selection risk in §7 makes this concrete, not abstract).
4. **Redemption-recognition timing (§12.3).** Recognize value at proposal-creation
   against projected value, or only at maturity against realized value — the escrow
   pattern to reuse is known, the specific release schedule is not designed.
5. **Ostracism's parameters (§11.1).** Threshold, cadence, and cost-to-invoke are
   entirely undesigned; only the principle (no-fault, community-triggered,
   periodic) is settled.
6. **Operator-competence vetting (§14).** No mechanism proposed at all — only the
   problem statement and its relationship to the schmoozing-gated-access goal.
7. **"Dividend" naming collision (§12.2).** Needs a rename decision before §6.12B
   is drafted, to avoid conflating this instrument with §6.5's existing usage.
8. **Regulatory/Howey classification (§8).** Needs an actual legal determination,
   not a design decision — flagged here so it is not skipped in sequencing.

---

## 18. Recommended next steps for whoever picks this up

1. Get a ruling on open decision #1 (the vote-weight curve) before drafting any
   governance-weight formula — it is the single highest-leverage unresolved question
   and touches almost every other mechanism in this document.
2. Draft the §6.12B mechanism specification (parallel to §6.12A's existing structure)
   using §4–§12 above as the source material, explicitly marking anything still
   OPEN/PROPOSED as such in the draft rather than silently resolving it.
3. Resolve the "dividend" naming collision (#7) before that draft goes further than a
   first pass — it's cheap to fix now and expensive to fix after the term has
   propagated through a full section.
4. Get an actual securities-law read on the Howey question (#8) in parallel — this
   does not block drafting the mechanism, but should not be discovered late.
5. Treat §11.1 (ostracism) and §14 (schmoozing-gated access / operator vetting) as
   separate, smaller design threads that can be picked up independently of the core
   token mechanism — they are genuinely new, less-developed ideas rather than
   extensions of the already-settled §4–§9 core.
6. Before promoting any of this into `docs/01_diagnosis.md`, `docs/02_specification.md`,
   or `docs/03_mechanisms.md`, get explicit sign-off from the architect — this document
   is a design/research artifact, not pre-approved whitepaper prose.

---

## 19. Addendum — the ledger session (2026-07-20, architect + Claude)

A follow-on design conversation resolved several of §17's open decisions and
corrected two framings in the body above. Same status discipline as the rest of this
document. Where this addendum conflicts with §4–§13, **the addendum wins** — it is
later and was ratified interactively.

### 19.1 The supply principle (RULING)

**Token supply tracks *contributed* value, not *total* basket value.** Supply must
never be pinned to NAV — supply == basket value produces a permanently flat
stablecoin-of-the-basket, not a store of value. Mint only against assets physically
delivered into the basket; every other flow moves existing tokens; the wedge between
value entering and tokens created is the appreciation, by design.

### 19.2 Entry-event accounting, made precise (READY)

Worked ledger for a three-way split (winner ⅓ / mirror ⅓ / mint ⅓ of asset X,
cleared value V):

- **Winner's leg**: pays ⅓·V in existing tokens → recirculate to the asset owner.
  Supply unchanged; the slice is the winner's private property and never enters the
  basket.
- **Mirror leg**: treasury spends trade-tax tokens. Treasury holdings are accounted
  like **corporate treasury stock — out of circulating float**. The spend releases
  ⅓·V of tokens back into float while the basket gains ⅓·V of asset.
- **Mint leg**: owner delivers ⅓ of X into the basket, receives ⅓·V of new tokens at
  NAV (creation-unit, balanced both sides).

Net: float +⅔·V of tokens (only ⅓ freshly minted), basket +⅔·V of assets — **the
entry event is exactly NAV-neutral**. Appreciation does not happen at entry; it
happens continuously as the trade tax pulls tokens from float into treasury while the
basket is unchanged. The IPO is the moment stored tax-appreciation converts into owned
assets.

**The leg-ratio knob does not affect per-token value** (every leg prices at the same
cleared price; the mint is balanced, so entry is neutral at any split). What the ratio
actually controls: treasury deployment speed (flywheel) and cumulative platform
ownership share (the §7 common-ownership cap). This narrows §17 open decision #3: the
incentive-compatibility analysis constrains adverse selection, not valuation.

### 19.3 Denomination (RULING — supersedes §9 Step 2)

**Per-initiative economies are currency-free: an initiative may denominate, mint, and
transact in any currency it wants. The platform token is required specifically at the
IPO/Vickrey gate — auctions settle in platform tokens.** This retains §9 Step 1's
core property (you cannot access the core marketplace without holding the governance
instrument) while dropping the "universal unit of account" claim of Step 2. The
MakerDAO-style stable-unit objection recorded in Step 2 is thereby mostly mooted:
ordinary commerce inside initiatives no longer routes through the volatile governance
instrument. §6.12B should be drafted with this ruling, not Step 2.

### 19.4 The tracking principle (RULING) and the exit mechanism (READY)

Architect's ruling, verbatim spirit: *"It's an ETF. It is supposed to track value —
it can't magically be shielded."* The token promises **honest tracking of whatever
the basket is actually worth — downside included**. No mechanism defends a level;
losses pass straight through to NAV. (This corrects the Terra-flavored caution in
§12.1's framing: Terra died defending a *peg* — a promised value. This token promises
no value, only tracking, so there is nothing to shield.)

Consequences, now settled:

- **Exit = proceeds-based market buyback and burn.** When an asset exits, the
  basket's share of sale proceeds (in whatever currency the sale realized) goes to
  escrow → buys platform tokens on the open market at **current market price** → those
  tokens are burned. Full stop.
  - Self-funding by construction: the obligation is defined by what the sale raised,
    so the mechanism can never be insolvent.
  - Nobody is burned involuntarily: supply is purchased from willing sellers at
    market. Holders who want the payout in cash sell into the buyback (a
    self-selected dividend); holders who don't now own a larger share of a smaller
    basket at unchanged NAV. The "what if the exiting owner holds no tokens" problem
    dissolves — the burn is never an obligation on a person.
  - Self-balancing against price drift: buying at a discount to NAV retires more
    claim than value departed (accretive — the standard closed-end-discount cure);
    buying at a premium retires less (leans against bubbles). No oracle, no asserted
    price: entry rides the Vickrey clearing price, exit rides the actual sale and the
    actual market.
- **Rejected: original-token-count burn** (retire at exit exactly the tokens minted at
  entry). It sneaks in a promise — "supply will always equal cumulative contributed
  value" — that the basket must spend real value to honor even when the asset didn't
  return that value, i.e. a hard obligation decoupled from realized cash, surfacing
  pro-cyclically. That is the anti-ETF move. Also rejected as a discretionary
  good-times top-up policy: the tracker carries no supply policy at all.
- **Rejected: pro-rata external-currency dividends at exit** — leaks basket value out
  of the token, contracts nothing, and volunteers the *Howey* fact pattern.
- **Fixed-reference-price buybacks rejected** in both directions: below market they
  never execute; above market they are an arbitrage drain on the escrow.

### 19.5 Escrow denomination (PROPOSED)

Escrow is **collateral-agnostic against a whitelist** (BTC, stablecoins, the platform
token, per §6.12A's buffer precedent) with per-asset haircuts (§7's LTV guardrail).
Exit proceeds are held as received and converted only at the moment of buyback. Not
yet explicitly ratified.

### 19.6 The honest asterisk (keep in any prose treatment)

The one place this is *not* an ETF: no continuous create/redeem arbitrage pins market
price to NAV. Creations happen only at IPO events, redemptions only at exits, so
price can drift between events (§7's closed-end-discount risk). Exit buybacks
discipline the drift episodically and lean the right way. If drift matters in
practice, the fix is **more frequent, smaller Vickrey checkpoints** (more marking and
more episodic discipline) — never a peg mechanism.

### 19.7 Updated open-decision list

Resolved from §17: #3 is narrowed (ratio = flywheel/ownership knob, not a valuation
knob; adverse-selection analysis still needed); the §12.2 redemption question is
settled (proceeds buyback-burn). Newly explicit and still open:

1. Fee-cut burn on IPO auction settlements (EIP-1559-style cut, principal to seller)
   — PROPOSED, unratified. This is now the *only* deflationary flow besides exits.
2. Escrow collateral whitelist + haircut schedule (§19.5) — PROPOSED, unratified.
3. Whether the treasury may ever refuel from exit proceeds. Current READY position:
   no — exits burn fully; the treasury's only inflow is the trade tax. Revisit only
   if tax inflow proves too thin to fund mirror legs.
4. Everything in §17 not named above (vote-weight curve, vesting delay, ostracism
   parameters, operator vetting, naming collision, Howey) remains open.

### 19.8 Correction to §19.2's tax accounting: the trade tax is in-kind (READY)

Trades on the marketplace are **trade-currency ↔ RWA tokens** (e.g. USDC for a
project's asset tokens) — per §19.3 they do not route through the platform token. So
the trade tax cannot be assumed to arrive as platform tokens, and §19.2's
"tax pulls tokens out of float into treasury" framing is wrong as stated. Per §4's
original Uniswap-LP framing ("you take a part of *it*"), the tax is taken **in kind
from both sides of the trade**:

- The **asset-side sliver** (RWA tokens) accrues directly **into the basket**: basket
  value grows with every trade, supply unchanged — this, not float-shrink, is the
  continuous appreciation engine.
- The **currency-side sliver** (USDC etc.) goes to the treasury, which **market-buys
  platform tokens** with it (constant structural bid) — held to fund future mirror
  legs, or burned per the §17 fee-burn decision.

Entry events remain NAV-neutral as in §19.2; only the description of how the
treasury acquires its tokens (market purchase funded by currency-side tax, not
direct receipt) and where appreciation accrues (in-kind basket accretion) changes.

### 19.9 The convention-free invariant, and the no-pre-mine rule (RULING on the invariant; READY on the rule)

Reconciling two equivalent ledgers (treasury-stock accounting recognizes appreciation
at tax collection and makes entry events NAV-neutral; all-tokens-outstanding
accounting recognizes the same appreciation at treasury deployment, making entry
events visibly accretive) produced the statement that survives any convention:

> **Over any period: token appreciation = Δbasket value not matched by mint.**

The deployed treasury value at an IPO is prior collected tax being converted, not
value created by the event. Prefer treasury-stock accounting in official ledgers so
appreciation is attributed to its cause (taxes, continuously) rather than to entry
events — "IPOs pump the token" is a manipulable narrative; "taxes pump the token,
IPOs convert" is the causal truth.

**No-pre-mine rule (READY):** the appreciation above exists only because treasury
tokens were funded by collected revenue. A genesis/pre-mined treasury spent on
mirror legs is new-supply-to-outsiders with no prior value collected — the
slow-motion printer. The treasury may only ever hold tokens purchased with collected
revenue. Belongs in §6.12B beside the no-unbacked-mint rule.

### 19.10 Fees, the cash-creation door, and the settlement-asymmetry findings (PROPOSED)

Architect-proposed, endorsed, unratified in detail:

1. **Platform service fee**, small, paid in platform tokens, to treasury. Revenue
   uncorrelated with IPO cycles; gives the token consumptive utility (helps the
   *Howey* posture).
2. **Margin on marketplace buys/sells** — an extension of the trade tax to more
   order flow. Keep near-zero on the platform token's own order book: exit buybacks
   and treasury market-buys route through it, and taxing them taxes the system's own
   discipline mechanisms.
3. **Cash-creation door**: buy newly created tokens from the platform at NAV; the
   cash enters the basket as a reserve sleeve (balanced creation, not a printer).
   Guard: creations only at fresh checkpoint marks or with swing pricing, else
   stale-NAV timing arbitrage. Side benefits: caps big-IPO float squeezes (bidders
   create at NAV+ε instead of sweeping thin books) and funds mirror legs without
   sales.

Adversarial findings on the settlement surface (F1–F4, from the same session):

- **F1 (high): premium/discount settlement asymmetry.** With token at 1.30 vs NAV
  1.00, mint-at-NAV lets a contributor turn a $15k asset into $19.5k of tokens —
  repeatable creation-arbitrage that flattens premiums (tolerable, but the premium
  accrues to contributors). At 0.80 vs NAV 1.00, mint-at-NAV under-rewards
  contribution and **discounts choke off IPOs exactly when fresh marks are most
  needed**. Rules that fall out: payment legs (winner, mirror) settle token-count at
  **market** price; the mint leg prices at **NAV**; in discount regimes shift the
  leg-split toward paid legs rather than ever minting at a below-NAV price (which is
  dilutive).
- **F2 (high): sliver-mark manipulation.** In-kind tax slivers marked at last trade
  are wash-tradeable; NAV distortion propagates into every subsequent mint. Natural
  partial defense: wash trades pay the in-kind tax. Guard: mark slivers at Vickrey
  checkpoint prices with staleness haircuts, never at last trade.
- **F3 (medium): NAV quality decay** from accumulating illiquid dust slivers. Guard:
  periodic sweeps of slivers into their own asset's market for cash (feeding the
  reserve sleeve), haircuts on unswept dust.
- **F4 (medium): big-IPO float squeeze** — large auctions force winners to sweep a
  thin token float, spiking the price into the mint pricing. Guard: the
  cash-creation door (#3).

**Uniform-ratio corollary (READY):** float × NAV = basket is true by definition, but
the token tracks *the platform* proportionally only if the co-buy/mint ratio is
uniform (or banded) across assets. The per-asset-knob framing in the body must be
tightened: a variable ratio silently skews index composition. (SPY does not own the
S&P; proportional composition, not total ownership, is the index property.)
Full-value minting was checked and rejected on arithmetic: minting 150k against 30k
delivered = 10% NAV haircut per event — the printer.

### 19.11 Adversarial panel synthesis (three independent attackers: market/arb, solvency, governance)

Run 2026-07-20 against the full design through §19.10. Verdict up front: **the exit
tracker survived; the Vickrey mark, the tax base, and the governance surface did
not.** Both headline invariants were formally attacked: NAV-neutrality of entries
holds **only at P = NAV exactly** (the mirror leg settles at market while the mint
settles at NAV, so any premium/discount makes every entry event itself
accretive/dilutive — a knife-edge, not a property); the appreciation invariant is
true as a ledger identity but false as a value claim unless the mark is anchored to
arm's-length money and the tax base actually binds.

**CRITICAL 1 — Circular Vickrey / manufactured marks.** The winner's payment
recirculates to the asset owner, so a seller-controlled bid ring pays itself: the
classic "overbidding costs you" Vickrey defense is void, commit-reveal is irrelevant
(it stops auctioneer fraud, not bidder collusion). Worked attack: garbage worth $1M
cleared at $5M → ring surrenders $0.67M of asset, receives $3.33M of tokens
($1.67M drained from the treasury's mirror leg + $1.67M over-mint), plus immediate
voting base. Fee-burns can't price it away (killing a 5× inflation needs a ~160%
fee). Guards (compose, all READY):
  - **Robust-mark rule** (architect-proposed): commit-reveal exposes the full bid
    distribution; a legitimate market clusters, a shill ring is detached top bids.
    The winner still wins at second price, but the mark that sizes mint/mirror/NAV
    uses a collusion-robust statistic — min(cleared price, best provably-unaffiliated
    bid, distribution-anchored bound). Faking it then requires funding a whole
    plausible distribution, not two bids.
  - **Bid deposits** (slashable, scale with bid) + **minimum independent-bidder
    count** (Tier-4-separated from seller); below the minimum, the asset enters
    unminted/escrowed until a later checkpoint clears with genuine depth.
  - **Reserve price** (seller-set) for the suppression side the distribution test
    cannot see.
  - **Vote weight counts held tokens only** — the assessed-value leg of §9 Step 4 is
    manufacturable (governance attacker: $980M of vote weight at ~zero net token
    cost) and the vesting delay does not stop a persistent ring. Marks feed
    accounting, never votes.

**CRITICAL 2 — Tax-base evaporation.** The in-kind tax binds only on-venue; RWA
tokens that are freely transferable migrate to DEX/OTC/wrappers/repo, driving the
appreciation engine and the treasury bid to ~0 by default (not by attack). Guard:
**transfer-restricted RWA tokens (contract-level KYC allowlist; wrappers are
non-whitelisted), tax levied on owner-change** — regulatorily aligned with the Howey
posture anyway. Residual: cash-settled off-chain derivatives (acceptable; they still
need the venue's print).

**CRITICAL 3 — Escrow-collateral circularity.** Whitelisting the platform token as
escrow collateral reopens the Terra loop through the side door (pre-credit against
the token's own price; token −50% → funded hole; plus a double-count if escrowed
tokens are marked while the basket they claim is in NAV). Guard: **strike the
platform token from the §19.5 whitelist** (or 100% haircut).

**HIGH — the P≠NAV surface (knife-edge findings).**
  - Premium round-trip: create at NAV → sell into an exit buyback executing above
    NAV → riskless E·(1−NAV/P) bled from holders. §19.4's "leans against bubbles"
    claim is falsified: at a premium the buyback is a price-insensitive buyer.
    Guard: **buyback price ceiling — never buy above NAV(1+ε); at a premium, exit
    proceeds park in the reserve sleeve instead** (still self-funding, keeps the
    accretive-at-discount half).
  - Stale-NAV door timing (2003 mutual-fund arb): per-asset freshness ≠ portfolio
    freshness; door users hold a free option on unmarked drift. Guard: **creation
    spread (1–2% over NAV) + swing pricing/basket-freshness threshold.**
  - Door as governance printer: unlimited cash → tokens at NAV with zero market
    impact bypasses the float frictions that make linear voting tolerable (23% of
    post-money supply in one checkpoint, vesting delay doesn't bite — it gates
    marks, not tokens). Guard: **per-checkpoint creation cap (2–5% of float) +
    door-token voting weight vests over N checkpoints.**
  - Settlement-print sandwiching: payment legs settling at spot on a thin float make
    every entry a sandwich target in both directions. Guard: **randomized-window
    TWAP/median settlement.**
  - Front-running the two announced mechanical flows (treasury bid, exit buyback):
    classic MEV against price-insensitive public programs; insiders with vote access
    worsen it (referee conflict). Guard: **run both as periodic sealed-bid batch
    auctions (the platform already owns Vickrey infrastructure) + blackout/firewall
    for anyone with governance or op-timing knowledge.**

**HIGH — governance spine.**
  - Rented-snapshot voting: ~$41k/day borrows $100M of voting weight at a
    predictable snapshot; held tokens are exempt from the vesting delay. Guard:
    **lock/time-weighted voting weight (the veCRV pattern §8 departed from) or
    randomized secret snapshots.**
  - Coalition capture of the parameter set: at 10% turnout, 51% of participating
    weight ≈ $102M of retained principal vs $100M+/yr of redirectable flow; the
    concentration curve is Sybil-splittable at ~0.1% overhead (regressive against
    honest small holders). Guards: **supermajority + real quorum (not
    plurality-of-turnout) + time-locked execution for flow parameters (tax rate,
    leg split, whitelist, fee routing, sleeve rules); super-linear Tier-4 bonds and
    slashable vouching for the curve.**
  - Crisis-window capture (composes with Critical 3): mid-drawdown the token is the
    cheapest it will ever be and the discount stalls entries; a captured vote then
    widens the escrow whitelist / unseals the sleeve. Guards above + **ratify the
    vesting delay**; state explicitly that **treasury-held and escrowed tokens never
    vote** (nowhere currently stated).
  - Ostracism weaponization: no-fault removal at low quorum lets a 5% active
    minority exile the largest honest bloc and, if the exiled weight redistributes,
    manufacture a working majority. Guards: **slashable invocation bond,
    supermajority + high quorum specifically for ostracism, exiled weight
    abstains/escrows (never redistributes).**
  - IPO-gate enclosure: the captured coalition can vote whitelist/deposit/fee rules
    that price rivals out of the only entry gate. Guard: **constitutional
    non-amendable open-access floor on entry rules, outside ordinary governance.**

**MEDIUM — structural rules confirmed cheap to close.**
  - Mirror leg is **best-efforts, capped at treasury balance, never minted, never
    sleeve-funded** — treasury capacity is token-denominated while obligations are
    value-denominated (73% forced shortfall in the worked example); verified that
    NAV-accounting survives on winner+mint alone, so nothing breaks by making it
    optional.
  - **Sleeve segregation**: basket property, never funds mirror legs or treasury
    token purchases (else laundered self-buy = §7's forbidden loop one hop removed,
    or double-counted NAV).
  - Float endgame: burns are unbounded, mints are entry-gated → near-zero-float
    deadlock (IPO gate needs tokens nobody has; escrows can't complete; quorums
    unreachable). Guard: **door issuance auto-eligible (spread-protected) when float
    < threshold × trailing exit volume**; in-flight escrow proceeds are inside NAV.
  - Buyback execution: TWAP with per-tranche ceiling at NAV (never buy above — above
    NAV the burn is dilutive by the design's own arithmetic).

**What genuinely survived:** the proceeds-defined exit obligation cannot be made
insolvent (attacked directly, held — tautologically funded); the no-unbacked-mint /
no-pre-mine core; the tracking principle itself. Every failure found lives in the
*unpriced promises around* the tracker: the mark, the tax base, the mirror
obligation, the door, and the vote. All guards above are parameter/rule-level, not
mechanism redesigns; the two that change already-made decisions are (1) vote weight
= held tokens only (amends §9 Step 4) and (2) transfer-restricted RWA tokens
(constrains §19.3's currency-freedom at the transfer layer, not the denomination
layer).

### 19.12 Layered defense against manufactured bid distributions (READY)

The robust-mark rule forces a ring to fake a whole distribution rather than two
bids. The follow-up question — how do you prevent bulk bid manufacture — has no
single answer; the design is that each layer moves the cost somewhere the attacker
can't recirculate it, and the payoff side is amputated independently:

1. **Manufactured bids can't move the mark without passing identity separation.**
   The mark anchors to the best *provably-unaffiliated* bid; a thousand pretty shill
   bids are cosmetic unless they defeat Tier-4 separation. The attack therefore
   collapses into a Sybil attack on §6.2 — which is priced (super-linear bonds,
   slashable vouches), graph-analyzable, and the one surface the whitepaper already
   invests machinery in.
2. **External, non-circular costs even for a fully circular ring:** protocol-held
   slashable deposits per bid, fees/taxes on every leg, and burned identities.
   (Forced "audit fills" of losing bids do NOT work here — a ring buying from
   itself recirculates the fill payment; deposits and fees are kept external by
   construction.)
3. **Time:** a mark only fully cures after surviving K staggered checkpoints with
   substantially disjoint bidder sets (bidder-asset incidence graph down-weights
   repeat cohorts). The conspiracy must be re-funded and re-staffed per checkpoint.
4. **Defection bounties** (§6.12.2 pattern): slashed ring deposits fund the
   whistleblower. An N-party conspiracy where any member profits more by defecting
   than by continuing is self-unstable at exactly the N the distribution test
   forces.
5. **Amputated payoff:** votes never derive from marks (held tokens only), and
   mint/mirror size off the unaffiliated anchor — so even a successful fake
   distribution mints against the best honest bid.

Net: bid manufacture is not prevented; it is made unprofitable — a multi-identity,
multi-checkpoint, deposit-funded conspiracy that must defeat KYC-graph analysis and
survive its own members' defection incentives, to inflate a number that the system
neither votes on nor mints against.

### 19.13 Tax redesign: currency-side only (PROPOSED, architect-initiated) + deposits-for-tokens confirmed

Architect challenged §19.8's in-kind asset-side sliver ("I don't think it can
exist"). On examination the objection holds:

- Initiatives configure their own cap-table rules (eligibility, transfer
  restrictions, minimum units) — the basket cannot be assumed an eligible holder of
  every instrument; slivers of restricted securities may be unholdable as a matter
  of each initiative's own law and configuration.
- Slivers hand the platform micro-positions (and potentially votes) in every
  initiative — the §7 referee conflict at maximum surface.
- The slivers were the attack surface for F2 (wash-trade mark manipulation) and F3
  (dust NAV decay) — both vanish if the basket never holds them.

Replacement: **tax the currency side only, split at collection**: x% directly into
the basket's cash sleeve (holders' accretion — objective value, no marking, no
custody problem), remainder to the treasury for operations and token market-buys.
Appreciation engine unchanged in economics (Δbasket not matched by mint, now arriving
as cash instead of slivers), strictly better in accounting. What is lost: passive
index exposure to the traded long tail (basket exposure becomes IPO'd assets + cash
only). Judged acceptable; in-kind collection can remain a per-initiative *option*
where instruments genuinely permit it, OPEN.

Note the source-of-funds distinction this sharpens: the sleeve ban (§19.11) forbids
**door-created** cash from funding platform buy-ins (self-buy loop); **earned tax
cash** routed to the sleeve is external value and may fund the basket's own
IPO-leg purchases. The rule is about provenance, not about the sleeve as such.

**Deposits mint tokens: confirmed.** "People deposit $500k" = the §19.10
cash-creation door: 500k tokens minted at NAV + spread, cash into the sleeve —
balanced creation, not a printer. Guards apply as ruled: fresh-marks/swing pricing,
per-checkpoint cap as % of float (a $500k deposit against a small float queues
across checkpoints), door-token governance weight vests over N checkpoints.

### 19.14 Operator funding, genesis sizing, and portability pricing (PROPOSED, architect-initiated)

- **Basket vs operator separation:** door cash backs tokens 1:1 (basket = holders'
  property). Operator revenue = disclosed issuance fee on door creations (NAV + fee,
  fee to operator), the service-fee schedule, the treasury's currency-tax share, and
  optionally an ETF-style expense ratio on the basket (the standard instrument given
  the tracking ruling). Token is not operator equity; if ops need real capital, the
  operator company raises separately. All fees are published governed parameters
  (transparency as mechanism, not marketing).
- **Genesis sizing:** small is fine — the door refills float on demand, so genesis
  seeds credibility, not capacity. Any raise target stays off public marketing pages
  (solicitation posture).
- **Portability pricing (replaces mandatory transfer restriction as the primary
  guard for the tax-evaporation critical):** initiatives choose. Venue-locked
  (tradeable only on-platform): discounted service fees — their tax flow funds the
  system. Portable: full/higher one-time fees (monetized once, no tax expected) and
  a marking haircut (off-venue trades are invisible to checkpoints). Note most RWA
  instruments require transfer allowlists for securities reasons anyway;
  venue-lock will frequently be the legal default.

### 19.15 The registrar principle (READY)

Portability is a **venue** choice, never a **registrar** change: the RWA token
contract remains the sole register of ownership wherever the tokens trade (the
platform playing the transfer-agent role securities law effectively requires).
Consequences:

- Lifecycle control survives portability. Liquidation = initiative-governed decision
  (or pre-configured trigger) → contract-level record-date snapshot + transfer
  freeze → sale proceeds through platform escrow → pro-rata payout to holders of
  record → tokens retired at the contract. The basket is just another holder of
  record; its share feeds the buyback-burn as ruled.
- **Redemption machinery is a mandatory issuance requirement**, not an option:
  record dates, freeze, payout claims, retirement must be in the token contract
  from day one.
- Wrapper/bridge caveat: the register sees the wrapper as one holder; its
  depositors claim through their wrapper. On restricted instruments, non-whitelisted
  contracts cannot be holders; on portable ones this is documented, and the
  record-date freeze prevents late unwrap front-running.
- So portability costs exactly what §19.14 prices — tax flow and mark visibility —
  and can never cost lifecycle control.

### 19.16 Basket vs. treasury: the custody distinction (READY — clarifies and amends §4's "platform becomes part-owner")

- **The basket** is the holders' property — what the token *is*. It holds RWA slices
  (both mirror-bought and mint-contributed) and the cash sleeve. Never platform
  tokens. Custodied and bankruptcy-remote from the operator.
- **The treasury/platform** is the operator's working capital. It holds cash (fees,
  currency-side tax share) and platform tokens bought with revenue (treasury stock:
  out of supply, non-voting, not assets). **It never holds RWA slices** — when
  treasury value funds a mirror leg, the slice lands in the basket, not the
  treasury. The treasury's assets are always money-shaped; the basket's are
  asset-shaped plus a cash buffer.
- The model is fund custody vs. manager balance sheet (an ETF's assets vs. its
  sponsor's corporate account). Three reasons the wall is load-bearing: NAV
  integrity (operator revenue/spending must not move NAV), bankruptcy remoteness
  (operator can fail without touching backing), and the self-buy firewall.
- **Amendment to §4/§7:** under this ledger the platform never owns assets — it owns
  fee flow. The §7 common-ownership/referee conflict as originally framed largely
  dissolves; what remains is the operator-conduct surface (§19.17 regulatory
  findings), not an ownership surface.

### 19.17 Adversarial panel, round two (mechanism / regulatory / systems-composition)

Run 2026-07-20 against §19.12–19.15 + held-tokens-only voting. Verdict: **the exit
tracker, held-only voting, the registrar core, and the no-pre-mine rule survived
recomposition; the "unaffiliated bidder" predicate, the currency-side tax base, the
bootstrap path, and the regulatory posture did not.**

**FATAL-TIER (strategic decision required, not a parameter):**
- **Investment Company Act of 1940, not Howey, is the kill shot.** The basket is
  structurally an unregistered interval fund; registration doesn't save it (§17(a)
  affiliate rules ban the operator's co-buys and standing bid; 22e-4/6c-11
  unmeetable for illiquid RWA). Cheapest viable posture: **§3(c)(7) + Reg D —
  qualified-purchaser/accredited-only with contract-level allowlists** (the §19.15
  registrar + §6.2 KYC infrastructure IS the compliance machinery). Cost: no
  retail — which contradicts the "democratic play" narrative and the current
  marketing posture. This must be decided explicitly. The pages' repeated
  ETF self-description is Exhibit A against the unregistered path.
- **The expense ratio is NAV-linked comp to the party that runs the marks** — the
  PE self-marking disease §6 exists to cure, reinstalled in the referee's hand
  (also triggers the Advisers Act). Sever: independent NAV administration from
  committed on-chain checkpoint data; fees only on lagged NAV that survived K
  checkpoints, or cost-plus; affiliation/haircut adjudication outside the operator.

**CRITICAL (mechanism):**
- **Rented genuine bidders break the robust mark**: real, clean-graph, Tier-4
  parties paid side-fees with private repurchase guarantees produce an honestly-
  clustered fake distribution that passes every §19.12 layer (~4.3× overmark for
  ~$150k). Affiliation is not a decidable predicate — stop trying to detect it;
  make the guarantee unexecutable: **winner slices escrow-locked, non-transferable
  and non-encumberable for the K-checkpoint cure period, and mint/mirror sizing
  additionally capped by a cross-asset comparable band.** A rented bidder must then
  carry real unhedgeable exposure to the fake price — the rental fee converges to
  just paying the fake price.
- **Genesis deadlocks, twice.** (a) The bidder-depth bar + K-disjoint-cohort curing
  are unsatisfiable when the whole genuine bidder population is one small cohort;
  (b) the float-refill valve is keyed to trailing exit volume ≡ 0 at genesis, and
  the door cap (%-of-float) cannot fund even one honest bid on the first real
  asset. Fixes: **paid-legs-only provisional entry** (below the bar, the winner leg
  executes as a real sale; mint = mirror = 0 until the mark cures; provisional
  marks display-only at a haircut — shill-safe because a ring buys nothing that
  mints, sizes, or votes); valve/cap keyed to **max(trailing exits, deposit-backed
  committed auction demand)**; cohort-disjointness graded against contemporaneous
  bidder-population size.
- **The currency-side tax can be structured to ~zero on-venue** (token-for-token
  barter, junk-denomination, understatement, netting) — and portability pricing
  adversely selects the remaining tax base toward garbage while venue-lock leaks at
  the account layer (sell the SPV/keys). One fix closes all three: **levy the tax
  at the registrar layer on owner-change, valued at the checkpoint mark of the RWA
  side (staleness-haircut), independent of stated consideration and venue.**
  Portability then prices only mark-visibility; the venue-lock discount becomes an
  ex-post rebate proportional to actually-taxed volume; portability flips charge
  retroactively.

**HIGH (composition/consistency — each fix is one sentence):**
- Quorum arithmetic freeze: the adopted guards shrink votable weight while the
  quorum denominator stands still → quorum denominates over **votable supply**
  (float − treasury − unvested − exiled-escrowed), snapshotted, with an absolute
  participation floor.
- Contraction outruns the capped refill in heavy exits → on valve trigger the door
  cap re-bases to max(cap% × float, trailing exit volume).
- Discount-state absorbing trap (tax base gone, door dead, mint/mirror at zero,
  only burns flowing) → ratify the IPO settlement fee as a burn/treasury **split**
  (auctions are the flow that persists in downturns), and permit the treasury to
  **sell** revenue-bought token inventory to entering winners (no-pre-mine
  constrains acquisition, not disposal).
- "Exits burn fully" vs. premium-park contradiction → third provenance color:
  parked exit proceeds are a **deferred-buyback liability** — spendable only as
  buyback-and-burn ≤ NAV(1+ε), FIFO, earmarked inside the sleeve; §19.7 #3 reads
  "exits burn fully, possibly deferred by the ceiling."
- Uniform ratio vs. treasury-capped mirror → solvency wins instant-by-instant;
  uniformity becomes an eventual invariant: **mirror shortfalls queue as
  first-claim treasury obligations**, topped up at later checkpoint marks until
  inside the band.
- Entry-side escrowed (unminted) assets carry **zero NAV weight** until their mark
  first cures (else a caught manipulation still inflates the buyback ceiling and
  door pricing); RWA tokens are never eligible bid-deposit collateral.
- Self-referential TWAPs → exclude platform-program prints (registrar-known
  accounts) from every settlement/NAV TWAP; settle on unaffiliated volume with
  min-depth, falling back to last cured mark + haircut. Record-date freezes switch
  the asset's NAV contribution atomically from mark-basis to expected-proceeds
  basis; venue order-cancel is two-phase with the freeze.
- Distribution poisoning is one-directional (min() only lowers) → two-sided trim
  (outliers dropped, never penalized against the seller), deposits scale with
  distance-from-reserve, bound computed over bids ≥ seller reserve.
- The slashing/bounty court doesn't exist → proof standard = signed coordination
  messages only; bounties capped at provable counterparties' deposits; appeals to
  a sortition panel (§6.12.4), never a token vote.
- Wrappers rebuild the Big Three one layer down (vote depositors' tokens, run
  freeze-window dark pools) → whitelist condition: pass-through voting or forced
  abstention; payouts per disclosed depositor snapshot or haircut.
- Record dates are scheduled MNPI → retroactive record date (last block before the
  proposal published); title-transferring loans are taxed owner-changes.
- Checkpoint-denominated guards thin as cadence rises (§19.6 says raise cadence) →
  dual-denominate all such parameters as max(K checkpoints, T wall-clock days).
  State plainly in prose: **held-only voting weight is buyable at NAV in unlimited
  total — the door makes the plutocracy open-market refillable; caps are rate
  limiters, not total limiters.**

**Marketing corrections (applied to the live pages during this round):** voting
formula updated to held-tokens-only (was still the amended-away assessed-value
rule); "invest through the marketplace" → "participate"; "backed by everything on
the platform" → "backed by real assets at auction-proven prices." **Still open,
architect's call:** the "money that can't be printed" hero (attackers: overclaim —
the honest form is "no discretionary printer"), the ETF self-description (regulatory
Exhibit A), the appreciation identity presented as a "result," downside disclosure,
fee-table completeness (expense ratio, portable fee), and the retail-vs-QP posture
that decides the whole marketing register.

### 19.18 The three pots, the managerless principle, and the rented-bidder residual (READY)

**Three pots, not two** (refines §19.16's two-sided split — "treasury" was
conflating the latter two):

1. **The basket** — holders' property: RWA slices + cash sleeve. The token is this.
2. **The deployment pool** — the *system's* money: the deployment share of the
   trade tax, earmarked by rule for mirror co-buys and the standing bid. Spent by
   rules on schedule, never by people; not available for operations. Its purchases
   land in the basket (tax converting into backing — the appreciation engine).
3. **The operator** — the company: issuance/tokenization/escrow/auction fees (and
   any management fee). Pays the team. Never touches pots 1–2.

**Managerless principle:** the basket has no discretionary manager — auctions and
the fixed leg-split decide what enters; checkpoints with robust marks price it;
pool trades execute mechanically (batched, scheduled, TWAP'd); exits are
initiative-governed. The operator has no discretion over the basket. Residual
human-judgment surfaces (listing standards, affiliation calls, scheduling) route to
fixed rules, governance, or sortition — never operator discretion. Note honestly:
managerlessness helps the Advisers-Act/conduct posture but does NOT itself exempt
from the 1940 Act (pooled investment is caught managed or not); the QP-vs-retail
decision stands regardless.

**Rented-bidder residual economics (architect-ratified direction):** the escrow
lock does not prevent the attack — it re-prices it, and that is the design goal.
Under the lock, the rented winner carries months of unhedgeable exposure plus
unsecured counterparty risk on the full overpayment (the repurchase guarantee
cannot execute while locked, and the fake mark decays under disjoint-cohort
re-marking meanwhile) → the rental fee converges to the overpayment itself. Payoff
side independently capped: comparable band on mint sizing, zero NAV until cure,
marks never vote. Residual worth-it case = overpay real money at real risk to push
one mint a band-width rich — bounded, priced, never cheaper than honesty. Same
standard as the whale answer (§19.11 discussion): manipulation is not impossible,
it is demonetized and rentable.

### 19.19 Naming ruling (architect): basket / treasury / operator

"Deployment pool" is dead. The three pots are: **the basket** (the ETF of assets —
holders' property), **the treasury** (the platform's liquidity — the tax's
deployment share, spent only by rules on mirror co-buys and the standing bid), and
**the operator** (the company — service fees, pays the team). All §19.16/§19.18
"deployment pool" references read "treasury"; the treasury remains distinct from
operator revenue exactly as §19.18 specifies — the rename does not re-merge the
pots.

### 19.20 Tax routing ruling (architect): 8:1:1, treasury-first

The trade tax (levied on each ownership change at the asset's last checkpoint mark)
splits **≈ 8:1:1 — treasury / basket / operator**, superseding §19.13's
basket-heavy split. Rationale: the platform must make its own money; the basket's
value story stays pure ("assets bought at proven prices"); appreciation arrives
predominantly through IPO deployments (treasury → mirror co-buys → basket) rather
than a continuous drip. The trade itself remains overwhelmingly buyer↔seller — the
tax is small.

Implications, all favorable to earlier findings: the treasury is genuinely funded
(mirror legs execute; the discount-state trap's "no inflow" leg weakens; the
operator gains volume-linked — not NAV-linked — recurring revenue, curing the
§19.17 expense-ratio concern's main motivation). Unchanged guards: treasury is
rule-spent only (mirror queue, standing bid), the split parameter sits behind the
constitutional floor/time-locks (bigger honeypot, same locks), and the invariant
holds — appreciation is still Δbasket unmatched by mint, now arriving lumpy at
deployments instead of continuously. Status: PROPOSED pending exact ratio
ratification; the 8:1:1 shape is architect-directed.

### 19.21 The cash-only simplification (PROPOSED as v1 — architect-prompted)

After two adversarial rounds, the architect observed that the design had become a
mess: the treasury is hard to fund early, and the mint leg is heavily incentivized
to be gamed. Assessment: correct. The entire §19.12/§19.17 defense stack (robust
marks, rented-bidder locks, comparable bands, cure periods, bidder minimums)
defends exactly one rule — that delivering an asset at an auction price creates
fresh tokens. Remove that rule and the stack collapses.

**Cash-only v1:**
1. **Tokens are created for cash only** (the door, at NAV + spread). Nothing else
   mints. No price input exists to inflate.
2. **The basket only ever buys assets** — with cash it has, at auctions, as a
   voluntary bidder: never obligated, capped at the comparable band, limited by its
   balance.
3. **Exits unchanged**: proceeds → buyback ≤ NAV → burn.

Consequences:
- The inflated-bid attack reduces to "trick a voluntary buyer that has a price cap
  and a budget" — worst case a bounded overpayment within the band, never
  issuance, never dilution. §19.12's machinery becomes optional hygiene, not
  load-bearing.
- Held-tokens-only voting emerges naturally: owners who want weight sell slices
  for cash and buy tokens through the door.
- Supply = cumulative cash delivered at NAV. Backing trivially complete. Entries
  trivially NAV-neutral.
- Sequencing honesty: early basket growth is door-funded (genesis + entrants);
  the tax trickle accumulates; treasury co-buys and the standing bid are
  maturity features that switch on when volume funds them. The 8:1:1 split
  (§19.20) stands, with realistic expectations about early magnitude.
- Given up: the ETF creation-unit (assets entering without a cash round-trip) and
  faster basket growth. The mint leg may return later only by earning its way in
  against this baseline, carrying the full §19.12–19.17 stack.

This is the recommended presentation baseline: three rules, no vigilance-dependent
guarantees, the attack dies of arithmetic.

### 19.22 Mirror governance and the IPO cycle (RULING — architect's words; implications labeled)

Architect rulings, verbatim intent:
1. **Non-votes are NOs.** Basket purchases (mirror co-buys) execute only on an
   affirmative majority; abstention denies. Plus the earlier one-line rule:
   sellers sit out votes on their own deals (gain is private, loss is shared —
   recusal makes self-dealing net-negative).
2. **Long public warning window** before every IPO.
3. **IPOs run per cycle** (analyst's reading, unconfirmed in detail: slate
   published at cycle start, votes during the window, approved mirrors execute
   batched at cycle close).

Implications (analyst's, not rulings): default-deny eliminates quorum arithmetic
and turnout games entirely — moving the basket requires an affirmative majority of
all votable tokens, raising coalition-capture cost from "majority of the engaged"
to "majority of everything"; the engagement burden on honest purchases is paid for
by the warning window and single per-cycle voting moment. A published cycle
calendar removes the private-schedule surface that motivated the front-running and
MNPI guards — batch execution stops being a defense and becomes the clock.

### 19.23 Door currencies (RULING) and the creation arithmetic confirmed

- **Governance defines the whitelist of currencies that convert into tokens at the
  door.** Analyst caveat, flagged as such: stables are trivial; volatile currencies
  reintroduce a rate-source (oracle) problem — default is a stables-first list,
  and any volatile addition must specify its conversion basis (e.g., the executed
  swap price on immediate conversion — a transacted price, preserving the
  no-oracle principle).
- Creation arithmetic confirmed with the architect's own example: pool $10M / 5M
  tokens → backing $2/token; $500k in → 250k tokens out → $10.5M / 5.25M, backing
  unchanged. Creation executes at the NAV (backing) rate + spread, never the
  market rate — at a market premium, NAV-rate creation is what prevents handing
  buyers paper gains against the basket.

### 19.24 Co-buy timing (RULING): one cycle delayed off the auction

The basket's co-buy executes one cycle after the auction. Analyst implications,
labeled as such: the vote is cast knowing the actual cleared price (not blind); the
winner's own tokens paid that price a full cycle before treasury cash moves, so the
basket only follows real money in; a manipulated auction must survive a cycle of
public scrutiny plus an informed default-deny vote before touching the treasury.
Open detail (not guessed): whether the basket pays the auction's cleared price or a
re-marked price at execution — default reading is the cleared price, pending
confirmation.

### 19.25 Two pots (RULING — supersedes §19.16/§19.18-19.20 pot structure)

The 8:1:1 tax split (§19.20) was an analyst misreading of the architect's
shorthand — **struck entirely**. With cash-only v1, no separate treasury exists:

- **The basket**: cash and assets, the token holders' property. The trade tax
  flows into it; voted co-buys are paid out of it; exit buybacks come from it.
- **The operator**: the company, paid only through the published fee schedule.

The three-pot structure (§19.16/§19.18) and its "deployment pool"/"treasury"
naming are superseded. The distinction that survives is the only one that
mattered: holders' money vs. the company's money.

### 19.26 Taxes, not fees (RULING)

The fee menagerie (issuance/tokenization/escrow/auction fees) was arbitrary.
Replaced by one uniform model: **every action on the platform pays a small
operator tax that is constitutionally fixed — it can never be raised — plus a
basket tax per action, set by governance from zero upward.** Operator revenue is
thereby guaranteed, small, and un-gameable by governance capture in either
direction (can't be raised by the operator, can't be zeroed by a hostile vote);
the holders control only how fast their own pot fills. Portability pricing
survives as differential basket-tax rates set by governance. Actions covered:
door creations, tokenization, escrow custody/release, ownership changes (valued
at last auction mark), auctions.

### 19.27 Lexical ruling: fees vs taxes, and the pot stays "the basket"

Architect: **fees go to the operator, taxes go to the basket.** The fixed
immutable per-action cut is a *fee* (a price, the company's); the governed
0-upward per-action levy is a *tax* (the community's, voted and received by the
holders' own pot). Same structure as §19.26, corrected vocabulary.

Pot naming (architect asked basket vs fund vs treasury; analyst recommendation,
accepted pending objection): **basket.** "Fund" is the regulatory self-label the
round-two panel flagged as Exhibit A; "treasury" implies the platform's money and
resurrects the pot confusion §19.25 killed; "basket" states the thing — the pool
of cash and assets backing the token.

### 19.28 Exit burn retired; redemption door added (architect-caught staleness + architect proposal)

- **Architect correction (confirmed):** the mandatory exit buyback-and-burn was a
  mint-era rule — supply created against assets had to contract when assets left.
  Under cash-only v1 supply is created only for cash, so an exit is an
  asset-for-cash swap at market value: **NAV-neutral, nothing to burn.** Rule
  removed.
- **Redemption door (architect proposal, analyst detailing labeled as such):**
  burn tokens → receive backing × tokens in cash. Mirror of creation,
  NAV-neutral by construction. Effect: a standing **floor at backing** —
  with the door capping premiums at backing + spread, the market price lives in
  a band around backing, enforced by open arbitrage, continuously.
- **No per-event vote for cash redemption** (a vote would kill the arb;
  redemption at backing cannot hurt remaining holders, and a small spread is
  mildly accretive to them). Governed parameters only: spread, and a cash floor
  so redemptions queue rather than force asset sales. **In-kind redemption
  banned** (or vote-gated): pulling assets out lets redeemers cherry-pick.
- Burn ✕ glyphs now mark the two real retirement events: RWA tokens retiring at
  the registrar on asset exit, and platform tokens burned at the redemption door.

### 19.29 The round-trip toll (architect insight, confirmed)

Why the basket can't be used as a free liquidity pool: the door's creation
fee+tax and the redemption exit fee price the round trip. Costless in-and-out
would let the basket be churned like a money market; with the toll, the doors
clear only for genuine entries/exits — or for arbitrage when the market price
leaves the backing band by more than the toll, which is exactly when arbitrage
is wanted. Corollary: the band's width around backing IS the toll (ETF creation
fees / AMM swap fees, same logic). Vocabulary note: "marks" and "NAV" are
retired page-side in favor of "last auction price" and "backing"; checkpoint
auctions are "re-auctions" in public copy.

### 19.30 Characterization + portability rationale updated (architect-confirmed)

- The honest one-line description: **an index fund whose venue pays it rent** —
  assets plus the perpetual tax flow of the marketplace it sits in, compounding
  into backing rather than sitting beside it. This is the differentiator from
  "a normal ETF": a tracker tracks, this earns.
- Portability split retained with corrected rationale: the registrar taxes every
  ownership change regardless of venue, so off-platform flow does NOT
  "contribute nothing" (old copy, fixed). Venue-lock buys **enforcement and
  visibility** — on-venue flow is automatically taxed and marks prices live;
  off-venue flow is trust-dependent (account-layer dodges) and price-silent
  between auctions. The tax discount prices verifiability, not contribution.

### 19.31 The long-horizon store-of-value thesis (framing for §6.12B)

How v1 fills §6.12A's "separate store of value required" gap, against the
implicit checklist:

1. **Un-debasable by arithmetic, not scarcity**: supply is elastic but every unit
   is fully paid for at backing — issuance can never tax holders; no privileged
   proximity to the door (Cantillon removed at the root).
2. **Productive, unlike gold/BTC**: a claim on real assets plus the venue's
   perpetual tax rent — the historically durable form of stored value
   (yielding land, compounding equity) in bearer form.
3. **Honest rather than stable**: tracks both directions; redemption floors at
   backing; no peg, hence no reflexive spiral — fails openly, corrects at the
   next cycle (§6.15).
4. **Completes the Graeber split**: earn/spend in kWh (elastic, unhoardable),
   save in the basket token. Bridge: the door's currency whitelist can
   eventually admit the kWh token — energy income converting to savings on the
   same rails, removing the fiat intermediation §19.22-era discussion accepted
   as temporary.
5. **Asymptote**: a diversified pro-rata claim on the productive on-platform
   economy, marked only by paid prices, governed only by holders.

Caveat for all prose: store-of-value status is earned, not declared — credibility
accrues with basket diversification, auction cadence, and the band holding
through its first real drawdown. The design's compounding advantage is that its
track record is verifiable.

### 19.32 The third currency (architect observation, closing note)

Money is three jobs; the system has two natives: basket = store of value, kWh =
future medium of exchange. The **stable unit of account** is currently borrowed
(USDC) — the third currency exists, it just isn't ours. Ruled discipline: do not
mint it — a native stablecoin means a peg (a promised value, the one promise the
design never makes) or MakerDAO-class collateral/liquidation machinery (the
complexity class v1 amputated). Instead: the platform bootstraps its own third
currency — energy inixiatives funded through the marketplace ARE the future
generation capacity that backs the kWh token (§6.12A's 1:1 production rule).
Sequence: settle in USDC as scaffolding → energy inixiatives accumulate → kWh
pilots inside them (e.g., a solar inixiative paying in kWh credits) → door
whitelists kWh → the platform prices in the unit its own assets produce. A
two-currency design running on a borrowed third, with the borrowed one scheduled
for replacement by the platform's own output.

### 19.33 The scheduled re-founding (architect seed; analyst construction labeled)

Architect observation: the basket is mostly currencies for a long time, until
co-buys convert it — and the conversion is a **constitutional amendment
opportunity**. Construction (analyst's, for ratification):

- **Objective trigger**: assets exceed a set share of backing (e.g., half),
  sustained N consecutive cycles — computed from the ledger and paid prices;
  nobody declares it.
- **One amendment window**, announced cycles ahead, under stricter rules than
  ordinary governance (supermajority of all votable supply). A single
  constitutional convention held when real operating data exists — instead of
  perpetual governance drift or premature lock-in.
- **The immutable core survives even the convention**: tokens only for cash at
  backing; no pre-mine; redemption at backing; held-tokens-only voting; operator
  fee lowerable, never raisable. Everything else — tax rates, cycle length,
  quorums, the currency whitelist (the natural moment to admit the kWh token) —
  is on the table exactly once.
- **Named risk**: the window is a capture target; defenses are the full-supply
  supermajority, the immutable core, and years of advance notice letting anyone
  buy a voice the only way the system allows — at backing.

Rationale: cash-era rules and asset-era rules differ; a constitution written
before either era is wrong somewhere. Naming in advance the one moment of
rewrite, its threshold, and what survives it is more honest than either
crypto's fake immutability or fiat's amendment-by-decree.

### 19.34 Platform voting weight: held tokens + IPO'd stake (RULING; guards PROPOSED)

Architect ruling (restoring the original two-leg formula, now with the v1 gate):
**platform voting weight = held platform tokens + the value of your RWA holdings
in IPO'd inixiatives.** Only auction-proven value counts — pre-IPO, self-assessed
assets confer zero platform weight. Inixiative-level voting unchanged (RWA tokens
govern their own inixiative).

This reopens only the voting channel of the manufactured-weight attack (the
basket's cash is already protected by the voted, cycle-delayed co-buy). Guards
(analyst proposal, unratified):
1. **Stranger-anchored**: stake counts at the price provably-unaffiliated bidders
   paid; a self-auction won by one's own shill confers nothing.
2. **Vesting + cure**: full weight only after surviving a re-auction with a
   disjoint bidder cohort.
3. **Age decay**: weight carries the same staleness haircut as the price, until
   re-proven.
4. **Dies at exit**: liquidation extinguishes the weight (power tied to live
   exposure, matching redemption-burn semantics).
Supersedes the held-tokens-only amendment recorded in §19.11/§19.17 discussion;
the earlier flat rule is retained in the record as the fallback if the guards
prove too weak in a future adversarial pass.

### 19.35 The tax-rate equilibrium (architect insight)

The tension between low taxes (marketplace stays saleable, flow stays on-venue)
and high taxes (value accrues to holders) self-corrects toward the right level —
a Laffer dynamic with the uniquely honest taxing authority: the rate-setters own
the venue being taxed and personally eat both failure modes. Structural
convergence aids: (1) the two-leg electorate IS the two-sided market — builders'
IPO'd-stake weight pulls rates down (they pay), holders' token weight pulls up
(they receive); the rate is continuously bargained between the platform's two
consumer classes in proportion to proven stakes. (2) The constitutionally fixed
operator fee sits outside the vote, keeping the bargain undistorted by a third
skimmer. Named caveat: short-horizon coalitions voting an extractive spike —
leaned against by redemption-at-backing (extraction must accrue before it can
exit; no front-running your own tax hike through the door).
