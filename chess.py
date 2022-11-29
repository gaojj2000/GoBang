# _*_ coding:utf-8 _*_
# FileName: chess.py
# IDE: PyCharm

from simple_engine import Engine


class Chessboard(object):
    def __init__(self):
        self.chessboard = []
        self.pos_x = 0
        self.pos_y = 0
        self.size = size
        self.flag = True
        self.flag0 = True
        self.flag1 = True
        self.flag2 = True
        self.shape1 = ""
        self.shape2 = ""
        self.pos_input1 = ""
        self.pos_input2 = ""
        self.num = 1

    def rem_shape(self):
        self.shape1 = shape1
        self.shape2 = shape2

    def return_flag(self):
        return self.flag

    def return_flag0(self):
        return self.flag0

    def return_flag1(self):
        return self.flag1

    def return_flag2(self):
        return self.flag2

    def create_board(self):
        self.chessboard.append("+" * size)
        self.chessboard = self.chessboard * size

    def show_board(self):
        print("  ", end="")
        for i in range(1, self.size + 1):
            print(chr(ord("a") + i - 1), end="")
        print()
        for i in range(1, self.size + 1):
            if i < 10:
                print(" ", end="")
            print(str(i) + self.chessboard[i - 1])

    def get_pos1(self):
        if len(pos_input1.split(",")) < 2:
            print("请输入正确的内容！")
        else:
            self.pos_input1 = pos_input1
            if self.pos_input1.split(",")[0].isdigit():
                self.pos_x = int(self.pos_input1.split(",")[0])
                self.pos_y = ord(self.pos_input1.split(",")[1]) - ord("a") + 1
                chess.go_chess_shape1()
                chess.show_board()
                chess.check_shape1_win()
            else:
                print("\n您输入的操作有误！")

    def get_pos2(self):
        if len(pos_input1.split(",")) < 2:
            print("请输入正确的内容！")
        else:
            self.pos_input2 = pos_input2
            if self.pos_input2.split(",")[0].isdigit():
                self.pos_x = int(self.pos_input2.split(",")[0])
                self.pos_y = ord(self.pos_input2.split(",")[1]) - ord("a") + 1
                chess.go_chess_shape2()
                chess.show_board()
                chess.check_shape2_win()
            else:
                print("\n您输入的操作有误！")

    def go_chess_shape1(self):
        if self.pos_x < 0 or self.pos_x > size or self.pos_y < 0 or self.pos_y > size:
            print("\n数据过界！\n")
            self.flag1 = True
        elif self.chessboard[self.pos_x - 1][self.pos_y - 1: self.pos_y] != "+":
            print("\n此处已有子！\n")
            self.flag1 = True
        else:
            self.flag1 = False
            if self.pos_y != self.size:
                self.chessboard[self.pos_x - 1] = self.chessboard[self.pos_x - 1][0: self.pos_y - 1] + self.shape1 + self.chessboard[self.pos_x - 1][self.pos_y - self.size:]
            else:
                self.chessboard[self.pos_x - 1] = self.chessboard[self.pos_x - 1][0: self.pos_y - 1] + self.shape1

    def go_chess_shape2(self):
        if self.pos_x < 0 or self.pos_x > size or self.pos_y < 0 or self.pos_y > size:
            print("\n数据过界！\n")
            self.flag2 = True
        elif self.chessboard[self.pos_x - 1][self.pos_y - 1: self.pos_y] != "+":
            print("\n此处已有子！\n")
            self.flag2 = True
        else:
            self.flag2 = False
            if self.pos_y != self.size:
                self.chessboard[self.pos_x - 1] = self.chessboard[self.pos_x - 1][0: self.pos_y - 1] + self.shape2 + self.chessboard[self.pos_x - 1][self.pos_y - self.size:]
            else:
                self.chessboard[self.pos_x - 1] = self.chessboard[self.pos_x - 1][0: self.pos_y - 1] + self.shape2

    def check_shape1_win(self):
        if self.pos_x < 0 or self.pos_x > size or self.pos_y < 0 or self.pos_y > size:
            return
        # 上下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            else:
                if self.chessboard[self.pos_x - self.num - 1][self.pos_y - 1] == shape1:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x + self.num - 1][self.pos_y - 1] == shape1:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape1))
        # 左右检测
        self.num = 1
        while True:
            if self.pos_y <= self.num:
                break
            else:
                if self.chessboard[self.pos_x - 1][self.pos_y - self.num - 1] == shape1:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x - 1][self.pos_y + self.num - 1] == shape1:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape1))
        # 左上右下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            if self.pos_y <= self.num:
                break
            else:
                if self.chessboard[self.pos_x - self.num - 1][self.pos_y - self.num - 1] == shape1:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x + self.num - 1][self.pos_y + self.num - 1] == shape1:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape1))
        # 右上左下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x - self.num - 1][self.pos_y + self.num - 1] == shape1:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            if self.pos_y <= self.num:
                break
            else:
                if self.chessboard[self.pos_x + self.num - 1][self.pos_y - self.num - 1] == shape1:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape1))

    def check_shape2_win(self):
        if self.pos_x < 0 or self.pos_x > size or self.pos_y < 0 or self.pos_y > size:
            return
        # 上下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            else:
                if self.chessboard[self.pos_x - self.num - 1][self.pos_y - 1] == shape2:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x + self.num - 1][self.pos_y - 1] == shape2:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape2))
        # 左右检测
        self.num = 1
        while True:
            if self.pos_y <= self.num:
                break
            else:
                if self.chessboard[self.pos_x - 1][self.pos_y - self.num - 1] == shape2:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x - 1][self.pos_y + self.num - 1] == shape2:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape2))
        # 左上右下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            if self.pos_y <= self.num:
                break
            else:
                if self.chessboard[self.pos_x - self.num - 1][self.pos_y - self.num - 1] == shape2:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x + self.num - 1][self.pos_y + self.num - 1] == shape2:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape2))
        # 右上左下检测
        self.num = 1
        while True:
            if self.pos_x <= self.num:
                break
            if self.pos_y + self.num > self.size:
                break
            else:
                if self.chessboard[self.pos_x - self.num - 1][self.pos_y + self.num - 1] == shape2:
                    self.num += 1
                else:
                    break
        while True:
            if self.pos_x + self.num > self.size:
                break
            if self.pos_y <= self.num:
                break
            else:
                if self.chessboard[self.pos_x + self.num - 1][self.pos_y - self.num - 1] == shape2:
                    self.num += 1
                else:
                    break
        # 判断输赢
        if self.num == 5:
            self.flag = False
            print("\n使用 {} 的用户赢了！".format(shape2))

    def ai(self):
        self.shape2 = "X"
        engine = Engine()
        engine.login(self.size, self.shape1, self.chessboard, self.pos_x, self.pos_y)
        self.pos_x, self.pos_y = engine.create_pos()
        print("\n电脑 X 已下的位置：{},{}".format(self.pos_x, chr(self.pos_y + ord("a") - 1)))
        chess.go_chess_shape2()
        chess.show_board()
        chess.check_shape2_win()


