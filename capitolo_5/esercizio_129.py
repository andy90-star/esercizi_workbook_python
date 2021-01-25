#!/bin/python3
def token(tok):
    list_token = list(tok)
    for index_2 in list_token:
        index_2 = str(index_2)
    return list_token
        
def main():
    tok = input("Enter expression mathical: ")
    sub = token(tok)
    print(sub)

if __name__ == "__main__":
    main()