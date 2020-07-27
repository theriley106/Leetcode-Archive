class Solution(object):

    def isCompleteTree(self, root):
        self.db = {}

        def f(root, index=0):
            if (root == None):
                if (index not in self.db):
                    self.db[index] = []
                self.db[index].append(None)
                return
            if (index not in self.db):
                self.db[index] = []
            self.db[index].append(root.val)
            f(root.left, (index + 1))
            f(root.right, (index + 1))
        f(root)
        if (len(self.db) > 1):
            h = (max(self.db.keys()) - 1)
        else:
            h = 1
        found = False
        print self.db
        for val in self.db[h][::(-1)]:
            if (val != None):
                found = True
            if ((val == None) and (found == True)):
                return False
        for i in range(h):
            if ((len(set(self.db[i])) > 1) and (None in set(self.db[i]))):
                return False
        return True