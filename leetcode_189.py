def rotate(nums: list[int], k: int):
  n = len(nums)-1
  for x in range(k):
    for idx in range(n):
      temp = nums[idx]
      nums[idx] = nums[len(nums)-1]
      nums[len(nums)-1] = temp
  return nums


if __name__ == '__main__':
  # Not Solved, Fix time limit
  nums = [1,2,3,4,5,6,7]
  k = 3
  assert rotate(nums, k) == [5,6,7,1,2,3,4]