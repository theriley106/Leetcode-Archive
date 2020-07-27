class Solution(object):

    def reverseString(self, s, i=0):
        n = len(s)

        def swap_two(one, two):
            if (two <= one):
                return
            tmp = s[one]
            s[one] = s[two]
            s[two] = tmp
            swap_two((one + 1), (two - 1))
        return swap_two(0, (n - 1))