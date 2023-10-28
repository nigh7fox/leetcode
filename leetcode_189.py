def rotate(nums: list[int], k: int):
  i = 0
  n = len(nums)-1
  for x in range(k):
    print('Rotate %d' % (x+1))
    while (i <= n):
      if (i+1) <= n:
        t = nums[i-1]
        nums[i-1] = nums[i]
        nums[i] = t
      else:
        t = nums[n-(i-1)]
        nums[n-(i-1)] = nums[i]
        nums[i] = t
      i += 1
      print(nums)
    i = 0  
  return nums


if __name__ == '__main__':
  nums = [1,2,3,4,5,6,7]
  k = 3
  rotate(nums, k)