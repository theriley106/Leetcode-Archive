class Solution(object):

    def levelOrder(self, root):
        levels = {}

        def traverse(root, i=0):
            if (root == None):
                return []
            if (i not in levels):
                levels[i] = []
            levels[i].append(root.val)
            traverse(root.left, (i + 1))
            traverse(root.right, (i + 1))
        traverse(root)
        return ([levels[i] for i in range((max(levels.keys()) + 1))] if (len(levels.keys()) > 0) else [])