class Solution(object):

    def increasingBST(self, root):
        self.vals = []

        def f(root):
            if (root == None):
                return
            f(root.left)
            self.vals.append(root.val)
            f(root.right)
        f(root)
        tree = None

        def fill(tree):
            if (len(self.vals) == 0):
                return None
            else:
                tree = TreeNode(self.vals.pop(0))
                tree.right = fill(tree)
                return tree
        a = fill(tree)
        return a
        while (a != None):
            print a.val
            a = a.right