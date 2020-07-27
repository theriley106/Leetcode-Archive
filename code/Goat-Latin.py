class Solution(object):

    def toGoatLatin(self, S):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels += [x.upper() for x in vowels]
        final = []
        for (i, val) in enumerate(S.split(' ')):
            if (val[0] in vowels):
                val = (val + 'ma')
            else:
                g = list(val)
                x = g.pop(0)
                g.append(x)
                val = (''.join(g) + 'ma')
            for e in range((i + 1)):
                val += 'a'
            final.append(val)
        return ' '.join(final)