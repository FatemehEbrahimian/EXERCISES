import sys
import csv
if len(sys.argv)==3:
 try:
    with open(sys.argv[1])as file_0 , open(sys.argv[2]) as file_1:
     writer=csv.DictWriter(file, fieldnames=["first", "last", "house"])
     writer.writerow({"first": first, "last": last, "house": house})
     reader=csv.DictReader()
     for row in reader:
      splited = row["name"].split(",")
      last, first = splited[0].split(", ")
      house = splited[1].rstrip()
 except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
elif len(sys.argv)>3:
 sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
 sys.exit("Too few command-line arguments")
else:
  sys.exit("Could not read invalid_file.csv")