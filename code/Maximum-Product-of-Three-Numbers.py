import itertools


def get_product(tupleVal):
    return ((tupleVal[0] * tupleVal[1]) * tupleVal[2])


class Solution(object):

    def maximumProduct(self, nums):
        nums.sort()
        temp_nums = (nums[:3] + nums[(-3):])
        for val in set(temp_nums):
            for i in range((temp_nums.count(val) - nums.count(val))):
                temp_nums.remove(val)
        print temp_nums
        all_products = []
        for val in itertools.combinations(temp_nums, 3):
            all_products.append(get_product(val))
        return max(all_products)
