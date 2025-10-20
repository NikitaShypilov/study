lst = [1, 3, 5, 7, 2, 2]

if len(lst) == 0:
   print("0")
else:
  pair_numbers = lst[::2]
  last = lst[-1]
  total_pairs = sum(pair_numbers)
  result = total_pairs * last
  print(result)
