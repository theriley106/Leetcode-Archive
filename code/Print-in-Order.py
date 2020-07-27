import time
import threading


class Foo(object, ):

    def __init__(self):
        self.owner = [1, 2, 3]
        self.firstVal = False
        self.secondVal = False
        self.thirdVal = False
        self.lock = threading.Lock
        pass

    def first(self, printFirst):
        printFirst()
        self.firstVal = True

    def second(self, printSecond):
        idVal = 2
        while (self.firstVal == False):
            pass
        printSecond()
        self.secondVal = True

    def third(self, printThird):
        idVal = 3
        while (self.secondVal == False):
            pass
        printThird()
        self.thirdVal = True
