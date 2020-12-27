def binario(a):
    cal = a % 2
    a /= 2
    print (int(cal))
    if int(a) != 0 :
        binario(a)

def main():
    try:
        a = int(input("Inserisci a "))
        binario(a)
    except ValueError:
        print("Bro hai sbagliato devi inserire un numero")
        main()

if __name__ == '__main__':
    main()
