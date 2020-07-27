class Solution(object):

    def sumEvenGrandparent(self, root):
        self.total = 0

        def traverse(root, prev=[], found=False):
            if (root == None):
                return
            if (len(prev) == 3):
                prev.pop(0)
            if (len(prev) == 2):
                found = ((prev[0] % 2) == 0)
            if found:
                print root.val
                self.total += root.val
            traverse(root.left, (prev + [root.val]), found)
            traverse(root.right, (prev + [root.val]), found)
        traverse(root)
        return self.total