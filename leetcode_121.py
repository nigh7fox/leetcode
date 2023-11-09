def maxProfit(prices: list[int]):
  ans = 0
  left = 0
  right = 1
  while (right < len(prices)):
    curr_day_max = prices[right] - prices[left]
    if (prices[left] < prices[right]):
      ans = max(curr_day_max, ans)
    else:
      left = right
    right += 1
  return ans


if __name__ == '__main__':
  # Solved with help
  prices = [7,1,5,3,6,4] # 5
  # prices = [7,6,4,3,1] # 0
  assert maxProfit(prices) == 5