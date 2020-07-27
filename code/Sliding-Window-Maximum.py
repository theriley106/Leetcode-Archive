class Solution(object):

    def maxSlidingWindow(self, nums, k):
        a = []
        for i in range(0, ((len(nums) - k) + 1)):
            vals = nums[i:(i + k)]
            if (len(vals) > 0):
                a.append(max(vals))
        return a