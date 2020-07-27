class Solution(object):

    def postorderTraversal(self, root):
        a = []

        def recursive(root):
            if (root == None):
                return
            recursive(root.left)
            recursive(root.right)
            a.append(root.val)
        recursive(root)
        return a