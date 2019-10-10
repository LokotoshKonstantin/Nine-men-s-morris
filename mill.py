def neighbourhood(pos):
    neighbourhood = [
        [1, 3],
        [0, 2, 9],
        [1, 4],
        [0, 5, 11],
        [2, 7, 12],
        [3, 6],
        [5, 7, 14],
        [4, 6],
        [9, 11],
        [1, 8, 10, 17],
        [9, 12],
        [3, 8, 13, 19],
        [4, 10, 15, 20],
        [11, 14],
        [6, 13, 15, 22],
        [12, 14],
        [17, 19],
        [9, 16, 18],
        [17, 20],
        [11, 16, 21],
        [12, 18, 23],
        [19, 22],
        [21, 23, 14],
        [20, 22]
    ]
    return neighbourhood[pos]


def check_mill_formation(position, board, player):
    mill = [
        (check_mill(player, board, 1, 2) or check_mill(player, board, 3, 5)),
        (check_mill(player, board, 0, 2) or check_mill(player, board, 9, 17)),
        (check_mill(player, board, 0, 1) or check_mill(player, board, 4, 7)),
        (check_mill(player, board, 0, 5) or check_mill(player, board, 11, 19)),
        (check_mill(player, board, 2, 7) or check_mill(player, board, 12, 20)),
        (check_mill(player, board, 0, 3) or check_mill(player, board, 6, 7)),
        (check_mill(player, board, 5, 7) or check_mill(player, board, 14, 22)),
        (check_mill(player, board, 2, 4) or check_mill(player, board, 5, 6)),
        (check_mill(player, board, 9, 10) or check_mill(player, board, 11, 13)),
        (check_mill(player, board, 8, 10) or check_mill(player, board, 1, 17)),
        (check_mill(player, board, 8, 9) or check_mill(player, board, 12, 15)),
        (check_mill(player, board, 3, 19) or check_mill(player, board, 8, 13)),
        (check_mill(player, board, 20, 4) or check_mill(player, board, 10, 15)),
        (check_mill(player, board, 8, 11) or check_mill(player, board, 14, 15)),
        (check_mill(player, board, 13, 15) or check_mill(player, board, 6, 22)),
        (check_mill(player, board, 13, 14) or check_mill(player, board, 10, 12)),
        (check_mill(player, board, 17, 18) or check_mill(player, board, 19, 21)),
        (check_mill(player, board, 1, 9) or check_mill(player, board, 16, 18)),
        (check_mill(player, board, 16, 17) or check_mill(player, board, 20, 23)),
        (check_mill(player, board, 16, 21) or check_mill(player, board, 3, 11)),
        (check_mill(player, board, 12, 4) or check_mill(player, board, 18, 23)),
        (check_mill(player, board, 16, 19) or check_mill(player, board, 22, 23)),
        (check_mill(player, board, 6, 14) or check_mill(player, board, 21, 23)),
        (check_mill(player, board, 18, 20) or check_mill(player, board, 21, 22)),
    ]
    return mill[position]


