def Fibbonici(x):
    n = 1
    output = [1]
    while len(output) < x:
        output.append(n)
        n += output[-2]
    return output




