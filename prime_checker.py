import math

import math


def prime_check(n):
	if (n%2==0 and n!=2) or n==1:
		return False
	p = True
	for i in range (3,math.ceil(math.sqrt(n)),2):
		if n % i == 0:
			p = False
			break
	if p is True:
		return True
	else:
		return False
