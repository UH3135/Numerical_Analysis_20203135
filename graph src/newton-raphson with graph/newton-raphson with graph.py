import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

xran = np.linspace(-0.85, 0, 100)
gfunc = lambda x: x ** 2 - 3 * x + np.e**x - 2

def newtonRaphson(start, func:sp.Add, dfunc:sp.Add):
    es = 10 ** -5
    x = sp.symbols('x')

    cnt = 0

    var = start

    while True:
        oldVar = var
        var = var - func.subs({x: var}) / dfunc.subs({x: var})

        f = lambda x: gfunc(oldVar) / (oldVar - var) * (x - var)
        plt.plot(xran, f(xran), 'b:')

        plt.text(oldVar-0.011, gfunc(oldVar) + 0.1, "f{}".format(cnt+1), fontsize=10)

        plt.scatter(oldVar, gfunc(oldVar), c='b', linewidths=1)
        plt.axvline(oldVar, 0, (1.5 + gfunc(oldVar))/3, color='gray', linestyle=':', linewidth='2')

        ea = np.abs((var - oldVar) / var)
        cnt += 1

        if ea < es:
            break

    return var, ea, cnt


if __name__ == '__main__':

    x = sp.symbols('x')
    func = x ** 2 - 3 * x + np.e**x - 2
    dfunc = sp.Derivative(func, x).doit()

    plt.plot(xran, gfunc(xran))

    var, ea, cnt = newtonRaphson(-0.6, func, dfunc)

    print(f"근의 값은 {var}이고, 상대 오차 값은 {ea}이고, 총 {cnt}번 반복했다.")
    plt.show()
