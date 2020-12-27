def conversione(s):
    alfabeto={
"a" : "alpha",
"b" : "bravo",
"c" : "charlie",
"d" : "delta",
"e" : "echo",
"f" : "foxtrot",
"g" : "golf",
"h" : "hotel",
"i" : "india",
"j" : "juliet",
"k" : "kilo",
"l" : "lima",
"m" : "mike",
"n" : "november",
"o" : "oscar",
"p" : "papa",
"q" : "quebec",
"r" : "romeo",
"s" : "sierra",
"t" : "tango",
"u" : "uniform",
"v" : "victor",
"w" : "whiskey",
"x" : "xray",
"y" : "yankee",
"z" : "zulu"
}
    li = list(s)
    for i in li:
        a = alfabeto.get(i)
        print(a)

def main():
    try:
        s = input("inserisci la frase ")
        conversione(s)
    except TypeError or ValueError : 
        print("Hai scritto la tua frase??")
        main() 

if __name__ == '__main__':
    main()