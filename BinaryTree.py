class BinaryTree():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, newValue):
        self.value = newValue

    def getNodeValue(self):
        return self.value

    def insert(self,newValue):
        if (newValue <= self.value):
            if self.left == None:
                self.left = BinaryTree(newValue)
            else:
                self.left.insert(newValue)
        else:
            if self.right == None:
                self.right = BinaryTree(newValue)
            else:
                self.right.insert(newValue)

