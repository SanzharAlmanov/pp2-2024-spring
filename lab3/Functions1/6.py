strin = 'abd fre der'
def Convert(strin):
  li = list(strin.split(" "))
  print(*li[::-1])
Convert(strin)