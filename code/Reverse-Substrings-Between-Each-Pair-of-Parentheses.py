class Solution(object):

    def reverseParentheses(self, s):

        def reverse(string):
            return string[::(-1)]
        a = '(ed(et(oc))el)'
        stack = []
        tempStrings = []
        newString = ''
        word = list(s)

        def recursive():
            string = ''
            while (len(word) > 0):
                letter = word.pop(0)
                if (letter == '('):
                    string += recursive()
                elif (letter == ')'):
                    return string[::(-1)]
                else:
                    string += letter
            return string
        return recursive()