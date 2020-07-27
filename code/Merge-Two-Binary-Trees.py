class Solution(object):

    def mergeTrees(self, t1, t2):
        a = {}

        def check(root, stringVal='', second=True):
            if (root == None):
                return
            if (stringVal in a):
                a[stringVal]['v'] += root.val
            else:
                a[stringVal] = {}
                a[stringVal]['v'] = root.val
                a[stringVal]['l'] = root
            root.left = check(root.left, (str((stringVal + 'L')) + '2'))
            root.right = check(root.right, (str((stringVal + 'R')) + '2'))
            return root

        def fill(root, stringVal='', second=True):
            r = a.get(stringVal, {'l': None})
            if (r['l'] == None):
                return
            root = r['l']
            root.val = r['v']
            root.left = fill(root.left, (str((stringVal + 'L')) + '2'))
            root.right = fill(root.right, (str((stringVal + 'R')) + '2'))
            return root
        b = check(t1, 'start')
        b = check(t2, 'start')
        a = fill(t2, 'start')
        print a
        return a