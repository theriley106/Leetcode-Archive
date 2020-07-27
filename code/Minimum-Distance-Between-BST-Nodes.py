class Solution(object):

    def minDiffInBST(self, root):
        self.vals = []

        def extract_all(root):
            if (root == None):
                return []
            return ((extract_all(root.left) + [root.val]) + extract_all(root.right))
        a = extract_all(root)
        largest = float('inf')
        for i in range(1, len(a)):
            if (abs((a[i] - a[(i - 1)])) < largest):
                largest = abs((a[i] - a[(i - 1)]))
        return largest