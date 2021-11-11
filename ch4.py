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

        

# test 
nums = [1,2,3,10,4,12,60]
print( sum(nums) )
print( count(nums) )
print( max(nums) )