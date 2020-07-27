class Solution(object):

    def numOfSubarrays(self, arr, k, threshold):

        def sliding_window(array, size):
            average = None
            prevNum = None
            prevSum = None
            count = 0
            for i in xrange(((len(array) - size) + 1)):
                if (average == None):
                    prevSum = sum(array[i:(i + size)])
                    average = (prevSum / size)
                else:
                    prevSum = (
                        (prevSum - array[(i - 1)]) + array[((i + size) - 1)])
                    average = average
                if ((float(prevSum) / float(size)) >= threshold):
                    count += 1
            return count
        return sliding_window(arr, k)
