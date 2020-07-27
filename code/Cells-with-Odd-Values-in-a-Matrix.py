class Solution(object):

    def oddCells(self, n, m, indices):
        a = [0 for i in range(m)]
        b = [list(a) for i in range(n)]
        for val in indices:
            print 'INDICE LOOP'
            row = val[0]
            column = val[1]
            for i in xrange(n):
                b[i][column] += 1
            for e in xrange(m):
                b[row][e] += 1
        count = 0
        for val in b:
            for v in val:
                if ((v % 2) != 0):
                    count += 1
        return count