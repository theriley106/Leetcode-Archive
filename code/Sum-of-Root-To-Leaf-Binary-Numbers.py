class Solution(object):

    def sumRootToLeaf(self, root):
        self.paths = []

        def f(root, path=''):
            if (root == None):
                return
            if ((root.right == None) and (root.left == None)):
                self.paths.append((path + str(root.val)))
            f(root.right, (path + str(root.val)))
            f(root.left, (path + str(root.val)))
        f(root)
        return sum([int(x, 2) for x in self.paths])