# Stacks - Towers of Hanoi + 2D Arrays
# IB Computer Science HL
# By Mr Simpson
# March 2017

towerMax = 10 # set maximum number of items on each pole stack to be 10

pole = [[] for y in range(0,3)]

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
    for index in range(7, 0, -1):
        push(index, pole[0])  # put all disks on pole1 stack

def displayTowers():
    # show Tower of Hanoi poles
    print("1: ", pole[0])
    print("2: ", pole[1])
    print("3: ", pole[2])
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

item = pop(pole[0]) # MOVE 1
push(item,pole[1])
displayTowers()

item = pop(pole[0]) # MOVE 2
push(item,pole[2])
displayTowers()

item = pop(pole[1]) # MOVE 3
push(item,pole[2])
displayTowers()

move(pole[0],pole[2]) # MOVE 4