# Alien-Invasion-Project, is a 2d game, where you have battleship and aliens are invading it. You have to shoot down all the aliens before they reach or pass your ship(You have 3 ships in reserve).
# When you shoot down all of the aliens difficulty of the game increases(The game has 3 stages).

# My application uses pygame library to create 2d battleship, which can shoot bullets. And aliens (the amount that can fit through some part of the screen), that come down on the screen while changing directions on the edges. 
# Managing aliens/battleships speed was very challenging and im hoping to modify the game so everyone can play the game on the same(at least relatable) speed.

# Steps To Run The Code:
# 1. install pygame library.
# 2. Open the code and run it in an alien_invasion.py file.
# 3. Click play with mouse, use left and right arrow keys to move the ship and spacebar to shoot the aliens.
# 4. Press 'q' button if you want to quit the game.

# If you want to manage the project here is the quick guide:
# alien_invasion.py is the main file where the game is executed. if you add some methods or functions in the code you have to modify this file too to see them in action.
# Settings.py is the file where you can manage the settings(Bullet's, ship's and alien's speed. Alien's direction. Colors and sizes of the objects. Difficulty of the game) for the game manually.
# game_stats.py is the file where the methods for managing game stats is defined.
# ship.py, aliens.py, bullet.py are the files where each object is defined.
# button.py file helps you create the button 'PLAY' for the game.
# scoreboard.py file helps you to create the scoreboard and highscore for the game.
