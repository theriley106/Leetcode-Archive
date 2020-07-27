class Solution(object):

    def tictactoe(self, moves):
        grid = [['-' for i in range(3)] for e in range(3)]

        def is_solved():
            for i in range(3):
                gVal = ''.join(grid[i])
                if (gVal == 'XXX'):
                    return 'A'
                if (gVal == 'OOO'):
                    return 'B'
            for i in range(3):
                gVal = ''
                for e in range(3):
                    gVal += grid[e][i]
                if (gVal == 'XXX'):
                    return 'A'
                if (gVal == 'OOO'):
                    return 'B'
            gVal = ((grid[0][0] + grid[1][1]) + grid[2][2])
            if (gVal == 'XXX'):
                return 'A'
            if (gVal == 'OOO'):
                return 'B'
            gVal = ((grid[2][0] + grid[1][1]) + grid[0][2])
            if (gVal == 'XXX'):
                return 'A'
            if (gVal == 'OOO'):
                return 'B'
        aTurn = True
        totalMoves = len(moves)
        print totalMoves
        for move in moves:
            (x, y) = move
            if (aTurn == True):
                grid[x][y] = 'X'
                aTurn = False
            else:
                grid[x][y] = 'O'
                aTurn = True
            returnVal = is_solved()
            if (returnVal != None):
                return returnVal
        for v in grid:
            print v
        if (totalMoves == 9):
            return 'Draw'
        return 'Pending'