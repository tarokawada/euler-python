# The prime factors of 13195 are 5, 7, 13 and 29

# What is the largest prime factor of the number 600851475143 13195000?

def getLargestPrime(number):
    factors = []
    primeFactors = []
    for x in range(3, number):
        if (x % 2 == 0):
            continue
        if (x % 3 == 0):
            continue
        if number % x == 0:
            factors.append(x)
    print(factors)
    # for x in factors:
    #     print(primeFactors)
    #     if isPrime(x, primeFactors) == True:
    #         primeFactors.append(x)
    #         print(x)

def isPrime(n, primeFactors):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    
    if len(primeFactors) > 0:
        for x in primeFactors:
            if n % x == 0:
                return False

    for x in range(3, n):
        if n % x == 0:
            return False

    return True

getLargestPrime(1319500000)