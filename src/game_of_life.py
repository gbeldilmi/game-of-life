# -*- coding: utf-8 -*

from random import randint # required for __init__()  [at line 36]

class GameOfLife:
    """Simulates Conway's game of life"""

    def __init__(self, width, height, probability_that_a_cell_is_alive):
        """Constructor : it will initialise all we need
        Warning : the arguments "width" and "height" must be at or above 2"""

        # check the arguments #
        if width < 2 or height < 2:
            print(" Error args: 'width' and 'height' must be at or above 2 ")
            input(" Press ENTER to close... ")
            exit()

        # define chosen size
        self.WIDTH = width
        self.HEIGHT = height

        self.generation_counter = 0

        self.current_generation = [[False, False], [False, False]] # create the generation
        # its size is adapted until it reaches the chosen size
        # first, the height is increased or not
        while len(self.current_generation) != self.HEIGHT:
            self.current_generation.append([False, False])
        # next, it's the width or not
        while len(self.current_generation[0]) != self.WIDTH:
            for pos in range(len(self.current_generation)):
                self.current_generation[pos].append(False)

        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                is_alive = (probability_that_a_cell_is_alive > randint(0, 99))
                self.current_generation[i][j] = is_alive
        return

    def display_generation(self):
        """Display current generation with its counter"""

        # we'll use a variable named "prompt" and add to it all that we want to display
        prompt = " @ " + str(self.generation_counter) +"\n" # add the counter
        prompt += "╔" + ("═" * self.WIDTH) + "╗\n" # add a nice border at the top

        for line in self.current_generation:
            # begin a new line
            prompt += "║" # add a nice border on the left

            for cell in line:
                if cell: # if the cell is alive
                    prompt += "O" # display a living cell
                else:
                    prompt += " " # display a dead cell

            prompt += "║\n" # a nice border on the right
            # line's end

        prompt += "╚" + ("═" * self.WIDTH) + "╝\n" # add a nice border at the bottom

        print(prompt) # display
        return

    def next_generation(self):
        """Return the next generation"""

        next_generation = [[False, False], [False, False]] # create the new generation

        # its size is adapted until it reaches the chosen size
        # first, the height is increased or not
        while len(next_generation) != self.HEIGHT:
            next_generation.append([False, False])
        # next, it's the width or not
        while len(next_generation[0]) != self.WIDTH:
            for pos in range(len(next_generation)):
                next_generation[pos].append(False)

        # for each cell, we'll count the number of adjacent living cells
        # and then define if the cell will be alive or not in the next generation
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                # it's our counter
                # by default, a cell has no living neighbour
                # if a neighboring cell is alive, this counter will be incremented
                living_neighbor = 0

                # up
                if 0 < y:
                    if self.current_generation[y - 1][x]:
                        living_neighbor += 1
                # down
                if y < self.HEIGHT - 1:
                    if self.current_generation[y + 1][x]:
                        living_neighbor += 1
                # left
                if 0 < x:
                    if self.current_generation[y][x - 1]:
                        living_neighbor += 1
                # right
                if x < self.WIDTH - 1:
                    if self.current_generation[y][x + 1]:
                        living_neighbor += 1
                # up left
                if 0 < y and 0 < x:
                    if self.current_generation[y - 1][x - 1]:
                        living_neighbor += 1
                # down left
                if y < self.HEIGHT - 1 and 0 < x:
                    if self.current_generation[y + 1][x - 1]:
                        living_neighbor += 1
                # up right
                if 0 < y and x < self.WIDTH - 1:
                    if self.current_generation[y - 1][x + 1]:
                        living_neighbor += 1
                # down right
                if y < self.HEIGHT - 1 and x < self.WIDTH - 1:
                    if self.current_generation[y + 1][x + 1]:
                        living_neighbor += 1

                # apply rules #
                # each dead cell adjacent to exactly three live neighbors will become live in the next generation
                if not(self.current_generation[y][x]):
                    if living_neighbor == 3:
                        next_generation[y][x] = True
                # each living cell adjacent to exactly two or three live neighbors will alive in the next generation
                if self.current_generation[y][x]:
                    if living_neighbor == 2 or living_neighbor == 3:
                        next_generation[y][x] = True

        self.generation_counter += 1
        return next_generation

    def is_living_cells(self):
        """Test if there is one living cell in current generation
        return True if there is
        else return False """

        for y in range(self.HEIGHT): # for each line
            for x in range(self.WIDTH): # for each cell
                if self.current_generation[y][x]: # check if the cell is alive
                    return True
        return False
