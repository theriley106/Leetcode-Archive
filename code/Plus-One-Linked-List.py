class Solution(object):

    def plusOne(self, head):
        number = ''
        while head:
            number += str(head.val)
            head = head.next
        number = (int(number) + 1)
        vals = list([int(x) for x in str(number)])

        def fill():
            if (len(vals) == 0):
                return None
            else:
                node = ListNode(vals.pop(0))
                node.next = fill()
                return node
        return fill()
        print number