# 2. Football

The office had a sound and the sound was the air handling.

You stopped hearing it at about nine in the morning and heard it again at about eight at night, and in between it was under everything, a long slow animal breathing somewhere above the ceiling tiles, and Alex Wójcik had worked to it for two years and could have hummed it.

Forty desks. A wall with VELUM on it in letters two metres high and, underneath, smaller, in a different hand, *ship it.*

Tuesday. Ten forty.

---

Velum's product was one idea worn very thin. You could watch what a program actually did at the moment it did it, instead of reading its intentions off a manifest beforehand. The interceptor was where the idea touched metal. Four thousand lines of C.

He had written most of it in eleven days, two years ago, in a state he had never been able to get back to. Thirty-one million dollars of other people's money sat on top of those four thousand lines like a cathedral on a canoe.

There was a race condition in it. He had known for five months, in the way of a tooth that is going to need work.

At ten forty he found it.

It was not where he had been looking. It was three files away, in the teardown path, and it was so simple and so stupid and so *his* that he made a noise out loud and the woman at the next desk took one earphone out and looked at him and he said sorry and she put it back.

And then the room went.

---

Because the thing about the teardown path is that it doesn't own anything, it only borrows, and the whole design had been built on that — borrow, use, hand back, and the refcount is the receipt — except that the handing back happens on a different thread from the borrowing, which was fine, which had always been fine, because the ordering was guaranteed by the quiesce, and the quiesce was guaranteed by the barrier, and the barrier was where he had stopped looking two years ago because the barrier was correct.

The barrier *was* correct. That was the beautiful part. Nothing here was wrong. Every single piece of it was doing exactly the thing it had been asked to do, and it had been asked by him, and he could still remember asking.

What had happened was that a fourth thing had been added in March, a small thing, forty lines, to flush the audit buffer on shutdown so you didn't lose the last two seconds of a trace, and it took the same lock, and it took it *after* the barrier, and for eighteen months out of every million teardowns nothing happened at all, and then a machine somewhere ran hot and the scheduler made a different choice and the flush arrived while the refcount was still one, and the object went, and the pointer stayed, and the next thing that touched it read whatever had moved in.

He drew it. Two lines on paper, thread A and thread B, and the little vertical strokes where they touched, and the gap. The gap was about four microseconds wide and had been sitting in production since the spring inside every deployment they had.

He could close it three ways.

Take the lock earlier, which worked, and cost a lock acquisition on a hot path forty thousand times a second, and he was not going to do that.

Or refuse the flush if the count was already falling, which worked, and quietly threw away the last two seconds of the trace, which was the thing the forty lines had been added to stop, so that was a circle.

Or — and this was the one, this was the one that arrived sideways the way they did, about ninety seconds after he stopped hunting for it — do not take the lock at all. Do not have a lock. Publish the count and let the flush read it and lose the race honestly, and make losing the race *mean* something: if you lose, you were late, and if you were late the buffer is already gone, and a buffer that is already gone does not need flushing. The bug becomes the answer. You stop asking the two threads to agree about who is holding the object and you let one of them find out it has been overtaken, and the finding-out is free, and it is one word, and the word is already there.

He wrote it out. He rewrote it out because the first version had the read on the wrong side. He drew the two lines again with the new shape and looked for the gap and there was no gap, there was no possible interleaving with a gap in it, he tried to build one for a long time and could not, and that was the best part of the whole seventy minutes.

For seventy minutes the world consisted of a screen and his hands. His mind, which normally ran like a fairground — the conversations he should have had, one he had had badly, the thing Ben said in December, the burn rate, his own voice at the last all-hands, tinny and apologetic and not his — went gloriously silent.

There was only the problem.

The problem did not care who he was. The problem had never once looked at him and waited for him to finish a sentence.

---

At eleven fifty-two Ben Farrow appeared beside him with his laptop already open, which was how Ben appeared.

"Mate. Arcus moved the call up. Twenty minutes."

Alex did not look away from the screen. "I'm in the middle of—"

"I know. I know you are. Twenty minutes, and then I will physically guard you for the rest of the day. I'll sit here with a stick." Ben smiled. Ben's smile was not a weapon, which was the difficulty. If it had been a weapon Alex could have named it. "They want to see the agent do the thing. You're the only one who can drive it without it falling over."

"Saul can drive it."

"Saul can drive it into a wall."

So he saved the work. He wrote three words in the notebook — *teardown, refcount, ordering* — and closed it, and went into the room called Riga.

The air handling was in there too. He noticed that.

The seventy minutes were over.

---

