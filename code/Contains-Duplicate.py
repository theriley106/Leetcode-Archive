class Solution(object):

    def containsDuplicate(self, nums):
        return (len(list(nums)) != len(set(nums)))