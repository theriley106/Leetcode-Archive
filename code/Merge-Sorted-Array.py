class Solution(object):

    def merge(self, nums1, m, nums2, n):
        a = list(nums1[:m])
        b = list(nums2[:n])
        while (len(nums1) > 0):
            nums1.pop(0)
        for i in sorted((a + b)):
            nums1.append(i)