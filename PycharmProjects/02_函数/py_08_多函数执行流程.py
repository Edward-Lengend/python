glo_num = 0  # ćšć±ćé


def test1():
    global glo_num
    glo_num = 100


def test2():
    print(glo_num)


test2()
test1()
test2()
