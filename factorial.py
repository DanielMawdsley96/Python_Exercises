def Factorial(x):
    y = x
    while x > 1:
        y *= (x-1)
        x -= 1
    return y

print(Factorial(4))

def Factorial2(x):
    y = range(1,x+1)
    A = 1
    for a in y:
        A *= a
    return A

print(Factorial2(6))


