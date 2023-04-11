import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def main():

    f = ""
    
    # for i in figlet.getFonts():
    #     print(i)
    
    if len(sys.argv) == 1:
        f = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] == ("-f" or "--font"):
        if sys.argv[2] in figlet.getFonts():
            f = sys.argv[2]
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")
    
    
    figlet.setFont(font=f)    
    text = input("Input : ")
    print(figlet.renderText(text))
    
if __name__ == "__main__":
    main()
    