class Solution(object):

    def twoSum(self, numbers, targetVal):

        def bst(nums, target):
            if (len(nums) == 0):
                return
            if (len(nums) == 1):
                if (nums[0] == target):
                    return nums[0]
                else:
                    return
            x = nums[(len(nums) / 2)]
            if (x > target):
                return bst(nums[:(len(nums) / 2)], target)
            elif (x == target):
                return x
            elif (x < target):
                return bst(nums[(len(nums) / 2):], target)
        for val in sorted(list(set(numbers)), reverse=True):
            t = (targetVal - val)
            h = list(numbers)
            h.remove(val)
            g = bst(sorted(list(set(h))), t)
            print g
            if (g != None):
                a = (numbers.index(val) + 1)
                b = (numbers.index(g) + 1)
                if (b == a):
                    b += 1
                return sorted([a, b])