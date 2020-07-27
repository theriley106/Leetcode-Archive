class Solution(object):

    def thirdMax(self, nums):
        a = sorted(set(nums), reverse=True)[:3]
        return a[(0 if (len(a) != 3) else (-1))]