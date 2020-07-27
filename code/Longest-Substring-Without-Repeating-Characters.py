class Solution(object):

    def lengthOfLongestSubstring(self, s):
        a = {}
        for val in s:
            if (val not in a):
                a[val] = 0
            a[val] += 1

        def is_repeat(value):
            return (max(a.values()) == 1)

        def sliding_window(size):
            for i in range(((len(s) - size) + 1)):
                if (len(s[i:(i + size)]) == len(set(s[i:(i + size)]))):
                    return True
            return False
        for i in range(1, (len(s) + 1)):
            if (sliding_window(i) == False):
                return (i - 1)
        return len(s)