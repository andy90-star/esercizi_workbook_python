#!/bin/python3
def aumento(cal):
    a=input(f"""Quale contenitore vuoi riciclare
    1 = 1L o meno;
    2 = +1L;
    0 = esci dal programma
    """)
    
    if a == "1":
        cal += 0.10
        aumento(cal)
    elif a == "2":
        cal += 0.25
        aumento(cal)
    elif a == "0":
        return print("Ecco il tuo guadagna " + str(cal))

def main():
    try:
        cal = 0
        aumento(cal)
    except ValueError or TypeError:
        print("Inseri i valori indicati")
        main()


if __name__ == '__main__':
    main()
