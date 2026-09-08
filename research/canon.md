# Canon

Fixed decisions for the draft in [book/](../book/). Names, places, and the rules the prose follows.
Anything not listed here is free.

## Structure

**27 chapters**, not the 32 of [outline2.md](outline2.md). The draft deliberately diverges: the
outline's four-per-beat symmetry produced four consecutive backstory chapters and two consecutive
four-POV montages, which sagged. The merges:

- Outline ch1+5 → **ch1 Twelve Minutes** (Kate: the day *and* the wound)
- Outline ch2+6 → **ch2 Football** (Alex: fights and loses, then stops fighting)
- Outline ch3+7 → **ch3 Deep Breath** (Michael: the grind *and* why)
- Outline ch4+8 → **ch4 The Exchange Rate** (Nik: the polish *and* its origin)
- Outline ch9+10 → **ch5 The Third Time** (one escalation, not two montages)
- Outline ch11–32 → **ch6–27**, unchanged in content, renumbered −5

Each character now gets one substantial introduction carrying both present-day noise and wound,
which is why the front no longer takes ten chapters to reach the hotel.

## Narration

Third person limited, past tense, close free indirect. One POV per chapter unless the chapter is
one of the four-part ensembles (9, 10, 11, 26) or a group scene (16, 25, 32), which move between
POVs across scene breaks. The narrator is dry but never superior — the comedy comes from what the
character believes about themselves, not from the narrator knowing better. No moralising, no
summing up. Chapters end on the image, not the conclusion.

Scene breaks are `---`. The chapter heading is `# N. Title`. Nothing else in the file.

## Setting

England, present day. The three companies and the bank are London-based; Lodestone is in Guildford.
The hotel is **The Ardenne**, a twelve-floor conference hotel outside Birmingham, near the NEC:
1974 concrete, refurbished twice, a ballroom called the **Warwick Suite**, a staff terrace on the
roof above it, a lobby bar, a breakfast room with too few tables, an atrium where the chess congress
sets up its boards. Three events run in the same building at once — Kate's board summit, the
banking conference where Michael speaks, and the Midlands Open chess congress.

## Kate Merrick — CEO, 41

**Bellwether**, a fast-growing multi-brand e-commerce group (homewares, then everything).

- **Dawn Fowler** — her assistant. Two children, leaves at five, brings food in tupperware.
  Dances on Wednesdays and has for eight years.
- **Gareth Pryce** — CTO, the man she talks over.
- **Tom Ferreira** — VP of Engineering, the man she talks *to*. Owns the crisis in ch27.
- **Harriet Nash** — board chair. **Roger** and **Elizabeth Merrick** — her parents.
- **Sasha** and **Bea** — the friends on the thread she keeps cancelling.

## Alex Wójcik — CTO and co-founder, 26

**Velum**, a runtime-security startup, Series B, forty-one people.

- **Ben Farrow** — co-founder and CEO. Articulate, warm, talks over him without noticing.
- **Saul** — third co-founder, GTM, mostly offstage.
- **Arcus** — the American acquirer that wants the product and the team.
- **Marek** and **Ewa Wójcik** — his parents. Came from Poland with nothing; Marek did nights at a
  bakery on Bethnal Green Road and days at a print works.
- **The dates.** Marek arrived in 1994, at thirty-seven, with Ewa and a trade that did not transfer.
  He is sixty-eight now. **Alex was born here, in 1999** — his parents have the accent and he does
  not, which is the whole of the pitch in ch2. He does not arrive as a child with them. The dead
  Compaq goes on the kitchen table in 2007, when he is eight, and takes eleven weeks.

## Michael Halloway — COO, 64

**Lauriston**, a bank founded in 1786. Coasting to retirement.

- **Ruth** — his wife, forty years. **Claire** — his daughter. **Danny** — son-in-law, works the way
  Michael worked at thirty-eight. **Iris**, nine, piano. **Sam**, six.
