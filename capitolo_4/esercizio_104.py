#!/bin/python3
def int2hex(number, hexa_2):
    """convert integer in hexadecimal"""
    final = ""
    for _ in range(0,len(number)):
        moment = int(number)%16
        number = int(number)/16
        print(moment)
        if moment in hexa_2:
            final += hexa_2.get(moment)
        elif not moment in hexa_2:
            final += str(moment)
    print("The number must be read at contrary")
    return final

def hex2int(number, hexa):
    """convert hexadecimal in integer"""
    final = ""
    list_new = list()
    result = 0
    final_2 = ""
    for number in number[0:]:
        if number in hexa:
            final += str(hexa.get(number)) + ","
        elif not number in hexa:
            final += str(number) + ","
    for number in final[0:]:
        if number != ",":
            final_2 += str(number)
        elif number == ",":
            list_new.append(final_2)
            final_2 = ""
    cont = len(list_new)-1
    for number in list_new:
        result += int(number) * (16**cont)
        cont -= 1
    return result

def main():
    hexa_int ={
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F",

    }
    hexa = {
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15,
    }
    select = input(f"""Select:
1.hexadecimal in integer;
2.integer in hexadecimal; 
""")
    if select == "1":
        number=input("Enter the hexadecimal number: ")
        first = hex2int(number,hexa)
        print(first)
    elif select == "2":
        number=input("Enter the  number: ")
        first = int2hex(number, hexa_int)
        print(first)


if __name__ == '__main__':
    main()