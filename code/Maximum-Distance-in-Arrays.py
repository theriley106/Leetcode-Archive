import itertools


class Solution(object):

    def maxDistance(self, arrays):
        for i in range(len(arrays)):
            arrays[i] = [i, arrays[i]]
        firstVals = sorted(arrays, key=(lambda k: k[1][0]))
        lastVals = sorted(arrays, key=(lambda k: k[1][(-1)]))
        while (firstVals[0][0] == lastVals[(-1)][0]):
            print firstVals
            print lastVals
            firstVals[1][1][0]
            lastVals[(-1)][1][(-1)]
            firstVals[0][1][0]
            lastVals[(-2)][1][(-1)]
            if (abs((firstVals[1][1][0] - lastVals[(-1)][1][(-1)])) > abs((firstVals[0][1][0] - lastVals[(-2)][1][(-1)]))):
                firstVals.pop(0)
            else:
                lastVals.pop((-1))
        return abs((firstVals[0][1][0] - lastVals[(-1)][1][(-1)]))
