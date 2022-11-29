# _*_ coding:utf-8 _*_
# FileName: engine.py
# IDE: PyCharm

import random


class Engine(object):
    def __init__(self):
        self.num = 0
        self.size = 0
        self.flag = 0
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = 0
        self.flag4 = 0
        self.pos_x = 0
        self.pos_y = 0
        self.count = 0
        self.space = 0
        self.ai = 0
        self.shape_list = [" " + chr(index) for index in range(65, 91)]
        self.shape1 = ""
        self.shape2 = ""
        self.board = []

    def judge(self):
        eg = Engine()
        if self.pos_x < 0 or self.pos_x > self.size or self.pos_y < 0 or self.pos_y > self.size:
            return
        # 上下检测
        self.ai = 0
        self.num = 1
        self.count = 0
        self.flag1 = 0
        self.space = 0
        self.flag = 1
        while True:
            if self.pos_x <= self.count + 1:
                break
            else:
                self.count += 1
                if self.board[self.pos_x - self.count - 1][self.pos_y - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x - self.count - 1][self.pos_y - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        eg.pass_chess()
        self.count = 0
        self.space = 0
        while True:
            if self.pos_x + self.count + 1 > self.size:
                break
            else:
                self.count += 1
                if self.board[self.pos_x + self.count - 1][self.pos_y - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x + self.count - 1][self.pos_y - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        # 判断棋子个数
        if self.num == 4:
            self.flag1 = 4
        elif self.num == 3:
            self.flag1 = 3
        elif self.num == 2:
            self.flag1 = 2
        eg.pass_chess()
        # 左右检测
        self.ai = 0
        self.num = 1
        self.count = 0
        self.flag2 = 0
        self.space = 0
        self.flag = 2
        while True:
            if self.pos_y <= self.count + 1:
                break
            else:
                self.count += 1
                if self.board[self.pos_x - 1][self.pos_y - self.count - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x - 1][self.pos_y - self.count - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        eg.pass_chess()
        self.count = 0
        self.space = 0
        while True:
            if self.pos_y + self.count + 1 > self.size:
                break
            else:
                self.count += 1
                if self.board[self.pos_x - 1][self.pos_y + self.count - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x - 1][self.pos_y + self.count - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        # 判断棋子个数
        if self.num == 4:
            self.flag2 = 4
        elif self.num == 3:
            self.flag2 = 3
        elif self.num == 2:
            self.flag2 = 2
        eg.pass_chess()
        # 左上右下检测
        self.ai = 0
        self.num = 1
        self.count = 0
        self.flag3 = 0
        self.space = 0
        self.flag = 3
        while True:
            if self.pos_x <= self.count + 1:
                break
            if self.pos_y <= self.count + 1:
                break
            else:
                self.count += 1
                if self.board[self.pos_x - self.count - 1][self.pos_y - self.count - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x - self.count - 1][self.pos_y - self.count - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        eg.pass_chess()
        self.count = 0
        self.space = 0
        while True:
            if self.pos_x + self.count + 1 > self.size:
                break
            if self.pos_y + self.count + 1 > self.size:
                break
            else:
                self.count += 1
                if self.board[self.pos_x + self.count - 1][self.pos_y + self.count - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x + self.count - 1][self.pos_y + self.count - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        # 判断棋子个数
        if self.num == 4:
            self.flag3 = 4
        elif self.num == 3:
            self.flag3 = 3
        elif self.num == 2:
            self.flag3 = 2
        eg.pass_chess()
        # 右上左下检测
        self.ai = 0
        self.num = 1
        self.count = 0
        self.flag4 = 0
        self.space = 0
        self.flag = 4
        while True:
            if self.pos_x <= self.count + 1:
                break
            if self.pos_y + self.count + 1 > self.size:
                break
            else:
                self.count += 1
                if self.board[self.pos_x - self.count - 1][self.pos_y + self.count - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x - self.count - 1][self.pos_y + self.count - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        eg.pass_chess()
        self.count = 0
        self.space = 0
        while True:
            if self.pos_x + self.count + 1 > self.size:
                break
            if self.pos_y <= self.count + 1:
                break
            else:
                self.count += 1
                if self.board[self.pos_x + self.count - 1][self.pos_y - self.count - 1] == self.shape1:
                    self.num += 1
                elif self.board[self.pos_x + self.count - 1][self.pos_y - self.count - 1] == self.shape2:
                    self.ai += 1
                    break
                else:
                    self.space += 1
        # 判断棋子个数
        if self.num == 4:
            self.flag4 = 4
        elif self.num == 3:
            self.flag4 = 3
        elif self.num == 2:
            self.flag4 = 2
        eg.pass_chess()

    def action(self):
        if self.flag1 == 4:
            for pos in range(0, 5):
                if 0 < self.pos_x - pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y - 1] == " +":
                        self.pos_x -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 4):
                if 0 < self.pos_x + pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y - 1] == " +":
                        self.pos_x += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag2 == 4:
            for pos in range(0, 5):
                if 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x - 1][self.pos_y - pos - 1] == " +":
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 4):
                if 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x - 1][self.pos_y + pos - 1] == " +":
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag3 == 4:
            for pos in range(0, 5):
                if 0 < self.pos_x - pos <= self.size and 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y - pos - 1] == " +":
                        self.pos_x -= pos
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 4):
                if 0 < self.pos_x + pos <= self.size and 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y + pos - 1] == " +":
                        self.pos_x += pos
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag4 == 4:
            for pos in range(0, 5):
                if 0 < self.pos_x + pos <= self.size and 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y - pos - 1] == " +":
                        self.pos_x += pos
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 4):
                if 0 < self.pos_x - pos <= self.size and 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y + pos - 1] == " +":
                        self.pos_x -= pos
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag1 == 3:
            for pos in range(0, 4):
                if 0 < self.pos_x - pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y - 1] == " +":
                        self.pos_x -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 3):
                if 0 < self.pos_x + pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y - 1] == " +":
                        self.pos_x += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag2 == 3:
            for pos in range(0, 4):
                if 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x - 1][self.pos_y - pos - 1] == " +":
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 3):
                if 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x - 1][self.pos_y + pos - 1] == " +":
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag3 == 3:
            for pos in range(0, 4):
                if 0 < self.pos_x - pos <= self.size and 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y - pos - 1] == " +":
                        self.pos_x -= pos
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 3):
                if 0 < self.pos_x + pos <= self.size and 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y + pos - 1] == " +":
                        self.pos_x += pos
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag4 == 3:
            for pos in range(0, 4):
                if 0 < self.pos_x + pos <= self.size and 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y - pos - 1] == " +":
                        self.pos_x += pos
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 3):
                if 0 < self.pos_x - pos <= self.size and 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y + pos - 1] == " +":
                        self.pos_x -= pos
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag1 == 2:
            for pos in range(0, 3):
                if 0 < self.pos_x - pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y - 1] == " +":
                        self.pos_x -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 2):
                if 0 < self.pos_x + pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y - 1] == " +":
                        self.pos_x += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag2 == 2:
            for pos in range(0, 3):
                if 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x - 1][self.pos_y - pos - 1] == " +":
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 2):
                if 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x - 1][self.pos_y + pos - 1] == " +":
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag3 == 2:
            for pos in range(0, 3):
                if 0 < self.pos_x - pos <= self.size and 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y - pos - 1] == " +":
                        self.pos_x -= pos
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 2):
                if 0 < self.pos_x + pos <= self.size and 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y + pos - 1] == " +":
                        self.pos_x += pos
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        elif self.flag4 == 2:
            for pos in range(0, 3):
                if 0 < self.pos_x + pos <= self.size and 0 < self.pos_y - pos <= self.size:
                    if self.board[self.pos_x + pos - 1][self.pos_y - pos - 1] == " +":
                        self.pos_x += pos
                        self.pos_y -= pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
            for pos in range(0, 2):
                if 0 < self.pos_x - pos <= self.size and 0 < self.pos_y + pos <= self.size:
                    if self.board[self.pos_x - pos - 1][self.pos_y + pos - 1] == " +":
                        self.pos_x -= pos
                        self.pos_y += pos
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        else:
            while True:
                x = random.choice([-1, 1])
                y = random.choice([-1, 1])
                if 0 < self.pos_x - x <= self.size and 0 < self.pos_y - y <= self.size:
                    if self.board[self.pos_x - x - 1][self.pos_y - y - 1] == " +":
                        self.pos_x -= x
                        self.pos_y -= y
                        self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                        return self.pos_x, self.pos_y
        return self.action()

    def pass_chess(self):
        if self.ai == 0:
            if self.flag == 1:
                if self.flag1 == 3:
                    self.flag2 = 0
                    self.flag3 = 0
                    self.flag4 = 0
            elif self.flag == 2:
                if self.flag2 == 3:
                    self.flag1 = 0
                    self.flag3 = 0
                    self.flag4 = 0
            elif self.flag == 3:
                if self.flag3 == 3:
                    self.flag1 = 0
                    self.flag2 = 0
                    self.flag4 = 0
            elif self.flag == 4:
                if self.flag4 == 3:
                    self.flag1 = 0
                    self.flag2 = 0
                    self.flag3 = 0
            return
        if self.space == 1:
            for xx in [-2, 0, 2]:
                for yy in [-2, 0, 2]:
                    if xx != 0 or yy != 0:
                        if 0 < self.pos_x - xx <= self.size and 0 < self.pos_y - yy <= self.size:
                            if self.board[self.pos_x - xx - 1][self.pos_y - yy - 1] == self.shape1:
                                self.pos_x -= int(xx/2)
                                self.pos_y -= int(yy/2)
                                self.board[self.pos_x - 1][self.pos_y - 1] = self.shape2
                                return self.pos_x, self.pos_y

    def get_pos(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def function(self, board, size, shape):
        self.size = size
        if shape in self.shape_list:
            self.shape_list.pop(self.shape_list.index(shape))
        self.shape1 = shape
        self.shape2 = random.choice(self.shape_list)
        self.board = board
        return self.shape2
