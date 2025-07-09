import Game_One as game
import Check_Game as check
import Board as board_import
def main():
    sol = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    board = board_import.board_stock(3) #Creates a board to play on
    for i in game.odd(7):
        board[i] = board[i].replace("   "," 0 ") #Initializing the board to be played on Tic-Tac-Toe
    for row1 in board:
        print(row1) #Prints the first blank board
    while True:
        sol, board, is_won_midgame = game.main(sol,board) #Starts the game
        if is_won_midgame: #Checks if it was won mid-game
            return
        is_won = check.main(sol) #checks if it was won at the end
        if is_won:
            return
main()