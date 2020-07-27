class Solution(object):

    def copyRandomList(self, head):
        import random
        a = []
        g = []
        db = {None: None}
        temp_head = head
        e = []
        while temp_head:
            randomVal = temp_head.random
            if (randomVal != None):
                e.append(randomVal)
                g.append(temp_head)
                print randomVal
            nodeVal = Node(temp_head.val, temp_head.next, randomVal)
            db[temp_head] = nodeVal
            a.append(nodeVal)
            temp_head = temp_head.next

        def fill():
            if (len(a) == 0):
                return
            nodeVal = a.pop(0)
            nodeVal.next = fill()
            nodeVal.random = db[nodeVal.random]
            return nodeVal
        return fill()