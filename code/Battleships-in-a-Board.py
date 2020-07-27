class Solution(object):

    def countBattleships(self, board):
        self.board = board

        def search(rowIndex, columnIndex):
            try:
                x = self.board[rowIndex][columnIndex]
                self.board[rowIndex][columnIndex] = (-1)
                if (x == 'X'):
                    x = 1
                else:
                    x = 0
            except:
                x = 0
            if (x > 0):
                i = search((rowIndex + 1), columnIndex)
                g = search(rowIndex, (columnIndex + 1))
            return x
        total = 0
        for i in range(len(board)):
            for e in range(len(board[0])):
                total += search(i, e)
        return total