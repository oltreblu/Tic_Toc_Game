def main(game_to_play_on, board_to_play_on, player):
    coordinates_player = user_input(player, game_to_play_on)
    game_to_play_on[coordinates_player[0] - 1][coordinates_player[1] - 1] = player #Converts coordinates by player into the coordinates of the game

    board_to_play_on = next_board(game_to_play_on, board_to_play_on) #Creates the next board

    for row in board_to_play_on:
        print(row) #Prints the Board
    return game_to_play_on, board_to_play_on

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

            elif (game[coordinates_player[0] - 1][coordinates_player[1] - 1] == 1
                  or game[coordinates_player[0] - 1][coordinates_player[1] - 1] == 2):
                #Converts coordinates by player into the coordinates of the game, then checks if it was already written
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
    board_column_index = [2, 6, 10] #These are columns of where the cross, x and o are going to be
    board_row = [1, 3, 5] #These are rows of where the cross, x and o are going to be

    for game_row in range(3):
        for game_column in range(3):
            board_to_modify[board_row[game_row]] = board_to_modify[board_row[game_row]][:board_column_index[game_column]] + str(game_matrix[game_row][game_column]) + board_to_modify[board_row[game_row]][board_column_index[game_column] + 1:]
            #Replaces the blank spaces with 1, 2 or 0.
            board_to_modify[board_row[game_row]] = board_to_modify[board_row[game_row]].replace("1", "X").replace("2", "O").replace("0", " ")

    return board_to_modify
