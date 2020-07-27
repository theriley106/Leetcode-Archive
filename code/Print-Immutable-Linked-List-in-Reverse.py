class Solution(object):

    def printLinkedListInReverse(self, head):
        a = []
        e = 0
        while (head != None):
            a.append(head)
            e += 1
            head = head.getNext()
        for val in a[::(-1)]:
            val.printValue()
        return 'adfas'