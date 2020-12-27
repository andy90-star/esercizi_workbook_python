def contrario(a):
    v = ""
    c = list(a)
    c.reverse()
    for i in c:
        v += i
    print(v)
    if v == a:
        print("la parola " + a + " è polindrica")

def main():
    try:
        a = input("Inserisci un nome ")
        contrario(a)
    except ValueError or TypeError:
        print("Inserire una parola !!!")
        main()


if __name__ == '__main__':
    main()
