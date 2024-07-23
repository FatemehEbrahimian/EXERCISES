amountdue=50
while True:
    print("Amont due:", amountdue )
    money=int(input("Insert coin: "))
    if money in [25,20,5]:
       if (money>=amountdue):
           print("changed owed:",money-amountdue)
           break
       amountdue-=money
    else:
        continue
