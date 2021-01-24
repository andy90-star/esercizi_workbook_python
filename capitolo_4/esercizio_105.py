#!/bin/python3
def change_base(number, base_final):
    list_mo = list()
    boolean = True
    final = ""
    while boolean:
        rest = number%base_final
        number = number/base_final
        final += str(int(rest))
        if number <= base_final:
            final += str(int(number))
            boolean = False
            for i in reversed(final):
                list_mo.append(i)
            final = "".join(list_mo)
            return final
            
def main():
    number=int(input("Enter the number: "))
    base_final = int(input("Enter the final base: "))
    first = change_base(number, base_final)
    print(first)
if __name__ == "__main__":
    main()