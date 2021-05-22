import numpy as np

def secant(num1, num2, func):
    es = 10 ** -5

    while True:
        fnum1 = func(num1)
        fnum2 = func(num2)

        temp = num1 - fnum1 * (num2 - num1) / (fnum2 - fnum1)
        ea = np.abs((num2 - num1) / num2)

        print(f"num1 : {num1}, fnum1: {fnum1}, ea : {ea}")

        if ea < es:
            break

        num1, num2 = num2, temp

    return num1, num2, ea


if __name__ == '__main__':
    func = lambda x: (2 * 9.81 / 1000) - 1.4 * 10**-5 * x**1.5 - 1.15 * 10**-5 * x**2
    num1, num2, ea = secant(30, 30.1, func)
    print(f"최종 근은 {num2}, 최종 상대오차는 {ea}")
