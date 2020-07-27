class Solution(object):

    def isMonotonic(self, A):
        maxVal = max(A)
        minVal = min(A)
        if ((minVal == A[(-1)]) and (maxVal == A[0])):
            i = 0
            while (i < (len(A) - 2)):
                if (A[i] < A[(i + 1)]):
                    return False
                i += 1
            return True
        if ((minVal == A[0]) and (maxVal == A[(-1)])):
            i = 0
            while (i < (len(A) - 2)):
                if (A[i] > A[(i + 1)]):
                    return False
                i += 1
            return True
        return False