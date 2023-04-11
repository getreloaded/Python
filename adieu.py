import sys
import inflect

def main():
    
    names = []
    
    while(True):
        try:
            x = input("Name: ")
            names.append(x)
        except EOFError:
            break
    
    name_list = inflect.engine().join(names)
    print("Adieu, Adieu, to " + name_list)

if __name__ == "__main__":
    main()      