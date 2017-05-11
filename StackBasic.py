# Stacks - Basic Structure
# IB Computer Science HL
# By Mr Simpson
# March 2017

firstStack = [] # set up secondStack as 1D array
secondStack = [] # set up secondStack as 1D array
thisStackMax = 10 # set maximum number of items in thisStack to be 10

def push(item, thisStack):
    if len(thisStack) == thisStackMax:
        print("Stack is full")
    else:
        thisStack.append(item)

def pop(thisStack):
    # get most recent item from thisStack
    index = len(thisStack)-1
    if index >= 0:
        item = thisStack[index]
        thisStack.remove(item)
    else:
        print("Stack is empty")
        item = ""
    return item

# main program
for index in range(0,10):
    push(chr(index+65), firstStack)
#push("HELLO", secondStack)

# show stack
print(firstStack)
print(secondStack)

for index in range(0,10):
    item = pop(firstStack) # If index goes beyond thisStackMax it should show "Stack is empty" error
    push(item, secondStack)

# show stack
print(firstStack)
print(secondStack)