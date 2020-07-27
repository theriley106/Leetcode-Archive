class Solution(object):

    def longestValidParentheses(self, s):
        stack = [(-1)]
        size = 0
        count = 0
        a = {')': '(', '(': ')'}
        maxVal = 0
        for (i, letter) in enumerate(s):
            if (letter == '('):
                stack.append(i)
            else:
                stack.pop((-1))
                if (len(stack) > 0):
                    x = (i - stack[(-1)])
                    if (x > maxVal):
                        maxVal = x
                else:
                    stack.append(i)
        return maxVal