# Medieval Quest

This is a project that uses PyGame to create a Medival Quest game in the style of the Original Legend of Zelda.

## Description

The plot of the game is the following. 
In a far away place, in another time, a King was the protector of his kingdom. But then, a swarm of monsters decided to attack. The King, as a great leader, went with his troops to fight the monsters.
(The Intro is still in progress) 
 
After that, the player “wakes up” (as the King) alone and far away from the castle, with no recollection of the fight. 
The idea of the game is that the player has to take the King back to the castle, and, in the process, defeat the Monster Leader (which we very creatively have called The Boss). At the start of the game, the player can only move and attack with his sword, and eventually, he is able to get Bombs, Potions and a Bow&Arrow. The visuals of the game will be similar to the original Legend of Zelda, you will see a frame where things might or might not move, and the player can walk to the borders, some of these leading towards other frames in the game. 

The layout of the game is a 3x3 screen of frames (of which the player only sees one at a time) and two separate frames that are caves, which the player can access at different points in the game. 

There are 4 enemies throughout the game: Trolls who throw javelins once they see the player, Bats, who follow the player and try to “bite” him, Shooters, which shoot at the player, and The Boss who has 3 different types of attack. We plan on making a good amount of classes for all of these characters and items. 

## Visuals

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