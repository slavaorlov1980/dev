def f1():
    x = 100
    def f2():
        nonlocal x
        x = 200
    f2()
    print(x)
f1()