def fib(number):
    a, b = 1, 1
    i = 1
    print (a)
    while (i < number):
        print (b)
        c = b
        b = a + b
        a = c
        i+=1

def main():
    fib(int(input("How many? ")))
    
main()
        
        