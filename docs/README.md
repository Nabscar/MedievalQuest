# The Game

## Goal of this project

Our goal for this project was to create an interactive fun game for people to play so that they would be ale to invest their time in quarentine towards an entretaining idea.

## Game Information

### Plot

In a far away place, in another time, a King was the protector of his kingdom. Everyone loved him, because he was the most benevolent King they had had. He cared for every single person in his kingdom and since his first day, vowed to put every life in his kingdom bfore his own. The people, although they loved him, thought this was just hyperbole, the king would not put his life last, he was human, and humans were selfish. 

Time passed, and everyone forgot about this promise, the kingdom was at the longest period of peace they had enjoyed, and there was no way to destroy that. Or so they thought. One day, at the crack of dawn, the people woke up to see their king walking the streets, with his trusty sword and bow, a bad of bombs and many more items. He was walking with purpose, like never before, and the people were scared. What was happening? Why was their king armed to the teeth?

The answer came as a roar out of the forest. The monsters had allied before The Boss, a mythical five headed monster that had been rumored ot kill countless soldiers. This was the moment where the people remember their Kings promise, the one they had cast out as an exageration. The moment the King stepped out of the fortress walls, order his men to close them, and told them to keep them that way until he was back the people realized, they king was ready to sacrifice his live to save theirs, and they hope he wouldn't have to, but they couldn't do anything now.

### GamePlay

<img src="images/king.png" align="left" width="50%">
This is how the story transpired up until the moment the player comes in. The moment the game start, the palyer is in the middle of the woods, having lost everything but his trusty sword, and he has to battle his way back to the castle, which has, right outside the gates, a waiting Boss who wants to take controll of the kingdom.<br>

At the start of the game, the player can only move and attack with his sword, and eventually, he is able to get Bombs, Potions and a Bow&Arrow. The Bombs and Potions have a counter at the bottom, a counter that shows how many of these the player has left. The Arrows for the Bow are unlimited.

The layout of the game is a 3x3 screen of frames (of which the player only sees one at a time) and two separate frames that are caves, which the player can access at different points in the game. What the player does to access these is walk up to the different parts of the border of the screen that lead to other frames, and when he collides with these, the player will be transported to the new screen.

<img src="images/enemies.png" align="right" width="50%">

There are 4 enemies throughout the game: 

- Trolls, who throw javelins once they see the player <br>
  
- Bats, who follow the player and try to bite him <br>
  
- Shooters, who shoot balls at the player <br>
  
- The Boss, who has 3 different types of attack<br>
  * Front attack: Both swords forward <br>
  * Side attack: One sword to each side <br>
  * Sweep attack: Swing in front and sides with ax <br>


### Installation

There are only two things required when installing Medieval Quest. 
1. Make sure to have PyGame installed.
  To install pygame in Linux run the following commands:
 ```
  $ apt-get build-dep python-pygame
  $ apt-get install mercurial python-dev python-numpy ffmpeg libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
  $ pip install pygame
 ```
2. Go to the main game file (`game.py`) and in the second line, change the path takes to the Levels folder to your own path on your computer.

### Usage

The usage of this game is really simple. Once the Installation procedure has been done, just go to the folder where `game.py` is in your computer and run
```
python game.py
```
in the terminal. Once you have done this, a screen will pop up showing you the first frame of the game. Now in game, you only need to use WASD to move (W is forwards, A if Left, S is Backwards, and D is Right) and the use J to attack with your sword, K to shoot your arrows (once acquired), L to place bombs (if you have them), and I to use Health Potions (If you have them)

<br>

## Results 
 <video>
  <source src="images/gameplay.mp4" type="video/mp4">
</video> 

## Software Impact Statement 
In our specific case, the ethical considerations of our project weren't so impactful. Since we just wanted to create a fun game for people to play with, our stakeholder were the players. The only impact on them would be having an amazing time when playing, and deciding they want more. There are no big unintended consequences qwee could think of when developing this software in real world scenarios. The only unitended consequence we could think of would be creating an amazing franchise of games that redefines gaming for all ages (just like The Legend of Zelda, the game which gave us our idea, did).

## Project evolution/narrative 

Medieval Quest was a game that evolved in a very simple and straightforward manner. When we started, we started working on three different fronts:
### Architecture
For the architecture of the game, we were able to very easily settle on what we currently use. We started by listing the classes we would need and separate them in different inheritance levels. 
<img src="images/architecture.png">
This slowly evolved into our current achitecture.The easiest way to explain it is throught a series of nested flow diagrams. The biggest one the shows the <b>overall architecture and run of the code</b> is this one.<br>
<img src="images/Overall.png">
As you can see, the most important part of this one is the <b>MainQuest</b>, which can be seen in more detail in teh following diagram.<br>
<img src="images/MainQuest.png">
As you can see,<b>MainQuest</b> has to very important parts, which can both be seen in more detail below. On the left, you can see how <b>LoadSprites</b> runs, and on the right, you can see how <b>MainLoop</b> works.
<img src="images/LoadSprites.png" width="45%" align="left">
<img src="images/MainLoop.png" width="45%" align="right">

### Visual Design
In our case, we both had very similar ideas to what our game should look like, so we just started working on images which eventually developed into bakcgrounds, enemies, and the player.
<img src="images/visuals.png">

### Game Layout
The game layout was fairly easy to do. When we started we settled on the idea of a 3x3 grid of frames, since this was a big enough number for the world to feel semi-developed, but small enough for it to be achievable between the two of us. We also decided we should have caves, and both of us agreed that two caves seemed to be the right number of caves for our 3x3 world. Initially our overall design was the following:
<img src="images/LayoutV1.png">
Which afterwards evolved into this design (Which is the hand-drawn sketch of the design we actually use for our levels):
<img src="images/levelLayoutIdeation.png">

## Attributions
The only external sources used were:
- <a href="https://en.wikipedia.org/wiki/The_Legend_of_Zelda">The Legend of Zelda</a> as a starting idea point <br>
- PyMan tutorial as a architecture tutorial and to see how to develop the game itself
