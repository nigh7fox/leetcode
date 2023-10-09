def removeElement(nums: list[int], val: int):
  # Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
  # The remaining elements of nums are not important as well as the size of nums.
  x = len(nums)-1
  while (x >= 0):
    if (nums[x] == val):
      nums.pop(x)
    x -= 1
  print(nums)
  return len(nums)


if __name__ == '__main__':
  # Solved - 8/10/2023
  nums = [0,1,2,2,3,0,4,2]
  val = 2
  k = removeElement(nums, val)