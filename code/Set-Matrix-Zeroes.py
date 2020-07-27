class Solution(object):

    def setZeroes(self, matrix):
        toModify = []
        for i in range(len(matrix)):
            for e in range(len(matrix[0])):
                if (matrix[i][e] == 0):
                    for i2 in range(len(matrix)):
                        toModify.append((i2, e))
                    for e2 in range(len(matrix[0])):
                        toModify.append((i, e2))
        toModify = set(toModify)
        for i in range(len(matrix)):
            for e in range(len(matrix[0])):
                if ((i, e) in toModify):
                    matrix[i][e] = 0