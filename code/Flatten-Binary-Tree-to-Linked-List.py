class Solution(object):

    def flatten(self, root):
        a = []

        def f(root):
            if (root == None):
                return
            a.append(root.val)
            f(root.left)
            root.left = None
            f(root.right)
        f(root)

        def fill(root=None):
            if (len(a) == 0):
                return None
            if (root == None):
                root = TreeNode(a.pop(0))
            else:
                root.val = a.pop(0)
            root.right = fill()
            return root
        print fill(root)
        return fill(root)