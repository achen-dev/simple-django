"""
This code drives the backend logic and AI agent for the connect 4 game
"""

# Setup the game board in a flat rotation where the left is the bottom and the right is the top
GAME_STATE = [
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
]

# Helper code for generating board
# for i in range(7):
#     str = "["
#     for j in range(5):
#         str += """"X", """
#     str += """"X"],"""
#     print(str)


def print_game_state():
    """
    Prints the current game state
    """
    for i in range(5, -1, -1):
        str = ""
        for j in range(7):
            str += GAME_STATE[j][i] + " "
        print(str)

def game_end(gamestate):
    """
    Checks if the game has ended
    """
    return False



if __name__ == "__main__":
    print_game_state()