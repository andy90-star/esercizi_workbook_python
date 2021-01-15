#!/bin/python3
from esercizio_125 import shuffle, createDeck
import random
def hands(shuf):
    list_moment = list
    dict_deck = {}
    for hand in range(0,4):
        list_moment = []
        for card in range(0,5):
            shuf_1 = random.randint(0,51)
            moment = shuf[shuf_1]
            list_moment.append(moment)
        dict_deck[hand] = list_moment
    return dict_deck



    
def main():
    cart = createDeck()
    shuf = shuffle(cart)
    deck_hand = hands(shuf)
    print(deck_hand)

if __name__ == "__main__":
    main()