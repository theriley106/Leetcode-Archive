class Solution(object):

    def crawl(self, startUrl, htmlParser):

        def get_hostname(string):
            return (('http://' + string.replace('http://', '').partition('/')[0]) + '/')
        self.allVals = set()
        self.hostname = get_hostname(startUrl)

        def scrape(url):
            if ((get_hostname(url) != self.hostname) or (url in self.allVals)):
                return
            self.allVals.add(url)
            for val in htmlParser.getUrls(url):
                scrape(val)
        scrape(startUrl)
        return self.allVals