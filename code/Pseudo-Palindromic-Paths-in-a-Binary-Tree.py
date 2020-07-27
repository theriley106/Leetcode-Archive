class Solution(object):

    def pseudoPalindromicPaths(self, root):

        def can_be_palindrome(listOfVals):
            info = {}
            for v in listOfVals:
                if (v not in info):
                    info[v] = 0
                info[v] += 1
            oddCount = 0
            evenCount = 0
            for x in info.values():
                if ((x % 2) == 0):
                    evenCount += 1
                else:
                    oddCount += 1
            return (oddCount < 2)
        self.vals = []

        def check(root, path=[]):
            if (root == None):
                return
            if ((root.left == None) and (root.right == None)):
                self.vals.append((path + [root.val]))
                return
            check(root.left, (path + [root.val]))
            check(root.right, (path + [root.val]))
        check(root)
        count = 0
        for v in self.vals:
            if can_be_palindrome(v):
                count += 1
        return count
        print self.vals