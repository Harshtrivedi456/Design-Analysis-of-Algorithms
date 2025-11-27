# def min_max(arr):
#     min=arr[0]
#     max=arr[0]
#     for i in range(arr):
#         if arr[i] < min:
#             min = arr[i]
#         if arr[i] > max:
#             max = arr[i]
#     return min, max

# n=int(input())

# for i in range(n):
#     arr=list(map(int, input().split()))
# print(min_max(arr))

def min_max(arr):
    if (len(arr) == 0):
        return None, None
    mid = int(len(arr)/2)
lmin,lmax = min_max(arr[:mid])
