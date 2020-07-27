class Solution(object):

    def deleteDuplicates(self, head):
        all_vals = []
        while head:
            if (head.val not in all_vals):
                all_vals.append(head.val)
            head = head.next
        return all_vals