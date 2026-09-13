'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            set_j = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in set_j:
                        return False
                    set_j.add(board[i][j])

            set_k = set()
            for k in range(9):
                if board[k][i].isdigit():
                    if board[k][i] in set_k:
                        return False
                    set_k.add(board[k][i])


        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                box_set = set()
                for i in range(box_row,box_row+3):
                    for j in range(box_col,box_col+3):
                        if board[i][j].isdigit():
                            if board[i][j] in box_set:
                                return False
                            box_set.add(board[i][j])

        return True