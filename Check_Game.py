def check(game_to_check):
    diagonal = []
    reverse_diagonal = []

    for index in range(3):
        line = game_to_check[index]
        column = [row[index] for row in game_to_check]
        diagonal.append(game_to_check[index][index])
        reverse_diagonal.append(game_to_check[index][2 - index])
        players = [1,2]

        for player in players:
            if line.count(player) == 3 or column.count(player) == 3:
                print(f"Congratulations! Player {player} WON!!")
                return True
            elif diagonal.count(player) == 3 or reverse_diagonal.count(player) == 3:
                print(f"Congratulations! Player {player} WON!!")
                return True
    return False

if __name__ == "__main__":
    game_test = [[1, 2, 1], [2, 2, 1], [2, 2, 1]]
    check(game_test)
