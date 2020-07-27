class Solution(object):

    def majorityElement(self, nums):
        all_vals = []
        tVal = (len(nums) / 3)
        for val in set(nums):
            if (nums.count(val) > tVal):
                all_vals.append(val)
        return all_vals