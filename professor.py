from random import choice
from game import check_pos_int as check_check

max_questions = 10 #Global

def get_int(level):

    range_start = int(10**(level-1))
    range_end = int(10**level)
    return int(choice(range(range_start,range_end)))
'''
def check_pos_int(i):
    if i.isnumeric() == True:
        if int(i) > 0 and math.modf(float(i))[0] == 0:
            return True
        else:
            return False
    else:
        return False
'''
    
def EEE(i):
    print("EEE")
    return i + 1

def question(level):
    
    a = get_int(level)
    b = get_int(level)
    eee = int(0)
    
    
    
    while ( eee < 3 ):
        c = input(f"{a} + {b} = ")
        if check_check(c) is True:
            c = int(c)
            if c == a + b:
                return "correct"
            else: eee = EEE(eee)
        else: eee = EEE(eee)
        
    else:
        print( a + b )
        return "incorrect"
    
def get_level():
    while True:
        try:
            x = input("Level: ")
            if check_check(x) is True:
                x = int(x)
                if x == 1 or x == 2 or x == 3:
                    return x
                    break
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Please input 1 , 2, or 3")

def main():
    
    #prompt the user for level
    
    level = get_level()
    
    # initialize number of questions and scoring system
    
    score = 0
    
    # define a function for asking questions.
    
       
    # in for loop of ten keep the scores and print at the end.
    
    for i in range(max_questions):
        x = question(level)
        if x == "correct":
            score = score + 1
        else:
            continue
    
    print(f"You score is: {score}/{max_questions}")
    
if __name__ == "__main__":
    main()