class Solution(object):

    def intersect(self, nums1, nums2):
        my_vals = []
        all_vals = set((nums1 + nums2))
        for val in all_vals:
            num1Count = nums1.count(val)
            num2Count = nums2.count(val)
            if ((num1Count > 0) and (num2Count > 0)):
                my_vals += ([val] * min(num1Count, num2Count))
        return my_vals