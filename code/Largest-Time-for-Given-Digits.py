import itertools


class Solution(object):

    def largestTimeFromDigits(self, A):
        highestVal = (-1)
        for val in list(itertools.permutations([str(x) for x in A])):
            thisNum = int(''.join(val))
            if ((thisNum >= highestVal) and (thisNum < 2400) and (int(val[2]) < 6)):
                highestVal = thisNum
        if (highestVal == (-1)):
            return ''
        x = str(highestVal)
        while (len(x) < 4):
            x = ('0' + x)
        h = list(x)
        return '{}{}:{}{}'.format(h[0], h[1], h[2], h[3])
