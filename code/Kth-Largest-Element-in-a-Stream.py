class KthLargest(object, ):

    def __init__(self, k, nums):
        self.nums = sorted(nums)
        try:
            self.kItem = self.nums[(- k)]
        except:
            self.kItem = 0
        self.k = k

    def add(self, val):
        self.nums.append(val)
        self.nums.sort()
        self.kItem = self.nums[(- self.k)]
        return self.kItem