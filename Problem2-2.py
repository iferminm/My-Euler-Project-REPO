# -*- encoding: utf-8 -*-
# Israel Fermín Montilla <ferminster@gmail.com>

# Another approach by using Binet's Formula with an arrangement
# to make all powers possitive
from math import sqrt

Phy = (1 + sqrt(5)) / 2

def nth_fib_number(n):
    return int(((Phy ** n) - ((-1 ** n) / (Phy ** n))) / sqrt(5))

counter = 1
result = 0

while True:
    fib = nth_fib_number(counter)
    if fib > 4000000: break
    if fib % 2 == 0: result += fib
    counter += 1

print result
