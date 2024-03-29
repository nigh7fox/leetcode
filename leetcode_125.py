import re

def isPalindrome(s: str):
  s = re.sub(r'[^a-zA-Z0-9]', '', s)
  return s.lower() == s.lower()[::-1]


if __name__ == '__main__':
  # s = "A man, a plan, a canal: Panama"
  s = "ab_a"
  assert isPalindrome(s) == True