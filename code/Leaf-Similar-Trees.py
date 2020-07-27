class Solution(object):

    def leafSimilar(self, root1, root2):

        def extract(root):
            if (root == None):
                return []
            if ((root.left == None) and (root.right == None) and (root.val != None)):
                return [root.val]
            else:
                return (extract(root.left) + extract(root.right))
        return (extract(root1) == extract(root2))