class Solution(object):

    def isSymmetric(self, root):
        db = {}

        def i(string):
            string = string.replace('r', 'x')
            string = string.replace('l', 'r')
            string = string.replace('x', 'r')
            return string

        def g(root, row=0, column=0):
            if (row not in db):
                db[row] = []
            if (root == None):
                db[row].append(None)
                return
            g(root.left, (row + 1), (column - 1))
            db[row].append(root.val)
            g(root.right, (row + 1), (column + 1))

        def f(root, path=''):
            if (root == None):
                return
            db[path] = root.val
            f(root.left, (path + 'l'))
            f(root.right, (path + 'r'))
        g(root)
        print db
        for (key, val) in db.iteritems():
            for (i, v) in enumerate(val):
                if (val[i] != val[(- (i + 1))]):
                    return False
        return True