#!/bin/python3
import time
def main():
    iz = "."
    ravvio = "Ravvio il programma"
    dizio = {
        "jackhammer" : 130,
        "gas lawnmower" : 106,
        "alarm clock" : 70,
        "quiet room" : 40
    }
    valore = input("inserisci nome del rumore ")
    if valore in dizio:
        print("ecco il suono del rumore " + valore + " è a " + str(dizio.get(valore)) + "db")
    else:
        for i in range(0,4):
            ravvio += iz
            print(ravvio)
            time.sleep(1)
        
        main()
if __name__ == '__main__':
    main()