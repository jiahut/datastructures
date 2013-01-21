class Queue:  
    def __init__(self,size = 16):  
        self.queue = []  
        self.size = size  
        self.tail = -1  
    def isEmpty(self):
        return self.tail == -1  
    def isFull(self):
        return self.tail + 1 == self.size
    def first(self):  
        if self.isEmpty():
            raise Exception("QueueIsEmpty")  
        else:  
            return self.queue[0]
    def last(self):  
        if self.isEmpty():
            raise Exception("QueueIsEmpty")  
        else:  
            return self.queue[self.tail]  
    def add(self,obj):  
        if self.isFull():
            raise Exception("QueueOverFlow")  
        else:
            self.tail += 1
            self.queue.append(obj)  
    def remove(self):
        if self.isEmpty():  
            raise Exception("QueueIsEmpty")  
        else:  
            self.tail -= 1 
            return self.queue.pop(0)  
    def info(self):  
        return self.queue