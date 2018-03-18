def Sum(x):
    y = x
    while x > 1:
        y += (x-1)
        x -= 1
    return y

print(Sum(4))

def Sum2(x):
    y = range(1,x+1)
    A = 0
    for a in y:
        A += a
    return A

print(Sum2(4))


