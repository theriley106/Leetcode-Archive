import threading


class FooBar(object, ):

    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo):
        for i in xrange(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.fooTurn = False
            self.bar_lock.release()

    def bar(self, printBar):
        for i in xrange(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()
