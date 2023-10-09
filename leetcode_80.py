def removeDuplicates(nums: list[int]) -> int:
  i = len(nums)-1
  t = 0
  while (i >= 0):
    if (nums[i] == nums[i-1]):
      t += 1
      if (t >= 2 and len(nums) > 2):
        nums.pop(i)
    else:
      t = 0
    i -= 1
  return len(nums)


if __name__ == '__main__':
  # Solved 9/10/2023
  # Can be faster, uses too much memory
  # nums = [1,1,1,2,2,3]
  nums = [0,0,1,1,1,1,2,3,3]
  assert removeDuplicates(nums) == 7