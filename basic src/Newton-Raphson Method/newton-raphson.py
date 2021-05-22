import sympy as sp
import numpy as np

def newtonRaphson(start, func:sp.Add, dfunc:sp.Add):
    es = 10 ** -5

    cnt = 0

    x = start

    while True:
        oldX = x
        a = func.subs({x: oldX})
        b = dfunc.subs({x: oldX})

        x = x - (a / b)

        ea = np.abs((x - oldX) / x)
        cnt += 1

        print(f"x: {oldX}, func(x): {x}, ea: {ea}, a: {a}, b: {b}")

        if ea < es:
            break

    return x, ea, cnt


if __name__ == '__main__':
    x = sp.symbols('x')
    f = x**2  - 3*x + np.e**x - 2
    fprime = sp.Derivative(f, x).doit()
    start = 0
    x, ea, cnt = newtonRaphson(start, f, fprime)

    print(f"근은 {x}, 상대오차는 {ea}, 총 {cnt}번 반복했습니다.")