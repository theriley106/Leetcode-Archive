class Solution(object):

    def countUnivalSubtrees(self, root):
        self.count = 0

        def traverse(root):
            if (root == None):
                return []
            x = ((traverse(root.left) + [root.val]) + traverse(root.right))
            if (len(set(x)) == 1):
                self.count += 1
            return x
        traverse(root)
        return self.count