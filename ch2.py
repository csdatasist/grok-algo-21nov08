# find smallest value in array, returns index
def findSmalleset(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# selection sort, sorts array with O(n^2)
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmalleset(arr)
        newArr.append(arr.pop(smallest))
    return newArr


# test
nums = [2,5,34,-4,12,4,-67]
result = findSmalleset(nums)

print(result)
print ( selectionSort(nums) )