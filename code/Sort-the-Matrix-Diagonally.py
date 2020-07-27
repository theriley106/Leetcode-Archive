class Solution(object):

    def diagonalSort(self, mat):
        self.starts = []
        db = {}

        def traverseBackwards(rowIndex, columnIndex):
            if ((rowIndex < 0) or (columnIndex < 0)):
                self.starts.append([(rowIndex + 1), (columnIndex + 1)])
                return []
            try:
                mat[rowIndex][columnIndex]
            except:
                return []
            x = (traverseBackwards((rowIndex - 1), (columnIndex - 1)) +
                 [mat[rowIndex][columnIndex]])
            mat[rowIndex][columnIndex] = None
            return x

        def traverseForwards(rowIndex, columnIndex):
            if ((rowIndex < 0) or (columnIndex < 0)):
                return []
            try:
                mat[rowIndex][columnIndex]
            except:
                return []
            if (mat[rowIndex][columnIndex] == None):
                return []
            x = ([mat[rowIndex][columnIndex]] +
                 traverseForwards((rowIndex + 1), (columnIndex + 1)))
            mat[rowIndex][columnIndex] = None
            return x

        def get_diag(rowIndex, columnIndex):
            r1 = traverseBackwards(rowIndex, columnIndex)
            print r1
            r2 = traverseForwards(rowIndex, columnIndex)
            print r2
            if (r2 == None):
                return []
            return [x for x in (r1 + r2[1:]) if (x != None)]
        for rowIndex in range(len(mat)):
            for columnIndex in range(len(mat[0])):
                x = get_diag(rowIndex, columnIndex)
                if (len(self.starts) > 0):
                    start = tuple(self.starts.pop((-1)))
                    if (start not in db):
                        db[start] = []
                    db[start] += x

        def fill(rowIndex, columnIndex, startIndex):
            if (len(db[startIndex]) == 0):
                return
            mat[rowIndex][columnIndex] = db[startIndex].pop(0)
            fill((rowIndex + 1), (columnIndex + 1), startIndex)
        for (k, v) in db.iteritems():
            db[k].sort()
        for (k, v) in db.iteritems():
            fill(k[0], k[1], k)
        return mat
