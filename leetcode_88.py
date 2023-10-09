def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
  """
  Do not return anything, modify nums1 in-place instead.
  O = (m + n)
  """
  i = m - 1 # 3 - 1 cause array
  j = n - 1 # 3 - 1 cause array
  k = m + n - 1 # 6 - 1 cause array 

  while (i >= 0 and j >= 0):
    if (nums1[i] > nums2[j]):
      nums1[k] = nums1[i]
      k -= 1
      i -= 1
    else:
      nums1[k] = nums2[j]
      k -= 1
      j -= 1
  while (j >= 0):
    nums1[k] = nums2[j]
    k -= 1
    j -= 1
  return nums1


if __name__ == '__main__':
  # Solved - 8/10/2023
  nums1 = [1,2,3,0,0,0]
  nums2 = [2,5,6]
  m = 3
  n = 3
  assert merge(nums1, m, nums2, n) == [1,2,2,3,5,6]