from Queue import *

class BinaryTree:
    class Node:  
        def __init__(self,data,left,right):  
            self.left = left  
            self.data = data  
            self.right = right 
    def __init__(self):  
        self.root = None
    def makeTree(self,data,left,right):  
        self.root = BinaryTree.Node(data,left,right)  
        #left.root = right.root = None  
    def isEmpty(self):  
        return self.root is None
    def preOrder(self,r):  
        if r.root is not None:  
            print(r.root.data)  
            if r.root.left is not None:  
                self.preOrder(r.root.left)  
            if r.root.right is not None:  
                self.preOrder(r.root.right)  
    def inOrder(self,r):  
        if r.root is not None:  
            if r.root.left is not None:  
                self.inOrder(r.root.left)  
            print(r.root.data)  
            if r.root.right is not None:  
                self.inOrder(r.root.right)  
    def postOrder(self,r):  
        if r.root is not None:  
            if r.root.left is not None:  
                self.preOrder(r.root.left)  
            if r.root.right is not None:  
                self.preOrder(r.root.right)  
            print(r.root.data)  
    def levelOrder(self,a):  
        q = Queue()  
        r = a  
        while r is not None:  
            print(r.root.data)
            if r.root.left is not None:  
                q.add(r.root.left)
            if r.root.right is not None:  
                q.add(r.root.right)  
            if q.isEmpty(): 
                print("empty")  
                r = None
            else:  
                r = q.remove()