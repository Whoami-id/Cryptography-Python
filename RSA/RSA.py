import math
import random


def is_prime(p):
    for i in range(2,math.isqrt(p)):
        if p % i == 0:
            return False
        else:
            return True


def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p 

def lcm(a, b):
    return a*b//math.gcd(a, b)


def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False


def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False


def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n//p

#step 1: Generate two  distinct primes
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated primes: ", p, q)

#step 2: compute n = q*q
n = q*p
print("Modulus n: ", n)


#step 3 lambda
lambda_n = lcm(p-1, q-1)
print("Lmabda n:" , lambda_n)

#step 4
e = get_e(lambda_n)
print("Pblic exponent e: ", e)

# step 5
d = get_d(e, lambda_n)
print("Secret exponent:", d)

#Done with key generation
print("Public key (e, n): ", e, n)
print("Secret Key (d): ", d)

#sendig message
m = 117
c = (m**e) % n 
print("Bob sends", c)

m2 = (c**d) % n 
print("Alice message", m2)


#Eve
print("Eve sess the following:")
print("Public key (e, n):", e, n)
print("Encrypted cipher: ", c)
p,q = factor(n)
print("Factors:", p,q)

lambda_n = lcm(p-1, q-1)
print("Eve: lambda n: ", lambda_n)
d = get_d(e, lambda_n)
print("Eve: secret exponent: ", d)

m3 = c**d %n
print("Eve message:", m3)