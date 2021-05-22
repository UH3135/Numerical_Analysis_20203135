import numpy as np

def fixedPointIteration(start, func):
    es = 10 ** -5

    x = start

    while True:
        oldX = x
        x = func(x)

        ea = np.abs((x - oldX) / x)

        print(f"x: {oldX}, func(x): {x}, ea: {ea}")

        if ea != 0 and ea < es:
            break

    return x, ea


if __name__ == '__main__':
    f = lambda x: (x**2 + np.e**x - 2) / 3
    start = 0
    x, ea = fixedPointIteration(start, f)

    print(f"근은 {x}이고, 상대오차는 {ea}입니다.")