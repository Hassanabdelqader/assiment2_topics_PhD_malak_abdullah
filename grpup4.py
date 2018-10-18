#number1
def first_last6(nums):
  if nums[0] == 6:
   return True
  elif nums[len(nums) -1] == 6:
   return True
  else:
    return False

#number2
def same_first_last(nums):
   return len(nums) > 0 and nums[0] == nums[-1]

#numbwe3
def make_pi():
  return [3, 1, 4]
#number4
def common_end(a, b):
 return a[0] == b[0] or a[-1] == b[-1]

#number5
def sum3(nums):
  return sum(nums) 

#number6
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

