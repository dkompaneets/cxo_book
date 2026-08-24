# 2. Football

The office had a sound and the sound was the air handling.

You stopped hearing it at about nine in the morning and heard it again at about eight at night, and in between it was under everything, a long slow animal breathing somewhere above the ceiling tiles, and Alex Wójcik had worked to it for two years and could have hummed it.

Forty desks. A wall with VELUM on it in letters two metres high and, underneath, smaller, in a different hand, *ship it.*

He had moved desk twice in two years. The first time was people. The second time was a laptop charger two seats down with a coil in it that sat a semitone under the building, so that the two of them went in and out of phase about every nine seconds, and he had lasted eleven days and then picked up his monitor and moved. He had explained why, once, because he was asked. It had gone into the company as a funny thing about Alex.

He worked with his shoes off. Nobody had ever mentioned it.

Tuesday.

---

Velum's product was one idea worn very thin. You could watch what a program actually did at the moment it did it, instead of reading its intentions off a manifest beforehand. Four thousand lines of C was where the idea touched metal, and he had written most of them in eleven days, two years ago, in a state he had never been able to get back to. Thirty-one million dollars of other people's money sat on top of those four thousand lines like a cathedral on a canoe.

There was a fault in it. He had known for five months, in the way of a tooth that is going to need work.

Then he found it, three files from where he had been looking, in the part of the thing that gives back what it borrowed, and it was so simple and so stupid and so *his* that he made a noise out loud and the woman at the next desk took one earphone out and looked at him.

"It's two counters on the same cache line," he said. "They're not sharing anything. They just live next door."

"Nice," she said, and put the earphone back.

And then the room went.

---

He drew it, because he could not think about it until it had a shape on paper. Two long horizontal lines, one for each thread, and the little vertical strokes where they touched, and between two of the strokes a gap, and the gap was about four microseconds wide and had been sitting inside every deployment they had since the spring.

Nothing in it was wrong. That was the beautiful part, that was the part he would still be turning over at midnight. Every piece was doing exactly the thing it had been asked to do, and it had been asked by him, and he could remember asking.

He could close the gap three ways and two of them were ugly. Take the lock earlier, which cost him an acquisition on a hot path forty thousand times a second and which he was not going to do. Or refuse the flush while the count was falling, which threw away the last two seconds of every trace, which was the thing the flush had been added to stop, so that was a circle, so that was nothing.

Or.

Or — and this was the one, this was the one that arrived sideways about ninety seconds after he stopped hunting for it, the way they did, the way they always did, sideways and from underneath and never once when he was looking straight at the place they came from — do not have a lock at all. Take the whole idea of holding out of it. Let the two of them race, publish the count where both can see it, and make losing the race *mean* something instead of being a disaster, because if you lost you were late, and if you were late the thing you were going to write into is already gone, and something already gone does not need writing into. The bug becomes the answer. You stop asking two threads to agree about who is holding the object and you let one of them find out it has been overtaken, and the finding-out costs nothing, and it is one word, and the word is already there.

He wrote it. He rewrote it, because the first version had the read on the wrong side. Then he drew the two lines again with the new shape on them and went looking for the gap and could not build one, tried for a long time to build one, tried in the delighted patient way of a man shaking a locked door he is fairly sure he has just welded shut, and could not, and that was the best part of the seventy minutes.

For seventy minutes the world was a screen and his hands.

The conversations he should have had. The one he had had badly. The thing Ben said in December. The burn rate. His own voice at the last all-hands, tinny and apologetic and not his. All of it went, and stayed gone, for seventy minutes.

There was only the problem.

---

At the end of the seventy minutes Ben Farrow appeared beside him with his laptop already open, which was how Ben appeared.

"Mate. Arcus moved the call up. Twenty minutes."

Alex did not look away from the screen. "I'm in the middle of—"

"I know. I know you are. Twenty minutes, and then I will physically guard you for the rest of the day. I'll sit here with a stick." Ben smiled. Ben's smile was not a weapon, which was the difficulty. If it had been a weapon Alex could have named it. "They want to see the agent do the thing. You're the only one who can drive it without it falling over."

"Saul can drive it."

"Saul can drive it into a wall."

