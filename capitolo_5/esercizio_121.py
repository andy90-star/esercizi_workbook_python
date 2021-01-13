#!/bin/python3
import random
def main():
    number = 8
    list_ticket = list()
    for i in range(1, 48, 8):
        gene = random.randint(i,number)
        list_ticket.append(gene)
        number += 8
    list_ticket.sort()
    print(list_ticket)    


if __name__ == "__main__":
    main()