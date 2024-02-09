def ispalindrome(word):
  copy = word[::-1]
  if copy == word:
    return True
  return False
print(ispalindrome("abbad")) # false
print(ispalindrome("abba")) #true