
first_list = [0, 1, 0, 12, 3]

result_list = []

zeros = 0

for number in first_list:
    if number == 0:
        zeros += 1
    else:
        result_list.append(number)

for i in range(zeros):
    result_list.append(0)

print(result_list)
