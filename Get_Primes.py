'''
Code to print the nth prime number 
'''
def get_primes(n):
	primes=[2]
	current_num=3
	while True:
		isprime=True
		for prime in primes:
			if current_num % prime ==0:
				isprime=False
				break
		if isprime==True:
			primes.append(current_num)
		current_num += 1
		if len(primes)==n:
			break
			'''return the nth prime number '''
	return primes[-1]
print (get_primes(6))