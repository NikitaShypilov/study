
n = int(input("Введіть 5-значне число: "))


d5 = n % 10
n = n // 10
d4 = n % 10
n = n // 10
d3 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d1 = n


reversed_num = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1

print(reversed_num)
