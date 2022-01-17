import math
from fractions import Fraction
def Factored(a,b,c):
  quadratic1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
  quadratic2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
  discrim = (b**2 - (4*a*c))
  return Fraction(denominator=quadratic1, numerator= 0)


print(Factored(2,5,2))