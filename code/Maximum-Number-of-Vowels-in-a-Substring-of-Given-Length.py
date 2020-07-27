class Solution(object):

    def maxVowels(self, s, k):

        def count(info):
            count = 0
            for val in list('aeiou'):
                count += info.get(val, 0)
            return count
        info = {}
        filled = False
        maxCount = 0
        for i in range(((len(s) - k) + 1)):
            if (filled == False):
                for v in s[i:(i + k)]:
                    if (v not in info):
                        info[v] = 0
                    info[v] += 1
                filled = True
            else:
                if (s[i:(i + k)][(-1)] not in info):
                    info[s[i:(i + k)][(-1)]] = 0
                info[s[i:(i + k)][(-1)]] += 1
            maxCount = max(count(info), maxCount)
            info[s[i:(i + k)][0]] -= 1
        return maxCount