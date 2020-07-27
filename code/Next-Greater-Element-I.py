class Solution(object):

    def nextGreaterElement(self, nums1, nums2):
        g = []
        for (i, num) in enumerate(nums1):
            nextMax = (-1)
            found = False
            for val in nums2:
                if (val == num):
                    found = True
                if (found == True):
                    if (val > num):
                        nextMax = val
                        break
            g.append(nextMax)
        return g