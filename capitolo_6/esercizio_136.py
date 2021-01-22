#!/bin/python3
def reverseLookup():
    dicto = {
        1: "milan",
        2: "inter",
        3: "atalanta",
        4: "roma",
        5: "napoli" 
    }
    for i in dicto.keys():
        print(i, dicto.get(i))
def main():
    reverseLookup()

if __name__ == "__main__":
    main()