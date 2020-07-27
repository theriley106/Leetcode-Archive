class Codec:

    def encode(self, strs):
        return strs[::(-1)]

    def decode(self, s):
        return s[::(-1)]