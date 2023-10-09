def majorityElement(nums: list[int]) -> int:
  i = len(nums)-1
  maj = 0
  sortedNums = sorted(nums)
  t = 0
  while(i >= 0):
    if (sortedNums[i] == sortedNums[i-1]):
      t += 1
      if (t == (len(nums) / 2) or t == len(nums) or t == (len(nums)-1) / 2):
        maj = sortedNums[i]
        break
    else: 
      t = 0
    i -= 1
  return maj

if __name__ == '__main__':
  # Solved 9/10/2023
  # nums = [3,2,3]
  nums = [-1,1,1,1,2,1]
  assert majorityElement(nums) == 1