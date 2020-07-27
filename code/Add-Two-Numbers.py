class Solution(object):

    def addTwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num = (int(num1[::(-1)]) + int(num2[::(-1)]))
        return [int(x) for x in list(str(num))[::(-1)]]