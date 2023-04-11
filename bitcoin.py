import requests
import sys
import json

def main():
    
    try:
        if len(sys.argv) == 2:
            value_btc = float(sys.argv[1])
        else: sys.exit("Need one float argument")
        
    except ValueError:
        sys.exit("Arguement has to be float")
        
    x = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print (json.dumps(x.json(), indent=2))
    
    if not (x) :sys.exit("Request Error") # " x " evaluates to True due to the behaviour coded in requests module.

    rate_btc = x.json()["bpi"]["USD"]["rate_float"]
    total = rate_btc * value_btc
    print (f"${float(total):,.4f}")

if __name__ == "__main__":
    main()