# Primes
primeFlags = [False, False]


def init_primes(n):
	primeFlags.extend([False] * (n - len(primeFlags)))
	for i in range(2, n):
		if primeFlags[i]:
			for j in range(2 * i, n, i):
				primeFlags[j] = False


def is_prime(n):
	if not n < len(primeFlags):
		init_primes(n + 1)
	return primeFlags[n]


# coding: UTF-8
from string import ascii_uppercase


def hex_to_string(h):
	n = 2
	try:
		return "".join([chr(int(h[i:i + n], 16)) for i in range(0, len(h) - n + 1, n)])
	except:
		return None


def string_to_hex(s):
	try:
		return ascii_uppercase("".join([hex(ord(c))[2:] for c in s]))
	except:
		return None


def binary_to_hex(b):
	r = hex(int(b, 2))[2:]
	if r[-1] == 'L':
		r = r[:-1]
	return r
