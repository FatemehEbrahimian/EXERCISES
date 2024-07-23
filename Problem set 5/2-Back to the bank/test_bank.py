from bank import value
def main():

 def test_hello():
  assert value("hello")=="0$"
  assert value("Hello,Newman")=="0$"

  def test_text():
    assert value("hi buddy.")=="20$"
    assert value("HEY")=="20$"

  def test_others():
    assert value("oh my god.")=="100$"
    
if __name__ == "__main__":
    main()
