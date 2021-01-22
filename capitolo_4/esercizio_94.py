#!/bin/python3
def is_triangle(first,second,third):
    final = first + second
    if third  >= final:
        print("not be possible")
    else:
        final = first + third
        if second >= final:
            print("not be possible")
        else:
            final = second + third
            if first >= final:
                print("not be possible")
            else:
                print("Be possible")
def main():
    try:
        first=int(input("Enter the first: "))
        second=int(input("Enter the second: "))
        third=int(input("Enter the first: "))
        is_triangle(first,second,third)
    except ValueError:
        print("Value not is int")


if __name__ == "__main__":
    main()