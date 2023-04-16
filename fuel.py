from game import check_pos_int as cpi

def main():
    while True:
        fraction = input("Fraction: ")
        percentage_fuel = convert(fraction)
        if percentage_fuel == False:
            continue
        else: 
            print(percentage_fuel) 
            break     

def convert(fraction):
    try:
        numden = fraction.split('/')
        assert len(numden) == 2
        num = numden[0]
        den = numden[1]
        
        if (((cpi(num) and cpi(den) == True) and 0<=int(num)/int(den)<=1) or int(num) == 0): pass
        else: raise ValueError()
        
        percent_fuel = int(num)/int(den)*100
        return gauge(int(percent_fuel))
            
    except (ValueError, ZeroDivisionError, AssertionError):
        return False

def gauge(percentage):
    if 0<=percentage<=1: return 'E'
    elif 1<percentage<99: return f"{percentage}%"
    elif 99<=percentage<=100: return "F"
    else: raise ValueError("Wrong fraction")

if __name__ == "__main__":
    main()