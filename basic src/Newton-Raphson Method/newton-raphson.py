import sympy as sp
import numpy as np

def newtonRaphson(start, func:sp.Add, dfunc:sp.Add):
    es = 10 ** -5
    x = sp.symbols('x')

    cnt = 0

    var = start

    while True:
        oldVar = var
        var = var - func.subs({x: var}) / dfunc.subs({x: var})

        ea = np.abs((var - oldVar) / var)
        cnt += 1

        if ea < es:
            break

    return var, ea, cnt


if __name__ == '__main__':
    x = sp.symbols('x')
    func = x ** 2 - 3 * x + np.e**x - 2
    dfunc = sp.Derivative(func, x).doit()

    var, ea, cnt = newtonRaphson(0, func, dfunc)

    print(f"근의 값은 {var}이고, 상대 오차 값은 {ea}이고, 총 {cnt}번 반복했다.")