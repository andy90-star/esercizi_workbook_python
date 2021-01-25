#!/bin/python3
def redunce(numerator, denominator):
    if denominator%numerator==0 and numerator%numerator==0:
        numerator_1 = numerator/numerator
        denominator = denominator/numerator
        return int(numerator_1), int(denominator)
    else:
        if numerator < denominator:
            for index in range(1,denominator):
                if numerator%index==0 and denominator%index==0:
                    numerator = numerator/index
                    denominator = denominator/index
                else:
                    return int(numerator),int(denominator)

        elif numerator >= denominator:
            for index in range(1,numerator):
                if numerator%index==0 and denominator%index==0:
                    numerator = numerator/index
                    denominator = denominator/index
                else:
                    return int(numerator),int(denominator)
def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        first = redunce(numerator, denominator)
        print(first)
    except ValueError:
        print("Value not is int")
if __name__ == "__main__":
    main()