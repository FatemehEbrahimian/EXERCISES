from datetime import date
import inflect
import sys
p = inflect.engine()

def main():
        birthday = input("Date of birth: ")
        return diff(birthday)

def diff(birthday):
    try:
        year, month, day = birthday.split("-")
        birthday = date((year), (month), (day))
    except:
        return sys.exit("Invalid")
    diff = (date.today() - birthday).days * 24 * 60
    result = p.number_to_words(diff, andword="")
    print(result.capitalize()+" minutes")
    return result + " minutes"

if __name__ == "__main__":
    main()