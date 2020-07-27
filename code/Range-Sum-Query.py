class NumArray(object, ):

    def __init__(self, nums):
        self.myNums = nums

    def update(self, i, val):
        self.myNums[i] = val

    def sumRange(self, i, j):
        return sum(self.myNums[i:(j + 1)])