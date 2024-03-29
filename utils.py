import copy
from Task2_3.mill import *

pruned = 0
states_reached = 0


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


class evaluator:
    def __init__(self):
        self.evaluator = 0
        self.board = []


def InvertedBoard(board, color_user, color_algorithm):
    invertedboard = []
    for i in board:
        if i == color_algorithm:
            invertedboard.append(color_user)
        elif i == color_user:
            invertedboard.append(color_algorithm)
        else:
            invertedboard.append("X")
    return invertedboard


def generateInvertedBoardList(pos_list, color_user, color_algorithm):
    result = []
    for i in pos_list:
        result.append(InvertedBoard(i, color_user, color_algorithm))
    return result


def removePiece(board_clone, board_list, color_user):
    for i in range(len(board_clone)):
        if board_clone[i] == color_user:
            if not close_mill(i, board_clone):
                new_board = copy.deepcopy(board_clone)
                new_board[i] = "X"
                board_list.append(new_board)
    return board_list


def numOfValue(board, value):
    return board.count(value)


def getPossibleMillCount(board, player):
    count = 0
    for i in range(len(board)):
        if board[i] == "X":
            if check_mill_formation(i, board, player):
                count += 1
    return count


def stage3Moves(board, color_user, color_algorithm):
    board_list = []
    for i in range(len(board)):
        if board[i] == color_algorithm:
            for j in range(len(board)):
                if board[j] == "X":
                    board_clone = copy.deepcopy(board)
                    board_clone[i] = "X"
                    board_clone[j] = color_algorithm
                    if close_mill(j, board_clone):
                        board_list = removePiece(board_clone, board_list, color_user)
                    else:
                        board_list.append(board_clone)
    return board_list


def stage2Moves(board, color_user, color_algorithm):
    board_list = []
    for i in range(len(board)):
        if board[i] == color_algorithm:
            adjacent_list = neighbourhood(i)
            for pos in adjacent_list:
                if board[pos] == "X":
                    board_clone = copy.deepcopy(board)
                    board_clone[i] = "X"
                    board_clone[pos] = color_algorithm
                    if close_mill(pos, board_clone):
                        board_list = removePiece(board_clone, board_list, color_user)
                    else:
                        board_list.append(board_clone)
    return board_list


def stage23Moves(board, color_user, color_algorithm):
    if numOfValue(board, color_algorithm) == 3:
        return stage3Moves(board, color_user, color_algorithm)
    else:
        return stage2Moves(board, color_user, color_algorithm)


def numberOfPiecesHeuristic(board, color_user, color_algorithm):
    numPlayerOneTokens = numOfValue(board, color_algorithm)
    numPlayerTwoTokens = numOfValue(board, color_user)
    movablePiecesBlack = len(stage23Moves(board, color_user, color_algorithm))
    if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
        evaluation = float('inf')
    elif numPlayerOneTokens <= 2:
        evaluation = float('-inf')
    else:
        evaluation = 200 * (numPlayerOneTokens - numPlayerTwoTokens)
    return evaluation


def getEvaluationStage23(board, color_user, color_algorithm):
    numWhitePieces = numOfValue(board, color_algorithm)
    numBlackPieces = numOfValue(board, color_user)
    mills = getPossibleMillCount(board, color_algorithm)
    evaluation = 0
    board_list = stage23Moves(board, color_user, color_algorithm)
    numBlackMoves = len(board_list)
    if numBlackPieces <= 2 or numBlackPieces == 0:
        return float('inf')
    elif numWhitePieces <= 2:
        return float('-inf')
    else:
        return 0


def alphaBetaPruning(board, depth, player1, alpha, beta, heuristic, color_user, color_algorithm):
    finalEvaluation = evaluator()
    global states_reached
    states_reached += 1
    if depth != 0:
        currentEvaluation = evaluator()
        if player1:
            possible_configs = stage23Moves(board, color_user, color_algorithm)
        else:
            possible_configs = generateInvertedBoardList(stage23Moves(InvertedBoard(board, color_user, color_algorithm),
                                                                      color_user, color_algorithm),
                                                         color_user, color_algorithm)
        for move in possible_configs:
            if player1:
                currentEvaluation = alphaBetaPruning(move, depth - 1, False, alpha, beta, heuristic,
                                                     color_user, color_algorithm)
                if currentEvaluation.evaluator > alpha:
                    alpha = currentEvaluation.evaluator
                    finalEvaluation.board = move
            else:
                currentEvaluation = alphaBetaPruning(move, depth - 1, True, alpha, beta, heuristic,
                                                     color_user, color_algorithm)
                if currentEvaluation.evaluator < beta:
                    beta = currentEvaluation.evaluator
                    finalEvaluation.board = move
            if alpha >= beta:
                global pruned
                pruned += 1
                break
        if player1:
            finalEvaluation.evaluator = alpha
        else:
            finalEvaluation.evaluator = beta
    else:
        if player1:
            finalEvaluation.evaluator = heuristic(board, color_user, color_algorithm)
        else:
            finalEvaluation.evaluator = heuristic(InvertedBoard(board, color_user, color_algorithm),
                                                  color_user, color_algorithm)

    return finalEvaluation


def AdvancedHeuristic(board, color_user, color_algorithm):
    evaluation = 0
    numPlayerOneTokens = numOfValue(board, color_algorithm)
    numPlayerTwoTokens = numOfValue(board, color_user)
    numPossibleMillsPlayer1 = getPossibleMillCount(board, color_algorithm)
    numPossibleMillsPlayer2 = getPossibleMillCount(board, color_user)
    moveablePiecesPlayer1 = 0
    moveablePiecesPlayer2 = 0
    movablePiecesBlack = len(stage23Moves(board, color_user, color_algorithm))
    potentialMillsPlayer1 = getPiecesInPotentialMillFormation(board, color_algorithm, color_user, color_algorithm)
    potentialMillsPlayer2 = getPiecesInPotentialMillFormation(board, color_user, color_user, color_algorithm)
    if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
        evaluation = float('inf')
    elif numPlayerOneTokens <= 2:
        evaluation = float('-inf')
    else:
        if numPlayerOneTokens < 4:
            evaluation += 100 * numPossibleMillsPlayer1
            evaluation += 200 * potentialMillsPlayer2
        else:
            evaluation += 200 * numPossibleMillsPlayer1
            evaluation += 100 * potentialMillsPlayer2
        evaluation -= 25 * movablePiecesBlack
        evaluation += 50 * (numPlayerOneTokens - numPlayerTwoTokens)

    return evaluation


def getPiecesInPotentialMillFormation(board, player, color_user, color_algorithm):
    count = 0
    for i in range(len(board)):
        if board[i] == player:
            adjacent_list = neighbourhood(i)
            for pos in adjacent_list:
                if player == color_algorithm:
                    if board[pos] == color_user:
                        board[i] = color_user
                        if close_mill(i, board):
                            count += 1
                        board[i] = player
                else:
                    if board[pos] == color_algorithm and potentialMillInFormation(pos, board, color_algorithm):
                        count += 1
    return count


def potentialMillInFormation(position, board, player):
    adjacent_list = neighbourhood(position)
    for i in adjacent_list:
        if (board[i] == player) and (not check_mill_formation(position, board, player)):
            return True
    return False
