class Solution(object):

    def tree2str(self, t):

        def traverse(root):
            if (root == None):
                return '()'
            if ((root.right == None) and (root.left == None)):
                return '({})'.format(root.val)
            return ((('({}'.format(root.val) + traverse(root.left)) + traverse(root.right)) + ')')
        return traverse(t).replace(')()', ')')[1:(-1)]