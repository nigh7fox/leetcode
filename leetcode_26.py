def removeDuplicates(nums: list[int]) -> int:
  i = len(nums)-1
  visited = []
  while (i >= 0):
    if nums[i] in visited:
      nums.pop(i)
    else:
      visited.append(nums[i])
    i -= 1
  return len(nums)


if __name__ == '__main__':
  # Solved 9/10/2023
  nums = [0,0,1,1,1,2,2,3,3,4]
  print(removeDuplicates(nums))
  assert removeDuplicates(nums) == 5