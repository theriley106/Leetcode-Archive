class Solution(object):

    def letterCasePermutation(self, S):
        a = []

        def vals(string, i):
            if (len(S) == i):
                a.append(''.join(string))
                return
            try:
                string[i] = string[i].upper()
                vals(string, (i + 1))
                string[i] = string[i].lower()
                vals(string, (i + 1))
            except Exception as exp:
                print exp
                pass
            a.append(''.join(string))
        vals(list(S), 0)
        return list(set(a))