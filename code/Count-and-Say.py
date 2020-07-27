class Solution(object):

    def countAndSay(self, n):

        def calc_next(prev):
            value = ''
            nums = list(prev)
            while (len(nums) > 0):
                count = 1
                currentValue = nums.pop(0)
                while ((len(nums) > 0) and (currentValue == nums[0])):
                    count += 1
                    nums.pop(0)
                    if (len(nums) == 0):
                        break
                value += '{}{}'.format(count, currentValue)
            return value
        start = '1'
        for i in range((n - 1)):
            start = calc_next(start)
        return start