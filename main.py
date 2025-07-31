from Check_Game import check
from Game_One import main as game
from Board import board_stock as board

def main():
    scores = {'player1': 0, 'player2': 0}
    game_score = 0
    while True:
        try:
            max_games = int(input(f"Please Tell me the max games you want to play: "))
            break
        except ValueError:
            print("ERROR! NOT VALID INPUT! TRY AGAIN!")

    while True:
        game_matrix = []

        for line in range(3):
            game_matrix.append([0,0,0])
        game_board = board(3)

        for row in game_board:
            print(row)
        is_won = 0

        while is_won == 0:
            for player in [1,2]:
                game_matrix, game_board = game(game_matrix, game_board, player)
                is_won = check(game_matrix)

                if is_won == 0: #No draw/win
                    continue
                elif is_won == -1: #Draw
                    break
                else: #Win
                    scores['player' + str(is_won)] += 1
                    break

        print("-" * 50)
        print(f"The score of Player 1 is: {scores['player1']}")
        print(f"The score of Player 2 is: {scores['player2']}")
        print("-" * 50)
        game_score += 1

        if game_score == max_games:
            if scores['player1'] == scores['player2']:
                print("FINAL - OH NO! IT'S A TIE!")
            else:
                player = max(scores['player1'], scores['player2'])
                print(f"FINAL - Congratulations! Player {player} WON THE GAME!!!")
            return

main()
