class Solution(object):

    def hasPathSum(self, root, sumVal):
        e = []

        def f(root, a=[]):
            if (root == None):
                return a
            if ((root.right == None) and (root.left == None)):
                e.append((sum((a + [root.val])) == sumVal))
                return True
            else:
                pass
            f(root.left, (a + [root.val]))
            f(root.right, (a + [root.val]))
            return True
        g = f(root)
        print e
        return (True in e)