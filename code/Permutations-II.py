class Solution(object):

    def permuteUnique(self, nums):
        return set(itertools.permutations(nums, len(nums)))