class Solution(object):

    def longestSubarray(self, nums, limit):
        startLeft = 0
        startRight = 0
        maxDiff = 0
        maxNum = 0
        minVal = None
        maxVal = None
        while ((startLeft <= startRight) and (startRight < len(nums))):
            if ((minVal == None) and (maxVal == None)):
                maxVal = max(nums[startLeft:(startRight + 1)])
                minVal = min(nums[startLeft:(startRight + 1)])
            if (nums[startRight] > maxVal):
                maxVal = nums[startRight]
            if (nums[startRight] < minVal):
                minVal = nums[startRight]
            maxDiff = (maxVal - minVal)
            if (maxDiff <= limit):
                if (((startRight - startLeft) + 1) > maxNum):
                    maxNum = ((startRight - startLeft) + 1)
            else:
                startLeft += 1
                minVal = None
                maxVal = None
            startRight += 1
        return maxNum