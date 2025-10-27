num = int(input("Input number: "))

result = 1
for digit in str(num):
    result *= int(digit)

while result > 9:
    temp = 1
    for digit in str(result):
        temp *= int(digit)
    result = temp

print(result)