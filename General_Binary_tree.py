class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_left(self, node, value):
        newNode = Node(value)
        node.left = newNode
        return newNode

    def add_right(self, node, value):
        newNode = Node(value)
        node.right = newNode
        return newNode
    
    # Top to bottom and left to right
    def preOrdertraversal(self, node):
        if node is None:
            return 
        print(node.data, end=" -> ")
        self.preOrdertraversal(node.left)
        self.preOrdertraversal(node.right)

    # Bottom to top and left to right
    def inOrdertraversal(self, node):
        if node is None:
            return 
        self.inOrdertraversal(node.left)
        print(node.data, end=" -> ")
        self.inOrdertraversal(node.right)

    # Left to right and bottom to top
    def postOrdertraversal(self, node):
        if node is None:
            return 
        self.postOrdertraversal(node.left)
        self.postOrdertraversal(node.right)
        print(node.data, end=" -> ")

myBinaryTree = BinaryTree()
root = Node("A")
myBinaryTree.root = root

print(f"Root: {myBinaryTree.root.data}")

rootLeft = myBinaryTree.add_left(root, "B")
rootRight = myBinaryTree.add_right(root, "C")

rootLeftLeft = myBinaryTree.add_left(rootLeft, "D")
rootLeftRight = myBinaryTree.add_right(rootLeft, "F")

rootRightLeft = myBinaryTree.add_left(rootRight, "E")
rootRightRight = myBinaryTree.add_right(rootRight, "G")

myBinaryTree.preOrdertraversal(root)
print()
myBinaryTree.inOrdertraversal(root)
print()
myBinaryTree.postOrdertraversal(root)