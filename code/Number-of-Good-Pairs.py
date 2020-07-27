class Solution(object):

    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for e in range((i + 1), len(nums)):
                if (nums[i] == nums[e]):
                    count += 1
        return count