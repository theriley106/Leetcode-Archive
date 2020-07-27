class Solution(object):

    def splitListToParts(self, root, k):
        all_vals = [[] for i in range(k)]
        all_vals2 = [[] for i in range(k)]
        newRoot = root
        number = [0]
        totalCount = [0]

        def insert(node, k):
            if (number[0] >= k):
                number[0] = 0
            all_vals[number[0]].append(node)
            number[0] += 1
            totalCount[0] += 1
        while root:
            insert(root.val, k)
            root = root.next
        h = [len(x) for x in all_vals]
        e = 0
        while newRoot:
            for i in range(h.pop(0)):
                all_vals2[e].append(newRoot.val)
                newRoot = newRoot.next
            e += 1
        return all_vals2