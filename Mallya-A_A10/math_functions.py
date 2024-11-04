def power(x, n): #raises x to the power of n
	
	if x == 0 and n == 0:
		return 1

	elif x == 0 and n < 0:
		raise ValueError('0 cannot be raised to a negative power.')

	return x**n


def divide(a, b): # return a / b
	if b == 0:
		raise ValueError('Undefined: attempted division by 0.')
	
	return a / b


		
