"""
This code drives the backend logic and AI agent for the connect 4 game
"""

# imports
import itertools
import random
from copy import copy, deepcopy

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
    state_string = ""
    for i in range(5, -1, -1):
        line = ""
        for j in range(7):
            if gamestate[j][i] == "B":
                line += '\033[93m' + "B" + '\033[0m' + " "

            elif gamestate[j][i] == "A":
                line += '\033[94m' + "A" + '\033[0m' + " "
            else:
                line += gamestate[j][i] + " "
        state_string += line + "\n"
    print(state_string)
    print("_____________")
    print("0 1 2 3 4 5 6")


def transpose_game_state(gamestate):
    output_list = []
    for i in range(5, -1, -1):
        line_list = []
        for j in range(7):
            if gamestate[j][i] == "B":
                line_list.append("B")
            elif gamestate[j][i] == "A":
                line_list.append("A")
            else:
                line_list.append("X")
        output_list.append(line_list)
    return output_list


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
    for diag_column in range(max(0, last_piece[0] - 3), min(len(game_state), last_piece[0] + 4)):
        column_slots = game_state[diag_column]
        col_dist_from_last_piece = last_piece[0] - diag_column

        # Check diagonal descending (top left to bottom right)
        relevant_slot_desc = last_piece[1] + (col_dist_from_last_piece)
        if 6 > relevant_slot_desc >= 0:
            rel_slot_status = column_slots[relevant_slot_desc]
            diagonal_desc_list.append(rel_slot_status)
            # print(diag_column,col_dist_from_last_piece, rel_slot_status) # Debug

        # Check diagonal ascending (bottom left to top right)
        relevant_slot_asc = last_piece[1] - (col_dist_from_last_piece)
        if 6 > relevant_slot_asc >= 0:
            rel_slot_status_asc = column_slots[relevant_slot_asc]
            diagonal_asc_list.append(rel_slot_status_asc)

    diagonal_desc_string = "".join(diagonal_desc_list)
    diagonal_asc_string = "".join(diagonal_asc_list)

    if win_pattern in diagonal_desc_string or win_pattern in diagonal_asc_string:
        return True
    return False


def place_piece(place_game_state, player, place_column):
    for slot in range(len(place_game_state[place_column])):
        if place_game_state[place_column][slot] == "X":
            place_game_state[place_column][slot] = player
            return place_game_state, (place_column, slot)
    return "Invalid move", None


def random_ai_move(game_state, current_player):
    """
    Randomly places a piece in a chosen_col
    """
    valid_columns = []
    for column in range(len(game_state)):
        if game_state[column][5] == "X":
            valid_columns.append(column)
    play_column = random.choice(valid_columns)
    return place_piece(game_state, current_player, play_column)


def legacy_minmax_ai_move(ai_state, current_player, alpha, beta, isMax, depth, chosen_column=None):
    """
    Uses the minmax algorithm to determine the best move
    Legacy spaghetti code
    """
    print(depth, alpha, beta, isMax)
    valid_columns = []
    for ai_column in range(len(ai_state)):
        if ai_state[ai_column][5] == "X":
            valid_columns.append(ai_column)

    if score_state(ai_state, "A") == 4 or score_state(ai_state, "B") == 4 or depth == 1000 or len(valid_columns) == 0:
        terminal_score = score_state(ai_state, "B") - score_state(ai_state, "A")
        print("Reached terminal node, score is: ", terminal_score)
        return terminal_score, chosen_column

    if isMax:
        best_column = None
        best_value = -float('inf')
        for ai_sim_column in valid_columns:
            next_ai_state, holder_piece = place_piece(ai_state, "B", ai_sim_column)
            if next_ai_state == "Invalid move":
                sel_column = random.choice(valid_columns)
                break
            print("Simulated State:")
            print_game_state(next_ai_state)
            value, sel_column = legacy_minmax_ai_move(next_ai_state, "B", alpha, beta, False, depth + 1, ai_sim_column)
            if value > best_value:
                best_value = value
                best_column = sel_column
            alpha = max(best_value, alpha)
            if beta <= alpha:
                break
        return best_value, best_column
    else:
        best_value = float('inf')
        best_column = None
        for ai_sim_column in valid_columns:
            next_ai_state, holder_piece = place_piece(ai_state, "A", ai_sim_column)
            if next_ai_state == "Invalid move":
                break
            print("Simulated State:", "Score is", score_state(next_ai_state, "B"))
            print_game_state(next_ai_state)
            value, sel_column = legacy_minmax_ai_move(next_ai_state, "A", alpha, beta, True, depth + 1, ai_sim_column)
            if value < best_value:
                best_value = value
                best_column = sel_column
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value, sel_column

    print(best_value)


