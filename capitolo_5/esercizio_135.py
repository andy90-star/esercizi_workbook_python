#!/bin/python3
def Sieve(limit, list_number):
    for i in range(0, limit + 1):
        list_number.append(i)
    list_number[1] = 0
    p = 2
    while p < limit:
        for i in range(p*2, limit + 1, p):
            list_number[i] = 0
    p = p + 1
    while p < limit and list_number[p] == 0:
        p = p + 1
    print("The primes up to", limit, "are:")
    for i in list_number:
        if list_number[i] != 0:
            print(i)

def main():
    limit = int(input("Identify all primes up to what limit? "))
    list_number = []
    Sieve(limit, list_number)
if __name__ == "__main__":
    main()