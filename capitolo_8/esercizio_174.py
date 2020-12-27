def euclide (a,b):
    if a == b:
        return print(str(a))
    elif a > b:
        a -= int(b)
        euclide(a,b)
    elif a < b:
        b -= int(a)
        euclide(a ,b)

def main():
    try:
        a = int(input("Inserisci il primo numero"))
        b = int(input("Inserisci il secondo numero"))
        euclide(a,b)
    except ValueError:
        print("C'è un errore di tipo  Value")
        main()

if __name__ == '__main__':
    main()
