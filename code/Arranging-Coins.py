class Solution(object):

    def arrangeCoins(self, n):
        count = 0
        if (n == 1):
            return 1
        for i in xrange(1, n):
            if ((n - i) < 0):
                break
            else:
                n = (n - i)
            count += 1
        return count