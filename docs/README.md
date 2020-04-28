# Game for the Brave

## Plot

In a far away place, in another time, a King was the protector of his kingdom. Everyone loved him, because he was the most benevolent King they had had. He cared for every single person in his kingdom and since his first day, vowed to put every life in his kingdom bfore his own. The people, although they loved him, thought this was just hyperbole, the king would not put his life last, he was human, and humans were selfish. 

Time passed, and everyone forgot about this promise, the kingdom was at the longest period of peace they had enjoyed, and there was no way to destroy that. Or so they thought. One day, at the crack of dawn, the people woke up to see their king walking the streets, with his trusty sword and bow, a bad of bombs and many more items. He was walking with purpose, like never before, and the people were scared. What was happening? Why was their king armed to the teeth?

The answer came as a roar out of the forest. The monsters had allied before The Boss, a mythical five headed monster that had been rumored ot kill countless soldiers. This was the moment where the people remember their Kings promise, the one they had cast out as an exageration. The moment the King stepped out of the fortress walls, order his men to close them, and told them to keep them that way until he was back the people realized, they king was ready to sacrifice his live to save theirs, and they hope he wouldn't have to, but they couldn't do anything now.

## Gameplay

<img src="images/king.png" width="425" heigth="475" align="left">

This is how the story transpired up until the moment the player comes in. The moment the game start, the palyer is in the middle of the woods, having lost everything but his trusty sword, and he has to battle his way back to the castle, which has, right outside the gates, a waiting Boss who wants to take controll of the kingdom.<br>

At the start of the game, the player can only move and attack with his sword, and eventually, he is able to get Bombs, Potions and a Bow&Arrow. The Bombs and Potions have a counter at the bottom, a counter that shows how many of these the player has left. The Arrows for the Bow are unlimited.

The layout of the game is a 3x3 screen of frames (of which the player only sees one at a time) and two separate frames that are caves, which the player can access at different points in the game. What the player does to access these is walk up to the different parts of the border of the screen that lead to other frames, and when he collides with these, the player will be transported to the new screen.

<img src="images/enemies.png" width="450" heigth="400" align="right">

There are 4 enemies throughout the game: 

- Trolls <br>
<nbsp>Throw javelins once they see the player
  
- Bats <br>
<nbsp>Follow the player and try to bite him
  
- Shooters<br>
<nbsp>Shoot balls at the player
  
- The Boss <br>
<nbsp>Has 3 different types of attack<br>
<nbsp>- Front attack: Both swords forward <br>
<nbsp>- Side attack: One sword to each side <br>
<nbsp>- Sweep attack: Swing in front and sides with ax <br>

<br><br><br>
## Installation

There are only two things required when installing Medieval Quest. 
* First, make sure to have PyGame installed.
  To install pygame in Linux run the following commands:
 ```
  $ apt-get build-dep python-pygame
  $ apt-get install mercurial python-dev python-numpy ffmpeg libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
  $ pip install pygame
 ```
* Second, go to the main game file (`game.py`) and in the second line, change the path takes to the Levels folder to your own path on your computer.

## Sources
The only external sources used were:
The Legend of Zelda as a starting idea point
PyMan tutorial as a architecture tutorial and to see how to develop the game itself

 
## Usage

The usage of this game is really simple. Once the Installation procedure has been done, just go to the folder where `game.py` is in your computer and run
```
python game.py
```
in the terminal. Once you have done this, a screen will pop up showing you the first frame of the game. Now in game, you only need to use WASD to move (W is forwards, A if Left, S is Backwards, and D is Right) and the use J to attack with your sword, K to shoot your arrows (onse acquired), L to place bombs (if you have them), and I to use Health Potions (If you have them)
