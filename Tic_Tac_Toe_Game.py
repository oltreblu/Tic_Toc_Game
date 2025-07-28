from Check_Game import check
from Game_One import main as game
from Board import board_stock as board

def main():
    scores = {'player1': 0, 'player2': 0}
    while True:
        try:
            max_score = int(input(f"Please Tell me the max score you want to play: "))
            break
        except ValueError:
            print("ERROR! NOT VALID INPUT! TRY AGAIN!")

    while True:
        game_matrix = []
        for line in range(3):
            game_matrix.append([0,0,0])
        game_board = board(3)
        for row in game_board:
            print(row)  # Prints the Board
        is_won = 0
        while is_won == 0:
            for player in [1,2]:
                game_matrix, game_board = game(game_matrix, game_board, player)
                is_won = check(game_matrix)
                if is_won == 0:
                    continue
                elif is_won == -1:
                    break
                else:
                    scores['player' + str(is_won)] += 1
                    break
        print("-" * 50)
        print(f"The score of Player 1 is: {scores['player1']}")
        print(f"The score of Player 2 is: {scores['player2']}")
        print("-" * 50)
        for player, score in scores.items():
            if score == max_score:
                if player == 'player1':
                    print("Congratulations! Player 1 WON!!!")
                else:
                    print("Congratulations! Player 2 WON!!!")
                return

main()
