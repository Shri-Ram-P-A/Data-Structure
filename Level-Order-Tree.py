class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class Tree:
    def __init__(self):
        self.root = None

    def ins(self,arr):
        self.root = self.insert(arr,self.root,0,len(arr))

    # insert through numerical
    def insert(self,arr,node,s,e):
        if(s<e):
            node = Node(arr[s])
            node.left=self.insert(arr,node.left,(s*2)+1,e)
            node.right=self.insert(arr,node.right,(s*2)+2,e)
        return node

    # insert through Queue
    def insertqueue(self, arr):
        if not arr:
            return None
        self.root = Node(arr.pop(0))
        q = [self.root]
        while arr:
            t = q.pop(0)
            if arr:
                t.left = Node(arr.pop(0))
                q.append(t.left)
            if arr:
                t.right = Node(arr.pop(0))
                q.append(t.right)

    def inOrder(self,root):
        if root:
            print(root.data,end=" ")
            self.inOrder(root.left)

            self.inOrder(root.right)


tree = Tree()
arr = [0,1,2,3,4,5,6,7,8,9]
tree.insertqueue(arr)
tree.inOrder(tree.root)

