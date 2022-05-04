'''
Class       : CSE 210 Programming with Classes.
Instructor  : Vaughn Poulson
Assignment  : W02 Prove: Developer - Solo Code Submission.
Student     : Fredy Navas.
Due date    : Wednesday, April 27th, 2022, 11:59 p.m.

Overview    : Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row,
              or a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid 
              of nine squares.
'''

import os
os.system("cls")

class Board():
    '''
    This is the board to display
    '''
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("———+———+———")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("———+———+———")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_number, player):
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player

board = Board()

def print_header():
    print("Welcome to Tic-Tac-Toe\n")

def refresh_screen():
    # clear the screen
    os.system("cls")

    # print the header
    print_header()

    # show the board
    board.display()

    
while True:
    refresh_screen()

    # get X input
    x_choice = int(input("\nX ) Please choose 1 - 9 : "))

    # update board
    board.update_cell(x_choice, "X")

    # refresh screen
    refresh_screen()

    # get O input
    o_choice = int(input("\nO ) Please choose 1 - 9 : "))

    # update board
    board.update_cell(o_choice, "O")
