class Solution(object):

    def isPowerOfThree(self, n):

        def is_power(n):
            if (n != int(n)):
                return False
            if (n == 3):
                return True
            if (n == 1):
                return True
            if (n < 3):
                return False
            return is_power((float(n) / 3.0))
        return is_power(n)