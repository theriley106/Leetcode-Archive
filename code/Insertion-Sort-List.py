class Solution(object):

    def insertionSortList(self, head):

        def insert(listVal, val):
            found = False
            for i in range(len(listVal)):
                if (listVal[i] > val):
                    listVal.insert(i, val)
                    found = True
                    break
            if (found == False):
                listVal.append(val)
            return listVal
        headVals = []
        while head:
            headVals.append(head.val)
            head = head.next
        j = list(headVals)
        if (len(headVals) == 0):
            return None
        listVals = [headVals.pop(0)]
        for i in range(len(headVals)):
            listVals = insert(listVals, headVals[0])
            headVals.pop(0)

        def fill(root):
            if (len(listVals) == 0):
                return
            head = ListNode(listVals.pop(0))
            head.next = fill(root)
            return head
        return fill(head)