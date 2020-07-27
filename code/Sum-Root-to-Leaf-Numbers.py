class Solution(object):

    def sumNumbers(self, root):
        self.sums = 0

        def r(root, prev=''):
            if (root == None):
                return
            if ((root.left == None) and (root.right == None)):
                prev += str(root.val)
                self.sums += int(prev)
                return
            r(root.left, (prev + str(root.val)))
            r(root.right, (prev + str(root.val)))
        r(root)
        return self.sums