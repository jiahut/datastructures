class Stack:  
    def __init__(self,size = 16):  
        self.stack = []  
        self.size = size  
        self.top = -1  
    def setCapacity(self, size):
        self.size = size  
    def isEmpty(self):  
        return self.top == -1
    def isFull(self):  
        return self.top + 1 == self.size
    def head(self):
        if self.isEmpty():  
            raise Exception("StackIsEmpty")  
        else:  
            return self.stack[self.top]
    def tail(self):
    	if self.isEmpty():
    		raise Exception("StackIsEmpty")
    	else:
    		return self.stack[0]
    def push(self,obj):  
        if self.isFull():  
            raise Exception("StackOverFlow")  
        else:  
            self.stack.append(obj)  
            self.top +=1  
    def pop(self):  
        if self.isEmpty():  
            raise Exception("StackIsEmpty")  
        else:  
            self.top -= 1  
            return self.stack.pop()
    def info(self):  
        return self.stack