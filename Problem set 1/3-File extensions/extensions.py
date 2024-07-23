answer=input("File name:").lower().strip()
if ".gif" in answer:
    print("imag/gif")
elif ".jpg" in answer:
    print("image/jpeg")
elif ".jpeg" in answer:
    print("image/jpeg")
elif ".png" in answer: 
    print("image/png")
elif ".pdf" in answer:
    print("application/pdf")
elif ".txt" in answer:
    print("text/plain")
elif ".zip" in answer:
    print("text/plain")
else :
    print("application/octet-stream")