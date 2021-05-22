import numpy as np
import matplotlib.pyplot as plt

def secant(num1, num2, func):
    ran = np.linspace(30, 40, 100)
    es = 10 ** -5
    cnt = 0

    while True:
        fnum1 = func(num1)
        fnum2 = func(num2)

        temp = num1 - fnum1 * (num2 - num1) / (fnum2 - fnum1)
        ea = np.abs((num2 - num1) / num2)

        plt.scatter(num1, fnum1, c='b')
        cnt += 1
        plt.text(num1, fnum1 + 0.0001, "f{}".format(cnt), fontsize=8)



        if ea < es:
            break

        num1, num2 = num2, temp

    return num1, num2, ea


if __name__ == '__main__':
    xran = np.linspace(30, 40, 100)

    func = lambda x: (2 * 9.81 / 1000) - 1.4 * 10**-5 * x**1.5 - 1.15 * 10**-5 * x**2
    plt.plot(xran, func(xran))

    num1, num2, ea = secant(30, 30.5, func)
    print(f"최종 근은 {num2}, 최종 상대오차는 {ea}")

    plt.axvline(num2, 0, 0.27, c='gray', linestyle='--')
    plt.show()