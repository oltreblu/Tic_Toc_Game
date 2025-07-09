def board_stock(number_of_squares):
    horizontal_line = " ---"
    vertical_line = "|"
    board = []
    for x in range(number_of_squares):
        board.append(horizontal_line * number_of_squares) #This creates the horizontal lines
        board.append((vertical_line + "   ") * number_of_squares + vertical_line) #This creates the vertical lines in one row
    board.append(horizontal_line * number_of_squares) #This creates the last horizontal lines
    return board
def main(do_not_use_this_function_if_using_import):
    while True:
        try:
            n = int(input("Input the size game board (positive integer): "))
            if n >= 0:
                break
            else:
                print("INPUT A POSITIVE INTEGER, RETRY!")
        except ValueError:
            print("ERROR! INPUT NOT VALID! PLEASE INPUT AN INTEGER, RETRY!")
    board = board_stock(n)
    for line in board:
        print(line)
if __name__ == "__main__":
    main(3)