def check_prime(i):
  for x in range(2, i):
      if i % x == 0:
         return False
  return True

lis = [1, 3, 4, 5, 8, 12, 11]      
def filter_prime(some_list):
  arr = []
  for i in some_list:
    if check_prime(i) == True:
        arr.append(i)
  return arr
lis1 = filter_prime(lis)
