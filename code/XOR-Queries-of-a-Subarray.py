class Solution(object):

    def xorQueries(self, arr, queries):
        newArray = [0]
        for (i, val) in enumerate(arr):
            x = (newArray[(-1)] ^ arr[i])
            newArray.append(x)
        return [(newArray[(val[1] + 1)] ^ newArray[val[0]]) for val in queries]