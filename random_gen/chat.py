def foo_1():
    if input('q') == '1':
        a = foo_2()
    return a


def foo_2():
    b = 1 + 2
    return b

def foo_3():
    c = 1 + 1
    return c


def res():
    res = foo_1() + foo_2()
    return res


print(res())
