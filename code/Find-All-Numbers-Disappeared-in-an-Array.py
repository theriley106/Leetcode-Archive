class Solution(object):

    def findDisappearedNumbers(self, nums):
        return list((set(list(range(1, (len(nums) + 1)))) - set(nums)))