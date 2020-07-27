class Solution(object):

    def findRestaurant(self, list1, list2):
        indexSums = {}
        bigList = (list1 + list2)
        for val in [x for x in set(bigList) if (bigList.count(x) == 2)]:
            indexSums[val] = (list1.index(val) + list2.index(val))
        minVal = min(indexSums.values())
        return [x for (x, i) in indexSums.iteritems() if (i == minVal)]