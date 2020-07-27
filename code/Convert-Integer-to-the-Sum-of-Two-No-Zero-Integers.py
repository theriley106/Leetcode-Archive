class Solution(object):

    def getNoZeroIntegers(self, n):
        a = (n - 1)
        b = 1

        def determine(a, b):
            return (('0' not in str(a)) and ('0' not in str(b)))
            return (((a % 10) != 0) and ((b % 10) != 0))
        while (a > 0):
            if determine(a, b):
                return [a, b]
            a = (a - 1)
            b += 1