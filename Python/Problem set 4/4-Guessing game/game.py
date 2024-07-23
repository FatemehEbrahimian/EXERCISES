import random
while True:
  level=int(input("level:"))
  if level>0:
    break
  else:
    pass
randoms=random.randint(1,level)
while True:
  try:
   Guess=input("Guess:")
   if randoms<Guess:
     print("Too large!")
   elif randoms>Guess:
     print("Too small!")
   elif randoms==Guess:
     print("Just right!")
     break
  except:
    pass