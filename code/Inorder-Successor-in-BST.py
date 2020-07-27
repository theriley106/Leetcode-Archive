class Solution(object):

    def inorderSuccessor(self, root, p):
        db = []

        def search(root):
            if (root == None):
                return
            search(root.left)
            db.append(root)
            search(root.right)
        search(root)
        db = sorted(db, key=(lambda k: k.val))
        for valz in db:
            if (valz.val > p.val):
                return valz