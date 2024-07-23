answer=(input("input:"))
for letter in answer:
    if not letter.lower() in["a" , "i" , "o" , "e" , "u"]:
     print(letter , end="")