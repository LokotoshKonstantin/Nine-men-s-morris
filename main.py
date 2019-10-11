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
                                close_mill(pos, self.board) and numberOfPiecesHeuristic(self.board, self.color_user,
                                                                                        self.color_algorithm) == 3):
                            self.board[pos] = "X"
                            userHasRemoved = True
                userHasPlaced = True

    def move_algorithm(self):
        evaluation = alphaBetaPruning(self.board, depth, False, alpha, beta, AdvancedHeuristic,
                                      self.color_algorithm, self.color_user)

        if evaluation.evaluator == float('-inf'):
            print("You Lost")
            exit(0)
        else:
            self.board = evaluation.board

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
        self.turn *= -1
        finishstate = False
        t = 0
        while not finishstate:
            print(" Time = "+str(t))
            if self.turn == 1:
                print("Turn to step Algorithm")
                self.move_algorithm()
            else:
                print("Turn to step User")
                boardOutput(self.board)
                userHasMoved = False
                while not userHasMoved:
                    self.move_user()
                    userHasMoved = True
                if getEvaluationStage23(self.board, self.color_algorithm, self.color_user) == float('inf'):
                    print("You Win!")
                    exit(0)
            self.turn *= -1
            t += 1
        # ==========================================


a = Nine_mens_morris()
a.Game()
