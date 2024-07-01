class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Ll:
    def __init__(self):
        self.head = None

    def app(self, a):
        node = Node(a)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def beg(self, a):
        node = Node(a)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def mid(self, a, p):
        node = Node(a)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        for i in range(1, p - 1):
            cur = cur.next
        temp = cur.next
        cur.next = node
        node.next = temp

    def dele(self):
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def delbeg(self):
        cur = self.head
        self.head = cur.next

    def delmid(self, a):
        cur = self.head
        for i in range(1, a - 1):
            cur = cur.next
        cur.next = cur.next.next

    def disp(self):
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        # print(cur.data,end="<-")
        # cur = t


l = Ll()
for i in range(1, 11):
    l.app(i)
# l.beg(67)
# l.mid(56,4)
# l.dele()
# l.delbeg()
# l.delmid(5)
l.disp()
