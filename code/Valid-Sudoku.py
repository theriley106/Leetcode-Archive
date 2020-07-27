class Solution(object):

    def checkAllVals(self, rowList):
        mList = []
        for r in rowList:
            total = 0
            for c in r:
                try:
                    a = int(c)
                    mList.append(a)
                    if ((a > 9) or (a < 1)):
                        return False
                except:
                    pass
        return (len(set(mList)) == len(mList))

    def getColumn(self, columnIndex):
        column = []
        for val in self.board:
            try:
                a = int(val[columnIndex])
                column.append(a)
            except:
                pass
        return (len(set(column)) == len(column))

    def getRow(self, rowIndex):
        column = []
        for val in self.board[rowIndex]:
            try:
                a = int(val)
                column.append(a)
            except:
                pass
        return (len(set(column)) == len(column))

    def isValidSudoku(self, board):
        aVals = []
        self.board = board
        for i in range(9):
            a = (self.getRow(i) and self.getColumn(i))
            if (a == False):
                return False
        for rowIndex in range(0, len(board), 3):
            for columnIndex in range(0, len(board[0]), 3):
                aVal = []
                for i in range(rowIndex, (rowIndex + 3)):
                    rVal = []
                    for e in range(columnIndex, (columnIndex + 3)):
                        rVal.append(board[i][e])
                    aVal.append(rVal)
                aVals.append(aVal)
        for val in aVals:
            a = self.checkAllVals(val)
            if (a == False):
                return False
            print val
        return True