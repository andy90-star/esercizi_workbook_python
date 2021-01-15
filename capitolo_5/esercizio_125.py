#!/bin/python3
import random
def shuffle(deck):
    moment = 0
    list_shuffle = list()
    for i in range(0,52):
        shuf = random.randint(1,51)
        moment = deck[shuf]
        list_shuffle.append(moment)
    return list_shuffle

def createDeck():
    seg = ""
    list_deck = list()
    list_seg = ["s","d","h","c"]
    list_letter = ["j","q","k","a"]
    for seg in  list_seg:
        for number in range(1, 10):
            cart = str(number)+seg
            list_deck.append(cart)
    for seg in  list_seg:
        for number in list_letter:
            cart = str(number)+seg
            list_deck.append(cart)
    return  list_deck

def main():
    deck = createDeck()
    deck_shuff = shuffle(deck)
    print(deck_shuff)

if __name__ == "__main__":
    main()