So he saved the work. He wrote three words in the notebook — *teardown, refcount, ordering* — and closed it, and found his shoes, and went into the room called Riga.

The air handling was in there too. He noticed that.

The seventy minutes were over.

---

The call ran fifty-five minutes. Alex spoke for four of them.

Arcus had six people on it and five of them talked. There was a slide with three arrows on it and a fourth arrow that had been added later by somebody else in a slightly different grey. Their VP of Engineering said that the fundamental tension in the category was between coverage and overhead, and that they had been living inside that tension for eighteen months, and that in fairness every vendor in the space was living inside it too, and that the real question — and he wanted to be direct about this, because he thought directness saved everybody time — was not whether you had the tension but whether you were honest with the customer about where you had chosen to sit on it, which was a maturity conversation more than a technology conversation. A woman whose title nobody had given described the problem from the point of view of the customer. Then a man described it from the point of view of the board. Then the woman came back and described it from the point of view of the customer again, briefly, and apologised for repeating herself, and nobody minded.

Alex had it in about ninety seconds. He waited, because Ben's hand had gone flat on the table in the way that meant let them finish.

He said: "It's not sampling. It's every call."

He said: "No. Because we're below the runtime."

Then the VP sat back and put both hands up.

"So that's the wall. Everyone hits the wall. Right? I mean — what do you even do with that."

"Just use multithreading," said Alex.

Six squares on a screen and nothing coming out of any of them. Somebody's microphone picked up a chair. In one of the squares a man looked down and to the left, the way you do when you are working out whether a thing that has been said is beneath you or above you and you would like to know before you speak.

Nobody asked.

He heard the size of the pause and did the thing he could not stop doing, which was to help.

"You do the enrichment off the write path and take the ordering hit at the sink instead of the source. Same total work. It just isn't in the way any more."

"Sure," said the VP. "Sure, sure."

"Which is a great bridge, actually," said Ben, "into where we've got to on the roadmap, because the thing Alex is describing is landing in the platform in Q1 and I want to show you the shape of it—"

The call ran another thirty-one minutes and did not go back.

Forty minutes in, Alex said, "Yes, that's right," to something that was not quite right, because correcting it would have taken ninety seconds and Ben had said the sentence before it.

Ben spoke for the other fifty-one minutes and was extraordinary. He made a company of forty people sound like a phenomenon. He told a story about a customer in Rotterdam that Alex had been in the room for, and in Ben's version it had a shape, and in Alex's memory it had been four days of horror and a fix at three in the morning.

Both were true. Ben's was more useful.

In the corridor afterwards Ben walked backwards for a few steps to say it properly. "That was great. You were great. The thread thing especially."

"Did they get it?"

"They loved it."

Alex turned that over and found that it was an answer to a different question.

"It's the simplest part of the whole system," he said. "It's two lines."

"I know," said Ben. "That's why it's great." And he was gone into the next thing, and he had meant every word, and both of those were true as well.

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

It was minuted as *compliance module, 2 sprints, Alex to scope.* A minute later Ben went past and put a hand on his shoulder and said, "Good meeting."

---

That night the building dropped its note the way it did after midnight, a tone and a half down and quieter, and Alex was alone in the office, the way he was two or three nights a week. Far lights off, one lamp.

He fixed the fault. It took four hours, because the seventy-minute state never came back on demand. He fixed it in the plodding way, by being stubborn at it, and nobody would ever know it had been broken.

The notebook took nouns. That was not a rule he had made, it was a rule he had noticed, going back through the four of them. *Teardown, refcount, ordering.* *Quiesce.* *Arena, then bump, then never free.* Names of things. In three years there were two sentences in it.

He got the notebook out and sat with the pen a long time and wrote the third.

*I was right today and it didn't matter, and I need to work out whether that's because I was wrong.*

---

The estate behind Roman Road had a strip of grass between two blocks that everybody called the pitch. From four o'clock every afternoon of his childhood it had fourteen or nineteen boys on it and the noise came up through the window of the flat like something boiling.

"Alek. Go out."

"I'm doing something."

"You're always doing something. Go out and do something with legs."

