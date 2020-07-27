class Solution(object):

    def get_tree(self, root):
        if (root == None):
            return []
        return ((self.get_tree(root.left) + [root.val]) + self.get_tree(root.right))

    def findTarget(self, root, k):
        search_tree = self.get_tree(root)
        for (i, val) in enumerate(search_tree):
            for (e, newVal) in enumerate(search_tree):
                if (i != e):
                    if ((newVal + val) == k):
                        return True
        return False