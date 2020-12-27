import random
import time
def lancio(lista):
    a = random.randint(1,6)
    c = random.randint(1,6)
    str(a)
    str(c)
    b = a+c
    lista.append(b)
   # print(b)


def verift(z,lista):
    if z == 1:
        lista[1] +=1
    if z == 2:
        lista[2] +=1
    if z == 3:
        lista[3] +=1
    if z == 4:
        lista[4] +=1
    if z == 5:
        lista[5] +=1
    if z == 6:
        lista[6] +=1
    if z == 7:
        lista[7] +=1
    if z == 8:
        lista[8] +=1
    if z == 9:
        lista[9] +=1
    if z == 10:
        lista[10] +=1
    if z == 11:
        lista[11] += 1
    if z == 12:
        lista[12] += 1

def media(lista):
    v = 1
    li =[]
    for i in lista:
        cal = lista[i]/12
        li.append(cal)
    for i in li:
        print("La probabilità del numero  " + str(v) + " %-23f" % i)
        v +=1 


def main():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    l = 0
    m = 0
    n = 0
    lista3 = {
        1 : a,
        2 : b,
        3 : c,
        4 : d,
        5 : e,
        6 : f,
        7 : g,
        8 : h,
        9 : i,
        10 : l,
        11 : m,
        12 : n,
    }
    lista=[]
    lista2=[]
    for i in range(0,1000):
        #time.sleep(1)
        lancio(lista)
    for i in lista:
        verift(i, lista3)
    print(lista3)
    media(lista3)

if __name__ == "__main__":
    main()