import random


class Solution(object):

    def __init__(self, head):
        self.a = []
        while head:
            self.a.append(head.val)
            head = head.next

    def getRandom(self):
        return random.choice(self.a)
