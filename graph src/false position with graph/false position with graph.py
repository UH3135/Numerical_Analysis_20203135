import numpy as np
import matplotlib.pyplot as plt

def falsePosition(min, max, func):
    es = 10 ** -5
    cnt = 0 # 반복 횟수

    if func(min) * func(max) > 0: #만약 min과 max의 부호가 같으면 에러 출력하고 함수 종료
        print("This section don't have root or have even-numbered root")
        return -1

    ax = min
    ay = func(ax)

    cx = max
    cy = func(cx)

    bx = (ax * cy - cx * ay) / (cy - ay)

    while True:
        oldBx = bx

        bx = (ax * cy - cx * ay) / (cy - ay)
        by = func(bx)

        if ay * by <= 0:
            cx = bx
            cy = by
        else:
            ax = bx
            ay = by

        ea = np.abs(bx - oldBx) / bx

        cnt += 1

        if ea != 0 and ea < es:
            break

    return ax, cx, ea, cnt


if __name__ == '__main__':
    range = np.linspace(3, 4.5, 100)
    f = lambda x: np.sin(10*x) + np.cos(3*x)
    start = 3.5
    end = 4

    b = (start * f(end) - end * f(start)) / (f(end) - f(start))

    sx, ex, ea, cnt = falsePosition(start, end, f)

    print(f"[{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea}")

    plt.plot(range, f(range))
    plt.axvline(start, 0, 0.29, color='gray', linestyle='-', linewidth='3')
    plt.axvline(b, 0, 0.32, color='gray', linestyle='--', linewidth='2')
    plt.axvline(end, 0, 0.92, color='gray', linestyle='-', linewidth='3')

    plt.scatter(start, f(start), c='b')
    plt.text(start-0.011, f(start) + 0.1, "a", fontsize=10)

    plt.scatter(b, f(b), c='r')
    plt.text(b-0.011, f(b) + 0.1, "b", fontsize=10)

    plt.scatter(end, f(end), c='b')
    plt.text(end-0.011, f(end) + 0.1, "c", fontsize=10)

    plt.show()