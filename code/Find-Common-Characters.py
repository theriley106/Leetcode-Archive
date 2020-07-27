class Solution(object):

    def commonChars(self, A):
        inAll = []
        for (letter, count) in [(letter, min([x.count(letter) for x in A])) for letter in set(''.join(A))]:
            for i in range(count):
                inAll.append(letter)
        return inAll