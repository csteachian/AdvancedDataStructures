from BinaryTree import *

def printInOrderTree(tree):
    # LEFT, ROOT, RIGHT
    if tree != None:
        printInOrderTree(tree.getLeftChild())
        print(tree.getNodeValue())
        printInOrderTree(tree.getRightChild())

def printPreOrderTree(tree):
    # ROOT, LEFT, RIGHT
    if tree != None:
        print(tree.getNodeValue())
        printPreOrderTree(tree.getLeftChild())
        printPreOrderTree(tree.getRightChild())

def printPostOrderTree(tree):
    # LEFT, RIGHT, ROOT
    if tree != None:
        printPostOrderTree(tree.getLeftChild())
        printPostOrderTree(tree.getRightChild())
        print(tree.getNodeValue())


# TEST TREE
myTree = BinaryTree(10)
myTree.insert(5)
myTree.insert(15)
myTree.insert(8)
printInOrderTree(myTree)
print()
printPreOrderTree(myTree)
print()
printPostOrderTree(myTree)

