def pay(s):
    s = s.strip().lower()
    if s[0] == 'h'and s[0:5] != 'hello': return 20
    elif s[0:5] == 'hello': return 0
    else: return 100

def main():
    s = input("Greet Kramer: ")
    payme = pay(s)
    
    print(f"${payme}.2f")
    
if __name__ == "__main__":
    main()