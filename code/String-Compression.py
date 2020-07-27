class Solution(object):

    def compress(self, chars):
        index = 0
        while (index < len(chars)):
            a = chars[index]
            b = False
            g = 1
            if ((index + 1) < len(chars)):
                while (chars[(index + 1)] == a):
                    g += 1
                    b = True
                    chars.pop((index + 1))
                    if ((index + 1) >= len(chars)):
                        break
            if b:
                for val in str(g):
                    chars.insert((index + 1), val)
                    index += 1
            index += 1
        return len(chars)