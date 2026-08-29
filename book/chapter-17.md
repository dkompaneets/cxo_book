# 17. CC

Room 914 had an extractor in the bathroom that came on with the light and stayed on for eleven minutes after it went off.

He had timed it on the Thursday. Eleven minutes, and a small dry tick in it at the top of the impeller, and under that the ninth floor's air handling, and under that nothing.

He read the thread on the Sunday afternoon because he was avoiding his parents.

That was the true and shabby reason.

They had gone to a canal on Saturday and loved it. On Sunday morning his mother had produced a printed itinerary that included a garden centre. At two o'clock Alex said he had one work thing, and went up, and opened the laptop.

Forty-one milliseconds to London.

Velum ran on a shared workspace with about four hundred channels in it. He had built the workspace when there were nine of them and was still in all four hundred, because leaving a channel is an act with a meaning and rejoining one is worse.

The channel was `#bd-pipeline`. He had not read it in five months.

The first message was Ben's, from Saturday morning.

> 🚨 warm intro from a COO at **Lauriston** (the bank) overnight — straight to me + Saul. Alex do you know anything about this?? Says he met one of us at a hotel. Decade-old reconciliation problem, 19 FTE in Sheffield, three consultancies burned, and he says our architecture is "the first thing anyone's shown me that starts in the right place." Reading between the lines this is eight figures.

And pasted under it, Michael's email. Four short paragraphs, no adjectives except the load-bearing ones, one joke. It said he had spent an evening with the CTO of a company called Velum. It said this person had got further into the problem in two hours and forty minutes than three firms had in eleven years.

It ended: *The man you want is Aleksander Wójcik. Talk to him, not about him.*

Alex read that last line twice.

Then he scrolled.

> **Saul** (09:31): this is unreal
> **Ben** (09:34): I know. ok I've come back proposing Tues 9.30, me + Saul, at theirs
> **Saul** (09:36): can we get Alex? feels like an Alex meeting
> **Ben** (09:41): he's at a hotel thing with his parents til Tues, taking them to the airport Tues am. Don't want to pull him out, he never takes time off and I've been leaning on him hard. Bring him in for round 2.
> **Ben** (09:44): also for a first meeting with a bank we want the commercial conversation, not a 2hr architecture session where they think we're a consultancy
> **Saul** (09:45): 100%
> **Ben** (14:20): call w/ their programme director just now — the recon thing's real but what they're actually *buying* this year is compliance evidencing, new regime lands Q1, budget's sitting in that line. Told them we ship a compliance module this quarter (true), recon is phase 2. He lit up.
> **Ben** (14:31): and if this converts the Arcus story changes completely. team + tech + a bank. different multiple. Let's not say that out loud yet.

Alex sat on the end of the bed.

*He's at a hotel thing with his parents.*

True. Kindly meant. He had said it to Ben himself, in a corridor, on the Wednesday.

The extractor was still going. Four minutes left on it.

---

Then he opened a new tab, because he wanted to be fair, and went and found the demo.

It was in a branch called `causal-order`. He had pushed the first cut on the Saturday after the business centre, having come up from the fifth floor and not slept, and had kept at it in the evenings while his parents were in bed.

Nine hundred lines.

And it was the cleanest thing he had written since the interceptor, because the whole of it turned on refusing to answer the question everybody asks, which is *when did this happen*, and asking instead the one both machines can answer for nothing, which is *what had I already seen when I did this*. You take the gateway's write and you hang on it the identity of the last batch it heard about. You take the ledger's post and you hang on it the identity of the last balance it read. Sixteen bytes on each side, a field nobody has to compute, because both numbers are already sitting in memory at the moment of writing and are currently being thrown away. And then you do not sort. Sorting is the mistake. You walk the two chains and wherever they touch you have a fact — not an estimate, not a tolerance, a fact, the same fact in nine hundred years — and everywhere they do not touch you have two events that never met and never could have, and which the nineteen people in Sheffield have been reconciling every morning since 2014 because a column of milliseconds told them the two things happened in an order that nothing in the universe actually put them in.

It took two synthetic ledgers with deliberately disagreeing clocks, and eleven thousand items a night of drift, and ordered them by causality, and produced one number. How many items a human being in Sheffield would have to look at in the morning.

The number was fourteen.

He ran it again while he sat there, because it was the only thing available to do with his hands, and watched it come out at fourteen, and it took eleven seconds.

He had built the thing Michael's email was about. He had built it in thirty hours, unasked, on holiday, for free.

There was a meeting on Tuesday morning about compliance evidencing. He was not in it.

---

He rang Ben.

"Alex! Mate, are your folks having a nice time? Where are you, still up north?"

"Yeah. Listen — I saw bd-pipeline. The Lauriston thing." He had stood up. He always stood up for the ones that mattered. "That intro's mine. The COO — I did the architecture with him on a flip chart on Friday night, that's who it's from. And I've built a working demo of the recon fix. Thirty hours. It takes eleven thousand items a night down to fourteen. It's in a branch, it runs. So I think — I should be in the room Tuesday. I can move the airport, my dad'll understand, I'll—"

"Alex, that's *incredible.*"

And Ben meant it. That was the thing. You could hear that he meant it.

"Fourteen? From eleven thousand? Mate, that's the whole — OK. OK. So here's what I'm thinking, and tell me if I'm wrong—"

And he was off. Warm, fast, unbeatable.

That Tuesday was a *commercial* first meeting. That if Alex walked in and opened a demo they would read Velum as a consultancy and anchor on a services price instead of a platform price. That the demo was "genuinely the round-two trump card, we do not want to burn it in the room where they're deciding whether we're serious people." That Alex should absolutely present it — "you, not me, it's yours" — at the second meeting, once the commercial frame was set. And that in the meantime he would be with his mum and dad, "which, mate, you *never* do, I'm not letting you sack that off for a first-meeting handshake I can do in my sleep."

"But it's—" said Alex.

And he heard it go.

In real time. On the phone. Standing in room 914 with the extractor going.

The volume coming out of his own voice. And the sentence he had built on the stairs — *it's not a services deal and it never was, the recon fix is the platform, the compliance thing is the mannequin, you're selling the wrong thing and it has my name on it* — arriving in his mouth as

nothing.

Not blocked. Not swallowed. Not there. And there was no way to say that, because saying it would have needed

"—yeah," he said. "No, you're right. Round two."

"You're a legend. Enjoy your folks. We'll do this properly next week, with you driving." A grin down the line. "And Alex — genuinely. Fourteen. You're a machine."

"Yeah," said Alex. "Thanks."

He put the phone down.

---

He sat on the end of the bed.

The extractor ran. It had four minutes on it and then it would stop and the room would get bigger.

He waited for it the way he waited for the other thing, sideways and complete and ninety seconds after you stop hunting.

The extractor stopped.

Nothing arrived.

---

His phone went. His mother.

*We are at the front. Papa says the garden centre closes at 5. It is 4. He says we go now or we don't go.*

Alex looked at it for a moment.

*coming*, he typed.

He went down in the lift and across the lobby past the fireplace with no fire in it, and out through both sets of doors into the car park, where his father was standing beside a taxi with the door already open, holding it, in the sun, waiting.

"Everything all right at the work?" said Marek.

"Yeah," said Alex. "Nothing important."
