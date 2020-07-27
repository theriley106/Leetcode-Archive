class Solution(object):

    def nextLargerNodes(self, head):
        stack = []
        listVals = []
        while head:
            listVals.append(head.val)
            head = head.next
        returnVals = ([0] * len(listVals))
        for i in range((len(listVals) - 1), (-1), (-1)):
            currentVal = listVals[i]
            if (len(stack) > 0):
                while (stack[(-1)] <= currentVal):
                    stack.pop((-1))
                    if (len(stack) == 0):
                        break
            if (len(stack) > 0):
                listVals[i] = stack[(-1)]
            else:
                listVals[i] = 0
            stack.append(currentVal)
        return listVals