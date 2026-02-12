class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, value):
        newNode = Node(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        poppedNode = self.head
        self.head = poppedNode.next
        self.size -= 1
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
        
    def toString(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
            
myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print(f"StackSize : {myStack.stackSize()}")
print(f"IsEmpty : {myStack.isEmpty()}")
print(f"Peek : {myStack.peek()}")
print(myStack.toString())

myStack.pop()
print(myStack.toString())