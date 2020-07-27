class MyLinkedList(object, ):

    def __init__(self):
        self.a = []

    def get(self, index):
        if (len(self.a) <= index):
            return (-1)
        return self.a[index]

    def addAtHead(self, val):
        self.a.insert(0, val)

    def addAtTail(self, val):
        self.a.append(val)

    def addAtIndex(self, index, val):
        if (len(self.a) == index):
            self.a.append(val)
        elif (len(self.a) < index):
            return
        else:
            self.a.insert(index, val)

    def deleteAtIndex(self, index):
        if (index >= len(self.a)):
            return
        self.a.pop(index)