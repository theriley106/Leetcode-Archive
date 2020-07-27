class Solution(object):

    def topKFrequent(self, words, k):
        a = [(words.count(word), word) for word in set(words)]
        maxNum = max([x[0] for x in a])
        a.sort(key=(lambda x: x[0]), reverse=True)
        h = {}
        totalCount = 0
        order = []
        prevVal = None
        for val in a:
            if ((val[0] != prevVal) or (totalCount <= k)):
                if (str(val[0]) not in h):
                    order.append(str(val[0]))
                    h[str(val[0])] = []
                h[str(val[0])].append(val[1])
            else:
                break
            if (prevVal != val[0]):
                totalCount += 1
            prevVal = val[0]
        for val in order:
            h[val] = sorted(h[val])
        newK = []
        for i in range(k):
            if (len(h[order[0]]) == 0):
                order.pop(0)
            newK.append(h[order[0]].pop(0))
        return newK