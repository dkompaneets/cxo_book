# 12. The Whiteboard

The business centre at The Ardenne was a room off the first-floor landing with two desks, a printer that had been out of magenta since March, and a flip chart on an easel. Its window looked into the atrium. At half past twelve on the Friday night it contained one man, one laptop, and a level of quiet fury that would have frightened anybody who had only met him at a bar.

Michael was trying to open an attachment.

That was the whole of it. Fiona had sent the Group's revised delegation schedule at half past ten and had put *worth a look before Monday* on it, and the attachment would not open on the laptop, and the reason it would not open — as Michael had established over the previous twenty-five minutes — was that the bank's mobile device management had decided that The Ardenne's wifi was an untrusted network, and had therefore put the file into a container, and the container wanted him to authenticate, and the authentication wanted a code from an app, and the app wanted the internet, and the internet was the thing it did not trust.

He had rung the service desk at ten past twelve. A very pleasant young man in Bangalore had asked him to describe what he saw on the screen, and Michael had described it, and the young man had said, "And can you see the padlock, sir?" and Michael had said, "I can see four padlocks. This machine is a Victorian jail."

Then he had said something else that he regretted immediately, and had apologised for it, and the young man had been extremely gracious, and Michael had put the phone down and sat in the business centre of a hotel at half past twelve at night with his hands flat on either side of a laptop.

It was not the attachment.

He knew it was not the attachment. He had been fine about the attachment for the first half of the twenty-five minutes. What had arrived at minute twelve, and had stayed, was a thing with a shape he did not care to look at directly, and its shape was: *there was a period of my life in which this would not have taken twenty-five minutes, and I do not know when it ended.*

That was when Alex went past the window.

---

Alex was going past the window because he could not sleep and the lift lobby on the ninth had the only reliable signal in the building, and he had gone down two floors on the stairs looking for a better one, and had ended up on the first-floor landing.

He saw, through the glass, an old man staring at a laptop in a small bright room at half past midnight, and the particular set of the shoulders that means a person has stopped trying and has not yet stood up.

He nearly walked on. That was the truth of it, and he thought about it afterwards. He got two steps past the door.

Then he came back and put his head in.

"Are you — sorry. Is it the container thing?"

Michael looked up.

"Ah," he said. "It's the chess."

"It's the container thing, isn't it. Where it says it can't verify the workspace."

"It says it can't verify the workspace."

"Yeah." Alex came in. "Can I? It's ninety seconds. It's not you, it's — everyone's is broken. It's a known thing."

It took eighty. Alex did not touch the laptop; he stood beside it with his hands behind his back and said "settings — no, the other settings, the gear — right, network — there'll be a thing that says something like *use secure gateway*, turn it off, no, it won't break anything, it'll just be slower — now open it again."

The file opened.

Michael sat back and looked at it, and then at Alex.

"Is that it?"

"That's it."

"Twenty-five minutes."

"You'd never find it," said Alex. "It's not findable. It's off by default for everyone except people whose device enrolled before some date, and nobody at your place knows that, and the service desk can't see it because it's a local setting." He shrugged. "It's not a you problem. It's genuinely a bad system."

And Michael, who had been told for three years, gently and by people who meant well, that these things were simply how it was now, felt something in his chest let go by about a quarter of an inch.

"Sit down," he said. "I'll buy you a drink."

"The bar's shut."

"Then I'll buy you a chair."

---

It was Michael who brought up the Ledger Gap, and he brought it up the way you show somebody a scar, as an anecdote, to be funny about.

"Do you want to hear about a genuinely hopeless problem," he said. "Not a difficult one. A hopeless one."

"Always."

"Right. So. There's a bank. It doesn't matter which bank, and there are forty of them like this. It has a core ledger written in 1994, which is the actual heart of the thing — six-point-four million current accounts, and it is, by the way, *excellent*, it does not go wrong, in thirty years I have never once seen it lose a penny."

"Mainframe?"

"Mainframe."

"Right," said Alex, sitting forward.

"And it does everything in a batch, overnight, in a window that starts at ten and has to be finished by four. And bolted onto the side of it, since about 2016, there's a payments gateway that does everything in real time, because customers now expect their money to move while they're looking at it, which — leave that. So you've got a real-time thing on the front and a batch thing at the back, and every morning at about half past four somebody has to work out whether they agree with each other."

"And they don't."

"They agree about ninety-nine-point-nine-something of the time," said Michael. "The rest is what we call the Gap. It's about eleven thousand items a night. And there are nineteen people in Sheffield whose entire job is to sit down at six in the morning and work out what those eleven thousand things are."

Alex had gone very still.

"How do they do it?"

"There's a spreadsheet," said Michael, "which is on its fourth author, and the third author is dead."

"How long has this been going on?"

"2014."

"And nobody's fixed it?"

"Three firms have fixed it," said Michael. "The first fixed it for nine million pounds and it did not work. The second fixed it for four and it worked for the current accounts but not for the ones with a joint holder, which is thirty-one per cent of them. The third was a very small very clever outfit from Bristol, and they got closest, and their managing partner cried in a meeting room on the fourth floor in 2019, and I have never told anybody that, and you can't either."

"Why did he cry?"

