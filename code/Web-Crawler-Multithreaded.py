import threading


class Solution(object):

    def crawl(self, startUrl, htmlParser):
        h = htmlParser
        Lock = threading.Lock()

        def get_hostname(string):
            return ('http://' + string.replace('http://', '').partition('/')[0])
        self.hostName = get_hostname(startUrl)
        self.visited = set()

        def crawl_vals(url):
            cont = True
            Lock.acquire()
            if ((url not in self.visited) and (get_hostname(url) == self.hostName)):
                self.visited.add(url)
            else:
                cont = False
            Lock.release()
            if cont:
                t = [threading.Thread(target=crawl_vals, args=(urlz,)) for urlz in h.getUrls(
                    url) if (get_hostname(urlz) == self.hostName)]
                for thread in t:
                    thread.start()
                for thread in t:
                    thread.join()
        crawl_vals(startUrl)
        return list(self.visited)
