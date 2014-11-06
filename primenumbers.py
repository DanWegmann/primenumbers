## Dan Wegmann
#Prime Number calculator
#calculates primes numbers up to N
import math
 

def isPrime(num):
    for k in range(2, num):
        if (num % k) == 0: return False #number is not prime
    return True #number is prime


def main():
    inputNum = int(input("What is the maximum number?: "))

    primeList = []

    while (inputNum < 1):
        print("Enter a number greater than 0")
        inputNum = int(input("Reenter number: ")) 

    # ranged(x,y), x is inclusive, y is exclusive so use y + 1
    # will check if number entered is prime in addition to all numbers lower than it
    # 2 should come up prime without needing a special case
    # 1 is not prime
    for x in range(2, inputNum + 1):
        if (isPrime(x)):
            primeList.append(x)

    print(primeList)

main()
