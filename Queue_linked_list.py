class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
        self.rear.next = newNode
        self.rear = newNode
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        dequeueNode = self.front
        self.front = dequeueNode.next
        self.size -= 1
        
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value
    
    def isEmpty(self):
        return self.size == 0
    
    def queueSize(self):
        return self.size
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
    
myQueue = Queue()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")

print(myQueue.printQueue())

print(f"QueueSize: {myQueue.queueSize()}")
print(f"IsEmpty : {myQueue.isEmpty()}")
print(f"Peek : {myQueue.peek()}")

myQueue.dequeue()

print(myQueue.printQueue())

print(f"QueueSize: {myQueue.queueSize()}")
print(f"IsEmpty : {myQueue.isEmpty()}")
print(f"Peek : {myQueue.peek()}")