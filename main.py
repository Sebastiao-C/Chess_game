# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import numpy as np
#import tkinter as tk
from tkinter import *
import ctypes

class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def get_piece_info(self):
        return f'{self.color}{self.name}'

    # def getName(self):
    #     return self.name

    # def getColor(self):
    #     return self.color

    def get_possible_moves(self, board, coords):
        moves = []
        if self.name == 'p':
            newMoves = self.get_pawn_moves(board, coords)

        if self.name == 'r':
            newMoves = self.get_rook_moves(board, coords)

        if self.name == 'n':
            pass
        if self.name == 'b':
            pass
        if self.name == 'q':
            pass
        if self.name == 'k':
            pass
        if newMoves is not None:
            for move in newMoves:
                moves.append(move)
            return moves

    def get_rook_moves(self, board, coords):
        moves = []
        for var in range(coords[0] + 1, 8):
            if board.squares[var][coords[1]] is None:
                moves.append([var-coords[0], 0])
            elif board.squares[var][coords[1]].color != self.color:
                moves.append([var - coords[0], 0])
                break
            else:
                break

        for var in range(coords[0]-1, -1, -1):
            if board.squares[var][coords[1]] is None:
                moves.append([var - coords[0], 0])
            elif board.squares[var][coords[1]].color != self.color:
                moves.append([var - coords[0], 0])
                break
            else:
                break

        for var in range(coords[1] + 1, 8):
            if board.squares[coords[0]][var] is None:
                moves.append([0, var - coords[1]])
            elif board.squares[coords[0]][var].color != self.color:
                moves.append([0, var - coords[1]])
                break
            else:
                break
        for var in range(coords[1] - 1, -1, -1):
            if board.squares[coords[0]][var] is None:
                moves.append([0, var - coords[1]])
            elif board.squares[coords[0]][var].color != self.color:
                moves.append([0, var - coords[1]])
                break
            else:
                break
        return moves

    def get_pawn_moves(self, board, coords):
        moves = []
        if self.color == 'w':
            if board.squares[coords[0] + 1][coords[1]] is None:
                moves.append([1, 0])
            if board.squares[coords[0] + 1][coords[1] - 1] is not None and \
                    board.squares[coords[0] + 1][coords[1] - 1].color != self.color:
                moves.append([1, -1])
            if board.squares[coords[0] + 1][coords[1] + 1] is not None and \
                    board.squares[coords[0] + 1][coords[1] + 1].color != self.color:
                moves.append([1, 1])
            if board.squares[coords[0] + 1][coords[1]] is None and \
                    board.squares[coords[0] + 2][coords[1]] is None and \
                    coords[0] == 1:
                moves.append([2, 0])
            if coords[0] == 4 and board.squares[coords[0]][coords[1] - 1] is not None and \
                    board.squares[coords[0]][coords[1] - 1].color != self.color and \
                        board.squares[coords[0]][coords[1] - 1].name == 'p':
                moves.append([1, -1])
            if coords[0] == 4 and board.squares[coords[0]][coords[1] + 1] is not None and \
                    board.squares[coords[0]][coords[1] + 1].color != self.color and \
                        board.squares[coords[0]][coords[1] + 1].name == 'p':
                moves.append([1, 1])

        if self.color == 'b':
            if board.squares[coords[0] - 1][coords[1]] is None:
                moves.append([-1, 0])
            if board.squares[coords[0] - 1][coords[1] - 1] is not None and \
                    board.squares[coords[0] - 1][coords[1] - 1].color != self.color:
                moves.append([-1, -1])
            if board.squares[coords[0] - 1][coords[1] + 1] is not None and \
                    board.squares[coords[0] - 1][coords[1] + 1].color != self.color:
                moves.append([-1, 1])
            if board.squares[coords[0] - 1][coords[1]] is None and \
                    board.squares[coords[0] - 2][coords[1]] is None and \
                    coords[0] == 6:
                moves.append([-2, 0])
            if coords[0] == 3 and board.squares[coords[0]][coords[1] - 1] is not None and \
                    board.squares[coords[0]][coords[1] - 1].color != self.color and \
                        board.squares[coords[0]][coords[1] - 1].name == 'p':
                moves.append([-1, -1])
            if coords[0] == 3 and board.squares[coords[0]][coords[1] + 1] is not None and \
                    board.squares[coords[0]][coords[1] + 1].color != self.color and \
                        board.squares[coords[0]][coords[1] + 1].name == 'p':
                moves.append([-1, 1])
        return moves


