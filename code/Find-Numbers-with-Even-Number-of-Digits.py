class Solution(object):

    def findNumbers(self, nums):
        return len([x for x in nums if ((len(str(x)) % 2) == 0)])