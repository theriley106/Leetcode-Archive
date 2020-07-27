class Solution(object):

    def transpose(self, A):
        width = len(A)
        length = len(A[0])
        matrixVal = []
        for e in range(length):
            tempVal = []
            for i in range(width):
                tempVal.append(A[i][e])
            matrixVal.append(tempVal)
        return matrixVal