class Solution(object):

    def findReplaceString(self, S, indexes, sources, targets):
        newString = list(S)
        for i in range(len(indexes)):
            x = ''.join(newString[indexes[i]:(indexes[i] + len(sources[i]))])
            if (x == sources[i]):
                newString[indexes[i]] = targets[i]
                for e in range((indexes[i] + 1), (indexes[i] + len(sources[i]))):
                    newString[e] = None
        a = [e for e in newString if (e != None)]
        return ''.join(a)