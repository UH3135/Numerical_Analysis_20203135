import numpy as np
import matplotlib.pyplot as plt

def bisection(min, max, func):
    es = 1 * 10**-5

    if func(min) * func(max) > 0: #만약 min과 max의 부호가 같으면 에러 출력하고 함수 종료
        print("This section don't have root or have even-numbered root")
        return -1

    ax = min
    bx = (min + max) / 2
    cx = max

    ay = func(ax)
    by = func(bx)
    cy = func(cx)

    while True:
        oldBx = bx

        bx = (ax + cx) / 2
        by = func(bx)

        if ay * by <= 0:
            cx = bx
            cy = by
        else:
            ax = bx
            ay = by

        ea = np.abs(bx - oldBx) / bx

        if ea != 0 and ea < es:
            break

    return ax, cx, ea


if __name__ == '__main__':
    range = np.linspace(3, 4.5, 100)
    f = lambda x: np.sin(10*x) + np.cos(3*x)
    start = 3.5
    end = 4

    sx, ex, ea = bisection(start, end, f)

    print(f"[{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea}")

    plt.plot(range, f(range))
    plt.axvline(start, 0, 0.29, color='gray', linestyle='-', linewidth='3')
    plt.axvline((start+end) / 2, 0, 0.5, color='gray', linestyle='--', linewidth='2')
    plt.axvline(end, 0, 0.92, color='gray', linestyle='-', linewidth='3')

    plt.scatter(start, f(start), c='b')
    plt.text(start-0.011, f(start) + 0.1, "a", fontsize=10)

    plt.scatter((start+end) / 2, f((start+end) / 2), c='r')
    plt.text(((start+end) / 2)-0.011, f((start+end) / 2) + 0.1, "b", fontsize=10)

    plt.scatter(end, f(end), c='b')
    plt.text(end-0.011, f(end) + 0.1, "c", fontsize=10)

    plt.show()