#!/bin/python3
def isInteger(word):
    new_word = list()
    change = int(word)
    if change:
        for letter in word[0:]:
            if letter==" ":
                continue
            else:
                new_word.append(letter)
        final = "".join(new_word)
        change = int(final)
    return change


def main():
    try:
        word =input("Enter the sentences: ")
        first = isInteger(word)
        print(first)
    except ValueError:
        print("Not be impossible!")
if __name__ == "__main__":
    main()