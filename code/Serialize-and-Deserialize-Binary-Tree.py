import json


class Codec:

    def serialize(self, root):

        def f(root):
            if (root == None):
                return [None]
            return (([root.val] + f(root.left)) + f(root.right))
        e = f(root)
        print e
        return json.dumps(e)

    def deserialize(self, data):
        self.x = json.loads(data)

        def load():
            if (len(self.x) == 0):
                return None
            d = self.x.pop(0)
            r = TreeNode(d)
            if (d == None):
                return None
            r.left = load()
            r.right = load()
            return r
        print self.x
        g = load()
        print g
        return g
