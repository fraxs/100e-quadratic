#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
import math
import fractions as f
def isInt(x):
  if x == int(x):
    return True
def findGCF(x):
  for i in reversed(range(10)):
    if isInt(x[0]/i) == True and isInt(x[1]/i) == True:
      x = [x[0]/i, x[1]/i]
      break
  return x
def Factored(a,b,c):
  discrim = (b**2 - (4*a*c))
  if discrim < 0:
    return None
  quadratic1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
  quadratic2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
  list1 = [1*a,quadratic1*a]
  list2 = [1*a,quadratic2*a]
  solution1 = findGCF(list1)
  solution2 = findGCF(list2)
  final = []
  ta1 = solution1[0]
  a1 = "" if ta1==1 else int(ta1)
  ta2 = solution2[0]
  a2 = '' if ta2==1 else int(ta2)
  if solution1[1] < 0:
    final.append(f"({a1}x + {int(-solution1[1])})")
  if solution1[1] > 0:
    final.append(f"({a1}x - {int(solution1[1])})")
  if solution2[1] < 0:
    final.append(f"({a2}x + {int(-solution2[1])})")
  if solution2[1] > 0:
    final.append(f"({a2}x - {int(solution2[1])})")
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
  main()
  


