class Solution(object):

    def isToeplitzMatrix(self, matrix):

        def isDiag(rowIndex, columnIndex):
            a = matrix[rowIndex][columnIndex]
            stillTrue = True
            while (((rowIndex + 1) <= len(matrix)) and ((columnIndex + 1) <= len(matrix[0])) and stillTrue):
                stillTrue = (matrix[rowIndex][columnIndex] == a)
                rowIndex += 1
                columnIndex += 1
            return stillTrue
        result = True
        for i in range(len(matrix)):
            result = (result and isDiag(i, 0))
        for e in range(len(matrix[0])):
            result = (result and isDiag(0, e))
        return result