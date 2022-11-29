# _*_ coding:utf-8 _*_
# FileName: gobang.py
# IDE: PyCharm

import os
import engine


class GoBang(object):
    def __init__(self):
        self.num = 0
        self.win = True
        self.flag = True
        self.size = 0
        self.pos_x = 0
        self.pos_y = 0
        self.shape1 = ""
        self.shape2 = ""
        self.in_put = ""
        self.board = []

    def create_board(self):
        self.board = [[" +" for col in range(self.size)] for row in range(self.size)]

    def check_pos(self):
        if self.in_put == "":
            self.show_board()
            print("请输入内容！")
        elif self.in_put.count(",") == 1:
            content = self.in_put.split(',')
            if content.count("") != 0:
                self.show_board()
                print("\n执行操作格式有误！")
                self.flag = True
            else:
                if ord(content[1]) in range(65, 65 + self.size):
                    content[1] = chr(ord(content[1]) + 32)
                if content[0].isdigit() and ord(content[1]) in range(97, 97 + self.size):
                    if 1 <= int(content[0]) <= self.size and 1 <= ord(content[1]) - ord("a") + 1 <= self.size:
                        self.pos_x = int(content[0])
                        self.pos_y = ord(content[1]) - ord("a") + 1
                        self.flag = False
                    else:
                        self.show_board()
                        print("\n落子范围有误！")
                        self.flag = True
                else:
                    self.show_board()
                    print("\n执行操作格式有误！")
                    self.flag = True
        else:
            self.show_board()
            print("\n执行操作格式有误！")
            self.flag = True

    def change_board(self, shape):
        if self.board[self.pos_x - 1][self.pos_y - 1] == self.shape1 or self.board[self.pos_x - 1][self.pos_y - 1] == self.shape2:
            self.show_board()
            print("\n此处已有子！\n")
            self.flag = True
        else:
            self.board[self.pos_x - 1][self.pos_y - 1] = shape
            self.flag = False

    def show_board(self):
        print("  ", end="")
        for i in range(1, self.size + 1):
            print(" " + chr(ord("a") + i - 1), end="")
        print()
        for row in range(self.size):
            if row < 9:
                print(" ", end="")
            print(row + 1, end="")
            for col in range(self.size):
                print(self.board[row][col], end="")
            print()

    def check_win(self, shape):
        if self.pos_x < 0 or self.pos_x > self.size or self.pos_y < 0 or self.pos_y > self.size:
            return
        # 上下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            else:
                if self.board[self.pos_x - self.num - 1][self.pos_y - 1] == shape:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            else:
                if self.board[self.pos_x + self.num - 1][self.pos_y - 1] == shape:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.win = False
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape))
        # 左右检测
        self.num = 1
        while True:
            if self.pos_y <= self.num:
                break
            else:
                if self.board[self.pos_x - 1][self.pos_y - self.num - 1] == shape:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.board[self.pos_x - 1][self.pos_y + self.num - 1] == shape:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.win = False
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape))
        # 左上右下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            if self.pos_y <= self.num:
                break
            else:
                if self.board[self.pos_x - self.num - 1][self.pos_y - self.num - 1] == shape:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.board[self.pos_x + self.num - 1][self.pos_y + self.num - 1] == shape:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.win = False
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape))
        # 右上左下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.board[self.pos_x - self.num - 1][self.pos_y + self.num - 1] == shape:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            if self.pos_y <= self.num:
                break
            else:
                if self.board[self.pos_x + self.num - 1][self.pos_y - self.num - 1] == shape:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.win = False
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape))

    def logic(self):
        print("\n欢迎来到五子棋对战系统：")
        while True:
            size = input("\n请输入棋盘大小（在5-26之间）：")
            if not size.isdigit():
                print("\n请输入正确的内容！")
            else:
                self.size = int(size)
                if self.size < 5 or self.size > 26:
                    print("\n请输入正确的棋盘大小！")
                else:
                    self.create_board()
                    print("\n这是初始棋盘：\n")
                    self.show_board()
                    while True:
                        shape1 = input("\n请输入您要用的棋子符号（除了+）：").replace(" ", "")
                        if shape1 == "+":
                            print("\n说了不准用+啦！")
                        elif len(shape1) != 1:
                            print("\n只能输入一个字符噢！")
                        else:
                            self.shape1 = " " + shape1
                            shape2 = input("\n请输入您的对手要用的棋子符号（除了+和您定义的符号）【输入AI选定对手为人工智能】：").replace(" ", "")
                            if shape2 == "+":
                                print("\n说了不准用加号啦！")
                            elif shape2 == shape1:
                                print("\n说了不准用一样的符号啦！")
                            elif shape2.lower() == "ai":
                                self.win = True
                                eg = engine.Engine()
                                self.shape2 = eg.function(self.board, self.size, self.shape1)
                                while self.win:
                                    self.flag = True
                                    while self.flag:
                                        self.in_put = input("\n请输入玩家 {} 要下的位置（数字，字母）：".format(self.shape1)).replace(" ", "").replace("，", ",")
                                        os.system("cls")
                                        self.check_pos()
                                        if not self.flag:
                                            self.change_board(self.shape1)
                                            self.show_board()
                                        self.check_win(self.shape1)
                                    if not self.win:
                                        break
                                    eg.get_pos(self.pos_x, self.pos_y)
                                    eg.judge()
                                    self.pos_x, self.pos_y = eg.action()
                                    os.system("cls")
                                    print("\n电脑 {} 已下的位置：{},{}".format(self.shape2, self.pos_x, chr(self.pos_y + ord("a") - 1)))
                                    self.show_board()
                                    self.check_win(self.shape2)
                                    if not self.win:
                                        break
                            elif len(shape2) != 1:
                                print("\n只能输入一个字符噢！")
                            else:
                                self.shape2 = " " + shape2
                                self.win = True
                                while self.win:
                                    for shape in [self.shape1, self.shape2]:
                                        self.flag = True
                                        while self.flag:
                                            self.in_put = input("\n请输入玩家 {} 要下的位置（数字，字母）：".format(shape)).replace(" ", "").replace("，", ",")
                                            self.check_pos()
                                            if not self.flag:
                                                self.change_board(shape)
                                                self.show_board()
                                                self.check_win(shape)
                                        if not self.win:
                                            break
                        if not self.win:
                            break
                    if not self.win:
                        while True:
                            go_on = input("\n是否继续下棋？（y/n）")
                            if go_on.lower() in ["y", "ye", "yes"]:
                                break
                            elif go_on.lower() in ["n", "no"]:
                                print("\n下棋结束！")
                                quit()
                            else:
                                print("请输入正确的指令！")
                                continue


if __name__ == "__main__":
    gb = GoBang()
    gb.logic()
