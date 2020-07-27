class Solution(object):

    def levelOrderBottom(self, root):
        levels = {}

        def traverse(root, level=0):
            if (root == None):
                return
            if (str(level) not in levels):
                levels[str(level)] = []
            levels[str(level)].append(root.val)
            traverse(root.left, (level + 1))
            traverse(root.right, (level + 1))
        traverse(root)
        a = []
        for val in sorted([int(x) for x in levels.keys()], reverse=True):
            a.append(levels[str(val)])
        return a