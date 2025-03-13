from twttr import shorten
def main():

 def test_twitter():
    assert shorten("twitter")=="twttr"

 def test_name():
    assert shorten("DAVID")=="DVD"

def test_harvard():
   assert shorten("harvard")=="hrvrd"

def test_cs50():
   assert shorten("CS50")=="CS50"

if __name__ == "__main__":
    main()
