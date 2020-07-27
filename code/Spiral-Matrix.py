class Solution(object):

    def spiralOrder(self, matrix):

        def rotate(matrix):
            x = list(matrix)
            if (len(x) == 0):
                return []
            vals = list(set(x[0]))
            if ((len(vals) == 0) and (vals[0] == 'x')):
                x.pop(0)
            if (x[0][(-1)] == 'x'):
                for i in range(len(x)):
                    x[i].pop((-1))
            if (len(x) == 0):
                return None
            while (len(x) < len(x[0])):
                x.append(['x' for i in range(len(x[0]))])
            while (len(x[0]) < len(x)):
                for i in range(len(x)):
                    x[i].append('x')
            newMatrix = [[] for i in range(len(x[0]))]
            lenVal = len(x)
            for e in range(len(x[0])):
                for i in range(lenVal):
                    newMatrix[((- i) - 1)].append(x[0].pop(0))
                x.pop(0)
            return newMatrix
        matrix = matrix
        allVals = []
        while (len(matrix) != 0):
            if (len(matrix) != 0):
                for v in matrix:
                    print v
                count = 0
                if (matrix != None):
                    for g in matrix[0]:
                        if (g != 'x'):
                            count += 1
                            allVals.append(g)
                        else:
                            break
                    matrix.pop(0)
                if (count > 0):
                    matrix = rotate(matrix)
        return allVals