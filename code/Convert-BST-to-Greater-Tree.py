class Solution(object):

    def convertBST(self, root):
        self.vals = [0]

        def get_total(root):
            if (root == None):
                return []
            return ((get_total(root.left) + [root.val]) + get_total(root.right))

        def update_total(root):
            if (root == None):
                return
            update_total(root.right)
            root.val += self.vals[(-1)]
            self.vals.append(root.val)
            update_total(root.left)
            return root
        return update_total(root)