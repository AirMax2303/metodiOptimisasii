def fun(x):
    return x ** 2 + 4 * x + 5


def dihotomy(sl, sr, e=5e-1, step=2e-1):
    k = 0
    while abs(sr - sl) > 2 * e:
        x = (sl + sr - step) / 2
        y = (sl + sr + step) / 2
        if fun(x) < fun(y):
            sr = y
        else:
            sl = x
        k += 1
    return (sl + sr) / 2, k


a = -4
b = 6
dih = dihotomy(a, b)
print(f'Количество итераций {dih[1]}')

print(f'Значение {dih[0]}')
