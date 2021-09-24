import math


def find_primes(n):
	p = None
	primes = []
	if len(primes) == 0: 
		start = 1
		if n>2:
			primes.append(2)
	for k in range(start,n,2):
		root = math.sqrt(k)
		p = True
		for prime in primes:
			if prime > root:
				break
			if k % prime == 0:
				p = False
				break
		if p is True and k!=1:
			primes.append(k)
	return primes