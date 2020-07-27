class Solution(object):

    def invertTree(self, root):
        db = {}

        def traverse(rootz, index=0, yaxis=0):
            if (rootz == None):
                return
            a = traverse(rootz.left, (index + 1), (yaxis - 1))
            b = traverse(rootz.right, (index + 1), (yaxis + 1))
            rootz.left = b
            rootz.right = a
            return rootz
        return traverse(root)
        return root