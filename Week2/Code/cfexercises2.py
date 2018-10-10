#!/usr/bin/env python3


#### To be modified to make it a "module"

def foo1(x):
    return x ** 0.5 #exponent, x to the power of 0.5 

def foo2(x, y):
    if x > y:
        return x
    return y

def foo3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo5(x): # a recursive function
    if x == 1:
        return 1
    return x * foo5(x - 1) #!x factorial of x 

foo5(15)

####
# once script is run, these function can be called on  
# and the value of x can be changed within terminal e.g foo4(10)
