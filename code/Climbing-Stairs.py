class Solution(object):

    def climbStairs(self, n):
        if (n == 1):
            return 1
        a = 1
        b = 1
        while (n >= 2):
            for i in range(2, (n + 1)):
                res = (a + b)
                a = b
                b = res
            return res