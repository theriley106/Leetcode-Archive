class Solution(object):

    def breakPalindrome(self, palindrome):
        palindrome = list(palindrome)
        aCount = 0

        def is_palindrome(string):
            string = list(string)
            a = string.pop(0)
            try:
                b = string.pop((-1))
            except:
                return True
            while ((a == b) and (len(string) > 0)):
                a = string.pop(0)
                try:
                    b = string.pop((-1))
                except:
                    return True
            return (a == b)
        vals = []
        for i in range(len(palindrome)):
            if (palindrome[i] != 'a'):
                x = palindrome[i]
                palindrome[i] = 'a'
                if (not is_palindrome(''.join(palindrome))):
                    vals.append(''.join(palindrome))
                palindrome[i] = x
            else:
                aCount += 1
                if (aCount > 1):
                    x = palindrome[i]
                    palindrome[i] = 'b'
                    if (not is_palindrome(''.join(palindrome))):
                        vals.append(''.join(palindrome))
                    palindrome[i] = x
        if (len(vals) > 0):
            return sorted(vals)[0]
        return ''