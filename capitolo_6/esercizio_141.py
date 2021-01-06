#!/bin/python3
def english_word(number):
    dicto_hundreds={
        "1":"one hundred",
        "2":"two hundred",
        "3":"three hundred",
        "4":"four hundred",
        "5":"five hundred",
        "6":"six hundred",
        "7":"seven hundred",
        "8":"eight hundred",
        "9":"nine hundred",
    }
    dicto_dozens={
        "2":"twenty",
        "3":"thirty",
        "4":"forty",
        "5":"fifty",
        "6":"sixty",
        "7":"seventy",
        "8":"eighty",
        "9":"ninety",
    }
    dicto_out={
        "10":"ten",
        "11":"eleven",
        "12":"twelve",
        "13":"thirteen",
        "14":"fuorteen",
        "15":"fifteen",
        "16":"sixteen",
        "17":"seventeen",
        "18":"eighteen",
        "19":"nineteen",
    }
    dicto_unity={
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine",
    }

    list_number = list(number)
    if number in dicto_out:
        print(dicto_out.get(number))
    elif len(list_number) == 2:
        if list_number[0] in dicto_dozens:
            print(dicto_dozens.get(list_number[0]))
            if list_number[1] in dicto_unity:
                print(dicto_unity.get(list_number[1]))
    elif len(list_number) == 3:
        if list_number[0] in dicto_hundreds:
            print(dicto_hundreds.get(list_number[0]))
            if list_number[1] in dicto_dozens:
                print(dicto_dozens.get(list_number[1]))
                if list_number[2] in dicto_unity:
                    print(dicto_unity.get(list_number[2]))
    elif len(list_number) == 1:
        if list_number[0] in dicto_unity:
            print(dicto_unity.get(list_number[0]))
    elif len(list_number) > 4:
        print("out range!")

        
def main():
    try:
        number=input("Enther the numberv 1-999 ")
        english_word(number)
    except:
        print("Errors")
        main()

if __name__ =='__main__':
    main()