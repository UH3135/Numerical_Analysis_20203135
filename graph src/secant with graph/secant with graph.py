import numpy as np
import matplotlib.pyplot as plt

xran = np.linspace(2.5, 4.5, 100)

f = lambda x: np.sin(10 * x) + np.cos(3 * x)

def secant(num1, num2, func):
    es = 10 ** -5
    cnt = 0

    while True:
        fnum1 = func(num1)
        fnum2 = func(num2)

        f = lambda x: (fnum2 - fnum1) / (num2 - num1) * (x - num1) + fnum1
        plt.plot(xran, f(xran), 'b:')

        temp = num1 - fnum1 * (num2 - num1) / (fnum2 - fnum1)
        ea = np.abs((num2 - num1) / num2)

        plt.scatter(num1, fnum1, c='k')
        cnt += 1
        plt.text(num1, fnum1 + 0.1, "f{}".format(cnt), fontsize=10)



        if ea < es:
            break

        num1, num2 = num2, temp

    return num1, num2, ea


if __name__ == '__main__':
    plt.plot(xran, f(xran))
    plt.axhline(0, 0, 1)
    plt.xlim(2.9, 4)
    plt.ylim(-2.1, 1.9)

    num1, num2, ea = secant(3, 3.5, f)
    print(f"최종 근은 {num2}, 최종 상대오차는 {ea}")

    plt.show()