def minimax_ai_move(minimax_game_state, ai_player, opponent_player, depth, alpha, beta, chosen_col=None, is_max=None):
    # print("Column:", chosen_col)
    # print("Is Max?", is_max)
    # print("Simulated State:")
    # print_game_state(minimax_game_state)

    valid_columns = []
    for choice_column in range(len(minimax_game_state)):
        if minimax_game_state[choice_column][5] == "X":
            valid_columns.append([choice_column, None])

    if depth == 0 or not valid_columns or score_state(minimax_game_state, ai_player) >= 4 or score_state(minimax_game_state, opponent_player) >= 4:
        state_score = score_heuristic(minimax_game_state, ai_player, opponent_player)
        # print("Terminal state reached with score of", state_score)
        return [chosen_col, state_score]

    if is_max:
        max_evaluation = [None, -float('inf')]
        for choice in valid_columns:
            fake_state = deepcopy(minimax_game_state)
            next_ai_state, last_ai_piece = place_piece(fake_state, ai_player, choice[0])
            if next_ai_state == "Invalid move":
                break
            evaluation = minimax_ai_move(next_ai_state, ai_player, opponent_player, depth-1, alpha, beta, choice[0], False)
            if evaluation[1] > max_evaluation[1]:
                max_evaluation = [choice[0],evaluation[1]]
            alpha = max(alpha, max_evaluation[1])
            if beta <= alpha:
                pass
        # print("Propagated chosen max option:", max_evaluation)
        return max_evaluation

    else:
        min_evaluation = [None, float('inf')]
        for choice in valid_columns:
            fake_state = deepcopy(minimax_game_state)
            next_ai_state, last_ai_piece = place_piece(fake_state, opponent_player, choice[0])
            if next_ai_state == "Invalid move":
                break
            evaluation = minimax_ai_move(next_ai_state, ai_player, opponent_player, depth-1, alpha, beta, choice[0], True)
            if evaluation[1] < min_evaluation[1]:
                min_evaluation = [choice[0],evaluation[1]]
            beta = min(beta, min_evaluation[1])
            if beta <= alpha:
                pass
        # print("Propagated chosen min option:", min_evaluation)
        return min_evaluation


def score_heuristic(heuristic_state, cur_player, opp_player):
    cur_player_score = score_state(heuristic_state, cur_player)
    opp_player_score = score_state(heuristic_state, opp_player)
    heuristic_score = cur_player_score-opp_player_score
    # print("cur_player_score", cur_player_score)
    # print("opp_player_score", opp_player_score)
    # print("heuristic_score", heuristic_score)
    if opp_player_score >= 4:
        heuristic_score = -999999
    return heuristic_score


def score_state(scored_state, scored_player):
    """
    Score the state for a given player by using the longest chain that exists in that game state
    """
    score = 0
    for col in range(len(scored_state)):
        for row in range(len(scored_state[col])):
            if scored_state[col][row] == scored_player:
                # Explore up
                up_chain = explore_chain(scored_state, scored_player, (col, row), 1, 0)
                # Explore top right
                top_right_chain = explore_chain(scored_state, scored_player, (col, row), 1, 1)
                # Explore right
                right_chain = explore_chain(scored_state, scored_player, (col, row), 0, 1)
                # Explore bottom right
                bottom_right_chain = explore_chain(scored_state, scored_player, (col, row), -1, 1)
                # Explore down
                down_chain = explore_chain(scored_state, scored_player, (col, row), -1, 0)
                # Explore bottom left
                bottom_left_chain = explore_chain(scored_state, scored_player, (col, row), -1, -1)
                # Explore left
                left_chain = explore_chain(scored_state, scored_player, (col, row), 0, -1)
                # Explore top left
                top_left_chain = explore_chain(scored_state, scored_player, (col, row), 1, -1)
                max_score = max(up_chain, top_right_chain, right_chain, bottom_right_chain, down_chain,
                                bottom_left_chain, left_chain, top_left_chain)
                if max_score > score:
                    score = max_score
            else:
                pass

    return score


def explore_chain(explore_state, explore_player, start_point, vertical, horizontal):
    start_x, start_y = start_point
    chain_length = 1
    while True:
        start_x += horizontal
        start_y += vertical

        if start_x >= len(explore_state) or start_y >= len(explore_state[0]) or start_x < 0 or start_y < 0:
            break
        elif explore_state[start_x][start_y] == explore_player:
            chain_length += 1
        else:
            break
    return chain_length


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
                    minmax_state = deepcopy(game_state)
                    opponent = "A"
                    ai_column, ai_score = minimax_ai_move(minmax_state, current_player, opponent, 4, -float('inf'), float('inf'), None, True)
                    print("AI score:", ai_score)
                    next_state, last_piece = place_piece(game_state, current_player, ai_column)
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
                # print('PLAYER TURNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
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
        print("Current Player", current_player)
        print("Current Player Score:", score_state(game_state, current_player))
        if game_end(game_state, last_piece):
            print(current_player + " wins!")
            break
