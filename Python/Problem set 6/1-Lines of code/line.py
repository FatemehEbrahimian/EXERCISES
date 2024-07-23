import sys
if len(sys.argv)==2:
  try:
   with open(sys.argv[1])as file:
    for line in file:
     if not line.lstrip().startwith("#") and line.lstrip() !="":
      print(line)
  except:
   raise FileNotFoundError
elif len(sys.argv)<2:
 sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
 sys.exit("Too many command-line arguments")
else:
 print("Not a python file.")
