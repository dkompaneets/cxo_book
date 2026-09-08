# 9. Nineteen Moves

The atrium ran a different note from the ninth floor.

Bigger space, slower air, the plant somewhere behind the lift core sitting about a tone under what it did in the rooms. He had found it on Wednesday and had been quietly pleased about it since.

Twenty past eleven. The congress had finished for the night and the atrium had gone back to being an atrium. Four boards still out at the far end, where a handful of people were playing blitz for nothing.

Alex had come down because the wifi on the ninth floor had lost a build at ninety per cent and he had needed to put twenty metres between himself and a laptop.

He walked the length of it twice.

He got a coffee out of a machine that produced a substance. The machine had a fan in it that ran on for about forty seconds after the cup was gone, and then stopped, and the room got bigger.

Then he stopped at the boards.

One man at the end table with a position set up and nobody opposite him, moving pieces with one hand and writing on a sheet with the other. Fortyish. Reading glasses. A tournament badge on a fern-adjacent lanyard that was, on inspection, a fourth colour altogether.

Alex watched him for a minute.

He had played between nine and fifteen, in the way a certain sort of boy does. School club. A couple of county things. One weekend in Hastings where he came eleventh. He stopped when he found compilers. He still played online at three in the morning sometimes, fast and badly, in a way he would not have described to anybody as playing chess.

He was, in his own estimation, decent.

"Are you allowed to play people," he said, "or is it all official?"

The man looked up.

"It's a hotel," he said. "You're allowed to do anything."

"Do you want a game?"

There was the smallest pause.

"All right," said Nik.

---

It took nineteen moves.

He could reconstruct the first eight afterwards and never got much further. He played e5, which he had always played. He developed his knights, which is correct. On move six he pushed a pawn to gain a tempo, and it felt strong.

On move nine he was fine.

He was still, at move nine, telling himself a story in which he was fine, and in which the man opposite was a hobbyist in a hotel with a badge on a lanyard, and in which Alex Wójcik, who reasoned about lock-free data structures for a living, was about to have quite an enjoyable half hour.

On move twelve his position stopped having any moves in it.

That was the sensation, and it was not losing. Losing he knew. He looked at the board and there were, in the technical sense, about thirty legal moves available, and every one of them was worse than the last one, and there had not been a plan since roughly move seven, and the man opposite had not done anything he could point at.

"Sorry," he said. "What happened?"

"On move six," said Nik, "you took a pawn's worth of space, and after that all your pieces had to go behind it."

"Right."

"It's a very common thing."

On move seventeen Nik put a knight on a square from which it attacked nothing at all, and Alex looked at it for two minutes, and then understood that it attacked nothing at all *yet*, and made a small involuntary noise.

He resigned on nineteen.

"That was—" He rubbed his face. "That was actually humiliating. Thank you."

"You play quickly," said Nik. "You're not bad. You just play like it's a race."

"It's the internet's fault."

"It's always the internet's fault." Nik was already resetting, pieces going back with the fast economical hand of a man who has done it forty thousand times. "Again?"

"Can we do one where I last past move nine?"

"We can try."

---

The second game took an hour and a half and neither of them was really playing it.

There was somewhere to look. That was all it was. Two or three minutes would go by with nobody saying anything and the gaps did not have to be filled, because a hand was moving a bishop about, and the machine's fan cut in and ran its forty seconds and cut out.

Alex found out that the man was called Nik, that he was a CFO, that he had two children, and that the younger one had been waking every night for eight months.

"Eight months," Alex said.

"Two hundred and forty nights. I did work it out. That was a mistake."

Then Nik said, moving the bishop and not looking up: "What is it you actually build?"

"You'll be bored."

"I've just spent two hours on move seventeen of a game I won. I have an infinite capacity for boredom."

So Alex started at the wrong end, because it was the only end he had.

"OK. So it sits underneath everything. Not in the app. Below the runtime."

And then it went.

Because the thing about below the runtime is that it is a road, and everything a program wants to do in the world has to come out onto that road and say what it is — open this file, talk to this address, start this child — and you are standing in the middle of it, and the whole game, the entire game, the only rule there is, is that you are not allowed to slow the traffic down — not by five per cent, not by two, because the day you cost a customer two per cent they measure you, and once they have measured you they turn you off, and a security product that is turned off is a slide. So you cannot take a lock. Not once, not anywhere, not for a microsecond, because the instant one core has to stop and wait on another core the road stops, and it stops hardest exactly when it is busiest, which is exactly the minute you are supposed to be worth having. So there is a ring for every core and the writer never waits: one atomic add on a counter, which gives him a slot that is his and nobody else's, and he fills the slot at his leisure, and then publishes it with a single store with a release fence on it — one instruction, a nanosecond and a half, the cheapest promise in computing — and that store says *everything I wrote before this line is now true for you as well.* And the reader on the other side comes round behind him at his own speed, acquiring, never blocking, never once tapping anyone on the shoulder, and if the reader is slow the ring fills and the writer does not wait then either, he drops, and counts the drop, because a dropped event you know about is data and a stalled machine is a phone call at four in the morning. And underneath the whole arrangement is one number, a monotonic sequence, which is the only thing in the entire system that everybody agrees about, and every question you will ever be asked — did this process open that socket before or after it was reparented, was the binary swapped under it, is this the same file it was two seconds ago — comes down in the end to two of those numbers and which one is bigger.

