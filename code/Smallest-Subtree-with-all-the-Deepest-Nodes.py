class Solution(object):

    def is_leaf(self, root):
        return ((root.right == None) and (root.left == None))

    def subtreeWithAllDeepest(self, root):
        self.db = {}
        self.depthFromRoot = {}
        self.maxDepth = 0
        self.maxPath = []

        def traverse(root, depth=1, path=[]):
            if (root == None):
                return None
            self.depthFromRoot[root] = depth
            if self.is_leaf(root):
                if (depth > self.maxDepth):
                    self.maxDepth = depth
                    self.maxPath = (path + [root])
                    return None
                elif (depth == self.maxDepth):
                    self.maxPath += (path + [root])
                    return None
                else:
                    return None
            traverse(root.left, (depth + 1), (path + [root]))
            traverse(root.right, (depth + 1), (path + [root]))
        traverse(root)
        tempDict = {}
        if (len(list(set(self.maxPath))) == len(self.maxPath)):
            return self.maxPath[(-1)]
        for val in self.maxPath:
            if (val not in tempDict):
                tempDict[val] = 0
            tempDict[val] += 1
        for (k, v) in tempDict.iteritems():
            if (v > 1):
                print k
        return sorted([k for (k, v) in tempDict.iteritems() if (v == max(tempDict.values()))], key=(lambda t: self.depthFromRoot[t]))[(-1)]