class Solution(object):

    def findMissingRanges(self, nums, lower, upper):
        missing = []
        if (len(nums) == 0):
            if (lower == upper):
                return [str(lower)]
            return ['{}->{}'.format(lower, upper)]
        nums = (([(lower - 1)] + nums) + [(upper + 1), (upper + 2)])
        nums.sort()
        print nums
        for i in range(1, len(nums)):
            r = (nums[i] - nums[(i - 1)])
            if (r > 1):
                if ((nums[(i - 1)] + 1) == (nums[i] - 1)):
                    missing.append(str((nums[(i - 1)] + 1)))
                else:
                    missing.append(
                        '{}->{}'.format((nums[(i - 1)] + 1), (nums[i] - 1)))
        return missing
