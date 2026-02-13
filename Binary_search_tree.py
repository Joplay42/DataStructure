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
    
    def remove(self, node, data):
        if not node:
            return None
        
        if data < node.data:
            node.left = self.remove(node.left, data)
        elif data > node.data:
            node.right = self.remove(node.right, data)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
                
            node.data = self.minValue(node.right).data
            node.right = self.remove(node.right, node.data)
        
        return node
        
    
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


removedNode = myBinaryTree.remove(root, 19)
removedNode = myBinaryTree.remove(root, 8)
print()
print(myBinaryTree.inOrdertraversal(root))