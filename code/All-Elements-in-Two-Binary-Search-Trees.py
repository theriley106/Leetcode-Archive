class Solution(object):

    def getAllElements(self, root1, root2):

        def trev(root):
            if (root == None):
                return []
            return ((trev(root.left) + [root.val]) + trev(root.right))
        a = trev(root1)
        a += trev(root2)
        return sorted(a)