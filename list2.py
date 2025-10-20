
lst = [1, 2, 3, 4, 5, 6, 7]


if len(lst) == 0:
    first = []
    second = []

else:
    n = len(lst)

    if n % 2 == 0:
        middle = n // 2
    else:
        middle = n // 2 + 1

    first = lst[:middle]
    second = lst[middle:]

result = [first, second]

print(result)
