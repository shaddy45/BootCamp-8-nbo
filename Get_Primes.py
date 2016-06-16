'''
Function to print a list of the fist n prime numbers  
'''

# define a function that accepts integer varibale,n 
def list_first_n_primes_numbers(n):  
# A list of prime numbers with 2 as the first know prime number

	list_of_primes = [2] 
	# Assign current_number_being_tested to 3 as the next interger after 2
	current_number_being_tested = 3 
	while True:
		isprime=True # assign a boolean variable to value True
		for prime in list_of_primes:
			if current_number_being_tested % prime == 0:
				isprime = False
				break				
		if isprime == True:
			# Add number to list ofprime numbers if it is a prime number
			list_of_primes.append(current_number_being_tested)  
			# increment current_number_being_tested by 1 to go to the next number 
		current_number_being_tested += 1 
	
		if len(list_of_primes) == n:
			break
			'''return the list of prime number '''
	return list_of_primes
# Assign variable m to value of user in put, the nummber of prime numbers to be printed.

m = int(input("How many prime numbers do you want to print? "))
print (list_first_n_primes_numbers(m)) # Call function to print a list of first 6 prime numbers
