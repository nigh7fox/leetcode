def rotate(nums: list[int], k: int):
  """
  Do not return anything, modify nums in-place instead.
  """
  if k == 0:
      return
  elif len(nums) > k:
      nums[:] = nums[-k:] + nums[:(len(nums) - k)]
  else:
      for i in range(k):
          rotation = nums[:-1]
          rotation.insert(0, nums[-1])
          nums[:] = rotation


if __name__ == '__main__':
  # Not Solved, Fix time limit
  nums = [1,2,3,4,5,6,7]
  k = 3
  assert rotate(nums, k) == [5,6,7,1,2,3,4]