import Board as board_import
import Check_Game as check
def main(game_to_play_on, board_to_play_on, turn):
    board_column_index = [2, 6, 10] #These are indexes of where the cross, x and o are going to be
    board_row = [1, 3, 5, 7] #These are indexes of where the cross, x and o are going to be
    coordinates_player1 = user_input(1, game_to_play_on)
    game_to_play_on[coordinates_player1[0] - 1][coordinates_player1[1] - 1] = 1 #Converts coordinates by player into the coordinates of the game
    for game_row in range(3):
        for game_column in range(3):
            board_to_play_on[board_row[game_row]] = board_to_play_on[board_row[game_row]][:board_column_index[game_column]] + str(game_to_play_on[game_row][game_column]) + board_to_play_on[board_row[game_row]][board_column_index[game_column] + 1:]
            board_to_play_on[board_row[game_row]] = board_to_play_on[board_row[game_row]].replace("1", "X").replace("2", "O")
    for row in board_to_play_on:
        print(row) #Prints the Board
    is_won = check.main(game_to_play_on) #Checks if the game was already won
    if (2 * turn) + 1 == 9:
        print("Oh no! IT'S A DRAW!")
        is_won = True
        return game_to_play_on, board_to_play_on, is_won
    if is_won:
        return game_to_play_on, board_to_play_on, is_won
    coordinates_player2 = user_input(2, game_to_play_on)
    game_to_play_on[coordinates_player2[0] - 1][coordinates_player2[1] - 1] = 2
    for game_row in range(3):
        for game_column in range(3):
            board_to_play_on[board_row[game_row]] = board_to_play_on[board_row[game_row]][:board_column_index[game_column]] + str(game_to_play_on[game_row][game_column]) + board_to_play_on[board_row[game_row]][board_column_index[game_column] + 1:]
            board_to_play_on[board_row[game_row]] = board_to_play_on[board_row[game_row]].replace("1", "X").replace("2", "O")
    for row in board_to_play_on:
        print(row)
    return game_to_play_on, board_to_play_on, is_won

def odd(n): #A simple function for odd numbers
    return [i for i in range(n) if i % 2 != 0]

def user_input(player, game):
    while True:
        try:
            coordinates_player = input(f'PLAYER {player}: INPUT THE COORDINATES IN THE FORMAT (integer from 1 to 3) "row,column": ').strip().split(",")
            coordinates_player = [int(i) for i in coordinates_player]
            if game[coordinates_player[0] - 1][coordinates_player[1] - 1] == 1 or game[coordinates_player[0] - 1][coordinates_player[1] - 1] == 2:
            #Converts coordinates by player into the coordinates of the game, then checks if it was already written once
                print("ERROR! THERE IS ALREADY A CROSS OR A CIRCLE THERE! TRY AGAIN!")
                continue
            elif len(coordinates_player) != 2:
                print("ERROR! INPUT 2 NUMBERS! TRY AGAIN")
                continue
            break
        except:
            print("ERROR! INPUT NOT VALID! RETRY!")
            continue
    return coordinates_player

if __name__ == "__main__":
    initial_board = board_import.board_stock(3)
    for i in odd(7):
        initial_board[i] = initial_board[i].replace("   "," 0 ")
    for row1 in initial_board:
        print(row1)
    main([[0, 0, 0],[0, 0, 0],[0, 0, 0]],initial_board, 0)
