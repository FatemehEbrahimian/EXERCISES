def main():
 final_fuel=get_percent()
 percent_fuel=round(int(final_fuel * 100))
 if percent_fuel<=1 :
    print("E")
 elif percent_fuel>=99:
   print("F")
 else:
   print(f"{percent_fuel}%")
def get_percent():
 try:
  while True:
    fraction=input("final fraction:" )
    x,y=fraction.split()
    x=int(x)
    y=int(y)
    fuel=x/y
    if fuel<=1:
      return fuel
 except:
   (ValueError , ZeroDivisionError)
   pass
main()