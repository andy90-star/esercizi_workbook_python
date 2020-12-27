
def media(a,b):
    cal=a/b
    return print(cal)


def main():
    lista = []
    conta = 0
    Bool = True
    while Bool:
        numeri = input("Inserisci il numero")
        lista.append(numeri)
        if numeri == str(0):
            Bool = False
            lunghezza = len(lista)
    for i in lista:
        conta += int(i) 
    media(conta, lunghezza)

        

if __name__ == '__main__':
    main()