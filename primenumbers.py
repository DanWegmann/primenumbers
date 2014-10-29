import math
 
def isPrime(num):
    for k in range(2, num):
        if (num % k) == 0:
            return False
    return True

def main():
    inputNum = int(input("What is the maximum number?: "))
    
    primeList = []
    primeList.append(2)
    
    for x in range(3, inputNum):
        if (isPrime(x)):
            primeList.append(x)

    print(primeList)
