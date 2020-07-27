class Solution(object):

    def binaryTreePaths(self, root):
        self.g = []

        def traverse(root, path=[]):
            if (root == None):
                return
            if ((root.left == None) and (root.right == None)):
                self.g.append('->'.join((path + [str(root.val)])))
            traverse(root.left, (path + [str(root.val)]))
            traverse(root.right, (path + [str(root.val)]))
        traverse(root)
        return self.g