if __name__ == "__main__":
    print("\n欢迎使用五子棋下棋系统：")
    while True:
        print("\n进入新棋局：")
        connect = input("\n请输入棋盘大小（大于4不超过26）：").replace(" ", "")
        if not connect.isdigit():
            print("\n请输入正确的内容！")
        else:
            size = int(connect)
            if size < 5 or size > 26:
                print("\n说了棋盘不能太小或太大！")
            else:
                chess = Chessboard()
                chess.create_board()
                print("\n初始五子棋棋盘：")
                chess.show_board()
                flag0 = chess.return_flag0()
                while flag0:
                    shape1 = input("\n请输入您要用的棋子符号（除了+）：").replace(" ", "")
                    if shape1 == "+":
                        print("\n说了不准用加号啦！")
                    elif len(shape1) != 1:
                        print("\n仅能输入一个字符哈！")
                    else:
                        shape2 = input("\n请输入对手要用的棋子符号（除了+和您定义的符号）【输入AI选定对手为人工智能】：").replace(" ", "")
                        if shape2 == "+":
                            print("\n说了不准用加号啦！")
                        elif shape2 == shape1:
                            print("\n说了不准用一样的符号啦！")
                        elif shape2.lower() == "ai":
                            flag0 = False
                            chess.rem_shape()
                            flag = chess.return_flag()
                            while flag:
                                flag1 = True
                                flag2 = True
                                while flag1:
                                    pos_input1 = input("\n请输入玩家 {} 要下的位置（数字，字母）：".format(shape1)).replace(" ", "").replace("，", ",")
                                    chess.get_pos1()
                                    flag1 = chess.return_flag1()
                                flag = chess.return_flag()
                                if flag:
                                    while flag2:
                                        chess.ai()
                                        flag2 = chess.return_flag2()
                                flag = chess.return_flag()
                        elif len(shape2) != 1:
                            print("\n能仅能输入一个字符哈！")
                        else:
                            flag0 = False
                            chess.rem_shape()
                            flag = chess.return_flag()
                            while flag:
                                flag1 = True
                                flag2 = True
                                while flag1:
                                    pos_input1 = input("\n请输入玩家 {} 要下的位置（数字，字母）：".format(shape1)).replace(" ", "").replace("，", ",")
                                    chess.get_pos1()
                                    flag1 = chess.return_flag1()
                                flag = chess.return_flag()
                                if flag:
                                    while flag2:
                                        pos_input2 = input("\n请输入玩家 {} 要下的位置（数字，字母）：".format(shape2)).replace(" ", "").replace("，", ",")
                                        chess.get_pos2()
                                        flag2 = chess.return_flag2()
                                flag = chess.return_flag()
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
