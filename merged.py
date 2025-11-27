# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result


# def mergedsort(arr):
    
#     if len(arr) <= 1:
#         return arr
       
#     mid = int(len(arr) / 2)
#     left = arr[:mid]
#     right = arr[mid:]
    
#     left = mergedsort(left)
#     right = mergedsort(right)

#     return (left, right)

# a=int(input("Enter number of elements: "))
# arr = []    
# for i in range(a):
#     arr.append(int(input("Enter element: ")))

# print("Sorted array:", mergedsort(arr))

def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted subarrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergedsort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergedsort(arr[:mid])
    right = mergedsort(arr[mid:])

    return merge(left, right)

# Input section
a = int(input())
arr = []    
for i in range(a):
    arr.append(int(input()))

# Output
print("Sorted array:", mergedsort(arr))
