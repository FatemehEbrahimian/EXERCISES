import sys
import requests
if len(sys.argv)==2:
    pass
try:
    value=float(sys.argv[1])
except:
   print("Command-line argument is not a number")
   sys.exit()
else:
    print("Missing command-line argument")
    sys.exit()
try:
 r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
 text=r.json()
 bitcoin=(text["bpi"]["USD"]["rate_float"])
 amount=bitcoin*value
 print=(f"${amount:,.4f}")
except requests.RequestException:
   sys.exit()