#-*-coding: utf-8-*-
# Israel Fermín Montilla <ferminster@gmail.com>

def fact(n): return (1 if n == 0 else n * fact(n - 1))
print sum(map(int, str(fact(100))))
