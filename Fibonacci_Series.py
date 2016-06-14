'''
Function that returns a Fibonacci series
'''

def fib():
    a,b = 1,1
    while 1:
        yield a
        a,b = b, a+b
import types
if type(fib()) == types.GeneratorType:
    counter = 0
    for n in fib():
        print n
        counter += 1
        if counter == 8:
            break
    

    
