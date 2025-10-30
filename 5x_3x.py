def common_elements():
    x3 = {x for x in range(100) if x % 3 == 0}
    x5 = {x for x in range(100) if x % 5 == 0}
    return x3 & x5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')