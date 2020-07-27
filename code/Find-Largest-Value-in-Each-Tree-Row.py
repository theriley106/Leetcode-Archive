class Solution(object):

    def __init__(self):
        self.biggest = {}

    def largestValues(self, root, i=1):
        if (root == None):
            return []
        if (str(i) not in self.biggest):
            self.biggest[str(i)] = root.val
        elif (root.val > self.biggest[str(i)]):
            self.biggest[str(i)] = root.val
        self.largestValues(root.left, (i + 1))
        self.largestValues(root.right, (i + 1))
        g = []
        for i in range(1, (max([int(x) for x in self.biggest.keys()]) + 1)):
            g.append(self.biggest[str(i)])
        return g