class Solution(object):

    def twoSumLessThanK(self, A, K):
        db = {}
        highest = (-1)
        for i in range(len(A)):
            for e in range((i + 1), len(A)):
                if (((A[i] + A[e]) < K) and ((A[i] + A[e]) > highest)):
                    highest = (A[i] + A[e])
        return highest