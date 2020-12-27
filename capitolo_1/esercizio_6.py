#!/bin/python3
import time
Tassa = 0.05
Mancia = 0.18
def costo():
    pago = float(input("Inserisci l'importo da pagare: "))
    print("Calcolo le tasse la mancia")
    for i in range(0, 3):
        time.sleep(1)
        print(".")
    tassa = pago * Tassa
    mancia = pago * Mancia
    totale =tassa + mancia + pago
    print("L'importo da pagare è di %.2f ,  le tasse: %.2f , la mancia, %.2f " % (totale,tassa,mancia))

def main():
    costo()


if __name__ == '__main__':
    main()