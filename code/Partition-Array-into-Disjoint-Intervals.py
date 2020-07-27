class Solution(object):

    def partitionDisjoint(self, A):
        maxLeft = float('-inf')
        indexVal = 0
        v = A[0]
        for i in range(len(A)):
            if (A[i] < v):
                indexVal = i
                v = maxLeft
            maxLeft = max(maxLeft, A[i])
        return (indexVal + 1)