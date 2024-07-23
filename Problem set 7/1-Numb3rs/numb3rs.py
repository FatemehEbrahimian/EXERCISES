import re
import sys
def main():
    print(validate(int(input("IPv4 Address: "))))
def validate(ip):
 ipv=re.search("^[1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)$",ip)
 if ipv:
     numbers = ip.split(".")
     if len(ipv)>4 or len(ipv)<4:
        return False
     for i in numbers:
        if int(i)>255 or int(i)<255:
           return False
        else:
           return True 
if __name__ == "__main__":
    main()
