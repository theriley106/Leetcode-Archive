import random


class Solution(object):

    def __init__(self, nums):
        self.db = {}
        for (i, val) in enumerate(nums):
            if (val not in self.db):
                self.db[val] = []
            self.db[val].append(i)

    def pick(self, target):
        return random.choice(self.db[target])
