def main():
    # x = get_int("what's X? ")
    x = (input("whats your sentence?"))
    print(f"the number of words in the sentence is {count_word(x, ' ') + 1} and the strlen is {len(x)} ")
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def count_word(sentence, word):
    return sentence.count(f'{word}')
        
if __name__ == "__main__":
    main()
            