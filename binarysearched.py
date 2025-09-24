def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # base case: not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

arr = [2, 4, 6, 8, 10, 12]
target = 11

result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")
