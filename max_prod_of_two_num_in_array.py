#Maximum product of two numbers in an array
# return (nums[i]-1)*(nums[j]-1).

nums = [3,4,5,2, 6,7]
first = second = float('-inf')
first_idx = second_idx = -1

for idx, num in enumerate(nums):
    if num>first:
        second = first
        second_idx = first_idx

        first = num
        first_idx = idx

    elif num>=second:
        second = num
        second_idx = idx
print((nums[first_idx]-1) * (nums[second_idx]-1))
