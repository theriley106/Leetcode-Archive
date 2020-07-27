class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        new = [nums1, nums2]
        a = []
        for vals in itertools.product(*new):
            a.append((vals, sum(vals)))
        return [x[0] for x in sorted(a, key=(lambda a: a[1]))][:k]