class Solution(object):

    def sortedSquares(self, A):
        return sorted([(x ** 2) for x in A])