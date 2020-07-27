class Solution(object):

    def canMakeArithmeticProgression(self, arr):
        diff = 0
        progression = True
        arr.sort()
        diff = (arr[1] - arr[0])
        prevVal = arr[0]
        for val in arr[1:]:
            progression = (progression and ((val - prevVal) == diff))
            prevVal = val
        return progression