class Board:
    def __init__(self):
        self.squares = [[None for x in range(8)] for y in range(8)]
        self.squaresPrint = [['**' for x in range(8)] for y in range(8)]
        self.currentPlayer = 'w'

    def init_board(self):

        self.squares = [[None for x in range(8)] for y in range(8)]
        self.squaresPrint = [['**' for x in range(8)] for y in range(8)]

        # Pawns
        for var in range(8):
            self.update_square((1, var), Piece('w', 'p'))
            self.update_square((6, var), Piece('b', 'p'))

        # Rooks
        self.update_square((0, 0), Piece('w', 'r'))
        self.update_square((0, 7), Piece('w', 'r'))
        self.update_square((7, 0), Piece('b', 'r'))
        self.update_square((7, 7), Piece('b', 'r'))

        # Knights

        self.update_square((0, 1), Piece('w', 'n'))
        self.update_square((0, 6), Piece('w', 'n'))
        self.update_square((7, 1), Piece('b', 'n'))
        self.update_square((7, 6), Piece('b', 'n'))

        # Bishops
        self.update_square((0, 2), Piece('w', 'b'))
        self.update_square((0, 5), Piece('w', 'b'))
        self.update_square((7, 2), Piece('b', 'b'))
        self.update_square((7, 5), Piece('b', 'b'))

        # Queens
        self.update_square((0, 3), Piece('w', 'q'))
        self.update_square((7, 3), Piece('b', 'q'))

        # Kings
        self.update_square((0, 4), Piece('w', 'k'))
        self.update_square((7, 4), Piece('b', 'k'))

    def update_square(self, coords, piece):
        self.squares[coords[0]][coords[1]] = piece
        if piece is not None:
            self.squaresPrint[coords[0]][coords[1]] = piece.get_piece_info()
        else:
            self.squaresPrint[coords[0]][coords[1]] = '**'

    def check_move_piece(self, coords, move):
        possible_moves = self.squares[coords[0]][coords[1]].get_possible_moves(self, coords)
        for mov in possible_moves:
            if mov == list(move):
                return 1
        return -1

    def move_piece(self, coords, move):
        if self.squares[coords[0]][coords[1]] is None:
            print('No piece there!')
            return -1

        if self.squares[coords[0]][coords[1]].color != self.currentPlayer:
            print('That piece isn\'t yours!')
            return -2

        if self.check_move_piece(coords, move) == 1:
            self.update_square((coords[0] + move[0], coords[1] + move[1]), self.get_piece(coords))
            self.update_square(coords, None)
            if self.currentPlayer == 'w':
                self.currentPlayer = 'b'
            else:
                self.currentPlayer = 'w'
        else:
            print('That piece can\'t do that move, sorry!')

    def is_legal(self):
        pass

    def print_board(self):
        for row in range(7, -1, -1):
            print(self.squaresPrint[row])
        print()

    def get_piece(self, coords):
        return self.squares[coords[0]][coords[1]]


class ChessWindow:
    def __init__(self, win):
        pass

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ctypes.windll.shcore.SetProcessDpiAwareness(2)

    window = Tk()
    # add widgets here
    window.minsize(470, 320)
    #btn = Button(window, text="This is Button widget", fg='blue')
    #btn.place(x=80, y=100)

    screen_width = window.winfo_width()
    screen_height = window.winfo_height()

    print(screen_width, screen_height)
    window.title('Hello Python')
    window.geometry("500x500+10+10")
    #window.mainloop()


    board = Board()
    board.init_board()
    board.print_board()

    #print(board.get_piece((1, 1)).get_possible_moves(board, (1, 1)))
    print(board.get_piece((0, 0)).get_possible_moves(board, (0, 0)))

    # board.updateSquare((4, 2), Piece('b', 'p'))
    # board.updateSquare((4, 3), Piece('w', 'p'))

    board.move_piece((1, 0), (1, 0))

    print(board.get_piece((0, 0)).get_possible_moves(board, (0, 0)))

    board.print_board()

    board.update_square((4, 3), Piece('w', 'r'))

    board.update_square((2, 0), None)
    board.update_square((0, 1), None)
    board.update_square((0, 2), None)

    print(board.get_piece((0, 0)).get_possible_moves(board, (0, 0)))
    print(board.get_piece((4, 3)).get_possible_moves(board, (4, 3)))

    board.print_board()

    board.move_piece((2, 1), (1, 0))

    board.print_board()

    board.move_piece((3, 1), (1, 0))

    board.print_board()

    board.move_piece((4, 1), (1, 0))

    board.print_board()

    board.move_piece((5, 1), (1, 0))

    board.print_board()

    board.move_piece((5, 1), (1, 1))

    board.print_board()

    board.move_piece((6, 2), (1, 1))

    board.print_board()

    # print(board.getPiece((4, 3)).get_possible_moves(board, (4, 3)))

    # board.initBoard()
    # board.printBoard()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
