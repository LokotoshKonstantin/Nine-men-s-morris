import random
from Task2_3.utils import *
from Task2_3.mill import *

alpha = float('-inf')
beta = float('inf')
depth = 3


class Nine_mens_morris(object):
    def __init__(self):
        self.board = []
        self.turn = None
        self.color_user = None
        self.color_algorithm = None
        self.finish_init_board = False
        self.point_for_next_step = None

    def toss(self):
        """
        Если turn(очередь) = 1, тогда первым ходит алгоритм и является Белыми.
        Если turn(очередь) = -1, тогда ходит пользователь и является Белыми.
        """
        if random.random() > 0.5:
            self.turn = 1
            self.color_algorithm = "W"
            self.color_user = "B"
        else:
            self.turn = -1
            self.color_algorithm = "B"
            self.color_user = "W"

    def choose_init_user(self):
        boardOutput(self.board)
        pos = int(input("\nPlace piece: "))
        while not check_place(self.board, pos):
            print("There is already a piece there")
            pos = int(input("\nPlace piece: "))
        self.board[pos] = self.color_user

    def choose_inti_algorithm(self, i):
        if i == 0:
            pos = random.randrange(0, 23, 1)
            while not check_place(self.board, pos):
                pos = random.randrange(0, 23, 1)
            self.board[pos] = self.color_algorithm
            self.point_for_next_step = pos
        else:
            flag = False
            while not flag:
                x = self.point_for_next_step
                if not close_mill(x, self.board):
                    if get_point_for_mill(x, self.board):
                        self.board[get_point_for_mill(x, self.board)] = self.color_algorithm
                        self.point_for_next_step = x
                        flag = True
                        break
                    else:
                        for t in neighbourhood(x):
                            if self.board[t] == "X":
                                self.board[t] = self.color_algorithm
                                self.point_for_next_step = t
                                flag = True
                                break
                if not flag:
                    pos = random.randrange(0, 23, 1)
                    while not check_place(self.board, pos):
                        pos = random.randrange(0, 23, 1)
                    self.board[pos] = self.color_algorithm
                    self.point_for_next_step = pos
                    flag = True
                    break

    def potentialMillInFormation(self, position, player):
        adjacent_list = neighbourhood(position)
        for i in adjacent_list:
            if self.board[i] == player and not check_mill_formation(position, self.board, player):
                return True
        return False

    def getPiecesInPotentialMillFormation(self, player):
        count = 0
        for i in range(len(self.board)):
            if self.board[i] == player:
                adjacent_list = neighbourhood(i)
                for pos in adjacent_list:
                    if player == self.color_algorithm:
                        if self.board[pos] == self.color_user:
                            self.board[i] = "2"
                            if close_mill(i, self.board):
                                count += 1
                            self.board[i] = player
                    else:
                        if self.board[pos] == "1" and self.potentialMillInFormation(pos, self.color_algorithm):
                            count += 1
        return count

    def AdvancedHeuristic(self):

        evaluation = 0

        numPlayerOneTokens = numOfValue(self.board, self.color_algorithm)
        numPlayerTwoTokens = numOfValue(self.board, self.color_user)

        numPossibleMillsPlayer1 = getPossibleMillCount(self.board, self.color_algorithm)
        numPossibleMillsPlayer2 = getPossibleMillCount(self.board, self.color_user)

        moveablePiecesPlayer1 = 0
        moveablePiecesPlayer2 = 0

        movablePiecesBlack = len(stage23Moves(self.board, self.color_user, self.color_algorithm))

        potentialMillsPlayer1 = self.getPiecesInPotentialMillFormation(self.color_algorithm)
        potentialMillsPlayer2 = self.getPiecesInPotentialMillFormation(self.color_user)

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

    def move_user(self):
        pos = int(input("\nMove piece: "))
        while self.board[pos] != self.color_user:
            pos = int(input("\nMove piece: "))
        userHasPlaced = False
        while not userHasPlaced:
            newPos = int(input("New Location: "))
            if self.board[newPos] == "X":
                self.board[pos] = 'X'
                self.board[newPos] = self.color_user
                if close_mill(newPos, self.board):

                    userHasRemoved = False
                    while not userHasRemoved:
                        pos = int(input("\nRemove piece: "))

                        if self.board[pos] == self.color_algorithm and not close_mill(pos, self.board) or (
                                close_mill(pos, self.board) and numberOfPiecesHeuristic(self.board,
                                                                                        self.color_algorithm,
                                                                                        self.color_user) == 3):
                            self.board[pos] = "X"
                            userHasRemoved = True
                userHasPlaced = True

    def move_algorithm(self):
        self.board = alphaBetaPruning(self.board, depth, False, alpha, beta, False, self.AdvancedHeuristic(),
                                      self.color_user, self.color_algorithm).board

    def Game(self):
        self.toss()
        if self.turn == 1:
            print(" The first goes Algorithm")
        else:
            print(" The first goes User")
        # =========== Stage 1 ======================
        print(" Stage 1: Initial arrangement")
        for i in range(24):
            self.board.append("X")
        for i in range(9):
            if self.turn == 1:
                print("Turn to step Algorithm")
                self.choose_inti_algorithm(i)
                print("Turn to step User")
                self.choose_init_user()
            else:
                print("Turn to step User")
                self.choose_init_user()
                print("Turn to step Algorithm")
                self.choose_inti_algorithm(i)

        self.turn *= -1
        boardOutput(self.board)
        # ==========================================

        # =========== Stage 2 ======================
        print(" Stage 2 : Move Piece")

        finishstate = False
        while not finishstate:
            if self.turn == 1:
                print("Turn to step Algorithm")

            else:
                print("Turn to step User")
                boardOutput(self.board)
                userHasMoved = False
                while not userHasMoved:
                    self.move_user()
                    userHasMoved = True
 
            self.turn *= -1

            # if getEvaluationStage23(self.board, self.color_user, self.color_algorithm) == float('inf'):
            #     print("You Win!")
            #     exit(0)
            #
            # boardOutput(self.board)
            #
            # evaluation = alphaBetaPruning(self.board, 3, False, float('-inf'), float('inf'), False,
            #                               numberOfPiecesHeuristic(self.board, self.color_algorithm, self.color_user),
            #                               self.color_user, self.color_algorithm)
            #
            # if evaluation.evaluator == float('-inf'):
            #     print("You Lost")
            #     exit(0)
            # else:
            #     self.board = evaluation.board

        # ==========================================


a = Nine_mens_morris()
a.Game()
