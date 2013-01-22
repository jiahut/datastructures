from Stack import Stack
from Queue import Queue
from BinaryTree import BinaryTree

def trrce(obj):
	print(obj.info())


print("--------------Stack----------------")

s = Stack(5)  
s.push(1)
trrce(s)
s.push(2)
trrce(s)  
s.push(3)
trrce(s)  
s.push(4)
trrce(s)  
s.push(5)  
trrce(s)
print("head = ", s.head())
print("tail = ", s.tail())
print("isFull? ", s.isFull())
s.pop()  
trrce(s)
s.pop()
trrce(s)
s.pop()
trrce(s)
s.pop()
trrce(s)
s.pop()
trrce(s)
print("isEmpty? ",s.isEmpty())

print("--------------Queue----------------")

q = Queue(5)
q.add(1)
trrce(q)
q.add(2)
trrce(q)
q.add(3)
trrce(q)
q.add(4)
trrce(q)
q.add(5)
trrce(q)
print("first = ", q.first())
print("last = ", q.last())
print("isFull? ", q.isFull())
q.remove()
trrce(q)
q.remove()
trrce(q)
q.remove()
trrce(q)
q.remove()
trrce(q)
q.remove()
trrce(q)
print("isEmpty? ",s.isEmpty())

print("--------------BinaryTree----------------")

tree = '''

			1
		2		3	
	4				5	

'''
print(tree)
r = BinaryTree() #root
rll = BinaryTree() 
rll.makeTree(4,None,None)
rr = BinaryTree()
rr.makeTree(2,rll,None)
rrr = BinaryTree()
rrr.makeTree(5,None,None) 
rl = BinaryTree()
rl.makeTree(3,None,rrr) 
r.makeTree(1,rr,rl)

print("preOrder")
r.preOrder(r)  
print("inOrder")
r.inOrder(r)  
print("postOrder")
r.postOrder(r)  
print("levelOrder")
r.levelOrder(r) 