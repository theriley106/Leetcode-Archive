class Solution(object):

    def postorder(self, root):
        a = []

        def recursive(root):
            if (root == None):
                return
            for val in root.children:
                recursive(val)
            a.append(root.val)
        recursive(root)
        return a