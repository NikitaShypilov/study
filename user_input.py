user_input = int(input("enter 4 numbers: "))

d1 = user_input // 1000
d2 = (user_input // 100) % 10
d3 = (user_input // 10) % 10
d4 = user_input % 10

print(d1)
print(d2)
print(d3)
print(d4)
