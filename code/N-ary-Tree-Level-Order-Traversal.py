class Solution(object):

    def levelOrder(self, root):
        levels = {}

        def s(root, i=0):
            if (root == None):
                return
            if (str(i) not in levels):
                levels[str(i)] = []
            levels[str(i)].append(root.val)
            for val in root.children:
                s(val, (i + 1))
        s(root)
        g = []
        for val in sorted([int(x) for x in levels.keys()]):
            g.append(levels[str(val)])
        return g