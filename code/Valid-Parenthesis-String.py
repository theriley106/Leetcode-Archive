class Solution(object):

    def checkValidString(self, s):
        listVal = []
        for letter in s:
            if ((letter == '(') or (letter == '*')):
                listVal.append('blah')
            elif (len(listVal) > 0):
                listVal.pop()
            else:
                return False
        listVal = []
        for letter in s[::(-1)]:
            if ((letter == ')') or (letter == '*')):
                listVal.append('blah')
            elif (len(listVal) > 0):
                listVal.pop()
            else:
                return False
        return True