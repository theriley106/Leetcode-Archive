class Solution(object):

    def reformat(self, s):
        db = {'int': [], 'string': []}
        for v in s:
            try:
                int(v)
                db['int'].append(v)
            except:
                db['string'].append(v)
        a = ''
        if (len(db['int']) > len(db['string'])):
            while (db['int'] or db['string']):
                try:
                    a += db['int'].pop(0)
                except:
                    return ''
                try:
                    a += db['string'].pop(0)
                except:
                    break
        else:
            while (db['int'] or db['string']):
                try:
                    a += db['string'].pop(0)
                except:
                    return ''
                try:
                    a += db['int'].pop(0)
                except:
                    break
        if (len(a) != len(s)):
            return ''
        return a