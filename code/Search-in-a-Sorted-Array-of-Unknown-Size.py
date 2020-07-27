class Solution(object):

    def search(self, reader, target):
        index = 0
        r = reader.get(index)
        while (r != 2147483647):
            index += 1
            if (r == target):
                return (index - 1)
            r = reader.get(index)
        return (-1)