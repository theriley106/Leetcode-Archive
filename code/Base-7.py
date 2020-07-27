import numpy


class Solution(object):

    def convertToBase7(self, num):
        return str(numpy.base_repr(num, 7))
