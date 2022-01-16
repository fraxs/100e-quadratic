#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
import math
from fractions import Fraction
def Factored(a,b,c):
  quadratic1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
  quadratic2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
  discrim = (b**2 - (4*a*c))
  if discrim < 0:
    return None
  final = []
  if quadratic1 < 0:
    
    final.append(f"(x + {int(-quadratic1)})")
  else:
    final.append(f"(x - {int(quadratic1)})")
  if quadratic2 < 0:
    final.append(f"(x + {int(-quadratic2)})")
  else:
    final.append(f"(x - {int(quadratic2)})")
  return final
  '''
  input parameters:
  a, b, c: signed float
  These are the coefficients in the quadratic function ax^2 + bx + c = 0
  
  Write the equation in a nicely formatted factored form. This means no fractions
  
  return:
  list : 2 string literals representing the factors.  The order does not matter
  None if the quadratic can not be factored
  '''
  return None

def main():
  assert ("(x + 3)" in Factored(1,1,-6)) == True
  assert ("(x - 2)" in Factored(1,1,-6)) == True
  assert ("(x + 2)" in Factored(1,7,10)) == True
  assert ("(2x + 1)" in Factored(2,5,2)) == True
  assert ("(x + 2)" in Factored(2,5,2)) == True
  assert ("(3x + 1)" in Factored(6,-7,-3)) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
  
if __name__ == "__main__":
  print(Factored(6,-7,-3))
  
