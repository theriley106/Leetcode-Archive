import json


class Codec:

    def serialize(self, root):

        def f(root):
            if (root == None):
                return [None]
            return (([root.val] + f(root.left)) + f(root.right))
        e = f(root)
        return json.dumps(e)

    def deserialize(self, data):
        self.vals = json.loads(data)

        def fill():
            if (len(self.vals) == 0):
                return None
            t = self.vals.pop(0)
            if (t == None):
                return t
            root = TreeNode(t)
            root.left = fill()
            root.right = fill()
            return root
        return fill()
