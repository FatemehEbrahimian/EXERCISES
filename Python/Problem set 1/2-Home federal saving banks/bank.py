answer=input("Greeting:").lower().strip()
if "hello" in answer:
    print("$0")
elif "h"==answer[0]:
    print("$20")
else:
    print("$100")