Both hands were doing it by then, drawing the ring in the air at about the size of a dinner plate and going round it the way the reader goes round it, anticlockwise, which is wrong, and which he did every time.

"—and the beautiful part, the genuinely beautiful part, is that there's no clock in it anywhere. Clocks lie. Two cores in the same box don't agree what time it is, and they can't, and there is no fixing it, because it isn't a bug, it's the shape of the universe. But *order* is free. Order you get for nothing, because it already happened. So you can be wrong about when and still be right about what came after what, and what came after what is the entire product."

He stopped.

It came to him, somewhere around then, that he had been talking for four minutes.

He knew because he had heard it, the way you hear your own footsteps change coming out of a corridor into a hall. Nothing had come in over the top. The man opposite had a bishop between two fingers and had not put it down.

"Sorry," he said. "That's—"

"No," said Nik. "That was the best thing I've heard all week. Keep going."

Alex kept going for another two minutes and then ran out, honestly, the way a tape runs out.

And what he thought afterwards, walking it back, was not that Nik had been polite. Nik had not been polite. Nik had been moving a bishop about and thinking, and had had nothing he needed to say.

Then, moving the bishop, Nik said:

"How is it, having a co-founder?"

And Alex said, with no preparation at all: "He talks over me."

---

It got to about one in the morning. They had stopped pretending about the second game around midnight and the position sat between them like a table decoration.

"The thing that gets me," Alex said, "is that he's not — he's genuinely a good person. That's what makes it impossible. If he was a shark I could deal with a shark. Every single time, if you filmed it and showed it to a jury, he's done nothing. He asks what I think. He waits. Once, in March, he sat there for a full — I timed it — twenty-two seconds."

"And you didn't say it."

"I said about a third of it. In a voice." He looked at the board. "You know when you can hear yourself? From outside. My voice goes down while it's happening and I can't get hold of it. It's not that I'm scared of him. It's not fear. It's more like—"

He stopped.

"It's more like," he said again.

The plant went on behind the lift core.

"No," he said. "Sorry. I don't have it."

Nik put the bishop down.

"Yes," he said.

"You get that?"

"I got that for about five years," said Nik. "Different reason."

And then he said it.

"When I came here I had an accent that people had to work at. Not a bad one. But there'd be a — half a second, and they'd lean in, and say *sorry?* And the sentence would go into the room four seconds late and about ten per cent smaller than everyone else's. And that happened maybe forty times a week for five years." He turned a captured pawn over in his fingers. "So I did what you do. I stopped talking. Which cost me a promotion in 2005 to a man who was worse than me, and I knew exactly why, and it was the correct decision by the company, because he'd said four thousand things and I'd said sixty."

"So then what?"

"So then I found the other thing," said Nik.

He put the pawn down.

"I polish," he said.

Alex looked up.

"I don't lie. I want to be very clear, because I've thought about this a great deal and it matters to me. I have never put a false number in front of a board in my life. It's all in the pack. It's all true. But if there's a bad thing on page nineteen and a good thing on page four, I know exactly which one I'm putting on page four, and I know exactly what a room does when I say *healthy* instead of *adequate.* And I do it every single time.

"I did it eleven days ago. My chair asked me a direct question about a clawback that could take our runway from fourteen months to six, and I said I was *relaxed.*" He said the word with a delicacy that made it sound like something he had picked up off the floor. "And afterwards the chief executive rang me and said I make it feel like there's a floor under everything."

Two tables away a man put a set into a bag, and the pieces went in with the sound pieces make.

"Why?" said Alex.

"Because if I say the plain thing they might get it wrong."

"That's it. That's the whole of it, and it sounds insane out loud, which is presumably why I've never said it out loud." He looked at the board. "I have said, to a stranger, at one in the morning, in a hotel, a thing I have not said to my wife in fourteen years of marriage. I'd like it noted that I'm aware of how that looks."

"Noted," said Alex.

"Right."

"It's fine, though. I don't count. You'll never see me again."

"No," Nik agreed. "That's the entire mechanism."

---

At ten past one Alex said, "My parents get here Saturday."

"Where from?"

"London. They flew in from — no, they live in London, they've lived in London for thirty years. My dad came over in ninety-four." He turned his king over and stood it back up. "They booked a hotel in Alabama. Not on purpose."

Nik laughed, and it was a different laugh from the one he had been using all evening.

"You'll like him," said Alex. And then heard it, and added, "sorry, that's — I don't know why I said that."

"I might be here."

"Yeah." He stood up. He was bad at the end of things. There was always a beat where he did not know what the shape was. "Well — good luck. With the — with the guarding thing."

Nik looked up sharply.

"I didn't say a guarding thing."

"You said you defend positions that don't need defending. You said it about twenty minutes ago, about the game."

"Did I."

"Yeah."

"Ah," said Nik, and sat back, and did not say anything else.

The lift to the ninth floor ran with a hum in it at about the pitch of the atrium and a rattle at the door that arrived a beat after it stopped.

Room 914. The extractor going.

He got into bed with the laptop on his knees and did not open it. He lay there for a while.

Then he reached over to the chair, and got the jacket, and took the notebook out of the inside pocket, and held it on his chest without opening it, and fell asleep like that with the light on.
