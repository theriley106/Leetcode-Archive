class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        self.left = 0
        self.right = 0
        db = {1: 0, 0: 0}
        maxVal = 0
        while ((self.left <= self.right) and (self.right < len(nums))):
            db[nums[self.right]] += 1
            if (((db[1] + db[0]) > maxVal) and (db[0] <= 1)):
                maxVal = (db[1] + db[0])
            while (db[0] > 1):
                db[nums[self.left]] -= 1
                self.left += 1
            self.right += 1
        return maxVal