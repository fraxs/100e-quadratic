import math
import fractions as f
a = 6
b = -7
c = -3
quadratic2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
x = f.Fraction(quadratic2)
print(x)