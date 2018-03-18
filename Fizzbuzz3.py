multiples = {3:'Fizz', 5:'Buzz', 7:'Boom', 2:'Bang'}
n = 100
def FizzBuzz(multiples, n):
    for i in range(1,n+1):
        output = ''
        for multiple in multiples:
            if i % multiple == 0:
                output += multiples[multiple]
        if output == '':
                output = i
        print(output)
        
FizzBuzz(multiples, n)