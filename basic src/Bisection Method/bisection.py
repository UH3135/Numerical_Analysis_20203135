import numpy as np

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

        print(f"ax: {ax}, ay: {ay}, bx: {bx}, by: {by}, cx: {cx}, cy: {cy}")

        if ay * by <= 0:
            cx = bx
            cy = by
        else:
            ax = bx
            ay = by

        ea = np.abs(bx - oldBx) / bx

        print(f"oldBx: {oldBx}, ea: {ea}")

        if ea != 0 and ea < es:
            break

    return ax, cx, ea


if __name__ == '__main__':
    f = lambda x: np.sin(10*x) + np.cos(3*x)
    start = 3.5
    end = 4

    sx, ex, ea = bisection(start, end, f)

    print(f"[{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea}")
