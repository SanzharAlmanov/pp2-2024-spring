def uniqe(smth):
  for i in range(len(smth)):
    for j in range(i + 1, len(smth)):
      if smth[j] == smth[i]:
        smth[j] = -1
  arr = []
  for i in smth:
    if i != -1:
      arr.append(i)
  return arr
smth = [1, 1, 1, 1, 3, 3, 4, 5, 6, 7, 7, 8]
print(*uniqe(smth))