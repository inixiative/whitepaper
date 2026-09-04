# Whitepaper — writing conventions

## Develop arguments, don't stack conclusions

The default failure is writing up the *result* of thinking instead of the thinking. A section
that states its conclusions in sequence — each one bolded, each one supported by a citation —
is unreadable even when every claim in it is true, because the reader is handed destinations
with no roads between them.

Write the working-through instead. The conclusion is easy to state and hard to earn, and the
steps are where the content is.

**How:**

- **Start where the reader already is.** Open with the position most people hold, stated at its
  strongest and treated as reasonable. Usually it is reasonable.
- **Build it up before breaking it.** Show what follows if the common position is right. Let it
  look clean.
- **Break it with one concrete question**, not a counter-thesis. "What did your society spend on
  you before you were old enough to agree to anything?"
- **Follow the real sequence.** Objection, counterexample, repair. If an argument was arrived at
  by having a hole poked in it, the hole belongs on the page.
- **Concrete before abstract.** Describe the thing, then name it. Ten households who have to
  produce their neighbour or pay the fine — *then* the word "frankpledge," *then* Greif on why
  it made trade possible.
- **Short sentences. Plain words.** Not "presupposes," "instantiates," "the implication runs."
- **Bold sparingly** — genuine landmarks only. Heavy bolding substitutes for argument: it lets a
  paragraph assert where it should reason.
- **Citations arrive where the argument needs them**, not stacked up front as authority.
- **State the counterargument at full strength**, especially against the position being taken.
  An unsettled question gets marked unsettled.

Length is not the enemy. Development takes space; compression that removes the reasoning has
removed the content.

## Where things live

- `docs/` — the whitepaper proper, tracked.
- `notes/` — drafts and working material, gitignored.
- `notes/_build/` — the essay HTML generator and its recovered style block. Never regenerate the
  CSS by hand; it is the published artifact's own.
