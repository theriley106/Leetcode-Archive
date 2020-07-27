class Solution(object):

    def missingNumber(self, arr):
        diffVals = {}
        total = (arr[(-1)] - arr[0])
        skip = (total / len(arr))
        if (skip == 0):
            return 0
        for i in range(0, (len(arr) - 1)):
            if ((arr[(i + 1)] - arr[i]) != skip):
                return (arr[(i + 1)] - skip)