The something was a Compaq Presario his father had brought home in the boot of a Vauxhall from a print works that was throwing out four of them. Three worked. The fourth did not, and Marek Wójcik, who could rewire a flat and rebuild a gearbox and could not spell the word *rebuild*, put the broken one on the kitchen table in front of his eight-year-old son and said, in Polish:

"This one's yours. It doesn't work."

It took eleven weeks.

Somewhere in the eighth week he understood a thing he was never afterwards able to explain to anybody without their face going polite. The machine was not withholding anything. Everything it did, it did for a reason, and the reason was findable, and when you found it the reason was simply there, and did not change depending on how you had asked.

On the pitch he was the small one with the accent his parents had and he did not, picked eleventh out of fourteen. Once — properly, actually — he scored, and turned round into a silence in which a boy called Dean said, "Off Robbie's leg."

It went into the record as off Robbie's leg. No referee. No replay. No reason. A room deciding.

He went back inside. He went back inside on a great many afternoons, and his mother stood in the kitchen doorway with a tea towel and reported him to his father like a symptom.

"He's inside again."

And his father, not looking up, doing nights at the bakery on Bethnal Green Road and days at the print works, six years in and four to go:

"Leave him. He's building something."

Four words. It cost Marek Wójcik nothing to say and everything to be able to say.

---

The second time was smaller and worse.

The following Tuesday. Not the sale — the sale had been lost the week before in a proper meeting where he had at least fought. This was a design session about how the agent would carry state across a restart, and Alex had drawn the thing he had been turning over for a month.

He said it well to begin with.

"The trick is you don't keep the state at all. You keep the *inputs*, in order, and run them again on restart, and then there's nothing to corrupt, because there's no state to be wrong — there's just the log and a function. It's slower to start and it can never lie to you. That's the whole trade, and it's the right way round for us, because the thing that kills us in the field is state that's quietly wrong six weeks later."

That was good. He could feel it being good. The rare physical sensation of a sentence leaving his mouth in the shape it had held in his head.

"Right," said Ben, already up and moving to the board, which was how it started. He picked up the red pen and drew a box around what Alex had drawn. "So the way I'd frame this is — do we need it now, or is it a v2 thing? It's elegant, genuinely, but the customer never sees a restart, and we've got forty people and a runway that ends in February, and I don't want to gold-plate the engine while the thing that closes deals sits in a backlog."

The room settled. Alex watched it happen. Saul leaning back. Fenella turning her laptop round. A pen going down. The small physical agreement a group makes when it has decided.

He had one move left. He knew what it was, because he had made it before. *Ben, hang on, give me ninety seconds and nobody talk.* It worked. It cost him hours of the afterwards, lying awake replaying the faces of people who had watched him ask a grown man for silence in his own company.

"So—" he said.

Ben turned. Pen down. Open, and willing to wait however long it took. Every face came round.

It was the patience that did it.

"So the thing is that it isn't gold-plating, it's the difference between an engine that fails loud and one that fails quiet, and the quiet one is the one that—"

He heard the volume go out of his own voice in real time. The sentence trailing toward a word he had not chosen yet.

"—it's fine," he said. "Never mind. It's a v2 thing. You're right."

"You sure?"

"Yeah."

"Good man," said Ben, and clapped him lightly on the arm, and the meeting ended eleven minutes early, which everybody was pleased about.

He sat at his desk afterwards, not working, turning the notebook over in his hands without opening it.

He could talk for forty minutes about memory ordering to a room full of strangers in Seattle. There was a video. Two thousand people had watched it and some had written to say it changed how they thought about their scheduler.

In Seattle they were deciding about the scheduler.

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

"Good," said Marek. "Because your mother has bought a coat for this." A pause. "What did you do today."

"I took a lock out."

"Good," said his father, who had no idea what that was, and meant it, and then, flat and clear, the way it always was: "How is the work."

Alex looked around him. Traffic going past. The office behind him with forty desks in it and the wall with VELUM on it. Thirty-one million dollars of other people's money and four thousand lines of C and a decision taken past him with a hand on his shoulder.

"It's great," he said. "It's going really well."

There was a pause on the line of exactly the length that meant his father had heard him.

"Good," said Marek Wójcik. "That's good."
