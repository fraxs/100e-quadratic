#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
import math
from fractions import Fraction
def Factored(a,b,c):
    
    

def main():
  assert "(x + 3)" in Factored(1,1,-6) == True
  assert "(x - 2)" in Factored(1,1,-6) == True
  assert "(x + 2)" in Factored(1,7,10) == True
  assert "(2x + 1)" in Factored(2,5,2) == True
  assert "(x + 2)" in Factored(2,5,2) == True
  assert "(3x + 1)" in Factored(6,-7,-3) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
  
if __name__ == "__main__":
  print(Factored(2,5,2))
  
