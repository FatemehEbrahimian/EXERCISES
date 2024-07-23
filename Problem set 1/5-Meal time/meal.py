def main():
 time=convert(input("What time is it?"))
 if 7<=time<=8:
    print("Brakfast time!")
 elif 12<=time<=13:
    print("Lunch time!")
 elif 18<=time<=19:
    print("Dinner time!")
def convert(time):
   hour,minute=time.split(":")
   return (float(hour)) + (float(minute))/60
if __name__ == "__main__":
    main