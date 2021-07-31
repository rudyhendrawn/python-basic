# Testing github copilot
def fiboprime(n):
	"""get fibonnace sequence of length n
	if the sequence is prime, store in x"""
	x = [1,2]
	while len(x) < n:
		x.append(x[-1] + x[-2])
	return x

fiboprime(10)

def palindrom(str):
	"""check if a string is palindrom"""
	return str == str[::-1]

palindrom("buruk")
