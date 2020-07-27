class Solution(object):

    def validMountainArray(self, A):
        if (len(A) < 3):
            return False
        largest = max(A)
        largestIndex = A.index(largest)
        if ((largestIndex == (len(A) - 1)) or (largestIndex == 0)):
            return False
        prevVal = largest
        for i in range((largestIndex + 1), len(A)):
            print 'COMPARING {} > {}'.format(A[i], prevVal)
            if (A[i] >= prevVal):
                return False
            prevVal = A[i]
        prevVal = largest
        for i in range((largestIndex - 1), (-1), (-1)):
            print 'COMPARING {} < {}'.format(A[i], prevVal)
            if (A[i] >= prevVal):
                print 'NUM 2'
                return False
            prevVal = A[i]
        return True