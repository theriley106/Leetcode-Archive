class Solution(object):

    def preorderTraversal(self, root):
        a = []

        def traversal(root):
            if (root == None):
                return
            a.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return a