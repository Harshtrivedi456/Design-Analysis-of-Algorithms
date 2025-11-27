# arr=[1,3,4,5,6]
# key=int(input("Enter key: "))


# if(key in arr):
#    print=arr[key]

 
def linear_search(arr,key):
    for i in range(0,len(arr)):
        if(key==arr[i]):
            print("found")
            return
    print("not found")

arr=[1,3,5,7,8]
key=6
linear_search(arr, key)


# code for counting a key occurance
# indetify the number of times key is occured in odd indices

