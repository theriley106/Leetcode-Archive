class Solution(object):

    def findClosestElements(self, arr, k, x):
        closestNums = []
        listOfNums = {}
        for val in arr:
            diff = str(abs((val - x)))
            if (diff not in listOfNums):
                listOfNums[diff] = []
            listOfNums[diff].append(val)
        listOfDiff = [int(x) for x in listOfNums.keys()]
        listOfDiff.sort()
        while True:
            for key in listOfDiff:
                for value in listOfNums[str(key)]:
                    closestNums.append(value)
                    if (len(closestNums) >= k):
                        closestNums.sort()
                        return closestNums