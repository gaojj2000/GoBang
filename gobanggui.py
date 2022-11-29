# _*_ coding:utf-8 _*_
# FileName: gobanggui.py
# IDE: PyCharm

import sys
import gobang
import tkinter
# import threading
# import random
import engine
from tkinter import messagebox


class GoBangGui(gobang.GoBang):
    def __init__(self):
        super().__init__()
        self.root = None
        self.buttons = []
        self.step = 0
        self.ai = False
        self.e = Engine()
        self.shape1 = 'X'
        self.shape2 = 'O'

    def create_board(self):
        # super().create_board()
        self.root = tkinter.Tk(className=' 五子棋对战系统')
        self.root.wm_attributes('-topmost', 1)
        for r in range(self.size):
            for c in range(self.size):
                button = tkinter.Button(self.root, bg='skyblue', font=("黑体", 10, "bold"), disabledforeground='', text='', activebackground='yellow', command=lambda p=(r, c): self.action(p))
                button.place(x=10+c*25, y=10+r*25, width=20, height=20)
                self.buttons.append(button)
        self.root.geometry(f"{self.size*25+20}x{self.size*25+20}")
        self.root.resizable(False, False)
        self.root.mainloop()

    def action(self, p):
        self.step += 1
        self.pos_x = p[0] + 1
        self.pos_y = p[1] + 1
        if self.step % 2:
            self.buttons[p[0]*self.size+p[1]].configure(text='X', disabledforeground='#ff017e', state=tkinter.DISABLED)
            self.board[self.pos_x - 1][self.pos_y - 1] = 'X'
            win = self.check_win('X')
            if self.ai and win:
                self.step += 1
                self.e.get_pos(self.pos_x, self.pos_y)
                self.e.judge()
                self.pos_x, self.pos_y = self.e.action()
                self.buttons[(self.pos_x-1)*self.size+(self.pos_y-1)].configure(text='O', disabledforeground='purple', state=tkinter.DISABLED)
                self.board[self.pos_x - 1][self.pos_y - 1] = 'O'
                self.check_win('O')
        else:
            self.buttons[p[0]*self.size+p[1]].configure(text='O', disabledforeground='purple', state=tkinter.DISABLED)
            self.board[self.pos_x - 1][self.pos_y - 1] = 'O'
            self.check_win('O')

    def check_win(self, shape):
        super().check_win(shape)
        if not self.win:
            messagebox.showinfo(title='恭喜！', message=f'{shape} 赢了！')
            if messagebox.askyesno(title='重新开始？', message='是否重新开始？'):
                self.step = 0
                self.win = True
                self.board = self.board = [[" +" for col in range(self.size)] for row in range(self.size)]
                self.e.function(self.board, self.size, self.shape1)
                for b in self.buttons:
                    b.configure(text='', state=tkinter.NORMAL)
                return False
            else:
                sys.exit(0)
        else:
            return True

    def show_board(self):
        # super().show_board()
        pass

    def logic(self):
        # super().logic()
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
                    self.board = self.board = [[" +" for col in range(self.size)] for row in range(self.size)]
                    if input('AI模式？（直接回车进入双人模式，任意内容为AI模式）'):
                        self.ai = True
                        self.e.function(self.board, self.size, self.shape1)
                    self.create_board()


class Engine(engine.Engine):
    def function(self, board, size, shape):
        self.size = size
        self.shape1 = shape
        self.shape2 = 'O'
        self.board = board


if __name__ == '__main__':
    GoBangGui().logic()
