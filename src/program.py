# -*- coding: utf-8 -*

### BOARD'S SIZE ###
WIDTH = 60 # min. 2
HEIGHT = 20 # min. 2
### PERCENTAGE CHANCE THAT A CELL IS ALIVE ###
# If PERCENTAGE_CHANCE_THAT_A_CELL_IS_ALIVE = 0     => all cells are dead
# If PERCENTAGE_CHANCE_THAT_A_CELL_IS_ALIVE = 100   => all cells are alive
PERCENTAGE_CHANCE_THAT_A_CELL_IS_ALIVE = 50

from game_of_life import * # Import all that we need
from utilities import clear_screen # Import a useful function

print("   ╔═════════════════════════════════╗\n   ║      Conway's Game of Life      ║\n   ╚═════════════════════════════════╝\n \n ")
input(" Press ENTER to begin... ") # wait before starting

game = GameOfLife(WIDTH, HEIGHT, PERCENTAGE_CHANCE_THAT_A_CELL_IS_ALIVE) # initialize a new one

while game.is_living_cells():
    clear_screen()
    game.display_generation() # display current generation
    game.current_generation = game.next_generation() # replaces the current generation with the next one

    # input(" Press ENTER to continue... ") # if you want a break between each generation

print(" All cells died at generation " + str(game.generation_counter))
input(" Press ENTER to close... ")
