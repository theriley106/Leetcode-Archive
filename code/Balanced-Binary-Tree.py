class Solution(object):

    def isBalanced(self, root):
        A = [True]

        def depth(root, d=0):
            if (root == None):
                return d
            a = depth(root.left, (d + 1))
            b = depth(root.right, (d + 1))
            print 'NODE DEPTH: {}'.format(d)
            print 'LEFT: {}'.format(a)
            print 'RIGHT: {}'.format(b)
            if (abs((a - b)) > 1):
                A[0] = False
            return max(a, b)
        print depth(root)
        return A[0]