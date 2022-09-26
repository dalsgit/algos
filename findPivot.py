import numpy as np
def pivotIndex(nums):
  sums = np.zeros(len(nums))
  for idx, x in enumerate(nums):
    i = idx
    while i >= 0:
      sums[idx] += nums[i]
      i = i-1

  return sums;
def runningsums(nums):
  if not nums: return nums
  sums = []
  sums.append(nums[0])
  for idx in range(1, len(nums)):
    sums.append(nums[idx] + sums[idx-1])
  return sums;
  
l=[1, 2, -8, 4]
print(runningsums(l))
l=[]
print(runningsums(l))