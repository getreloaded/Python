import random
import math

def check_pos_int(i):
    if i.isnumeric() == True:
        if int(i) > 0 and math.modf(float(i))[0] == 0:
            return True
        else:
            return False
    else:
        return False

def get_number(prompt):
    
    while (True):
        x = input(prompt)
        if check_pos_int(x) is True:
            break
    return int(x)


def main():
    
    difficulty = get_number("Level: ")
    selectedNum = random.choice(range(difficulty))
    
    while True:
        x = get_number("Guess: ")
        if x > difficulty:
            print("Guess within range please.")
        else:    
            if x > selectedNum:
                print("Too Large")
            elif x < selectedNum:
                print("Too Small")
            else:
                print("Perfect")
                break
    
if __name__ == "__main__":
    main()