import sys, math

def get_primes(start, n):
	primes = [2]
	next_prime = 3
	return_list = []
	if start < 2:
		return_list.append(2)
	while len(return_list) < n:
		sqrt = math.sqrt(next_prime)
		i = 0
		flag = True
		while primes[i] <= sqrt:
			if next_prime%primes[i] == 0:
				flag = False
				break
			if i>=len(primes):
				break
			i += 1

		if flag:
			#print next_prime
			primes.append(next_prime)
			if next_prime > start:
				return_list.append(next_prime)
		next_prime += 2
	i = 0	
	
	return return_list

