class Solution(object):

    def duplicateZeros(self, arr):
        a = len(arr)
        i = 0
        for e in range(a):
            if (arr[i] == 0):
                arr.insert(i, 0)
                i += 1
            i += 1
        while (len(arr) > a):
            arr.pop((-1))