class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
            
    def insert(self, position, value):
        newNode = Node(value)
        
        if position == 1:
            newNode.next = self.head
            self.head = newNode
            
        
        self.size += 1
        
        
    def isListEmpty(self):
        return self.size == 0
    
    def length(self):
        return self.size
            
myLinkedList = LinkedList()

myLinkedList.insert(1, "A")
myLinkedList.insert(1, "B")
myLinkedList.insert(1, "C")

print(myLinkedList.traverseAndPrint())

myLinkedList.insert(2, "Z")

print(myLinkedList.traverseAndPrint())

print(f"isListEmpty: {myLinkedList.isListEmpty()}")
print(f"length: {myLinkedList.length()}")