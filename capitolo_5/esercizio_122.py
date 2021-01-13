#!/bin/python3
def latin(word):
    contator = 0
    list_vocal_1 = ["w","a","y"]
    list_cons = ["a","y"]
    list_word = list(word)
    list_vocal = ["a","e","i","o","u"]
    for vocal in  list_vocal:
        if word.startswith(vocal):
            for add in list_vocal_1:
                list_word.append(add)
                contator += 1
            if contator == 3:
                word_1 = "".join(list_word)
                break
        else:
            list_word.pop(0)
            for const in list_cons:
                list_word.append(const)
                contator += 1
            if contator == 2:
                word_1 = "".join(list_word)
                break
            
    print(word_1)
           
                 
            


def main():
    word=input("Enter the word: ").lower()
    latin(word)

if __name__ == "__main__":
    main()