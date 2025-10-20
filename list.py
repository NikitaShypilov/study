lst = [8, 5, 6, 2, 54, 23]

if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)