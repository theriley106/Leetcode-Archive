class Solution(object):

    def heightChecker(self, heights):
        return len([i for (i, x) in enumerate(heights) if (heights[i] != sorted(heights)[i])])