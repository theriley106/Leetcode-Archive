class Solution(object):

    def sumOfLeftLeaves(self, root):
        self.lefts = []

        def f(root, path=''):
            if (root == None):
                return
            if ((path == 'l') and (root.right == None) and (root.left == None)):
                self.lefts.append(root.val)
            f(root.right, path='r')
            f(root.left, path='l')
        f(root)
        print self.lefts
        return sum(self.lefts)