class Solution(object):

    def binaryGap(self, N):
        x = list(str(bin(N))[2:])
        prev = None
        maxVal = 0
        while True:
            try:
                a = x.index('1')
                x[a] = 'A'
                if (prev == None):
                    pass
                elif ((a - prev) > maxVal):
                    maxVal = (a - prev)
                prev = a
            except:
                break
        return maxVal