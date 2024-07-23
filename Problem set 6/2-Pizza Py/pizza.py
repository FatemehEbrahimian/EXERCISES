import sys
import tabulate
import csv
if len(sys.argv)==2 and ".Cvs" in (sys.argv[1]):
 try:
   with open(sys.argv[1])as file:
      reader=csv.DictReader(file)
      print(tabulate.tabulate(headers="firstrow", tablefmt="grid"))
 except:
   raise FileNotFoundError
elif len(sys.argv)>2:
 sys.exit("Too many command-line arguments")
elif len(sys.argv)<2:
 sys.exit("Too few command-line arguments")
else:
  sys.exit("Not a CSV file.")