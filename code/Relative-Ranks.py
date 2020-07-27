class Solution(object):

    def findRelativeRanks(self, nums):
        sortNums = list(nums)
        sortNums.sort()
        sortNums = sortNums[::(-1)]
        prizeList = []
        prizes = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

        def getNum(num):
            return sortNums.index(num)
        for i in range(4, (len(nums) + 1)):
            prizes.append(str(i))
        for val in nums:
            e = getNum(val)
            prizeList.append(prizes[e])
        return prizeList