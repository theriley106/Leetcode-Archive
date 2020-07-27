class Solution(object):

    def swapPairs(self, head):
        listVal = []
        while (head != None):
            listVal.append(head.val)
            head = head.next
        for i in range(0, (len(listVal) - 1), 2):
            tempVal = listVal[i]
            listVal[i] = listVal[(i + 1)]
            listVal[(i + 1)] = tempVal
        return listVal