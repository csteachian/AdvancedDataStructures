# Stacks - Towers of Hanoi, qwick change
# IB Computer Science HL
# By Mr Simpson
# March 2017

towerMax = 10 # set maximum number of items on each pole stack to be 10

pole0 = []
pole1 = []
pole2 = []

def push(item, stack):
    if len(stack) == towerMax:
        print("Stack is full")
    else:
        stack.append(item)

def pop(stack):
    # get most recent item from stack
    index = len(stack)-1
    if index >= 0:
        item = stack[index]
        stack.remove(item)
    else:
        print("Stack is empty")
        item = ""
    return item

def initGame():
    for index in range(6, 0, -1):
        push(index, pole0)  # put all disks on pole1 stack

def displayTowers():
    # show Tower of Hanoi poles
    print("1: ", pole0)
    print("2: ", pole1)
    print("3: ", pole2)
    print("---------------")

def test(stackA, stackB):
    item = pop(stackA)
    item2 = pop(stackB)
    if item == "" and item2 == "":
        print("No item to move.")
        return False
    elif item == "":
        push(item2,stackB)
        return True
    elif item2 == "":
        push(item,stackA)
        return True
    elif int(item) > int(item2):
        print("You cannot place a larger disk on a smaller disk")
        push(item,stackA)
        push(item2,stackB)
        return False

def move(stackA, stackB):
    if test(stackA, stackB) == True:
        item = pop(stackA)
        push(item,stackB)
    else:
        print("Move failed")
    displayTowers()

# main program
initGame()
displayTowers()

item = pop(pole0) # MOVE 1
push(item,pole1)
displayTowers()

item = pop(pole0) # MOVE 2
push(item,pole2)
displayTowers()

item = pop(pole1) # MOVE 3
push(item,pole2)
displayTowers()

move(pole0,pole1) # MOVE 4