class Solution(object):

    def cloneGraph(self, node):
        db = {}

        def traverse(node):
            if (node in db):
                return
            if (node == None):
                return
            db[node] = Node(node.val)
            for n in node.neighbors:
                traverse(n)
        traverse(node)
        for (k, v) in db.iteritems():
            v.neighbors = [db[x] for x in k.neighbors]
        finished = set()

        def traverse2(n):
            node = db[n]
            return node
        return db.get(node)
        node = traverse2(node)
        return node