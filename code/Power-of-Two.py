class Solution(object):

    def isPowerOfTwo(self, n):

        def is_power(n):
            if ((n == 1) or (n == 2)):
                return True
            if (n < 2):
                return False
            if (n != int(n)):
                return False
            return is_power((float(n) / 2.0))
        return is_power(n)