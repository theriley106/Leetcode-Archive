class Solution(object):

    def findDuplicate(self, nums):
        visitedNums = {}
        for number in nums:
            if (number in visitedNums):
                return number
            visitedNums[number] = ''