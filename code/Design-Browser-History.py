class ListNode(object, ):

    def __init__(self, prev, url):
        self.next = None
        self.prev = prev
        self.url = url


class BrowserHistory(object, ):

    def __init__(self, homepage):
        self.page = ListNode(None, homepage)

    def visit(self, url):
        self.page.next = ListNode(self.page, url)
        self.page.next.prev = self.page
        self.page = self.page.next

    def back(self, steps):
        url = self.page.url
        for i in range(steps):
            if (self.page.prev == None):
                break
            self.page = self.page.prev
            url = self.page.url
        return self.page.url

    def forward(self, steps):
        url = self.page.url
        for i in range(steps):
            if (self.page.next == None):
                break
            self.page = self.page.next
            url = self.page.url
        return self.page.url
