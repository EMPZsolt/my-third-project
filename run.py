import random

"""A dictionary to keep track of scores for the computer and player"""
scores = {"computer": 0, "player": 0}


class Board:
    """Represents the game board and provides methods for the game logic"""

    def __init__(self, size):
        # Initialize the board with a given size
        self.size = size
        # Create a 2D grid
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        # To store already guessed locations
        self.hits = set()
        # To store computer's hidden ships
        self.hidden_ships = set()

    def place_ships(self, num_ships):
        """To place ships randomly on the board"""

        for _ in range(num_ships):
            while True:
                # Randomly choose a row and column to place the ship
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                """ If the chosen cell is empty, place the ship ('⚓')
                and add its location to hidden_ships set"""
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = '⚓'
                    # Add hidden ship location
                    self.hidden_ships.add((row, col))
                    break

    def display(self, show_ships=False):
        """To display the current state of the board"""

        print("\n   A  B  C  D  E")
        print(" +--+--+--+--+--+")
        row_number = 1
        for i, row in enumerate(self.grid):
            if show_ships:
                """ If show_ships is True, display the ships ('⚓')
                and empty cells as '🌊'"""
                display_row = [cell if cell != ' ' else '🌊' for cell in row]
                print(f"{i} {' '.join(display_row)}")
            else:
                """ Otherwise, show only hits ('💥'), misses ('❌'),
                and empty cells as '🌊'"""
                hidden_row = [
                    '💥' if (i, j) in self.hits and (i, j) in self.hidden_ships
                    else '❌' if (i, j) in self.hits
                    else '🌊'
                    for j, cell in enumerate(row)
                ]
                print(f"{i} {' '.join(hidden_row)}")

    def make_guess(self, row, col):
        """To handle player's guesses and update the board accordingly"""

        if (row, col) in self.hits:

            return False

        # Add the guessed location to hits set
        self.hits.add((row, col))

        if (row, col) in self.hidden_ships:
            # If the guessed location contains a hidden ship, mark it as '💥'
            self.grid[row][col] = '💥'
            return True
        elif self.grid[row][col] == ' ':
            # If the guessed location is empty, mark it as '❌'
            self.grid[row][col] = '❌'
        return False

    def get_random_coordinate(self):
        """To get a random valid coordinate for the computer's guess"""

        row = random.randint(0, self.size - 1)
        col = random.randint(0, self.size - 1)
        return row, col


def summary(player_name, player_score, computer_score):
    """This function is responsible for displaying the score summary
    after each round."""

    print("------------- Score Summary -------------")
    print(f"{player_name}'s Score: {player_score}")
    print("Computer's Score:", computer_score)
    print("-----------------------------------------")


def get_valid_coordinate(promt, size, guessed_coordinates):
    """This function validate the player's input for row and
    column coordinates."""

    while True:
        coordinate = input(promt)
        # Check if input is alphabetic (A, B, C, etc.)
        if coordinate.isalpha():
            # Convert letter to numeric column index
            col = ord(coordinate.upper()) - ord('A')
            if 0 <= col < size:
                if (col, None) not in guessed_coordinates:
                    return col
            else:
                print("Coordinates must be between A and " +
                      f"{chr(ord('A') + size - 1)}.")
        else:
            try:
                row = int(coordinate)
                if 0 <= row < size:
                    if (None, row) not in guessed_coordinates:
                        return row
                else:
                    print(f"Coordinates must be between 0 and {size - 1}.")
            except ValueError:
                print("Invalid input. Please enter a number or a letter.")


def game():
    """Call all the necessary functions to run the game"""

    # Initialize the game parameters
    size = 5
    num_ships = 4

    # The welcome messages and get the player's name
    print("-" * 35)
    print("Welcome to Emoji Battleships!")
    print("-" * 35)
    print("Game description")
    print("The object of Battleship is to try and sink all of the computer's" +
          "before it sinks all of your ships.")
    print("All of the computer's ships are somewhere on its board.")
    print("You try and hit them by calling out the coordinates of one of the" +
          "squares on the board.")
    print("Happy sailing and good hunt!")
    print("-" * 35)
    print("Game features")
    print(f"Board size: {size}")
    print(f"Number of ships: {num_ships}")
    print("-" * 35)
    print("Infos")
    print("Coordinates: 0-A, 1-B, 2-C, 3-D, 4-E")
    print("Both types can be used based on the compliance rules.")
    print("If the same coordinates are entered, the round is repeated")
    print("The game ends when the player or the computer has sunk all the" +
          "ships.")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    # Create player's and computer's boards
    player_board = Board(size)
    computer_board = Board(size)

    # Place ships randomly on the boards
    player_board.place_ships(num_ships)
    computer_board.place_ships(num_ships)

    # Initialize player and computer scores
    player_score = 0
    computer_score = 0

    # Lists to store player's and computer's guesses
    player_guesses = []
    computer_guesses = []

    # The Game loop
    while True:

        # Display the boards
        print(f"\n{player_name}'s Board:")
        player_board.display(show_ships=True)

        print("\nComputer's Board:")
        computer_board.display()

        # Player's turn
        print("\nYour turn:")
        row = get_valid_coordinate(
            "Enter row (0 to 4 or A to E): ",
            size,
            player_guesses
        )
        col = get_valid_coordinate(
            "Enter column (0 to 4 or A to E): ",
            size,
            player_guesses
        )

        # Record player's guess
        player_coordinate = (col, row)
        if player_coordinate in player_guesses:
            print("You already shot there. Try a different location.")
            continue

        player_guesses.append(player_coordinate)

        if computer_board.make_guess(row, col):
            print("Perfect! You hit an enemy ship! 💥\n")
            player_score += 1

        else:
            print("You missed!\n")

        if player_score == num_ships:
            print(f"Congratulations, {player_name}! You won!\n")
            break

        # Computer's turn
        print("Computer's turn:")
        computer_row, computer_col = computer_board.get_random_coordinate()

        # Record computer's guess
        computer_coordinate = (computer_col, computer_row)
        while computer_coordinate in computer_guesses:
            computer_row, computer_col = computer_board.get_random_coordinate()
            computer_coordinate = (computer_col, computer_row)

        computer_guesses.append(computer_coordinate)

        if player_board.make_guess(computer_row, computer_col):
            print("The computer hit one of your ships! 💥\n")
            computer_score += 1
        else:
            print("The computer missed!\n")

        if computer_score == num_ships:
            print("Sorry! The computer sunk all your ships." +
                  "Better luck next time!\n")
            break

        # Display the summary after each round
        summary(player_name, player_score, computer_score)


# Execute the game function
if __name__ == "__main__":
    game()
