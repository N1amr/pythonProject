MAX = 10000

isPrime = MAX * [True]
isPrime[0] = False
isPrime[1] = False
for i in range(2, MAX):
	if isPrime[i] == True:
		for j in range(2 * i, MAX, i):
			isPrime[j] = False
primes = []
for i in range(MAX):
	if isPrime[i]:
		primes.append(i)

def plus(n):
	return n + 1

def ans():
	for i in range(0, len(primes)):
		for j in range(i + 1, len(primes)):
			for k in range(j + 1, len(primes)):
				q = [primes[i], primes[j], primes[k]]
				Q = map(plus, q)
				N = 1
				for x in q:
					N = N * x
				NN = N + 1
				if NN % Q[0] + NN % Q[1] + NN % Q[2] == 0:
					return "N = " + str(N) + " = " + str(q[0]) + " * " + str(q[1]) + " * " + str(q[2])

print ans()
