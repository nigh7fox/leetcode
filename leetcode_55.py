def canJump(nums: list[int]):
  l = len(nums)-1
  i = 0
  ans = False
  if (l == 0):
      return True
  elif(nums[0] == 0):
      return False
  while i < l:
      if (i + nums[i] >= l or nums[i] != 0):
          return True
      i += 1
  return False


if __name__ == '__main__':
  # Not Solved
  nums = [1, 0, 1, 0]
  # nums = [2,3,1,1,4] # True
  # nums = [3,2,1,0,4] # False
  assert canJump(nums) == False