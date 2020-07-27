class Codec:

    def __init__(self):
        self.tree = {}

    def serialize(self, root):
        self.tree[str(root)] = root
        return str(root)

    def deserialize(self, data):
        return self.tree[data]