import random

""" A dictionary to keep track of scores for the computer and player"""
scores = {"computer": 0, "player": 0} 

class Board:
    """Represents the game board and provides methods for the game logic"""

    def __init__(self, size):
        #Initialize the board with a given size
        self.size = size
        #Create a 2D grid
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        #To store already guessed locations
        self.hits = set()    
        #To store computer's hidden ships     
        self.hidden_ships = set() 

    def place_ships(self, num_ships):
        """To place ships randomly on the board"""

        for _ in range(num_ships):
            while True:
                # Randomly choose a row and column to place the ship
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                # If the chosen cell is empty, place the ship ('⚓') and add its location to hidden_ships set
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = '⚓'
                    # Add hidden ship location
                    self.hidden_ships.add((row, col))
                    break
    
    def display()

    def make_guess()

    def get_random_coordinate()

    
        