
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    try:
        assert (s[0:2]).isalpha() == True
        assert s.isalnum() == True
        
        if len(s) >= 2 and len(s) <= 6:
            pass
        else:
            return False
        
        for i in range(len(s)-1):
            if s[i].isalpha() and s[i+1] == '0':
                return False
            elif s[i].isdecimal() and s[i+1].isalpha():
                return False
        else: return True
                 
    except AssertionError:
        return False

if __name__ == "__main__":
    main()