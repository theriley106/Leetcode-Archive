class Solution(object):

    def countSmaller(self, nums):
        db = {}
        dbSet = []
        x = [0 for i in range(len(nums))]
        start = (-1)

        def binary_search(value, array, index=0):
            if (len(array) == 0):
                return index
            middle = (len(array) / 2)
            if (array[middle] == value):
                return ((index + middle) - len([x for x in array[:middle] if (x == value)]))
            if (value < array[middle]):
                return binary_search(value, array[:middle], index)
            else:
                return binary_search(value, array[(middle + 1):], ((index + middle) + 1))

        def insert_val(value):
            r = binary_search(value, dbSet)
            dbSet.insert(r, value)
            return r
        while ((len(nums) * (-1)) != (start + 1)):
            x[start] = insert_val(nums[start])
            start = (start - 1)
        return x