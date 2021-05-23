import numpy as np

def modified_falsePosition(min, max, func):
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

        if ea != 0 and ea < es:
            break

    return ax, cx, ea, cnt

def setK(setK, addK):
    setK = 0
    addK += 1

    return setK, addK

if __name__ == '__main__':
    f = lambda x: np.sin(10*x) + np.cos(3*x)
    start = 3.5
    end = 4

    sx, ex, ea, cnt = modified_falsePosition(start, end, f)

    print(f"[{sx}, {ex}] 사이에 근이 존재, 상대오차는 {ea}, 총 {cnt}번 반복했습니다.")