- **Fiona Redgrave** — the bank's CEO. **Callum Deitch** — the younger executive in the program
  review. **Terry Nwosu** — the colleague whose career Michael launched, who makes the call in ch24.
- **The Ledger Gap** — the bank's decade-old reconciliation problem between a 1994 core ledger and
  the payments gateway. Three consultancies, no fix. What Alex solves on a flip chart.
- **The deep breath.** Michael takes one after each finished thing. It is planted from ch3 and never
  once explained, remarked on, or noticed by another character. It is the only channel the reader
  has to him. Do not resolve it. See the note that Michael alone gets no vantage on himself.

## Nikhil "Nik" Raghavan — CFO, 42

**Lodestone Games**, Guildford. Mid-size studio, wobbling, not collapsing.

- **Meera** — his wife. **Anaya**, nine. **Rohan**, three, still waking at night.
- **Gus Delaney** — the studio's founder-CEO. **Priyesh** — the FD who reports to Nik.
- **Raghavan** and **Shobha** — his parents, in Chennai. His surname is his father's name.
- **Wilf Tanner** — retired structural engineer, eighty-three, sixty years of tournament chess.
  Nik's post-mortem partner in ch12.
- The suitcase is one of the original two. Twenty-six years old, one wheel drags.

## Rules the book keeps

- The vise is real *and* self-tightened. Never let a scene imply the pressure was imaginary.
- Nobody is redeemed by being told something. They are changed by seeing it on someone else.
- Michael's jokes always land. That is the problem with them.
- No character explains the theme out loud. Wilf comes closest and is allowed to, once.

## The chain

The vise is made of each other. Each of the four calls the pressure the board, the co-founder, the
number. It arrives through a chain that runs through the other three, and the reflex each uses to
survive it sends it on down the line. None of the four ever learns this, with two exceptions the prose
allows: Kate names the shared fund to Nik in ch20, and Colin tells Kate in ch26 that he was in Hall 2.
The reader assembles the rest. Nothing below is ever explained by the narrator.

- **Velum's agent runs on Marrowbone's step-up authentication hosts.** Alex fixes the teardown-ordering
  fault on the Thursday of ch2 and does not ask for a release slot. Marrowbone's German step-up fails one
  in nine for four days in ch5. Ben closes the P1 as config; Alex merges the fix at ten past one, alone,
  and the record goes on saying config. Kate's belief that anything she is not holding will be dropped
  hardens on that bug.
- **Lauriston settles for Marrowbone.** After Tom's retry fix in ch1, Bellwether's refunds go out in
  bursts of about four hundred at eleven at night. A third of the Ledger Gap's growth since June is
  Bellwether (ch3, ch12). In ch22 it is Lauriston that rejects Marrowbone's settlement file.
- **Michael approves the repricing of the commercial overdraft book at 8:27 in ch3.** Nik's letter in
  ch4, forty basis points worse and *partnership* twice, is that approval.
- **Hollis** is the fund on both boards. Simon sits for it at Bellwether, Aaron at Lodestone. Kate chose
  it over a cheaper term sheet because it was known to be demanding.
- **Velum's control-plane certificate expires at twenty to four on the Thursday of ch22 and ch24.** Every
  agent fails closed, Marrowbone stops taking cards, and Bellwether's app is down for two hours and
  twenty minutes while Kate keeps her hands in her lap and Alex tells Ben, across town, that the company
  runs on a model of its CTO. The certificate was in Alex's calendar in 2023.
- **The Ardenne's consortium** was Halloway & Grieves' largest debtor: nineteen thousand of the
  forty-one. Wilf Tanner checked the calculations on the slab in 1973 and was never paid. Michael stayed
  in the building in 2004 and shows Kate its roof in ch11. Whether Michael knows which hotel it was is
  never stated, and must not be.
- **Colin** chaired the Banking Operations Forum, asked for Michael by name, introduced him in ch19, and
  has danced on Milkwood Road with Dawn for eight years.
- **Ocean** runs Bellwether's logistics. Danny runs its south-east. The client who moves his Thursday
  call is Kate.

