class Solution(object):

    def bitwiseComplement(self, N):
        return int((str(bin(N))[:2] + str(bin(N))[2:].replace('1', '2').replace('0', '1').replace('2', '0')), 2)