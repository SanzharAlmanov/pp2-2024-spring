from itertools import permutations
st = input("input the string you want to permutate - ")
list1 = list(permutations(st))
for x in list1:
  print(x)