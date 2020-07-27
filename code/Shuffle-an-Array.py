import random


class Solution(object):

    def __init__(self, nums):
        self.array = nums
        self.t = list(self.array)

    def reset(self):
        self.array = list(self.t)
        return self.array

    def shuffle(self):
        random.shuffle(self.array)
        return self.array
