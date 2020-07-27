class Solution(object):

    def diameterOfBinaryTree(self, root):
        self.max = 1

        def get_largest(root, path=''):
            if (root == None):
                return 0
            L = get_largest(root.left, (path + 'L'))
            R = get_largest(root.right, (path + 'R'))
            self.max = max(((L + R) + 1), self.max)
            return (max(L, R) + 1)
        if (root == None):
            return 0
        get_largest(root)
        return (self.max - 1)