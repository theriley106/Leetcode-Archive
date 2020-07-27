import statistics


class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        return statistics.median((nums1 + nums2))
