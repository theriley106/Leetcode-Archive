class Solution(object):

    def findBottomLeftValue(self, root):
        a = {}

        def f(root, i=0):
            if (root == None):
                return
            if (i not in a):
                a[i] = []
            a[i].append(root.val)
            f(root.left, (i + 1))
            f(root.right, (i + 1))
        f(root)
        return a[max(a.keys())][0]