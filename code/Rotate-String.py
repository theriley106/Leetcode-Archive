class Solution(object):

    def rotateString(self, A, B):
        if (A == B):
            return True
        for i in range(len(A)):
            tempVal = A[0]
            A = (A[1:] + tempVal)
            if (A == B):
                return True
        return False