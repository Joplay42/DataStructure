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
            
    def insert(head, position, value):
        pass
        
        
    def isListEmpty(self):
        return self.size == 0
    
    def length(self):
        return self.size
            
myLinkedList = LinkedList()

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")

myLinkedList.head = node1
myLinkedList.size = 4
node1.next = node2
node2.next = node3
node3.next = node4

print(myLinkedList.traverseAndPrint())

print(f"isListEmpty: {myLinkedList.isListEmpty()}")
print(f"length: {myLinkedList.length()}")