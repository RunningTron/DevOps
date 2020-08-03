def feibo(n):
    x = 1
    y = 1
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            yield 1
        else:
            ret = x + y
            yield ret
            x = y
            y = ret


if __name__ == '__main__':
    g = feibo(10)
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
