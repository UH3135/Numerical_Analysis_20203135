import numpy as np

def bisection(min, max, func, stand):
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

        if ea != 0 and ea < es or cnt >= stand:
            break

    return ax, cx, ea, cnt


def modified_falsePosition(min, max, func, stand):
    es = 10 ** -5
    cnt = 0 # 반복 횟수

    if func(min) * func(max) > 0: #만약 min과 max의 부호가 같으면 에러 출력하고 함수 종료
        print("This section don't have root or have even-numbered root")
        return -1

    KR = 0
    KL = 0

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

            KR, KL = setK(KR, KL)

            if KL > 1:
                cy /= 2
        else:
            ax = bx
            ay = by

            KL, KR = setK(KL, KR)

            if KR > 1:
                ay /= 2

        ea = np.abs(bx - oldBx) / bx

        cnt += 1

        if ea != 0 and ea < es or cnt >= stand:
            break

    return ax, cx, ea, cnt

def setK(setK, addK):
    setK = 0
    addK += 1

    return setK, addK


if __name__ == '__main__':
    f = lambda x: np.sin(10 * x) + np.cos(3 * x)
    start = 3.5
    end = 4

    print("반복의 최대 횟수가 5로 고정될 경우")
    print()
    stand = 5

    sx, ex, ea1, cnt = bisection(start, end, f, stand)
    print(f"이분법: [{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea1}, 총 {cnt}번 반복했습니다.")

    sx, ex, ea2, cnt = modified_falsePosition(start, end, f, stand)
    print(f"가위치법: [{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea2}, 총 {cnt}번 반복했습니다.")

    if ea1 > ea2:
        print(f"이분법이 수정 가위치법보다 {ea1 - ea2}만큼 더 오차가 발생했습니다")
    elif ea1 < ea2:
        print(f"수정 가위치법이 이분법보다 {ea2 - ea1}만큼 더 오차가 발생했습니다")
    else:
        print("이분법, 수정 가위치법 둘 다 같은 횟수만큼 오차가 났습니다.")

    print()
    print("----------------------------------------------------------------------")
    print()

    print("반복의 최대 횟수가 10으로 고정될 경우")
    print()
    stand = 10

    sx, ex, ea1, cnt = bisection(start, end, f, stand)
    print(f"이분법: [{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea1}, 총 {cnt}번 반복했습니다.")

    sx, ex, ea2, cnt = modified_falsePosition(start, end, f, stand)
    print(f"가위치법: [{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea2}, 총 {cnt}번 반복했습니다.")

    if ea1 > ea2:
        print(f"이분법이 수정 가위치법보다 {ea1 - ea2}만큼 더 오차가 발생했습니다")
    elif ea1 < ea2:
        print(f"수정 가위치법이 이분법보다 {ea2 - ea1}만큼 더 오차가 발생했습니다")
    else:
        print("이분법, 수정 가위치법 둘 다 같은 횟수만큼 오차가 났습니다.")