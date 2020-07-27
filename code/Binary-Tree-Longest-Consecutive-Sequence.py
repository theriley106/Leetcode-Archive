class Solution(object):

    def __init__(self):
        self.max = 0
        self.totalVals = []

    def longestConsecutive(self, root):

        def traverse(root, prev=[], count=0):
            if (root == None):
                if (len(prev) > self.max):
                    self.max = len(prev)
                    self.totalVals = prev
                return
            if (len(prev) != 0):
                if ((root.val - prev[(-1)]) == 1):
                    count += 1
                else:
                    count = 0
                    prev = []
            if (len((prev + [root.val])) > self.max):
                self.max = (len(prev) + 1)
                self.totalVals = (prev + [root.val])
            traverse(root.left, (prev + [root.val]), count=count)
            traverse(root.right, (prev + [root.val]), count=count)
        traverse(root)
        return self.max