The call ran fifty-five minutes. Alex spoke for four of them.

He said: "It's not sampling, it's every call."

He said: "No. Because we're below the runtime."

He said, when the Arcus VP of Engineering asked what happened under memory pressure: "It degrades to sampling, and it tells you it has."

And at twelve forty-four he said, "Yes, that's right," to something that was not quite right, because correcting it would have taken ninety seconds and Ben had said the sentence before it.

Ben spoke for the other fifty-one minutes and was, Alex thought without any bitterness at all, extraordinary. He made a company of forty people sound like a phenomenon. He told a story about a customer in Rotterdam that Alex had been in the room for, and in Ben's version it had a shape, and in Alex's memory it had been four days of horror and a fix at three in the morning.

Both were true. Ben's was more useful.

---

The deciding meeting was Thursday, and Alex was right, and lost.

Build the multi-tenant control plane now — six weeks, two engineers, the thing that would let them sell to companies with more than one subsidiary. Or the compliance reporting module, which took two weeks, looked spectacular in a demo, and was, in his private and precise judgement, a mannequin.

He had prepared. That was the part he came back to at two in the morning. This time, for once, he had actually fought.

He had written it out the night before in the small square handwriting he had had since he was fourteen. Four numbered points and a diagram. He made all four. He got the whole argument into the room, out loud, in order, which for him was close to a personal record. The control plane wasn't a feature, it was the shape of the thing. The report was two weeks of work that would sell to companies they physically could not then serve. Every customer it won would arrive in Q4 with subsidiaries and a wall.

"Can I just—" said Saul, twice, and both times Alex said "hang on, one more," and kept going, and the second time his voice did something he had not heard from it before, which was to get slightly louder rather than quieter.

He finished. There was a pause. He could feel that he had landed it. For a moment he thought he had won.

"That's completely right," said Ben.

And then Ben talked for four minutes about timing.

It was good. It was good, and none of it contradicted anything Alex had said, and that was the trouble. It accepted the whole argument and set it gently to one side, the way a chair is moved. Q4 was a risk they'd be lucky to have. February was a certainty. A platform is what you call an engine after somebody has paid for it.

By the end the room's centre of gravity had gone. No vote. And when Ben said, "Alex, you're the one who has to build it — what do you think?" the honest answer was *I think you've just spent four minutes making it impossible for me to think.*

What he said was:

"I mean. We can do the compliance thing quickly."

"That's what I thought too," said Ben warmly.

At four fifty it was minuted as *compliance module, 2 sprints, Alex to scope.* At four fifty-one Ben went past and put a hand on his shoulder and said, "Good meeting."

---

Two oh seven that morning. Alone in the office, the way he was two or three nights a week. Far lights off, one lamp. The building breathing.

He had fixed the race condition. It took four hours, because the seventy-minute state never came back on demand. He fixed it in the plodding way, by being stubborn at it, and nobody would ever know it had been broken, and that was correct, that was the job.

He got the notebook out and sat with the pen a long time and wrote:

*I was right today and it didn't matter, and I need to work out whether that's because I was wrong.*

---

The estate behind Roman Road had a strip of grass between two blocks that everybody called the pitch. From four o'clock every afternoon of his childhood it had fourteen or nineteen boys on it and the noise came up through the window of the flat like something boiling.

"Alek. Go out."

"I'm doing something."

"You're always doing something. Go out and do something with legs."

The something was a Compaq Presario his father had brought home in the boot of a Vauxhall from a print works that was throwing out four of them. Three worked. The fourth did not, and Marek Wójcik, who could rewire a flat and rebuild a gearbox and could not spell the word *rebuild*, put the broken one on the kitchen table in front of his eight-year-old son and said, in Polish:

"This one's yours. It doesn't work."

It took eleven weeks.

Somewhere in the eighth week he understood a thing he was never afterwards able to explain to anybody without their face going polite. The machine was not withholding anything. It had no opinion about him. It was not deciding whether he was clever enough to be told. Everything it did, it did for a reason, and the reason was findable, and when you found it the reason was simply there, and did not change depending on how you had asked.

People were not like that.

People decided what you were within four seconds and then heard everything you said through it. On the pitch he was the small one with the accent his parents had and he did not, picked eleventh out of fourteen. Once — properly, actually — he scored, and turned round into a silence in which a boy called Dean said, "Off Robbie's leg."

It went into the record as off Robbie's leg. No referee. No replay. No reason. A room deciding.

He went back inside. He went back inside on a great many afternoons, and his mother stood in the kitchen doorway with a tea towel and reported him to his father like a symptom.

