# _*_ coding:utf-8 _*_
# FileName: simple_engine.py
# IDE: PyCharm

import random


class Engine(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.shape1 = ""
        self.shape2 = "▇"
        self.chessboard = []

    def login(self, size, shape1, chessboard, x, y):
        self.x = x
        self.y = y
        self.size = size
        self.shape1 = shape1
        if shape1 == "X":
            self.shape2 = "x"
        else:
            self.shape2 = "x"
        self.chessboard = chessboard

    def create_pos(self):
        if (self.chessboard[self.x][self.y] == self.shape1 or
           self.chessboard[self.x][self.y - 1] == self.shape1 or
           self.chessboard[self.x][self.y - 2] == self.shape1 or
           self.chessboard[self.x - 1][self.y] == self.shape1 or
           self.chessboard[self.x - 1][self.y - 2] == self.shape1 or
           self.chessboard[self.x - 2][self.y] == self.shape1 or
           self.chessboard[self.x - 2][self.y - 1] == self.shape1 or
           self.chessboard[self.x - 2][self.y - 2] == self.shape1):
            if self.chessboard[self.x][self.y] == self.shape1:
                if self.chessboard[self.x - 2][self.y - 2] != self.shape1:
                    self.x -= 1
                    self.y -= 1
                    return self.x, self.y
            if self.chessboard[self.x][self.y - 1] == self.shape1:
                if self.chessboard[self.x - 2][self.y - 1] != self.shape1:
                    self.x -= 1
                    return self.x, self.y
            if self.chessboard[self.x][self.y - 2] == self.shape1:
                if self.chessboard[self.x - 2][self.y] != self.shape1:
                    self.x -= 1
                    self.y += 1
                    return self.x, self.y
            if self.chessboard[self.x - 1][self.y] == self.shape1:
                if self.chessboard[self.x - 1][self.y - 2] != self.shape1:
                    self.y -= 1
                    return self.x, self.y
            if self.chessboard[self.x - 1][self.y - 2] == self.shape1:
                if self.chessboard[self.x - 1][self.y] != self.shape1:
                    self.y += 1
                    return self.x, self.y
            if self.chessboard[self.x - 2][self.y] == self.shape1:
                if self.chessboard[self.x][self.y - 2] != self.shape1:
                    self.x += 1
                    self.y -= 1
                    return self.x, self.y
            if self.chessboard[self.x - 2][self.y - 1] == self.shape1:
                if self.chessboard[self.x][self.y - 1] != self.shape1:
                    self.x += 1
                    return self.x, self.y
            if self.chessboard[self.x - 2][self.y - 2] == self.shape1:
                if self.chessboard[self.x][self.y] != self.shape1:
                    self.x += 1
                    self.y += 1
                    return self.x, self.y
        else:
            flag = True
            while flag:
                row = random.randint(-1, 1)
                col = random.randint(-1, 1)
                if (row != 0 or col != 0) and self.chessboard[self.x - row][self.y - col] != self.shape1:
                    self.x = self.x - row
                    self.y = self.y - col
                    flag = False
        return self.x, self.y

    def show_board(self):
        print("  ", end="")
        for i in range(1, self.size + 1):
            print(chr(ord("a") + i - 1), end="")
        print()
        for i in range(1, self.size + 1):
            if i < 10:
                print(" ", end="")
            print(str(i) + self.chessboard[i - 1])


if __name__ == "__main__":
    engine = Engine()
    size = 5
    shape1 = "*"
    chessboard = ["+" * size]
    chessboard = chessboard * size
    engine.login(size, shape1, chessboard, 4, 3)
    engine.show_board()
