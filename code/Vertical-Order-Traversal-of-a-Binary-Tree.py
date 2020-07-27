class Solution(object):

    def verticalTraversal(self, root):
        a = {}

        def f(root, e=0, i=0):
            if (root == None):
                return
            if (e not in a):
                a[e] = []
            f(root.left, (e - 1), (i + 1))
            a[e].append({'i': i, 'val': root.val})
            f(root.right, (e + 1), (i + 1))
        f(root)
        e = sorted(a.keys())
        g = []
        for val in e:
            g.append(a[val])
        k = []
        for val in g:
            t = []
            print val
            newlist = sorted(val, key=(lambda k: k['val']))
            newlist = sorted(newlist, key=(lambda k: k['i']))
            for u in newlist:
                t.append(u['val'])
            k.append(t)
        print k
        return k