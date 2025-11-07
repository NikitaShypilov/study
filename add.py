def add_one(some_list: list[int]):
    num = int(''.join(str(d) for d in some_list))
    num += 1
    result = [int(ch) for ch in str(num)]
    return result
    
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
