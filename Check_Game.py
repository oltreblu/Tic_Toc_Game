def check(game_to_check):
    diagonal = []
    reverse_diagonal = []
    players = [1, 2]

    for index in range(3):
        line = game_to_check[index]
        column = [row[index] for row in game_to_check]
        diagonal.append(game_to_check[index][index])
        reverse_diagonal.append(game_to_check[index][2 - index])

        for player in players:
            if line.count(player) == 3 or column.count(player) == 3:
                print(f"Congratulations! Player {player} WON!!")
                return player

    for player in players:
        if diagonal.count(player) == 3 or reverse_diagonal.count(player) == 3:
            print(f"Congratulations! Player {player} WON!!")
            return player


    line_count = 0
    for line in game_to_check:
        if 0 not in line:
            line_count += 1

    if line_count == 3:
        print(f"Oh no! It's a DRAW!!")
        return -1

    return 0

if __name__ == "__main__":
    game_test = [[1, 2, 1], [2, 1, 1], [2, 1, 2]]
    check(game_test)
