class Solution(object):

    def hammingDistance(self, x, y):

        def getBinary(num):
            return bin(num)[2:].zfill(4)
        x = getBinary(x)
        y = getBinary(y)
        f = 0
        if (len(x) > len(y)):
            y = y.zfill(len(x))
        else:
            x = x.zfill(len(y))
        for (i, val) in enumerate(x):
            if (y[i] != val):
                f += 1
        return f