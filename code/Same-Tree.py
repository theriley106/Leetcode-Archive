class Solution(object):

    def isSameTree(self, p, q):
        a = []
        b = []

        def fun(root):
            if (root == None):
                a.append(None)
                return []
            a.append(root.val)
            fun(root.left)
            fun(root.right)

        def fun2(root):
            if (root == None):
                b.append(None)
                return []
            b.append(root.val)
            fun2(root.left)
            fun2(root.right)
        fun(p)
        fun2(q)
        print a
        print b
        return (a == b)