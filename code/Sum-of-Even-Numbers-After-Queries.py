class Solution(object):

    def sumEvenAfterQueries(self, A, queries):
        y = []
        newList = []
        for x in A:
            if ((x % 2) == 0):
                newList.append(x)
            else:
                newList.append(0)
        prevSum = sum(newList)
        print newList
        print prevSum
        for (i, val) in enumerate(queries):
            prevVal = A[val[1]]
            A[val[1]] += val[0]
            if (((A[val[1]] % 2) == 0) and ((prevVal % 2) == 0)):
                prevSum = (prevSum - prevVal)
                prevSum += A[val[1]]
            elif ((A[val[1]] % 2) == 0):
                newList[i] = A[val[1]]
                prevSum += A[val[1]]
            elif (((prevVal % 2) == 0) and ((A[val[1]] % 2) != 0)):
                prevSum = (prevSum - prevVal)
                newList[i] = 0
            y.append(prevSum)
        return y