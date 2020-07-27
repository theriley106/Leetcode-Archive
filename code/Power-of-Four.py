class Solution(object):

    def isPowerOfFour(self, num):

        def is_power(n):
            if ((n == 1) or (n == 4)):
                return True
            if (n < 1):
                return False
            if (n != int(n)):
                return False
            return is_power((float(n) / 4))
        return is_power(num)