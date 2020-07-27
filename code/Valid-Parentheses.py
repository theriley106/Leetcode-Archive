class Solution(object):

    def isValid(self, s):
        stack = []
        if ((len(s) % 2) != 0):
            return False
        openCloseDict = {'}': '{', ']': '[', ')': '('}
        openChars = ['(', '{', '[']
        closedChars = [')', '}', ']']
        for char in s:
            if (char in openChars):
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                if (stack.pop() != openCloseDict[char]):
                    return False
        return (len(stack) == 0)