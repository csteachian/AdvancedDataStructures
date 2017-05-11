from sense_hat import SenseHat

def printguess(x,y):
  global hits, stopMe # NEW
  if board[x][y] == "X":
    sense.set_pixel(x,y,0,255,0)
    hits += 1 # NEW
    if hits == boatbits: # NEW
      print("Game over - you win!") #NEW
      stopMe = True
  else:
    sense.set_pixel(x,y,255,0,0)

def compsetup():
  board[2][1] = "X"
  board[2][2] = "X"
  board[2][3] = "X"

sense = SenseHat()
boatbits = 3 #NEW
hits = 0 # NEW
stopMe = False # NEW
board = [[0 for x in range(0,8)] for y in range(0,8)]
compsetup()
sense.clear()
while stopMe != True: # NEW
  xpos = int(input("Enter a x position (0-7)"))
  ypos = int(input("Enter a y position (0-7)"))
  printguess(xpos,ypos)