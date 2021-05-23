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

def secant(num1, num2, func):
    es = 10 ** -5
    cnt = 0

    while True:
        fnum1 = func.subs(x, num1)
        fnum2 = func.subs(x, num2)

        temp = num1 - fnum1 * (num2 - num1) / (fnum2 - fnum1)
        ea = np.abs((num2 - num1) / num2)
        cnt += 1

        if ea < es:
            break

        num1, num2 = num2, temp

    return num2, ea, cnt


if __name__ == '__main__':
    x = sp.symbols('x')
    func = x ** 2 - 3 * x + np.e ** x - 2
    dfunc = sp.Derivative(func, x).doit()

    var, ea, cnt1 = newtonRaphson(0, func, dfunc)

    print(f"뉴튼 랩슨법: 근의 값은 {var}이고, 상대 오차 값은 {ea}이고, 총 {cnt1}번 반복했다.")

    num2, ea, cnt2 = secant(0, 0.1, func)

    print(f"할선법: 근의 값은 {num2}이고, 상대 오차 값은 {ea}이고, 총 {cnt2}번 반복했다.")

    if cnt1 > cnt2:
        print(f"뉴튼 랩슨법이 할선법보다 {cnt1 - cnt2}만큼 더 반복했습니다")
    elif cnt1 < cnt2:
        print(f"할선법이 뉴튼 랩슨법보다 {cnt2 - cnt1}만큼 더 반복했습니다")
    else:
        print("뉴튼 랩슨법, 할선법 둘 다 같은 횟수만큼 반복하였습니다.")