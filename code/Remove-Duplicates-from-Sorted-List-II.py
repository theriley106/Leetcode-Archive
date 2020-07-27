class Solution(object):

    def deleteDuplicates(self, head):
        vals = []
        while (head != None):
            vals.append(head.val)
            head = head.next
        return [h for h in vals if (vals.count(h) < 2)]