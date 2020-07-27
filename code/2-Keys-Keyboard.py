class Solution(object):

    def minSteps(self, n):
        f = 2
        factors = []
        while (n > 1):
            while ((n % f) == 0):
                factors.append(f)
                n = (n / f)
            f += 1
        return sum(factors)