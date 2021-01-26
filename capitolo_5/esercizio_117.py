#!/bin/python3
def delete(word):
    list_moment = list()
    name = ""
    list_word = list(word)
    for letter in  list_word:
        if letter !="," and letter != " " and letter != "?" and letter != "!" and letter != "." and letter != "'":
            name += letter
        elif letter == "," or letter == " " or letter == "?" or letter == "!" or letter == "." or letter == "'":
            list_moment.append(name)
            name =""
    final = " ".join(list_moment)
    return final


def main():
    word = input("Enter a sentence with punctuation marks: ")
    first = delete(word)
    print(first)
if __name__  == '__main__':
    main()