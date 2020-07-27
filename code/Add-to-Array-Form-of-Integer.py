class Solution(object):

    def addToArrayForm(self, A, K):
        g = ''.join([str(x) for x in A])
        j = (int(g) + K)
        return [int(x) for x in str(j)]