class Solution(object):

    def rotate(self, matrix):
        matrix2 = []
        for i in range(len(matrix)):
            t = []
            for e in range(len(matrix[0])):
                t.append(matrix[e][i])
            matrix2.append(t[::(-1)])
        for i in range(len(matrix)):
            for e in range(len(matrix)):
                matrix[i][e] = matrix2[i][e]