class Solution(object):

    def findMode(self, root):
        a = {}

        def f(root):
            if (root == None):
                return
            if (root.val not in a):
                a[root.val] = 0
            a[root.val] += 1
            f(root.left)
            f(root.right)
        f(root)
        o = []
        if (len(a) > 0):
            g = max(a.values())
            for (key, val) in a.iteritems():
                if (val == g):
                    o.append(key)
        return o