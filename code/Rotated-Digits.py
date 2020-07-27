VALID_NUMS = [1, 5, 2, 6, 9, 0, 8]
NUM_DICT = {'1': '1', '5': '2', '2': '5',
            '6': '9', '9': '6', '0': '0', '8': '8'}


class Solution(object):

    def can_rotate(self, num):
        rotate = ''
        num = str(num)
        for val in num:
            if (val not in NUM_DICT):
                return False
            else:
                rotate += NUM_DICT[val]
        return (num != rotate)

    def rotatedDigits(self, N):
        count = 0
        for val in range(1, (N + 1)):
            if (self.can_rotate(val) == True):
                count += 1
        return count