"He's inside again."

And his father, not looking up, doing nights at the bakery on Bethnal Green Road and days at the print works, six years in and four to go:

"Leave him. He's building something."

Four words. It cost Marek Wójcik nothing to say and everything to be able to say.

---

The second time was smaller and worse.

Following Tuesday. Not the sale — the sale had been lost the week before in a proper meeting where he had at least fought. This was a design session about how the agent would carry state across a restart, and Alex had drawn the thing he had been turning over for a month.

He said it well to begin with.

"The trick is you don't persist the state at all. You persist the *inputs*, in order, and replay them on restart, and then there's nothing to corrupt, because there's no state to be wrong — there's just the log and a function. It's slower to start and it can never lie to you, and for us that's the whole trade, because the thing that kills us in the field is state that's silently wrong."

That was good. He could feel it being good. The rare physical sensation of a sentence leaving his mouth in the shape it had held in his head.

"Right," said Ben, already up and moving to the board, which was how it started. He picked up the red pen and drew a box around what Alex had drawn. "So the way I'd frame this is — do we need it now, or is it a v2 thing? It's elegant, genuinely, but the customer never sees a restart, and we've got forty people and a runway that ends in February, and I don't want to gold-plate the engine while the thing that closes deals sits in a backlog."

The room settled. Alex watched it happen. Saul leaning back. Fenella turning her laptop round. A pen going down. The small physical agreement a group makes when it has decided.

He had one move left. He knew what it was, because he had made it before. *Ben, hang on, give me ninety seconds and nobody talk.* It worked. It cost him hours of the afterwards, lying awake replaying the faces of people who had watched him ask a grown man for silence in his own company.

"So—" he said.

Ben turned. Pen down. Entirely open. Entirely willing to wait however long it took. Every face came round.

It was the patience that did it.

"So the thing is that it isn't gold-plating, it's the difference between an engine that fails loud and one that fails quiet, and the quiet one is the one that—"

He heard the volume go out of his own voice in real time. The sentence trailing toward a word he had not chosen yet.

"—it's fine," he said. "Never mind. It's a v2 thing. You're right."

"You sure?"

"Yeah."

"Good man," said Ben, and clapped him lightly on the arm, and the meeting ended eleven minutes early, which everybody was pleased about.

He sat at his desk afterwards, not working, turning the notebook over in his hands without opening it.

He could talk for forty minutes about memory ordering to a room full of strangers in Seattle. There was a video. Two thousand people had watched it and some had written to say it changed how they thought about their scheduler.

The difference was that in Seattle nobody in the room was deciding anything about *him*. They were deciding about the scheduler.

The moment a room turned to decide about Alex, the machinery went off. And what went off with it was not his courage. It was the words. Actual access to actual vocabulary, gone, like a hand going numb.

---

They rang that evening, both at once, from different distances, the way they did.

"Alek! We booked it. The flights. Marek said don't tell him until it's booked, so — it's booked. The fourteenth."

"The fourteenth of this month?"

"Two weeks!" His mother's voice went up. "We come Saturday morning, we stay at the hotel by you — no, not by you, we found one, Marek found one, it's cheap—"

"Send me the link."

She sent the link. He looked at it standing on Old Street with a finger in one ear.

"Mama. That's Birmingham, Alabama."

"What?"

"It's in America. The one you've booked is in America."

A long pause. Then, distantly, his mother saying to his father, in Polish, "He says it's in America," and his father saying something back, and his mother returning: "Papa says how can it be in America if it's twenty-nine pounds."

"Don't book anything. I'll book you into the one where the thing is."

"No, no, no. Too expensive."

"Mama." He was already on the site. "There's an offer."

So he booked The Ardenne and lied about the price, and his mother said, "Twenty-nine pounds?" and Alex said, "There was an offer," and his mother said, "You see, Marek! An offer!"

Then his father, close to the phone now, four words at a time.

"You will have time. For us. That weekend. You are not too busy."

"I'm not too busy."

"Because if you are busy, we come anyway, we sit in the hotel. It's fine."

"Papa. I'm not too busy."

"Good," said Marek. "Because your mother has bought a coat for this." A pause. Then, flat and clear, the way it always was: "How is the work."

Alex looked around him. Traffic going past. The office behind him with forty desks in it and the wall with VELUM on it. Thirty-one million dollars of other people's money and four thousand lines of C and a decision taken past him with a hand on his shoulder.

"It's great," he said. "It's going really well."

There was a pause on the line of exactly the length that meant his father had heard him.

"Good," said Marek Wójcik. "That's good."
