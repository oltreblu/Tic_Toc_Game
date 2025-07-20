from Game_One import main as game
from Check_Game import check
from Board import board_stock as board

def main():
    sol = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    game_board = board(3) #Creates a board to play on

    for row1 in game_board:
        print(row1) #Prints the first blank board

    for turn in range(5):
        sol, game_board, is_won_midgame = game(sol, game_board, turn) #Starts the game

        if is_won_midgame: #Checks if it was won mid-game
            return
        is_won = check(sol) #Checks if it was won at the end

        if is_won:
            return

    print("Oh no! It's a Draw!")

main()
