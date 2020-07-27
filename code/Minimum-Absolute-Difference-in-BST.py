class Solution(object):

    def getAll(self, root):
        if (root == None):
            return
        self.tree.append(root.val)
        if (self.smallest == None):
            self.smallest = root.val
        if (self.largest == None):
            self.largest = root.val
        if (root.val < self.smallest):
            self.smallest = root.val
        if (root.val > self.largest):
            self.largest = root.val
        self.getAll(root.left)
        self.getAll(root.right)

    def getMinimumDifference(self, root):
        self.tree = []
        self.smallest = None
        self.largest = None
        self.getAll(root)
        self.biggestDiff = 9999999999
        self.tree.sort()
        for i in range(1, len(self.tree)):
            x = abs((self.tree[i] - self.tree[(i - 1)]))
            if (x < self.biggestDiff):
                self.biggestDiff = x
        print self.tree
        return self.biggestDiff