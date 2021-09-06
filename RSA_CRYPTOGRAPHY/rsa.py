import math
import random


def primesInRange(x, y):
    prime_list = list()
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def find_lowest_coprime(EULER_FUNCTION_N):
	for number in range(1,EULER_FUNCTION_N):
		print(number)
		if gcd(number,EULER_FUNCTION_N) == 1:
			return number

def calculate_encryption_value(p,q,EULER_FUNCTION_N):
	output_list = list()
	for number in range(2,EULER_FUNCTION_N):
		if gcd(number,EULER_FUNCTION_N) == 1 and number%p != 0 and number%q != 0:
			output_list.append(number)
	return output_list

def calculate_decryption_value(e,N):
	x = 1
	while True:
		d = (N*x) + 1
		if (d%e == 0):
			return int(d/e)
		x += 1


PRIME_RANGE_MIN = 10
PRIME_RANGE_MAX = 100

p_primes_list = primesInRange(PRIME_RANGE_MIN,PRIME_RANGE_MAX)
p = p_primes_list[random.randint(0,len(p_primes_list)-1)]
print("p:",p)

q_primes_list = primesInRange(PRIME_RANGE_MIN,PRIME_RANGE_MAX)
q = q_primes_list[random.randint(0,len(q_primes_list)-1)]
print("q:",q)

n = p*q
EULER_FUNCTION_N = (p-1)*(q-1)

print("n:",n)
print("FI FUNCTION:",EULER_FUNCTION_N)

e_values_list = calculate_encryption_value(p,q,EULER_FUNCTION_N)
e = e_values_list [random.randint(0,len(e_values_list)-1)]
print("e:",e)

d = calculate_decryption_value(e,n)
print("d:",d)

##ZKOUSKA##

print(end="\n\n")

test_message_value = 4
print("TESTING")
print("test message value:",test_message_value)

ciphered_message_value = pow(test_message_value,e)%n
print("ciphered message value:",ciphered_message_value)

deciphered_message_value = pow(ciphered_message_value,d)%n
print("deciphered message value:",deciphered_message_value)

if test_message_value == deciphered_message_value:
	print("TEST OK")
else:
	print("TEST FAILED")

