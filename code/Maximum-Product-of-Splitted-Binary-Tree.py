class Solution(object):

    def maxProduct(self, root):
        self.entireSum = 0
        self.i = []

        def traverse(root):
            if (root == None):
                return
            self.entireSum += root.val
            x = self.entireSum
            traverse(root.left)
            y = self.entireSum
            r = (y - x)
            x = self.entireSum
            traverse(root.right)
            y = self.entireSum
            t = (y - x)
            self.i.append(t)
            self.i.append(r)
        traverse(root)
        print self.entireSum
        vals = [(maxVal * abs((self.entireSum - maxVal))) for maxVal in self.i]
        print vals
        return (max(vals) % ((10 ** 9) + 7))