from Board import board_stock as board
from Check_Game import check

def main(game_to_play_on, board_to_play_on, turn):
    coordinates_player1 = user_input(1, game_to_play_on)
    game_to_play_on[coordinates_player1[0] - 1][coordinates_player1[1] - 1] = 1 #Converts coordinates by player into the coordinates of the game

    board_to_play_on = next_board(game_to_play_on, board_to_play_on) #Creates the next board

    for row in board_to_play_on:
        print(row) #Prints the Board

    is_won = check(game_to_play_on) #Checks if the game was already won
    if (2 * turn) + 1 == 9:
        print("Oh no! IT'S A DRAW!")
        is_won = True
        return game_to_play_on, board_to_play_on, is_won

    if is_won:
        return game_to_play_on, board_to_play_on, is_won

    coordinates_player2 = user_input(2, game_to_play_on)
    game_to_play_on[coordinates_player2[0] - 1][coordinates_player2[1] - 1] = 2

    board_to_play_on = next_board(game_to_play_on, board_to_play_on)

    for row in board_to_play_on:
        print(row)
    return game_to_play_on, board_to_play_on, is_won

def user_input(player, game):
    while True:
        try:
            coordinates_player = input(f'PLAYER {player}: INPUT THE COORDINATES IN THE FORMAT (integer from 1 to 3) "row,column": ').strip().split(",")
            coordinates_player = [int(i) for i in coordinates_player]
            restart_while = False

            for axis in range(2):
                if coordinates_player[axis] < 1 or coordinates_player[axis] > 3:
                    print("ERROR! INPUT NUMBERS BETWEEN 1 TO 3!")
                    restart_while = True
                    break

            if restart_while:
                continue

            elif game[coordinates_player[0] - 1][coordinates_player[1] - 1] == 1 or game[coordinates_player[0] - 1][coordinates_player[1] - 1] == 2:
                #Converts coordinates by player into the coordinates of the game, then checks if it was already written once
                print("ERROR! THERE IS ALREADY A CROSS OR A CIRCLE THERE! TRY AGAIN!")
                continue

            elif len(coordinates_player) != 2:
                print("ERROR! INPUT 2 NUMBERS! TRY AGAIN")
                continue

            break

        except:
            print("ERROR! INPUT NOT VALID! RETRY!")

    return coordinates_player

def next_board(game_matrix, board_to_modify):
    board_column_index = [2, 6, 10] #These are indexes of where the cross, x and o are going to be
    board_row = [1, 3, 5] #These are indexes of where the cross, x and o are going to be

    for game_row in range(3):
        for game_column in range(3):
            board_to_modify[board_row[game_row]] = board_to_modify[board_row[game_row]][:board_column_index[game_column]] + str(game_matrix[game_row][game_column]) + board_to_modify[board_row[game_row]][board_column_index[game_column] + 1:]
            board_to_modify[board_row[game_row]] = board_to_modify[board_row[game_row]].replace("1", "X").replace("2", "O").replace("0", " ")

    return board_to_modify


if __name__ == "__main__":
    initial_board = board(3)

    for row1 in initial_board:
        print(row1)

    main([[0, 0, 0],[0, 0, 0],[0, 0, 0]],initial_board, 0)
