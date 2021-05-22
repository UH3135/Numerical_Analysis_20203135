import numpy as np

def bisection(min, max, func):
    es = 1 * 10**-5
    cnt = 0

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
        cnt += 1

        if ea != 0 and ea < es:
            break

    return ax, cx, ea, cnt


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
    f = lambda x: np.sin(10*x) + np.cos(3*x)
    start = 3.5
    end = 4

    sx, ex, ea, cnt1 = bisection(start, end, f)
    print(f"이분법: [{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea}, 총 {cnt1}번 반복했습니다.")

    sx, ex, ea, cnt2 = falsePosition(start, end, f)
    print(f"가위치법: [{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea}, 총 {cnt2}번 반복했습니다.")

    if cnt1 > cnt2:
        print(f"이분법이 가위치법보다 {cnt1 - cnt2}만큼 더 반복했습니다")
    elif cnt1 < cnt2:
        print(f"가위치법이 이분법보다 {cnt2 - cnt1}만큼 더 반복했습니다")
    else:
        print("이분법, 가위치법 둘 다 같은 횟수만큼 반복하였습니다.")
