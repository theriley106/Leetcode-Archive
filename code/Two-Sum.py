class Solution(object):

    def twoSum(self, nums, target):
        for (i, val) in enumerate(nums):
            for (e, newVal) in enumerate(nums):
                if (i != e):
                    if ((val + newVal) == target):
                        return [i, e]