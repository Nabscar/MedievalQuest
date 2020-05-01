# Medieval Quest

This is a project that uses PyGame to create a Medival Quest game in the style of the Original Legend of Zelda.

## Website

https://sd2020spring.github.io/Medieval-Quest/

## Description

The plot of the game is the following. 
In a far away place, in another time, a King was the protector of his kingdom. Everyone loved him, because he was the most benevolent King they had had. He cared for every single person in his kingdom and since his first day, vowed to put every life in his kingdom bfore his own. The people, although they loved him, thought this was just hyperbole, the king would not put his life last, he was human, and humans were selfish. 

Time passed, and everyone forgot about this promise, the kingdom was at the longest period of peace they had enjoyed, and there was no way to destroy that. Or so they thought. One day, at the crack of dawn, the people woke up to see their king walking the streets, with his trusty sword and bow, a bad of bombs and many more items. He was walking with purpose, like never before, and the people were scared. What was happening? Why was their king armed to the teeth?

The answer came as a roar out of the forest. The monsters had allied before The Boss, a mythical five headed monster that had been rumored ot kill countless soldiers. This was the moment where the people remember their Kings promise, the one they had cast out as an exageration. The moment the King stepped out of the fortress walls, order his men to close them, and told them to keep them that way until he was back the people realized, they king was ready to sacrifice his live to save theirs, and they hope he wouldn't have to, but they couldn't do anything now.
 
After that, the player “wakes up” (as the King) alone and far away from the castle, with no recollection of the fight. 
The idea of the game is that the player has to take the King back to the castle, and, in the process, defeat the Monster Leader (which we very creatively have called The Boss). At the start of the game, the player can only move and attack with his sword, and eventually, he is able to get Bombs, Potions and a Bow&Arrow. The visuals of the game will be similar to the original Legend of Zelda, you will see a frame where things might or might not move, and the player can walk to the borders, some of these leading towards other frames in the game. 

The layout of the game is a 3x3 screen of frames (of which the player only sees one at a time) and two separate frames that are caves, which the player can access at different points in the game. 

There are 4 enemies throughout the game: Trolls who throw javelins once they see the player, Bats, who follow the player and try to “bite” him, Shooters, which shoot at the player, and The Boss who has 3 different types of attack. We plan on making a good amount of classes for all of these characters and items. 

## Visuals

These are some visuals from the game.
![Alt](/MQ1.png "Medieval Quest 1")
![Alt](/MQ2.png "Medieval Quest 2")
![Alt](/MQ3.png "Medieval Quest 3")

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

 
## Usage

The usage of this game is really simple. Once the Installation procedure has been done, just go to the folder where `game.py` is in your computer and run
```
python game.py
```
in the terminal. Once you have done this, a screen will pop up showing you the first frame of the game. Now in game, you only need to use WASD to move (W is forwards, A if Left, S is Backwards, and D is Right) and the use J to attack with your sword, K to shoot your arrows (onse acquired), L to place bombs (if you have them), and I to use Health Potions (If you have them)

## Sources
The only external sources used were:
The Legend of Zelda as a starting idea point
PyMan tutorial as a architecture tutorial and to see how to develop the game itself
