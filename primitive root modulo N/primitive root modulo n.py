import math
import random


def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

print("PUBLICLY AGREED UPON:")

primes_list = primesInRange(100,1000)
random_prime_value_index = random.randint(0,len(primes_list))
p = primes_list[random_prime_value_index]
print("p =",p)

prim_root_list = primRoots(p)
random_prim_root_value_index = random.randint(0,len(prim_root_list))
g = prim_root_list[random_prim_root_value_index]
print("g =",g)

print()
print("SECRETELY CHOSEN:")

# ALICE
a = random.randint(0,100)
print("a =",a)
A = pow(g,a)%p
print("A =",A)

print()
# BOB
b = random.randint(0,100)
print("b =",b)
B = pow(g,b)%p
print("B =",B)

print()
#####################

alice_key = pow(B,a)%p
bob_key = pow(A,b)%p

print("key1:",alice_key)
print("key2:",bob_key)

