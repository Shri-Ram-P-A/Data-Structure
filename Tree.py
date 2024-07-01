class Node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,a):
        self.root = self._insert(self.root,a)
    def _insert(self,node,a):
        if node is None:
            return Node(a)
        if a < node.data:
            node.left = self._insert(node.left,a)
        if a >= node.data:
            node.right = self._insert(node.right,a)
        return node

    def traverse_inorder(self):
        self._inOrder(self.root,"")
    def _inOrder(self,root,n):
        if root:
            self._inOrder(root.left,"\t"+n)
            print(n, root.data)
            self._inOrder(root.right,"\t"+n)

    def traverse_preorder(self,root):
        if root is not None:
            print(root.data)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def traverse_postorder(self):
        return self._postorder(self.root,"")
    def _postorder(self,root,n):
        if root is not None:
            self._postorder(root.left," "+n)
            self._postorder(root.right," "+n)
            print(n,root.data)

    def find(self,a):
        return self._find(self.root,a)
    def _find(self,node,a):
        if node is None:
            return False
        elif a == node.data:
            return True
        elif a < node.data:
            return self._find(node.left,a)
        elif a > node.data:
            return self._find(node.right,a)
        return False

    def Max(self):
        return self.max(self.root)
    def max(self,node):
        if node.right is None:
            return node.data
        return self.max(node.right)

    def Min(self):
        return self.min(self.root)
    def min(self,node):
        if node.left is None:
            return node.data
        return self.min(node.left)
    
    def delete(self, i):
        return self._delete(self.root,i)
    def _delete(self,node,a):
        if a > node.data:
            if node.right:
                node.right = self._delete(node.right,a)
        elif a < node.data:
            if node.left:
                node.left = self._delete(node.left,a)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            
            min_val = self.Min(node.right)
            node.data = min_val
            node.right = self._delete(node.right,min_val)
        return self.traverse_inorder()


tree = Tree()

tree.insert(4)
tree.insert(3)
tree.insert(5)
tree.insert(6)
tree.insert(6)

tree.insert(9)
tree.insert(1)
tree.insert(10)
tree.traverse_inorder()

tree.delete(5)
