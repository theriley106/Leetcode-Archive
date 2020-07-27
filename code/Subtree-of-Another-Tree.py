class Solution(object):

    def isSubtree(self, s, t):
        self.found = False

        def traverse(root):
            if (root == None):
                return ['None']
            return ((((((['L'] + traverse(root.left)) + ['L']) + [root.val]) + ['R']) + traverse(root.right)) + ['R'])
        a = ''.join([str(x) for x in traverse(s)])
        b = ''.join([str(x) for x in traverse(t)])
        return (b in a)
        return self.found