def boardOutput(board):
    print(board[0] + "(00)---------------------- " + board[1] + "(01)---------------------- " + board[2] + "(02)")
    print("|                           |                           |")
    print("|        " + board[8] + "(08)-------------- " + board[9] + "(09)-------------- " + board[10] + "(10)  |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print(
        "|       |         " + board[16] + "(16)----- " + board[17] + "(17)----- " + board[18] + "(18)    |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(board[3] + "(03)--- " + board[11] + "(11)---- " + board[19] + "(19)                " + board[20] + "(20)---- "
          + board[12] + "(12)--- " + board[4] + "(04)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(
        "|       |         " + board[21] + "(21)----- " + board[22] + "(22)----- " + board[23] + "(23)    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print(
        "|        " + board[13] + "(13)-------------- " + board[14] + "(14)-------------- " + board[15] + "(15)  |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(board[5] + "(05)---------------------- " + board[6] + "(06)---------------------- " + board[7] + "(07)")


def check_place(board, pos):
    if board[pos] == "X":
        return True
    else:
        return False
