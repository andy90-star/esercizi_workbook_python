#!/bin/python3
list_add = list()

def main():
    try:
        select=input("Enter the sentence ")
        if select in list_add:
            print("sentence already called" + select)
            main()
        elif select == "end":
            print(list_add)
        else:
            list_add.append(select)
            main()
    except:
        print("Sorry!I don't understand")
        main()
if __name__ == '__main__':
    main()