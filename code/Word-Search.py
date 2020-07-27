class Solution(object):

    def exist(self, board, word):
        self.og = len(word)
        self.board = [list(x) for x in list(board)]
        self.path = None

        def stillExists(rowIndex, columnIndex, boardClone, wordVal, path=[]):
            if (columnIndex < 0):
                return False
                nColumn = (len(boardClone[0]) + columnIndex)
            else:
                nColumn = columnIndex
            if (rowIndex < 0):
                return False
                nRow = (len(boardClone) + rowIndex)
            else:
                nRow = rowIndex
            if (len(wordVal) == 0):
                for (ih, v) in enumerate(self.board):
                    for (ig, g) in enumerate(v):
                        if ([ih, ig] in path):
                            v[ig] = '*'
                    print v
                print 'WORD FOUND'
                return True
            if ([nRow, nColumn] in path):
                return False
            if ((rowIndex >= len(boardClone)) or (abs(rowIndex) > len(boardClone))):
                return False
            elif ((columnIndex >= len(boardClone[0])) or (abs(columnIndex) > len(boardClone[0]))):
                return False
            x = False
            if (boardClone[rowIndex][columnIndex] == wordVal[0]):
                x = (x or stillExists((rowIndex + 1), columnIndex,
                                      list(boardClone), wordVal[1:], (path + [[nRow, nColumn]])))
                x = (x or stillExists((rowIndex - 1), columnIndex,
                                      list(boardClone), wordVal[1:], (path + [[nRow, nColumn]])))
                x = (x or stillExists(rowIndex, (columnIndex + 1),
                                      list(boardClone), wordVal[1:], (path + [[nRow, nColumn]])))
                x = (x or stillExists(rowIndex, (columnIndex - 1),
                                      list(boardClone), wordVal[1:], (path + [[nRow, nColumn]])))
            return x
        g = list([list(x)[::(-1)] for x in list(board)])
        for i in range(len(board)):
            for e in range(len(board)):
                print (i, e)
                if stillExists(i, e, board, word):
                    return True
        for i in range(len(board)):
            for e in range(len(board)):
                if stillExists(i, e, g, word):
                    return True
