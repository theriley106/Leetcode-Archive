class Solution(object):

    def longestOnes(self, A, K):
        self.left = 0
        self.right = 0
        count = {1: 0, 0: 0}
        maxVal = 0
        while ((self.left <= self.right) and (self.right < len(A))):
            count[A[self.right]] += 1
            if (((count[1] + count[0]) > maxVal) and (count[0] <= K)):
                maxVal = (count[1] + count[0])
            while (count[0] > K):
                count[A[self.left]] -= 1
                self.left += 1
            self.right += 1
        return maxVal