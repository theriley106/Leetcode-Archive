class Solution(object):

    def subsets(self, nums):
        a = []
        for i in range((len(nums) + 1)):
            for v in itertools.combinations(nums, i):
                a.append(v)
        return a