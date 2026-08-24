# 2. Football

The Overground had a note and the note was the traction motor, and it fell a fourth when the train came off the power and floated into Hoxton, and rose again, and Alex Wójcik had ridden it two years and could have sung the whole line.

He always took the third door. Not for a reason he would have defended.

Then the escalator at Old Street, which had been running with a fault in it since February, a small dry tick once a revolution that nobody but him appeared to hear, and which he had reported twice, in writing, politely, and which was still there and which he had come to think of as his.

Forty desks. A wall with VELUM on it in letters two metres high and, underneath, smaller, in a different hand, *ship it.*

Under all of it the air handling, a long slow animal breathing somewhere above the ceiling tiles. You stopped hearing it around nine and heard it again around eight.

Tuesday.

---

The demo for Arcus was at the end of the morning and the agent fell over in it.

Not badly. It fell over the way a thing falls over when it has been asked to do something in front of people, which is to say completely and at the third minute. On the shared screen a green pane went white and stayed white and a number in the corner stopped moving.

Six squares on the call. Somebody said, "Are we seeing this," and somebody else said, "We're seeing it," and Ben Farrow said, without any change in his voice at all, "This is actually useful, because it lets me talk about the failure model, which is the thing I always want to get to anyway—" and he was away, warm, unhurried, an entire building of confidence with nobody in it panicking.

Alex had already stopped listening. He had a second machine open and his shoes were off under the table.

It was their box, not his agent. Their box had come up with two sources of time on it and the second one had come up wrong, and everything downstream was doing exactly what it had been told to do by a clock that was, in the mildest possible sense, lying. He found it in about ninety seconds. He had seen its cousin nine months ago on a customer in Rotterdam and it had cost four days then.

He typed for forty seconds. The white pane filled in. The number in the corner started moving.

"Oh, nice," said the woman whose title nobody had given. "What was that?"

"It's a clock thing," said Alex. "Their box has got two clocks and neither of them is lying, they just don't agree, and we were believing the wrong one at the join."

"Right," she said. "Right, right."

He heard the size of the pause after it. He could feel the sentence he had just produced lying on the table in front of everybody like something that had been brought in from outside.

He did the thing he could not stop doing, which was to help.

"It's fine. It's not us. It'll do it on any host with an unsteered TSC. You just pin the read to the monotonic source and it goes away for ever."

Nobody asked. In one of the squares a man looked down and to the left, the way you do when you are working out whether a thing that has been said is beneath you or above you and you would like to know before you speak.

"So what Alex is describing," said Ben, "is exactly why we run below the runtime rather than inside it. Let me show you what that means when it's your fleet and not our laptop."

The call ran another forty minutes and did not go back.

---

Afterwards Ben walked backwards for a few steps in the corridor to say it properly, because Ben said things properly.

"That was the best thing that could have happened. Genuinely. They saw it break and they saw us not care."

"It was their clock."

"They saw us *not care*, mate." He was already looking at his phone. "You were great."

By the evening the story had a shape. It went into the company as the demo where the thing died and Ben talked for a minute and it came back from the dead on its own. Alex heard a version of it from someone in the kitchen who had not been on the call, and the version had no hands in it, and he stood there with a glass of water and let it finish, and said, "Yeah," and went back to his desk.

Both versions were true. Ben's was more useful.

---

The deciding meeting was Thursday, and Alex was right, and lost.

Build the multi-tenant control plane now — six weeks, two engineers, the thing that would let them sell to companies with more than one subsidiary. Or the compliance reporting module, which took two weeks, looked spectacular in a demo, and was, in his private and precise judgement, a mannequin.

He had prepared. That was the part he came back to at two in the morning. This time, for once, he had actually fought.

Four numbered points and a diagram, written out the night before in the small square handwriting he had had since he was fourteen. He made all four. He got the whole argument into the room, out loud, in order, which for him was close to a personal record. The control plane wasn't a feature, it was the shape of the thing. The report was two weeks of work that would sell to companies they physically could not then serve. Every customer it won would arrive in Q4 with subsidiaries and a wall.

"Can I just—" said Saul, twice, and both times Alex said "hang on, one more," and kept going, and the second time his voice did something he had not heard from it before, which was to get slightly louder rather than quieter.

He finished. There was a pause. He could feel that he had landed it.

"That's completely right," said Ben.

And then Ben talked for four minutes about timing.

It was good. It was good, and none of it contradicted anything Alex had said, and that was the trouble. It accepted the whole argument and set it gently to one side, the way a chair is moved. Q4 was a risk they'd be lucky to have. February was a certainty. A platform is what you call an engine after somebody has paid for it.

By the end the room's centre of gravity had gone. No vote. And when Ben said, "Alex, you're the one who has to build it — what do you think?" the honest answer was *I think you've just spent four minutes making it impossible for me to think.*

What he said was:

"I mean. We can do the compliance thing quickly."

"That's what I thought too," said Ben warmly.

It was minuted as *compliance module, 2 sprints, Alex to scope.* A minute later Ben went past and put a hand on his shoulder and said, "Good meeting."

---

Toby was twenty-three and four months in and had broken the ingest queue at nine at night, and had stayed to fix it, which was the only reason Alex knew his name.

They sat on the fire escape because the extractor over the kitchen ran all night and it was the one place in the building where you could hear yourself think, and the extractor was audible out there too, one floor down and to the left, a steady grey hum with a rattle in it every few seconds where something had come loose in the housing.

