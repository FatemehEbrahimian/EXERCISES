list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
 Date=input("Date:")
 try:
  if "/" in Date:
   month,day,year=Date.split("/")
  if int(month)>=1 and int(month)<=12 and int(day)>=1 and int(day)<=31:
   break
  elif "," in Date:
   Date=Date.replace(",", "")
   month,day,year=Date.split(" ")
   if month in list and int(day) <= 31:
    month = Date.index(month) + 1
    break
 except:
  pass
print(f"{int(year)}-{int(month):02}-{int(day):02}")