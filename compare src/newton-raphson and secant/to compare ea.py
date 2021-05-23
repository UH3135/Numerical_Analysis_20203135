import sympy as sp
import numpy as np

def newtonRaphson(start, func:sp.Add, dfunc:sp.Add, stand):
    es = 10 ** -5
    x = sp.symbols('x')

    cnt = 0

    var = start

    while True:
        oldVar = var
        var = var - func.subs({x: var}) / dfunc.subs({x: var})

        ea = np.abs((var - oldVar) / var)
        cnt += 1

        if ea < es or cnt >= stand:
            break

    return var, ea, cnt

def secant(num1, num2, func, stand):
    es = 10 ** -5
    cnt = 0

    while True:
        fnum1 = func.subs(x, num1)
        fnum2 = func.subs(x, num2)

        temp = num1 - fnum1 * (num2 - num1) / (fnum2 - fnum1)
        ea = np.abs((num2 - num1) / num2)
        cnt += 1

        if ea < es or cnt >= stand:
            break

        num1, num2 = num2, temp

    return num2, ea, cnt


if __name__ == '__main__':
    x = sp.symbols('x')
    func = x ** 2 - 3 * x + np.e ** x - 2
    dfunc = sp.Derivative(func, x).doit()

    print("반복의 최대 횟수가 5로 고정될 경우")
    print()
    stand = 5

    var, ea1, cnt = newtonRaphson(0, func, dfunc, stand)
    print(f"뉴튼 랩슨법: 근은 {var} 이고, 상대오차는 {ea1}, 총 {cnt}번 반복했습니다.")

    num, ea2, cnt = secant(0, 0.1, func, stand)
    print(f"할선법: 근은 {num} 이고, 상대오차는 {ea2}, 총 {cnt}번 반복했습니다.")

    if ea1 > ea2:
        print(f"뉴튼 랩슨법이 할선법보다 {ea1 - ea2}만큼 더 오차가 발생했습니다")
    elif ea1 < ea2:
        print(f"할선법이 뉴튼 랩슨법보다 {ea2 - ea1}만큼 더 오차가 발생했습니다")
    else:
        print("할선법, 뉴튼 랩슨법 둘 다 같은 횟수만큼 오차가 났습니다.")

    print()
    print("----------------------------------------------------------------------")
    print()

    print("반복의 최대 횟수가 10으로 고정될 경우")
    print()
    stand = 10

    var, ea1, cnt = newtonRaphson(0, func, dfunc, stand)
    print(f"가위치법: [근은 {var} 이고, 상대오차는 {ea1}, 총 {cnt}번 반복했습니다.")

    num, ea2, cnt = secant(0, 0.1, func, stand)
    print(f"할선법: 근은 {num} 이고, 상대오차는 {ea2}, 총 {cnt}번 반복했습니다.")

    if ea1 > ea2:
        print(f"뉴튼 랩슨법이 할선법보다 {ea1 - ea2}만큼 더 오차가 발생했습니다")
    elif ea1 < ea2:
        print(f"할선법이 뉴튼 랩슨법보다 {ea2 - ea1}만큼 더 오차가 발생했습니다")
    else:
        print("할선법, 뉴튼 랩슨법 둘 다 같은 횟수만큼 오차가 났습니다.")