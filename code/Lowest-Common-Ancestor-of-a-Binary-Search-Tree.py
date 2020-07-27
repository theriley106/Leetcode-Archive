class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        self.vals = []

        def traverse(root, depth=0):
            if (root == None):
                return []
            a = ((traverse(root.left, (depth + 1)) +
                  [root]) + traverse(root.right, (depth + 1)))
            if ((p in a) and (q in a)):
                self.vals.append((root, depth))
            return a
        traverse(root)
        x = sorted(self.vals, key=(lambda k: k[1]))
        print x
        return x[(-1)][0]
