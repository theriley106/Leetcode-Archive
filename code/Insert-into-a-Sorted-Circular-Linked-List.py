class Solution(object):

    def insert(self, head, insertVal):
        vals = []
        newVals = []
        newNode = []
        values = []

        def fill_linked_list(i=0, node=None):
            if (i == len(newVals)):
                return newVals[0]
            node = newVals[i]
            node.val = values.pop(0)
            node.next = fill_linked_list((i + 1), node)
            return node
        db = {}
        if (head == None):
            return Node(insertVal)
        tempNode = head
        insert = False
        while (tempNode not in db):
            db[tempNode] = True
            d = tempNode
            tempNode = tempNode.next
            if ((tempNode.val > insertVal) and (insert == False)):
                g = Node(insertVal)
                newVals.append(g)
                newNode.append(g)
                insert = True
            vals.append(tempNode.val)
            newVals.append(tempNode)
        if (insert == False):
            print 'INSERT'
            g = Node(insertVal)
            newNode.append(g)
            newVals.insert((-1), g)
        newVals.sort(key=(lambda k: k.val))
        for value in [v.val for v in newVals]:
            values.append(value)
        print values
        while (newVals[0].val != head.val):
            newVals.append(newVals.pop(0))
            values.append(values.pop(0))
        print values
        x = fill_linked_list()
        return x
        while ((x != head) and (x == newNode[0])):
            print 'ROTATE'
            x = x.next
        return x
        return db