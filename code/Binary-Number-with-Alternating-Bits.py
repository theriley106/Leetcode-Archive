class Solution(object):

    def hasAlternatingBits(self, n):
        prev = None
        for v in str(bin(n))[2:]:
            if (v == prev):
                return False
            prev = v
        return True