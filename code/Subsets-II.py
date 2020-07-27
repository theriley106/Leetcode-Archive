import itertools


class Solution(object):

    def subsetsWithDup(self, nums):
        a = []
        for i in range((len(nums) + 1)):
            for val in itertools.combinations(nums, i):
                a.append(tuple(sorted(val)))
        return list(set(a))
