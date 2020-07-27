class Solution(object):

    def removeLeafNodes(self, root, target):
        self.changes = 0

        def traverse(root):
            if (root == None):
                return root
            if ((root.left == None) and (root.right == None) and (root.val == target)):
                self.changes += 1
                return None
            root.left = traverse(root.left)
            root.right = traverse(root.right)
            return root
        prevRoot = root
        while True:
            x = traverse(prevRoot)
            if (self.changes == 0):
                return x
            self.changes = 0
            prevRoot = x
        return prevRoot