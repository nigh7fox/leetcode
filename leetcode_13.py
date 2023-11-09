def romanToInt(s: str):
    r = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L':50,
        'C':100,
        'D':500,
        'M': 1000
    }
    return sum([r[x] for n in s.split() for x in n])


if __name__ == '__main__':
  # Not Solved
  s = 'III'
  print(romanToInt(s))
  assert romanToInt(s) == 3