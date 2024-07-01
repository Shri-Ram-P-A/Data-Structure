class Node:
    def __init__(self,data):
        self.pre = None
        self.data = data
        self.next = None
class Dll:
    def __init__(self):
        self.head=None

    def beg(self,data):
        node = Node(data)
        t=self.head
        self.head = node
        t.pre = node
        node.next = t

    def end(self,data):
        node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        t = cur.next
        cur.next = node
        node.pre = t

    def pos(self,p,data):
        node = Node(data)
        cur = self.head
        for i in range(1,p-1):
            cur = cur.next
        t = cur.next
        node.pre = t
        cur.next = node
        node.next = cur.next.pre
        cur.next.pre = node

    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.pre = cur

    def dbeg(self):
        self.head = self.head.next

    def dend(self):
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def dpos(self,p):
        cur = self.head
        for i in range(1, p - 1):
            cur = cur.next
        t = cur
        cur.next = cur.next.next
        cur.next.pre = t

    def disp(self):
        if self.head is None:
            print("No value present in Linked List")
            return
        cur = self.head
        while cur:
            print(cur.data,end="<->")
            cur = cur.next
        print("None")

dl = Dll()
for i in range(1,6):
    dl.append(i)

# TO ADD THE ELEMENT AT THE BEGINNING
dl.beg(3)

# TO ADD THE ELEMENT AT THE GIVEN POSITION
dl.pos(3,100)

# TO DELETE THE ELEMENT AT BEGINNING
dl.dbeg()

# TO DELETE THE ELEMENT AT THE GIVEN POSITION
dl.dpos(3)

dl.disp()
