class Solution(object):

    def countSquares(self, matrix):

        def get(i, j):
            try:
                return (matrix[i][j] == 1)
            except:
                return False

        def dfs(i, j):
            size = 0
            total = 0
            while True:
                a = []
                for row in range(i, ((1 + i) + size)):
                    for column in range(j, ((1 + j) + size)):
                        a.append(get(row, column))
                if all(a):
                    total += 1
                    size += 1
                else:
                    return total
        allVals = 0
        for i in range(len(matrix)):
            for e in range(len(matrix[0])):
                allVals += dfs(i, e)
        return allVals