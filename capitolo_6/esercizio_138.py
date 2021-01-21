#!/bin/python3
def output_number(word):
    final = ""
    moment = 0
    dict_letter={
        2:["a","b","c"],
        3:["d","e","f"],
        4:["g","h","i"],
        5:["j","k","l"],
        6:["m","n","o"],
        7:["p","q","r","s"],
        8:["t","u","v"],
        9:["w","x","y","z"]
    }
    for number_letter in word:
        for num in range(2,8):
            letter = dict_letter.get(num)
            for index in range(0,len(letter)):
                if letter[index] == number_letter:
                    moment = str(num) * (index+1)
                    final += str(moment)
    return final
def main():
    word=input("Enter the word: ")
    output=output_number(word)
    if output:
        print(output)
if __name__ == "__main__":
    main()