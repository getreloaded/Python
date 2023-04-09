import cowsay
import sys

for i in dir(cowsay)[10:]:
    print(i)

while(True):
    
    x=input("what do you want? Type from the list \n1.dir for list of items \n2.nothing to exit the program  \n" )
    
    if x == "nothing":
        sys.exit()
    elif x == "dir":
        for i in dir(cowsay)[10:]:
            print(i)
        continue
    elif x in dir(cowsay):
        output = getattr(cowsay, x)
        output("Hi, Jambu")
    else:
        print("option not in dir")
    