import math


def recursive_modulus(p, q, r=0):
	if p % q == 0:
		r = recursive_modulus(p/q,q,r+1)
	return r

#Algorithm Function:
def prime_factorize(n):
	all_primes = find_primes(math.ceil(n/2)+1)
	factorization = {}
	c = 1
	for prime in all_primes:
		if n % prime == 0:
			factorization[prime] = recursive_modulus(n,prime)
			c*=(prime**factorization[prime])
			if c == n:
				break
	if len(factorization)==0:
		factorization[n]=1
	return factorization
#Algorithm function ends here


def get_super(x):
    normal = "0123456789"
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


#Returns styled factorization:
def stylize_factorization(n):
	d = prime_factorize(n)
	print(d)
	x = 1
	s = ""
	for factor in d:
		x*=d[factor]+1 
		s+=str(factor)+get_super(str(d[factor]))+" x "
	s = s[:-3]
	return s


