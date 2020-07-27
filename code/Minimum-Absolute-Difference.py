class Solution(object):

    def minimumAbsDifference(self, arr):
        arr.sort()
        minVal = float('inf')
        allVals = []
        for i in range((len(arr) - 1)):
            diff = (arr[(i + 1)] - arr[i])
            if (diff < minVal):
                minVal = diff
                allVals = [[arr[i], arr[(i + 1)]]]
            elif (diff == minVal):
                allVals.append([arr[i], arr[(i + 1)]])
        return allVals