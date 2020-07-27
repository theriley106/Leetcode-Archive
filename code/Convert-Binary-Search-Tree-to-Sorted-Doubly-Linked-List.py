class Solution(object):

    def treeToDoublyList(self, root):
        a = []

        def check(root):
            if (root == None):
                return
            a.append(root.val)
            check(root.left)
            check(root.right)
        check(root)
        a.sort()
        g = []

        def linkedList(start=False, prev=None):
            if (len(a) == 0):
                g.append(prev)
                return g[0]
            e = Node(a.pop(0))
            if (start == True):
                g.append(e)
            e.left = prev
            e.right = linkedList(prev=e)
            return e
        print a
        r = linkedList(True, prev=None)
        if (len(g) == 0):
            return
        if (r == None):
            return
        r.left = g[(-1)]
        return r