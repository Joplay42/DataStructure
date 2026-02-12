class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Bottom to top and left to right
    def inOrdertraversal(self, node):
        if node is None:
            return 
        self.inOrdertraversal(node.left)
        print(node.data, end=" -> ")
        self.inOrdertraversal(node.right)

    def search(self, node, target):
        if node is None:
            return None
        elif node.data == target:
            return node
        elif target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)
        
    def insert(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            elif data > node.data:
                node.right = self.insert(node.right, data)
            return node

    def minValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
myBinaryTree = BinarySearchTree()
root = Node(13)
myBinaryTree.root = root
        
node1 = Node(7)
root.left = node1
node2 = Node(3)
node1.left = node2
node3 = Node(8)
node1.right = node3
node4 = Node(15)
root.right = node4
node5 = Node(14)
node4.left = node5
node6 = Node(19)
node4.right = node6

myBinaryTree.inOrdertraversal(root)

myBinaryTree.insert(root, 12)

print()
myBinaryTree.inOrdertraversal(root)

foundNode = myBinaryTree.search(root, 7)
print()
print(f"Found: {foundNode.data}")

minNode = myBinaryTree.minValue(root)
print(f"Min: {minNode.data}")