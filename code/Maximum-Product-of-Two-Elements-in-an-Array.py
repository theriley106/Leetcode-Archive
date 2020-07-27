class Solution(object):

    def maxProduct(self, nums):
        maxVal = None
        for e in xrange(len(nums)):
            for i in xrange(len(nums)):
                if (i != e):
                    r = ((nums[i] - 1) * (nums[e] - 1))
                    if (maxVal == None):
                        maxVal = r
                    else:
                        maxVal = max(r, maxVal)
        return maxVal