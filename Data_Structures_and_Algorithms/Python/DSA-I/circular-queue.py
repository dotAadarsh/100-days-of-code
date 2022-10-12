class MyCircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1

    def enqueue(self, data):

        if ((self.tail + 1) % self.k) == self.head:
            print("Queue is full\n")
        
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
    
    def dequeue(self):
       
        if (self.head == -1):
            print("The queue is empty\n")
        
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp 
        
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp 

    def printCircularQueue(self):
        
        if self.head == -1:
            print("Queue is empty\n")
        
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end= " ")
            print()
        
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end = " ")
            
            for i in range(0, self.tail + 1):
                print(self.queue[i], end = " ")
            print()
            
cq = MyCircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.printCircularQueue()

cq.dequeue()
cq.printCircularQueue()

cq.dequeue()
cq.printCircularQueue()

cq.enqueue(11)
cq.printCircularQueue()