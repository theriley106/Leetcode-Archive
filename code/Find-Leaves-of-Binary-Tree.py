class Solution(object):

    def findLeaves(self, root):
        db = {}

        def f(rootz, depth=0):
            if (rootz == None):
                return
            print rootz.val
            if ((rootz.right == None) and (rootz.left == None)):
                if (depth not in db):
                    db[depth] = []
                db[depth].append(rootz.val)
                return
            rootz.left = f(rootz.left, depth)
            rootz.right = f(rootz.right, depth)
            return rootz
        rootz = root
        i = 0
        while True:
            x = len(db)
            root = f(root, i)
            i += 1
            print db
            if (root == None):
                return db.values()