"Because," said Michael, "he'd worked out on day nine what it takes everyone a year to work out, which is that the problem isn't the reconciliation. The problem is that the two systems don't agree about what *time* it is."

Alex stood up.

---

He got the flip chart.

He did not ask whether he could get the flip chart. He wheeled the easel round so it faced the two of them, and took the cap off a marker with his teeth, and said, "Right — sorry — right. Can I ask you a dozen questions and some of them will be stupid?"

"Nobody's asked me a dozen questions in a row since 2013," said Michael. "Go on."

The first four were about the ledger. Michael answered them. The fifth was about the gateway, and Michael answered that one too. The sixth was: "When the gateway writes a payment, does it write a timestamp, or does it write a sequence number?"

"A timestamp."

"With what precision?"

"Milliseconds."

"From what clock?"

Michael opened his mouth, and stopped.

"I don't know," he said.

"That's the answer," said Alex, and wrote on the flip chart, *WHOSE CLOCK*, and underlined it twice, and from that point on he was not really talking to Michael at all.

It went on for two hours and forty minutes.

Michael watched him.

That was, in the end, what the night was: Michael Halloway, sixty-four years old, sitting in a plastic chair in the business centre of a hotel at one in the morning, watching a twenty-six-year-old man in a hoodie fill four sheets of flip-chart paper, and then tear them off and stick them on the wall with the little bits of tape that come on the pad, and start a fifth.

He did not follow all of it. He followed about sixty per cent, which was more than he had expected and considerably more than he had followed in any of the three consultancies' final presentations, because Alex kept stopping and saying "sorry, do you know what a vector clock is" and then explaining it in forty seconds with a drawing of two people posting letters.

The solution — insofar as Michael understood it, and he understood it well enough to describe it to Fiona a fortnight later in four minutes flat — was not to reconcile the two systems at all. It was to stop asking them to agree about time, and instead to have each of them say, about every item, what it *knew* and what it had *heard*, and then to let a very small thing in the middle work out the order afterwards from the causality rather than the clocks. "You can't fix the disagreement," Alex said, at about half past two, with his hair standing up on one side, "because they're both right. They're right in different frames. So you stop trying to have one truth and you have one *order*."

"And the joint accounts?"

"The joint accounts are the *proof* it's a clock problem," said Alex, and drew a thing with two arrows, and Michael looked at it for four seconds and said "oh," out loud, in the voice of a man who has been shown where his glasses are.

And then Alex said, "Sorry. Sorry, I've — you've been sat there for two hours."

"Do you know what," said Michael, "I've enjoyed that more than anything I've done since March."

---

At ten to three Alex sat down on the floor with his back against the desk, which is a thing men of twenty-six do and men of sixty-four have to plan.

"Would it work?" said Michael.

"Some of it. The clock thing works. The rest I've made up in two hours in a hotel, so, you know." He was tearing a corner off a flip-chart sheet. "You'd want to actually look at the data. There'll be four things in there that break it."

"There always are."

"Yeah."

Michael looked at the wall. Five sheets of paper. Boxes, arrows, a thing that was either a diagram or a fish.

"What do you charge?" he said.

Alex laughed. Then he stopped laughing, because Michael had not.

"I don't — I'm not a consultant. I've got a company."

"I know. What's on that wall—" Michael tipped his head at it. "Two of the three firms I paid never got as far as the first sheet. The one that did charged four million pounds and it took them nine weeks and there were fourteen of them. You've done it in two hours and forty minutes in a hotel with a marker pen, and you keep apologising."

Alex looked at the floor.

He was aware — he was extremely aware — of a thing happening in his chest that he had not felt since he was about nineteen, and which was not pride exactly. Pride was familiar; he got pride off a benchmark. This was different, and it had a stranger in it. This was a man with no reason on earth to flatter him, who had not seen his CV, who did not know what his company had raised or who his investors were or that he had once given a talk in Seattle that two thousand people watched, who had watched him do the thing he was actually good at for two hours and forty minutes and had then, in the light of that and nothing else, said *what do you charge.*

"It's just—" he said. "That's just how I think. It's not—"

"Yes," said Michael. "That's what it's worth."

He stood up, and put a hand briefly on the back of the chair, and looked at the five sheets on the wall.

"I'm going to make an introduction," he said. "There's a fellow at my place who runs the whole of that estate, and I'm going to write to him tonight before I lose the thread of it, and I'll copy your — what's it called?"

"Velum."

"Velum. And after that it's nothing to do with me, because I'm not on that committee any more, thank God. But he'll take my call." He took his laptop under his arm. "Get some sleep. Come and heckle my speech."

"Two o'clock Monday," said Alex.

"Nobody has ever come," said Michael, and went up to bed, and took a breath at the lift, in, and out, and slept better than he had in a month.

Alex stayed on the floor of the business centre for another ten minutes, looking up at the five sheets.

Then he took the notebook out of his jacket and wrote, standing up, leaning on the desk:

*Told a stranger how I think for 2h40 and he asked what I charge. Nobody at V has ever asked what I charge. Note: he wasn't being nice. He wasn't being anything. He just asked.*

He tore the five sheets carefully off the wall, and folded them, and took them upstairs.
