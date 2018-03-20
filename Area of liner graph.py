import numpy as ny
def area_line(L, U, a, b):
    Upper = 0.5*a*U**2 + b*U
    Lower = 0.5*a*L**2 + b*L
    Area = Upper - Lower
    print('The area of {}x+{} between {} and {} is {}'.format(a,b,L,U,Area))
area_line(0,5,2,-2)
