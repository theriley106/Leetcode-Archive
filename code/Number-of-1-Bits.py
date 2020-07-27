class Solution(object):

    def hammingWeight(self, n):
        return str(bin(n)).count('1')