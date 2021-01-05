#!/bin/python3
def eliminate_max(list_number, terminate):
    i = 0
    list_number.sort()
    list_number.pop(i)
    terminate += 1
    if terminate == 2:
        print(list_number)
    else:
        eliminate_max(list_number, terminate)

    
def eliminate_min(list_number, terminate):
    i=0
    list_number.sort(reverse=True)
    list_number.pop(i)
    terminate += 1
    if terminate == 2:
        print(list_number)
    else:
        eliminate_min(list_number, terminate)

def main():
    terminate = 0
    contator = 0
    boolean = True
    list_number = []
    while boolean:
        contator += 1
        number = int(input("Enter the number"))
        list_number.append(number)
        if number == 0 and contator >= 4:
            break
    eliminate_max(list_number, terminate)
    eliminate_min(list_number, terminate)

    
if __name__ == '__main__':
    main()