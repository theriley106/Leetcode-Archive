class Solution(object):

    def closestValue(self, root, target):
        self.minVal = float('inf')
        self.val = None

        def traverse(root):
            if (root == None):
                return
            xVal = abs((float(target) - float(root.val)))
            if (xVal < self.minVal):
                self.minVal = xVal
                self.val = root.val
            if (target < root.val):
                traverse(root.left)
            else:
                traverse(root.right)
        traverse(root)
        return self.val