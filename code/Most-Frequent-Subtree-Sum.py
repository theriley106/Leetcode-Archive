class Solution(object):

    def findFrequentTreeSum(self, root):
        db = {}

        def search(root):
            if (root == None):
                return 0
            x = ((search(root.left) + root.val) + search(root.right))
            if (x not in db):
                db[x] = 0
            db[x] += 1
            return x
        search(root)
        return [k for (k, v) in db.iteritems() if (v == max(db.values()))]
        g = sorted([], key=(lambda k: k[1]), reverse=True)
        return [h[0] for h in g]
        print db