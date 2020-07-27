class Solution(object):

    def deepestLeavesSum(self, root):
        db = {}

        def traverse(root, depth=0):
            if (root == None):
                return
            if (depth not in db):
                db[depth] = 0
            db[depth] += root.val
            traverse(root.left, (depth + 1))
            traverse(root.right, (depth + 1))
        traverse(root)
        x = max(db.keys())
        return db[x]