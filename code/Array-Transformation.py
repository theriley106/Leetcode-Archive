class Solution(object):

    def transformArray(self, arr):
        array = arr

        def change(tempArray, index):
            if ((tempArray[index] < tempArray[(index - 1)]) and (tempArray[index] < tempArray[(index + 1)])):
                return 1
            elif ((tempArray[index] > tempArray[(index - 1)]) and (tempArray[index] > tempArray[(index + 1)])):
                return (-1)
            return 0
        for e in range(len(arr)):
            changes = [0 for i in range(len(array))]
            for i in range(1, (len(array) - 1)):
                changes[i] = change(array, i)
            for (i, val) in enumerate(changes):
                array[i] += val
        return array