
def shorten(s):
    vowels = ('A','E','I','O','U','a','e','i','o','u')
    for c in s:
        if c in vowels:
            s = s.replace(c, "")       
    return s

def main():
    print(shorten(input("Please enter the tweet: ")))
    
if __name__ == "__main__":
    main()