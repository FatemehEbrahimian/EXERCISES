def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
 if len(s)>6 or len(s)<2:
    return False
 if s[0].isalpha()==False or s[0].isalpha()==False:
     return False
 for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isalpha:
       return False
 for i in s:
    if i.isdigit():
       return i !=0
 else:
    return True
main()