class Solution(object):

    def fixedPoint(self, A):
        for (i, val) in enumerate(A):
            if (i == val):
                return i
        return (-1)