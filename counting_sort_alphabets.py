def counting_sort_alphabets(arr):
    # Make all letters uppercase
    for i in range(len(arr)):
        arr[i] = arr[i].upper()

    # Create count array for 26 alphabets (A-Z)
    count = [0] * 26

    # Count each character
    for i in range(len(arr)):
        index = ord(arr[i]) - ord('A')
        count[index] = count[index] + 1

    # Build the sorted array
    sorted_arr = []
    for i in range(26):
        for j in range(count[i]):
            sorted_arr.append(chr(i + ord('A')))

    return sorted_arr

# Example
arr = ['D', 'B', 'A', 'C', 'D', 'B']
sorted_arr = counting_sort_alphabets(arr)
print("Sorted Alphabets:", sorted_arr)
