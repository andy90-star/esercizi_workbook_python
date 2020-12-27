def convertire(a, ver):
    while ver:
        cal =  a % 2
        a /= 2
        print(int(cal))
        if int(a) == 0 :
            ver = False


def iniziamo():
    ver = True
    a = int(input("inserisci il numero "))
    convertire(a, ver)

def main():
    try:
        iniziamo()
    except ValueError:
        print("Ho detto inserisci un numero")
        main()
if __name__ == '__main__':
    main()
