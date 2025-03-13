import pytest
from fuel import convert,gauge

def main():

 def test_convert():
  assert convert("3/4")=="75%"
  assert convert("1/2")=="50%"
  assert convert("0/100")=="0%"

 def test_gauge():
  assert gauge(convert("100/100"))=="F"
  assert gauge(convert("1/10"))=="E"

 def test_error():
   with pytest.raises(ValueError):
    assert convert(1.34/9)
   with pytest.raises(ZeroDivisionError):
        assert(convert("65/0"))
        
if __name__ == "__main__":
    main()
