class Solution(object):

    def longestRepeatingSubstring(self, S):
        longest = 1

        def sliding_window(size, array):
            e = set()
            for i in range(((len(S) - size) + 1)):
                x = array[i:(i + size)]
                if (x in e):
                    return True
                e.add(x)
            return False
        count = 0
        i = 2
        while (sliding_window(i, S) == True):
            count = i
            i += 1
        return count