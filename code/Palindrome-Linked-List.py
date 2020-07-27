class Solution(object):

    def isPalindrome(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return (''.join([str(e) for e in a]) == ''.join([str(e) for e in a[::(-1)]]))