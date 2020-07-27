class Solution(object):

    def entityParser(self, text):
        db = {'&quot;': '"', '&apos;': "'", '&amp;': 'PLACEHOLDER',
              '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        for (k, v) in db.iteritems():
            text = text.replace(k, v)
        return text.replace('PLACEHOLDER', '&')
        return page.title.string
