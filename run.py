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
    
    def display(self, show_ships=False):
        """To display the current state of the board"""

        print("\n   A  B  C  D  E")
        print("  +-+--+--+--+--+")
        row_number = 1
        for i, row in enumerate(self.grid):
            if show_ships:
                #If show_ships is True, display the ships ('⚓') and empty cells as '🌊'
                display_row = [cell if cell != ' ' else '🌊' for cell in row]
                print(f"{i} {' '.join(display_row)}")
            else:
                #Otherwise, show only hits ('💥'), misses ('❌'), and empty cells as '🌊'
                hidden_row = ['💥' if (i, j) in self.hits and (i, j) in self.hidden_ships else '❌' if (i, j) in self.hits else '🌊' for j, cell in enumerate(row)]
                print(f"{i} {' '.join(hidden_row)}")

    def make_guess(self, row, col):
        """To handle player's guesses and update the board accordingly"""

        if (row, col) in self.hits:
            print("You alread shot there. Try a different location.")
            return False
        # Add the guessed location to hits set
        self.hits.add((row,col))

        if(row, col) in self.hidden_ships:
            # If the guessed location contains a hidden ship, mark it as '💥'
            self.grind[row][col] = '💥'
            return True
        elif self.grind[row][col] == ' ':
            # If the guessed location is empty, mark it as '❌'
            self.grid[row][col] = '❌'
        return False

    #def get_random_coordinate():

#def summary():

#def get_valid_coordinate():

def game():
    """Call all the necessary functions to run the game"""

    # Initialize the game parameters
    size = 5
    num_ships = 4

    # The welcome messages and get the player's name
    print("-" * 35)
    print("Welcome to Emoji Battleships!")
    print(f"Board size: {size}, Number of ships: {num_ships}")
    print("Coordinates row: 0-1-2-3-4, col: A-B-C-D-E")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)