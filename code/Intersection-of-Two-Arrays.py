class Solution(object):

    def intersection(self, nums1, nums2):
        my_vals = []
        for val in set(nums1):
            if (val in nums2):
                my_vals.append(val)
        return list(set(my_vals))