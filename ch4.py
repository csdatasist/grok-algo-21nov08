# sum using recursion
def sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:]) # : substring, returns array mius 0th index

# count items in list, recursive
def count(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return 1
    else:
        return 1 + count(list[1:])

# find max value, recursive
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

# quick sort 
def quicksort(array):
    if len(array) < 2: # base case
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] #subarray of elements less than pivot
        greater = [i for i in array[1:] if i > pivot] #subarray of elements greater than pivot
        return quicksort(less) + [pivot] + quicksort(greater)
        

# test 
nums = [1,2,3,10,4,12,60,-7,23]
print( sum(nums) )
print( count(nums) )
print( max(nums) )
print( quicksort(nums) )