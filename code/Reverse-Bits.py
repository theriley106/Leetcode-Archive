class Solution:

    def reverseBits(self, n):
        x = str('{0:b}'.format(n))
        while (len(x) < 32):
            x = ('0' + x)
        x = x[::(-1)]
        return int(x, 2)