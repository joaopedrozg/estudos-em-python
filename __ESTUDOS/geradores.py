


"""
def fib(max):
    x, y = 1, 1
    while x < max:
        yield x
        x, y = y, x + y


gen = fib(100)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""
def algo():
    return 1+2

def get_primos(input_list):
    return(e for e in input_list if is isprime(e))
