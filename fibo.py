# from http://docs.python.org/3/tutorial/modules.html
# Fibonacci numbers module

def fib(n): # write Fibonacci series up to n
	a, b = 0, 1
	while b < n:
		end = ' '
		print(b, end,)
		a, b = b, a+b
	print()
	
def fib2(n): # return Fibonacci series up to n
	result = []
	a = 0
        b = 1
	while b <= n:
		result.append(b)
		a, b = b, a+b
	return result
