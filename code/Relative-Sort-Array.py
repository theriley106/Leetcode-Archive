class Solution(object):

    def relativeSortArray(self, arr1, arr2):
        return sorted(arr1, key=(lambda k: (arr2.index(k) if (k in arr2) else (k + len(arr2)))))