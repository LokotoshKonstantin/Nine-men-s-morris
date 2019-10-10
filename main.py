import random
from Task2_3.utils import *
from Task2_3.mill import *
from collections import deque


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
            print(" Algorithm choose " + str(pos))
        else:
            flag = False
            while not flag:
                x = self.point_for_next_step
                if not close_mill(x, self.board):
                    print(" He these"+str(pair_piece(x, self.board)))
                    if get_point_for_mill(x, self.board):
                        # сделать третий элемент
                        self.board[get_point_for_mill(x, self.board)] = self.color_algorithm
                        self.point_for_next_step = x
                        print(" Algorithm choose " + str(x))
                        flag = True
                        break
                    else:
                        # сделать соседний элемент
                        for t in neighbourhood(x):
                            if self.board[t] == "X":
                                self.board[t] = self.color_algorithm
                                print("x = "+str(x))
                                print("t = " + str(t))
                                self.point_for_next_step = t
                                print(" Algorithm choose " + str(t))
                                flag = True
                                break
                        if not flag:
                            pos = random.randrange(0, 23, 1)
                            while not check_place(self.board, pos):
                                pos = random.randrange(0, 23, 1)
                            self.board[pos] = self.color_algorithm
                            self.point_for_next_step = pos
                            print(" Algorithm choose " + str(pos))
                            flag = True
                            break

    def Game(self):
        # Жеребьевка
        self.toss()
        if self.turn == 1:
            print(" The first goes Algorithm")
        else:
            print(" The first goes User")

        # Начальная расстановка
        print(" Stage 1: Initial arrangement")
        for i in range(24):
            self.board.append("X")
        for i in range(9):
            if self.turn == 1:
                # Первым ходит алгоритм
                print("Turn to step Algorithm")
                # Ход делает алгоритм
                self.choose_inti_algorithm(i)
                print("Turn to step User")
                self.choose_init_user()

            else:
                # Первым ходит пользователь
                print("Turn to step User")
                self.choose_init_user()
                print("Turn to step Algorithm")
                self.choose_inti_algorithm(i)

        self.turn *= -1
        boardOutput(self.board)
        print(" Stage 2 : Move Piece")


a = Nine_mens_morris()
a.Game()