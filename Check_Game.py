def main(game_to_check):
    diag = []
    diag_2 = []

    for index in range(3):
        line = game_to_check[index]
        column = [row[index] for row in game_to_check]
        diag.append(game_to_check[index][index])
        diag_2.append(game_to_check[index][2 - index])

        for player in range(1,3):
            if line.count(player) == 3 or column.count(player) == 3:
                print(f"Congratulations! Player {player} WON!!")
                return True

    for player in range(1,3):
        if diag.count(player) == 3 or diag_2.count(player) == 3:
            print(f"Congratulations! Player {player} WON!!")
            return True

    else:
        return False

if __name__ == "__main__":
    game_test = [[2, 1, 1], [2, 1, 0], [2, 0, 1]]
    main(game_test)
