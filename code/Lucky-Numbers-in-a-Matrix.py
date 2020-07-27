class Solution(object):

    def luckyNumbers(self, matrix):
        minRows = {}
        for (i, val) in enumerate(matrix):
            minRows[i] = min(val)
        maxColumns = {}
        for e in range(len(matrix[0])):
            maxColumns[e] = max([row[e] for row in matrix])
        for (i, val) in enumerate(matrix):
            minRows[i] = min(val)
        allVals = []
        for i in range(len(matrix)):
            for e in range(len(matrix[0])):
                if ((matrix[i][e] == minRows[i]) and (matrix[i][e] == maxColumns[e])):
                    allVals.append(matrix[i][e])
        return allVals