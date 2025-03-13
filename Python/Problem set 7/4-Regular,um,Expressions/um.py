import re
import sys
def main():
    print(count(input("Text: ")))
def count(s):
 text=re.search(r"\b(?=\w)um\b(?!\w)",s)
 if text:
    return len(text)
if __name__ == "__main__":
    main()