"I don't understand why it's slower with more of them," Toby said. "That's the bit. It should be four times faster. It's four times less work each."

And Alex, who had not spoken more than nine consecutive words to another human being since Thursday, put his cup down.

"Right. First thing to get out of your head is that memory is fast."

"It isn't?"

"It hasn't been since about the year you were born."

And then it came, the way it did about four times a year, unasked and from underneath and at the wrong hour of the night, and he was talking, and after a while he was not exactly talking to Toby any more. Memory is four hundred cycles away and everything you think of as a computer is an elaborate lie built to hide that fact from you, and the lie is a stack of little bins of borrowed lines, each of which believes it owns what it is holding, so when four workers go at the same structure they are not sharing it, they are fighting over it, and every time one of them writes a single byte the other three have to throw away the line it lived on and go and fetch it again, four hundred cycles, four hundred, and they do this to one another tens of thousands of times a second, politely, in strict rotation, and the profile shows you nothing at all because not one of them is doing anything wrong. Four men in a corridor passing a bucket back and forth all afternoon and calling it a fire brigade. The cure is not a lock and it is not a queue. The cure is to give each of them their own bucket, their own line, their own bin, so that they are never once obliged to agree about anything until the end, and at the end you add up four numbers, which is free, and that is the whole trick, that is the entire trick, and it is not even a clever one, it is a thing about the shape of the machine that nobody tells you and that you will then see in everything for about a year, in queues and in kitchens and in the way a road merges, and it will make you extremely annoying to be near.

Toby was quiet for a second.

"So padding," he said. "That's what the padding is."

"That's what the padding is."

"Why doesn't the — hang on. Why doesn't the compiler just—"

"Because it can't know," said Alex, and he was up now, standing, drawing on nothing with two fingers, and the answer to that ran another eleven minutes and took in the allocator, and a thing about page colouring that he had learned from a paper written before either of them was born, and a story about a Dutch bank whose whole trading floor had once been made forty per cent slower by a single well-meant field added to a structure by a man on his second week, and neither of them noticed the time going, and the extractor rattled below them the entire while.

At the end of it Toby said, "That's mental," and went back in to try it, and Alex sat on the fire escape on his own with the extractor rattling below him, which was the happiest he had been all week and possibly since March.

---

The estate behind Roman Road had a strip of grass between two blocks that everybody called the pitch. From four o'clock every afternoon of his childhood it had fourteen or nineteen boys on it and the noise came up through the window of the flat like something boiling.

"Alek. Go out."

"I'm doing something."

"You're always doing something. Go out and do something with legs."

The something was a Compaq Presario his father had brought home in the boot of a Vauxhall from a print works that was throwing out four of them. Three worked. The fourth did not, and Marek Wójcik, who could rewire a flat and rebuild a gearbox and could not spell the word *rebuild*, put the broken one on the kitchen table in front of his eight-year-old son and said, in Polish:

"This one's yours. It doesn't work."

It took eleven weeks. It had a fan in it that ran at a pitch he could still produce on request, and for eleven weeks he took the machine apart in the evenings while the pitch went up and down through the wall of the flat and his mother said the electricity was not free.

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

The following Tuesday, a design session about how the agent would carry state across a restart, and he had done the thing he never did, which was to rehearse.

He rehearsed it on the train with the traction motor under him, four stops, the whole argument compressed into two sentences and then one. *You don't keep the state. You keep the inputs and run them again.* He got it down to eleven words on the Overground and it was still eleven words when he walked in.

He said it well to begin with.

"You don't keep the state at all. You keep the *inputs*, in order, and run them again on restart, and then there's nothing to corrupt, because there's no state left to be wrong — there's just the log and a function. It's slower to start and it can never lie to you. That's the trade, and it's the right way round for us, because the thing that kills us in the field is state that's quietly wrong six weeks later."

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

Eleven words on the train. He had them in the room and he had the room and he put them down.

---

He stayed that night, the way he did two or three nights a week. Far lights off, one lamp. After midnight the building dropped its note a tone and a half and got quieter, and by then he had padded the counters and gone through Toby's branch line by line and left three comments on it, all of them nouns.

The notebook took nouns. That was not a rule he had made, it was a rule he had noticed, going back through the four of them. *Teardown, refcount, ordering.* *Quiesce.* *Arena, then bump, then never free.* Names of things. In three years there were two sentences in it.

He got the notebook out and sat with the pen a long time and wrote the third.

*I was right today and it didn't matter, and I need to work out whether that's because I was wrong.*

---

They rang that evening, both at once, from different distances, the way they did.

"Alek! We booked it. The flights. Marek said don't tell him until it's booked, so — it's booked. The fourteenth."

"The fourteenth of this month?"

"Two weeks!" His mother's voice went up. "We come Saturday morning, we stay at the hotel by you — no, not by you, we found one, Marek found one, it's cheap—"

"Send me the link."

She sent the link. He looked at it standing on Old Street with a finger in one ear and the escalator ticking behind him once a revolution.

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

Alex looked around him. Traffic going past. The office behind him with forty desks in it and the wall with VELUM on it. Thirty-one million dollars of other people's money and a decision taken past him with a hand on his shoulder.

"It's great," he said. "It's going really well."

There was a pause on the line of exactly the length that meant his father had heard him.

"Good," said Marek Wójcik. "That's good."
