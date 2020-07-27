class Solution(object):

    def maxLevelSum(self, root):
        db = {}

        def search(root, row=0):
            if (root == None):
                return
            if (row not in db):
                db[row] = 0
            db[row] += root.val
            search(root.right, (row + 1))
            search(root.left, (row + 1))
        search(root)
        x = max(db.values())
        for (k, v) in db.iteritems():
            if (v == x):
                return (k + 1)