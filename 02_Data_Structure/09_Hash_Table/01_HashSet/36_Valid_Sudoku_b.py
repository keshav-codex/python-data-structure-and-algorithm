'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
from ast import List



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

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                value = board[i][j]

                if value == ".":
                    continue

                box = (i // 3) * 3 + (j // 3)

                if value in rows[i]:
                    return False

                if value in cols[j]:
                    return False

                if value in boxes[box]:
                    return False

                rows[i].add(value)
                cols[j].add(value)
                boxes[box].add(value)

        return True