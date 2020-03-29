def fibonacci_sequence (n):
	if n < 0:
		raise ValueError("You better change the sign of that number")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)