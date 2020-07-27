class Solution(object):

    def maxUncrossedLines(self, A, B):
        matrix = [([0] * (len(B) + 1)) for i in range((len(A) + 1))]

        def get_max(row, column):
            return max(matrix[(row - 1)][column], matrix[row][(column - 1)])
        maxVal = 0
        for r in range(len(A)):
            row = (r + 1)
            for c in range(len(B)):
                column = (c + 1)
                if (A[r] == B[c]):
                    matrix[row][column] = (matrix[(row - 1)][(column - 1)] + 1)
                else:
                    matrix[row][column] = get_max(row, column)
                if (matrix[row][column] > maxVal):
                    maxVal = matrix[row][column]
        for v in matrix:
            print v
        return maxVal