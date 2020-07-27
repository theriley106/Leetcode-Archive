class Solution(object):

    def inorderTraversal(self, root):
        a = []

        def recursive(root):
            if (root == None):
                return
            recursive(root.left)
            a.append(root.val)
            recursive(root.right)
        recursive(root)
        return a