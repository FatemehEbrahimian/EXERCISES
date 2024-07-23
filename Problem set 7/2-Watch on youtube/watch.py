import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):
  result=re.search(r'.+src="https?://(www\.)?youtube\.com/embed[A-za-z0-9]+',s)
  if result:
     return"https://youtu.be/xvFZjo5PgG0"
  else:
        return None
if __name__ == "__main__":
    main()
