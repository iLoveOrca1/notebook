# How do you get better at CTF?

I've been studying how to solve CTF by some weeks now. Basic CTF is ok, but when we go to the specific i feel like there are too much knowledge to know and dont know where to go.

For example:

- Cryptography: I studied steganography, the various base64, rot13, XOR, symmetryc and private key, substitution ciphers and transposition ciphers. I've saw some simple example of xortool but in pratice i really dont know what to do or search up
    
- Web: the basic ones it's ok. If it's something about login or crack the form with given php file it's ok. But i got a web ctf with a webpage with a 2D physic simulator. wtf. i dunno where to search. Also, thx for a tip, i know the existence of robots.txt. Before that how can i know that?
    
- Network: wireshark, 3 hand shaking ok ok, TPC, HTTP, ok ok, then when i go to make challenges, new protocols
    
- reverse engineering: ghidra, oh yes find the main, substitute random value name with better ones, understand the flows ok ok, but in challenges, the main is missing, each function are empty lmao
    

It's like you can have an entire course for each topic. But you guys, how do you improve yourself? I've read that reading writeups really helps, but other than that?

# Answer

> How do you get better at CTF?

Play. Most strong teams have been playing for `years`, so with `some weeks now` you still have a lot ahead of you.

The trick is you pick a task at a CTF and you just focus on it. It's not unusual to spend 20h-30h on a single task. Don't expect you'll get it in 5 minutes. A network task might require to read a hundred RFCs and dive into implementation of tcp/ip stack in linux. Crypto task might require reading a bunch of academic papers before you have any idea what is going on. Web task may require reading source code of the browser to see how javascript engine JITs some code.

The whole point is not to give up because `I don't know what to do` after spending 5 minutes.

---

It is overwhelming, even after you've been doing it for years. It's easy to feel "imposter syndrome", because as you learn and grow you are continuously following people at higher and higher levels of expertise and comparing yourself. Don't. Compare yourself to YOU and your skill level last week/month/year. Once you do that you'll feel better about your progress. It will always be a struggle though. A famous hacker once said "If you don't feel like a newb, you're not trying hard enough.".

Don't jump all around. Pick one thing you need to learn and learn it well before moving on to the next thing. Otherwise you'll get overwhelmed and jump continuously from one distraction to another and get frustrated.

Keep trying, and keep improving. It's a journey, not a destination.

source:
reddit.com/r/securityCTF