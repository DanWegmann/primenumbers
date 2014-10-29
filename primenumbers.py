##Dan Wegmann
#Prime Number calculator
#calculates primes numbers up to N
import math

def isPrime(num):
    for k in range(2, num):
        if (num % k) == 0:
            return False #number is not prime
    return True #number is prime

def main():
    inputNum = int(input("What is the maximum number?: "))

    while (inputNum < 1):
        print("Enter a number greater than 0")
        inputNum = int(input("Reenter number: ")) 
    
    if (inputNum == 1):
        primeList = [1]
        print(primeList)
    else:
        primeList = []
        primeList.append(2) #2 is always prime

        for x in range(3, inputNum):
            if (isPrime(x)):
                primeList.append(x)
    
        print(primeList)

