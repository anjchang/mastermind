#code here https://replit.com/@AngelaChang7/Mastermind-Blitz#main.py
import random
from collections import Counter

colors = "R,O,Y,G,B,P".split(',')
key = ['X','X','X','X']

def calc(pegs):
  print(pegs, key)   #debug
  if key == pegs:
    return "DONE"
  Bs = 0
  Ws = 0
  key2 = key[:]
  for peg in pegs:  #take each peg
    if peg in key2:  #check if that peg is in the answer
      if pegs[key2.index(peg)] == key2[key2.index(peg)]:
        Bs = Bs + 1  #correct color in correct position
        key2[key2.index(peg)] = "_"  #blank out key for tally
      else:
        Ws = Ws + 1  #correct color, but incorrect position
        key2[key2.index(peg)] = "_"
  print("\t\t\tBs:" + str(Bs) + " Ws:" + str(Ws))

def prettify(wandb):
  # counts = {"W":2}
  counts = Counter(wandb)
  for peg, no in counts.items():
    print(peg + " " + str(no))

def play():
  global key
  for x in range(4):
    key[x]=random.choice(colors)  #used to be append, but had trouble with local/global so I changed this to a 4-item list
  count = 0
  while count <= 9:
    guess = list(input(f"Guess #{count+1}\nEnter 4-peg ROYGBP order\n"))
    result = calc(guess)
    if result == "DONE":
      break
    #print(f"Tally {result}")
    prettify(result)
    count = count + 1

  if result == "DONE":
    print("You Won!")
  else:
    print("You Lose!")
  print(key)

  playagain = input("Play again? Y\n")
  if (playagain.upper() == 'Y'):
    play()
  else:
    print("Goodbye!")


play()

#####scratch
#print(colors)
#print(key)

# def calc(pegs):
#   print(pegs, key)
#   if (key == pegs):
#     return "DONE"
#   # Copy key so we can mutate it
#   key2 = key[:]
#   # Will be "B" or "W"
#   result = []
#   fofor idx, peg in enumerate(pegs):
#     # Correct color in correct position is "BLACK"
#     if key[idx] == peg:
#       result.append("B")
#       key2[idx] = "Z"
#       continue
#     if peg in key2:
#       key2[idx] = "Z"
#       print(key2)
#       result.append("W")
#   return result
