"""
This code drives the backend logic and AI agent for the connect 4 game
"""

# imports
import itertools

# Helper code for generating board
# for i in range(7):
#     str = "["
#     for j in range(5):
#         str += """"X", """
#     str += """"X"],"""
#     print(str)


def initialise_game():
    """
    Set up the game board in a flat rotation where the left is the bottom and the right is the top
    """
    return [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ]


def print_game_state(gamestate):
    """
    Prints the current game state
    """
    for i in range(5, -1, -1):
        str = ""
        for j in range(7):
            str += gamestate[j][i] + " "
        print(str)
    print("_____________")
    print("0 1 2 3 4 5 6")
def game_end(gamestate):
    """
    Checks if the game has ended, placeholder for now
    """
    return False


def place_piece(gamestate, player, column):
    for slot in range(len(gamestate[column])):
        if gamestate[column][slot] == "X":
            gamestate[column][slot] = player
            return gamestate, (column, slot)
    return "Invalid move"


if __name__ == "__main__":
    players = itertools.cycle(["A", "B"])
    game_state = initialise_game()
    print_game_state(game_state)
    while True:
        if game_end(game_state):
            break
        player = next(players)
        print("Player " + player + "'s turn")
        column = int(input("Column: "))
        next_state, last_piece = place_piece(game_state, player, column)
        if next_state == "Invalid move":
            print("Invalid move")
            continue
        else:
            game_state = next_state
        print("_____________")
        print_game_state(game_state)