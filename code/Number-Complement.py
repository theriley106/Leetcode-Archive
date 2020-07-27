class Solution(object):

    def findComplement(self, num):
        return int(str(bin(num)[2:]).replace('1', 'X').replace('0', '1').replace('X', '0'), 2)