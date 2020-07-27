class Solution(object):

    def isPerfectSquare(self, num):
        return (int((num ** 0.5)) == float((num ** 0.5)))