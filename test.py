

import numpy as np
import MCintegrate as mc

def f(x):
    return 0.5*x**3

a = 0
b = 1
n = 500000
integral = mc.MCint(f, a, b, n)

print(f"integral = {integral: 0.3f}")
print('actual answ = .125' )
