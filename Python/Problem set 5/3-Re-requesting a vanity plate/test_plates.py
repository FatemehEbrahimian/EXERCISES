from plates import is_valid
def main():
 def test_s():
   assert is_valid("43")==False

 def test_cs50():
   assert is_valid("cs50")==True
   assert is_valid("cs05")==False

 def test_word_invalid():
   assert is_valid("A")==False
   assert is_valid("GOODBYE")==True

 def test_word_valid():
   assert is_valid("Hello")==True

if __name__ == "__main__":
    main()