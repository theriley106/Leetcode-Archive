class Solution(object):

    def findErrorNums(self, nums):
        a = len(nums)
        duplicate = list((set(range(1, (a + 1))) - set(nums)))
        missing = ((a + 1) if (len(duplicate) == 0) else duplicate[0])
        double = [x for x in set(nums) if (nums.count(x) == 2)][0]
        return [double, missing]