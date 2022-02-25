#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

from sqlite3 import Row


ROW = "ABCDEFGHI"
COL = "123456789"

def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

def initDict():
# return dictionary that will keep track of remaining feasible values for each cell
    dict_ = {}
    for i in range(9):
        for j in range(9):
            dict_[ROW[i]+str(j+1)] = [
                n for n in range(1,10)
                ]
    return dict_

def get_remaining_values_from(board):
# return updated dictionary with feasible values

    remaining = initDict()

    for i in range(9):
        for j in range(9):
            if board[ROW[i]+str(j+1)] != 0:
                value = board[ROW[i]+str(j+1)]
                remaining = remove_values(ROW[i],j+1,value, remaining)

    return d

def remove_values(x,y,value,remaining):

def possible(row, col, num, board):

    """Search through the row"""
    for i in range(0,9):
        if board[row + COL[i]] == num:
            return False

    """Search through the column"""
    for i in range(0,9):
        if board[ROW[i] + col] == num:
            return False
    
    """Search the square"""
    row0 = ((ord(row)-65)//3)*3
    col0 = ((int(col)-1)//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[chr(row0 + i + 65) + str(col0 + j + 1)] == num:
                return False
    
    return True


def solved(board):
    empty = 0
    for value in board.values():
        if value == 0:
            empty +=1
    if empty == 0:
        return True
    return False

def createInitialDict():
    

def backtracking(board):
    """Takes a board and returns solved board."""
    for key, value in board.items():
        if value == 0:
            for i in range(1,10):
                if possible(key[0], key[1], i, board):
                    board[key] = i
                    backtracking(board)
                    if solved(board):
                        return board
                    board[key] = 0
            return

if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudoku_boards.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        print_board(board)
        # Solve with backtracking
        solved_board =  backtracking(board)
        # # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)

        # # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    print("Finishing all boards in file.")