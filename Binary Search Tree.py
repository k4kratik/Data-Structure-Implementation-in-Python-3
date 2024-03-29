#()
class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinartSearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)


    def insertNode(self, data, root_node):
        if data < root_node.data:
            if root_node.leftChild:
                self.insertNode(data,root_node.leftChild)
            else:
                root_node.leftChild = Node(data)

        else:
            if root_node.rightChild:
                self.insertNode(data,root_node.rightChild)
            else:
                root_node.rightChild = Node(data)

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, root_node):

        if root_node.leftChild:
            self.traverseInOrder(root_node.leftChild)

        print("%s" % root_node.data)

        if root_node.rightChild:
            self.traverseInOrder(root_node.rightChild)


    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, root_node):
        if root_node.leftChild:
            return self.getMin(root_node.leftChild)
        return root_node.data
        
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, root_node):
        if root_node.rightChild:
            return self.getMax(root_node.rightChild)
        return root_node.data
        

        
v = BinartSearchTree()
v.insert(10)
v.insert(5)
v.insert(15)
v.insert(6)
v.traverse()
