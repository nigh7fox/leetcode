def maxProfit(prices: list[int]):
  ans = 0
  i = 0
  for x in prices:
    curr_day_max = 0
    for y in prices[i:]:
      print(prices[i:])
      if (y - x) > curr_day_max:
          curr_day_max = (y - x)
      if curr_day_max > ans:
          ans = curr_day_max
    i += 1
  return ans


if __name__ == '__main__':
  # Not Solved
  prices = [7,1,5,3,6,4] # 5
  prices = [7,6,4,3,1] # 0
  assert maxProfit(prices) == 5