def check_pair_formation(position, board, player):
    mill = [
        (check_pair(player, board, 1) or check_pair(player, board, 3)),
        (check_pair(player, board, 0) or check_pair(player, board, 9) or check_pair(player, board, 2)),
        (check_pair(player, board, 1) or check_pair(player, board, 4)),
        (check_pair(player, board, 0) or check_pair(player, board, 11) or check_pair(player, board, 5)),
        (check_pair(player, board, 2) or check_pair(player, board, 12) or check_pair(player, board, 7)),
        (check_pair(player, board, 3) or check_pair(player, board, 6)),
        (check_pair(player, board, 5) or check_pair(player, board, 14) or check_pair(player, board, 7)),
        (check_pair(player, board, 4) or check_pair(player, board, 6)),
        (check_pair(player, board, 9) or check_pair(player, board, 11)),
        (check_pair(player, board, 8) or check_pair(player, board, 1) or check_pair(player, board, 10) or check_pair(
            player, board, 17)),
        (check_pair(player, board, 9) or check_pair(player, board, 12)),
        (check_pair(player, board, 3) or check_pair(player, board, 8) or check_pair(player, board, 19) or check_pair(
            player, board, 13)),
        (check_pair(player, board, 20) or check_pair(player, board, 10) or check_pair(player, board, 15) or check_pair(
            player, board, 4)),
        (check_pair(player, board, 11) or check_pair(player, board, 14)),
        (check_pair(player, board, 13) or check_pair(player, board, 6) or check_pair(player, board, 22) or check_pair(
            player, board, 15)),
        (check_pair(player, board, 12) or check_pair(player, board, 14)),
        (check_pair(player, board, 17) or check_pair(player, board, 19)),
        (check_pair(player, board, 9) or check_pair(player, board, 16) or check_pair(player, board, 18)),
        (check_pair(player, board, 17) or check_pair(player, board, 20)),
        (check_pair(player, board, 16) or check_pair(player, board, 11) or check_pair(player, board, 21)),
        (check_pair(player, board, 12) or check_pair(player, board, 18) or check_pair(player, board, 23)),
        (check_pair(player, board, 19) or check_pair(player, board, 22)),
        (check_pair(player, board, 14) or check_pair(player, board, 21) or check_pair(player, board, 23)),
        (check_pair(player, board, 20) or check_pair(player, board, 22)),
    ]
    return mill[position]


def check_third(position, board, player):
    mill = [
        (third(player, board, 1, 2) or third(player, board, 3, 5)),
        (third(player, board, 0, 2) or third(player, board, 9, 17)),
        (third(player, board, 0, 1) or third(player, board, 4, 7)),
        (third(player, board, 0, 5) or third(player, board, 11, 19)),
        (third(player, board, 2, 7) or third(player, board, 12, 20)),
        (third(player, board, 0, 3) or third(player, board, 6, 7)),
        (third(player, board, 5, 7) or third(player, board, 14, 22)),
        (third(player, board, 2, 4) or third(player, board, 5, 6)),
        (third(player, board, 9, 10) or third(player, board, 11, 13)),
        (third(player, board, 8, 10) or third(player, board, 1, 17)),
        (third(player, board, 8, 9) or third(player, board, 12, 15)),
        (third(player, board, 3, 19) or third(player, board, 8, 13)),
        (third(player, board, 20, 4) or third(player, board, 10, 15)),
        (third(player, board, 8, 11) or third(player, board, 14, 15)),
        (third(player, board, 13, 15) or third(player, board, 6, 22)),
        (third(player, board, 13, 14) or third(player, board, 10, 12)),
        (third(player, board, 17, 18) or third(player, board, 19, 21)),
        (third(player, board, 1, 9) or third(player, board, 16, 18)),
        (third(player, board, 16, 17) or third(player, board, 20, 23)),
        (third(player, board, 16, 21) or third(player, board, 3, 11)),
        (third(player, board, 12, 4) or third(player, board, 18, 23)),
        (third(player, board, 16, 19) or third(player, board, 22, 23)),
        (third(player, board, 6, 14) or third(player, board, 21, 23)),
        (third(player, board, 18, 20) or third(player, board, 21, 22)),
    ]
    return mill[position]


def check_pair(player, board, pos):
    if board[pos] == player:
        return True
    return False


def check_mill(player, board, pos1, pos2):
    if board[pos1] == player and board[pos2] == player:
        return True
    return False


def third(player, board, pos1, pos2):
    if board[pos1] == player and board[pos2] == "X":
        return pos2
    elif board[pos2] == player and board[pos1] == "X":
        return pos1
    else:
        return False


def close_mill(position, board):
    player = board[position]
    if player != "X":
        return check_mill_formation(position, board, player)

    return False


def pair_piece(pos, board):
    player = board[pos]
    if player != "X":
        return check_pair_formation(pos, board, player)
    return False


def get_point_for_mill(pos, board):
    player = board[pos]
    if player != "X":
        return check_third(pos, board, player)
