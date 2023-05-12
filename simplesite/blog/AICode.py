"""
This code drives the backend logic and AI agent for the connect 4 game
"""

# imports
import itertools
import random
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


def game_end(game_state, last_piece):
    """
    Checks if the game has ended, placeholder for now
    """
    last_piece_value = game_state[last_piece[0]][last_piece[1]]
    win_pattern = last_piece_value * 4
    # Check vertical
    vert_string = "".join([slot for slot in game_state[last_piece[0]]])
    if win_pattern in vert_string:
        return True
    # Check horizontal
    horizontal_string = "".join([game_state[i][last_piece[1]] for i in range(len(game_state))])
    if win_pattern in horizontal_string:
        return True
    # Check diagonals
    diagonal_desc_list = []
    diagonal_asc_list = []
    for diag_column in range(max(0, last_piece[0]-3), min(len(game_state), last_piece[0]+4)):
        column_slots = game_state[diag_column]
        col_dist_from_last_piece = last_piece[0] - diag_column

        # Check diagonal descending (top left to bottom right)
        relevant_slot_desc = last_piece[1]+(col_dist_from_last_piece)
        if 6 > relevant_slot_desc >= 0:
            rel_slot_status = column_slots[relevant_slot_desc]
            diagonal_desc_list.append(rel_slot_status)
            # print(diag_column,col_dist_from_last_piece, rel_slot_status) # Debug

        # Check diagonal ascending (bottom left to top right)
        relevant_slot_asc = last_piece[1]-(col_dist_from_last_piece)
        if 6 > relevant_slot_asc >= 0:
            rel_slot_status_asc = column_slots[relevant_slot_asc]
            diagonal_asc_list.append(rel_slot_status_asc)

    diagonal_desc_string = "".join(diagonal_desc_list)
    diagonal_asc_string = "".join(diagonal_asc_list)

    if win_pattern in diagonal_desc_string or win_pattern in diagonal_asc_string:
        return True
    return False


def place_piece(game_state, player, column):
    for slot in range(len(game_state[column])):
        if game_state[column][slot] == "X":
            game_state[column][slot] = player
            return game_state, (column, slot)
    return "Invalid move", None


def random_ai_move(game_state, current_player):
    """
    Randomly places a piece in a column
    """
    column = random.randint(0, 6)
    return place_piece(game_state, current_player, column)


def minmax_ai_move(game_state, current_player):
    """
    Uses the minmax algorithm to determine the best move
    """
    pass


def mcts_ai_move(game_state, current_player):
    """
    Uses the Monte Carlo Tree Search algorithm to determine the best move
    """
    pass


if __name__ == "__main__":
    players = itertools.cycle(["A", "B"])
    game_state = initialise_game()
    game_mode = input("Enter game mode (1 for 1 player vs AI, 2 for 2 player): ")
    ai_difficulty = ""
    if game_mode == "1":
        ai_difficulty = input("Enter AI difficulty (1 for easy, 2 for medium, 3 for hard): ")
    print_game_state(game_state)
    while True:
        current_player = next(players)
        while True:

            # If it's the AI's turn, make a move accordingly
            if ai_difficulty != "" and current_player == "B":
                if ai_difficulty == "1":  # Random AI
                    next_state, last_piece = random_ai_move(game_state, current_player)
                elif ai_difficulty == "2":  # Minmax AI
                    pass
                elif ai_difficulty == "3":  # MCTS AI
                    pass
                else:
                    print("Invalid AI difficulty")
                    continue
                print("AI's turn")
                print("AI placed at", last_piece)

            # If it's the player's turn, ask for input
            else:
                print("Player " + current_player + "'s turn")
                column = int(input("Column: "))
                next_state, last_piece = place_piece(game_state, current_player, column)
            if next_state == "Invalid move":
                print("Invalid move")
                continue
            else:
                game_state = next_state
                break
        print("_____________")
        print_game_state(game_state)
        if game_end(game_state, last_piece):
            print(current_player + " wins!")
            break



