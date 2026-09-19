# A bureaucracy without a career

*Substack draft. Supplemental to the whitepaper; the argument connects to Document 2 §4 (the
bureaucracy-versus-chaos dialectic and the thin-elites requirement) and Document 3 §6.12
(limits on elite accumulation, sortition, distributed audit). Not part of the paper proper.*

---

Most people who think about AI and government arrive quickly at the same picture. The permit
office that takes six weeks and ten people will take six minutes and none. The forms will fill
themselves in. The clerk who checks the form against the rule will be a model, and the model
does not go to lunch. Fewer people in the machine, faster answers out of it, and a budget line
that finally goes down instead of up.

This is a reasonable picture and most of it is true. What a bureaucracy mostly does is three
things. It remembers, so that the decision made last year binds the decision made this year. It
routes, so that the right case reaches the right desk. And it applies rules, so that the case is
decided by the rule and not by whoever happens to be sitting there. Those three functions are
exactly the ones a language model does well, and they are the ones that justified the headcount.
Take the headcount away and something else goes with it. The people whose income depends on the
problem staying unsolved are the people at the desks. Remove the desks and you remove the class.
This is the strongest version of the hope, and it is worth letting it look clean before asking
the question that breaks it.

What was the six weeks doing?

It was the only brake. Every rule a bureaucracy enforces has to be staffed, and staffing shows
up in a budget, and budgets get argued about. When someone in the permit office proposed a
fourth review step, the answer was often no, because the fourth step meant two more people and
the two more people had to be justified upstairs. The friction was never designed as a limit on
how much rule a society could bear. It just worked as one. Michael Zanini's work on
administrative growth, which Jiang draws on for the empire-building argument, describes a
ratchet: each layer of administration creates demand for the next layer. The ratchet ran
against labor cost the whole time. Labor cost was the thing it had to overcome.

Now make the cost zero. A rule that costs nothing to enforce gets enforced everywhere. A form
that costs nothing to process gets required for everything. The fourth review step is free, so
you add it, and the fifth, and a check on every transaction rather than a sample, because why
would you sample when checking is free. This is Jevons on coal applied to administration: make
the thing cheaper and you get more of it, not less. The bureaucracy that AI produces by default
is not a smaller one. It is a total one. Every interaction logged, every rule applied to every
case, and no clerk anywhere with the discretion to say this one is fine, let it through.

So the opportunity is real but it is not the one the first picture names. The win is not fewer
people in the machine. The win is that the machine stops having a career.

Here it helps to remember what the machine was supposed to be. Weber's model of bureaucracy,
the one every civics class still teaches, has the legislature making the rules and the official
applying them. The official's discretion is the residue, the small gap between the rule and the
case. On that model the bureaucracy is subservient to law by construction, because it does not
write the law, it only runs it.

That is not what happened. The rules migrated into the bureaucracy. A legislature writes a
statute that says the agency shall ensure safe drinking water, and the agency writes the rest,
and the rest runs to thousands of pages that nobody in the legislature has read. This was not a
coup. Legislatures delegated because they could not keep up. Tainter's account of complexity is
the relevant one here: each success adds a layer, each layer needs specialists, and the
specialists end up holding the pen. The courts noticed. In 2024 the US Supreme Court threw out
the doctrine that told judges to defer to agencies on what an ambiguous statute means. That
moved the interpretation from the agency to the judge. It did not move the writing. The agency
still writes the rules. It just argues about them in a different room now.

The ratchet, in other words, never lived in the applying. It lived in the rulemaking. And this is
the thing that changes when the process becomes software.

Today a regulation is prose, interpreted by people, and its actual behavior is knowable only by
living under it. You find out what the rule does when it is applied to you. If the process runs
as software, the rule is the configuration. A configuration can be read. It can be diffed
against last week's. It can be reviewed before it takes effect and reverted after. The whole
apparatus that software engineers built for managing change in a system too large for any one
person to hold in their head becomes available for managing a bureaucracy, which is also a system
too large for any one person to hold in their head. Democratic governance of the administrative
state stops meaning governing an organization, which nobody has ever managed, and starts meaning
governing a change process, which is a thing we know how to do.

And it is how law already works, when it works. There is a fast lane for small changes, a slow
lane for structural ones, and a much slower lane for changing the lanes themselves. A parameter
moves through the first with a tripwire on it: if outcomes shift past a threshold, it reverts
on its own and goes to review. A change to the structure of the rules goes through the second
with a vote. A change to who gets to vote, or what counts as structural, goes through the third.
Constitutions, statutes, regulations. The tiers are old. What is new is that the bottom tier can
be made legible, and legibility is what the bottom tier never had.

Now the objection, at full strength, because it is a good one.

Who reads the diff?

Nobody reads statutes now. A change log of ten thousand rules is not more readable than the
rules, it is less. And the picture has quietly made another thing worse. The people who
configure the machine are fewer than the people who used to staff it, and fewer people are
cheaper to capture. A thousand clerks with a thousand small discretions are hard to buy. Six
engineers with commit access are not. On this reading the software bureaucracy is not more
democratic than the human one. It is a smaller oligarchy with a better audit trail that nobody
looks at.

The repair has two parts and neither is a full answer.

The first is that reading does not have to mean everyone reads everything. It can mean that
some people, chosen at random, read some things, on a budget. Sortition does the choosing, and
it does it for the same reason juries use it: you cannot capture a reviewer you cannot predict.
The budget matters because the failure mode of citizen audit is exhaustion. Ask people to check
everything and they check nothing. Give them a finite number of audits and a finite number of
flags and the audits get spent where the reviewer's own life tells them something is wrong.
That is not a general reading of the rules. It is a sample, and a sample is what you can afford.

The second is that most of the change log should not be read by anyone. It should be watched by
a reflex. Deliberation is for what people can attend to. For everything else the right control
is a tripwire: the rule changed, the outcome moved, the rule reverts, a human is told. The body
does not deliberate about pulling a hand off a stove. A system with ten thousand rules and a few
hundred attentive citizens needs most of its safety in the reflexes and only the residue in the
deliberation. That is the reverse of how bureaucracies are built now, where everything is
deliberated, slowly, by the people who wrote it.

Three things remain unsettled and should be said plainly.

The first is whether a citizen can audit a rule they did not write, even with a model
explaining it to them. The model explaining the rule is built by the same people who configured
the rule. That is not a fatal objection. Auditors already rely on the audited for the books. But
it is a real one and nothing above answers it.

The second is that the enforcement asymmetry gets worse, not better. A bureaucracy finds the
compliant, because the compliant are findable. The person who filed the form is in the system.
The person who did not is not. A cheap, tireless machine is better at this than a tired clerk,
which means the fix has to be in the rule and cannot be in the machine. If the rule says find
everyone, the machine will find the people who can be found.

The third is the jobs. Administrative work is a very large share of what the middle class does
for a living. Graeber's account of pointless work was an account of misery, and the misery was
real, but the paycheck was also real. A society that removes the desks removes the income that
sat at them, and the case for doing it has to include what those people do next. It usually
does not.

None of that changes the shape of the argument. The thing to want from AI is not a smaller
bureaucracy. A smaller bureaucracy is what you get for a year, before the ratchet finds that
its old enemy is gone. The thing to want is a bureaucracy that cannot want anything: no
positions to create, no budget to grow, no reason for the problem to stay unsolved. And a way
for the people who live under it to change it that does not run through the people who built
it. The first of those, the machine is about to hand us for free. The second we will have to
build on purpose, and the window for doing it is the year before the ratchet works out what
happened.
