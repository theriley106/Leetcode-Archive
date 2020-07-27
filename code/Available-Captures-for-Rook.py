class Solution(object):

    def numRookCaptures(self, board):
        total = 0
        for rowIndex in range(len(board)):
            if ('R' in board[rowIndex]):
                (row, column) = [rowIndex, board[rowIndex].index('R')]
                break
        a = [board[i][column] for i in range(8) if (board[i][column] != '.')]
        b = [board[row][i] for i in range(8) if (board[row][i] != '.')]
        while ('.' in a):
            a.remove('.')
        while ('.' in b):
            b.remove('.')
        g = a.index('R')
        f = b.index('R')
        if (g > 0):
            if a[(g - 1)].islower():
                total += 1
        if (f > 0):
            if b[(f - 1)].islower():
                total += 1
        if ((g + 1) < len(a)):
            if a[(g + 1)].islower():
                total += 1
        if ((f + 1) < len(b)):
            if b[(f + 1)].islower():
                total += 1
        return total