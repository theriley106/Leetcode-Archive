class Solution(object):

    def get_num(self, index):
        try:
            return (sum(self.nums[:index]) == sum(self.nums[(index + 1):]))
        except Exception as exp:
            print exp
            return False

    def pivotIndex(self, nums):
        self.nums = nums
        for i in range(len(nums)):
            if (self.get_num(i) == True):
                return i
        return (-1)