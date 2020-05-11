from math import exp

def sinh(coeff):
    return (exp(coeff)-exp(-coeff))/2

def temps(t,a):
     c=299792458
     coeff=a*t/(4*c)
     return 4*c/a*sinh(coeff) 

acceleration=96.170384222
t=5E-5
print(temps(t,acceleration))

