class Solution(object):

    def countBits(self, num):
        genBinary = (lambda num: str(bin(num)[2:]).count('1'))
        return [genBinary(x) for x in range((num + 1))]