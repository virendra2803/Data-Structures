#Maximum product of three numbers

nums = [1,2,-3,-4,-2,3]

first_smallest = float("inf")
second_smallest = float("inf")
first_largest = float("-inf")
second_largest = float("-inf")
third_largest = float("-inf")
for i in nums:
    if i > first_largest:
        third_largest = second_largest
        second_largest = first_largest
        first_largest = i
    elif i>second_largest:
        third_largest = second_largest
        second_largest = i
    elif i> third_largest:
        third_largest = i

    if i<first_smallest:
        second_smallest = first_smallest
        first_smallest = i
    elif i< second_smallest:
        second_smallest = i
a = (first_smallest*second_smallest*first_largest)
b = (first_largest*second_largest*third_largest)

print (max(a,b))