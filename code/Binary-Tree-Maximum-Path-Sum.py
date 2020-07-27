class Solution(object):

    def maxPathSum(self, root):
        self.max = float('-inf')

        def check(root, path=[]):
            if (root == None):
                return (0, [])
            x = root.val
            (l, lz) = check(root.left, (path + [root.val]))
            (r, rz) = check(root.right, (path + [root.val]))
            mVal = max([((x + l) + r), x, (x + l), (x + r)])
            print mVal
            if (mVal > self.max):
                self.max = mVal
            returnVal = 0
            return (max([x, (x + l), (x + r)]), ((lz + [x]) + rz))
        check(root)
        return self.max