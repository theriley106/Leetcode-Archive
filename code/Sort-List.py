def sort_list(left, right):
    result = []
    while ((len(left) > 0) and (len(right) > 0)):
        if (left[0] <= right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while (len(left) > 0):
        result.append(left.pop(0))
    while (len(right) > 0):
        result.append(right.pop(0))
    return result


class Solution(object):

    def __init__(self):
        self.list = []

    def sortList(self, head):
        if (type(head) != list):
            h = []
            while head:
                h.append(head.val)
                head = head.next
            head = h
        if (len(head) <= 1):
            return head
        middle = (len(head) / 2)
        first = head[:middle]
        second = head[middle:]
        left = self.sortList(first)
        right = self.sortList(second)
        return sort_list(left, right)
