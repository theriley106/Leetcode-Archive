class Solution(object):

    def frequencySort(self, s):
        string = ''
        frequency = {}
        counts = []
        for val in set(s):
            if (str(s.count(val)) not in frequency):
                counts.append(s.count(val))
                frequency[str(s.count(val))] = []
            frequency[str(s.count(val))].append(val)
        for nums in sorted(counts)[::(-1)]:
            for val in frequency[str(nums)]:
                string += str((val * nums))
        return string