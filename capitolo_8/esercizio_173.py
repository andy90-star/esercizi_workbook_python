def somma(t):
    a = input("Inserisci il numero")
    if str(a) == "" or  str(a) == " ":
        return print(str(t))
    else:
        t += int(a)
        somma(t)

def main():
    v = 0
    somma(v)

if __name__ == '__main__':
    main()
