def in_place_sorting(arr):
    
    for i in range(0,len(arr)):
        minimum_index=i
        for j in range(i+1,len(arr)):
            if(arr[minimum_index]>arr[j]):
                minimum_index=j

        arr[i],arr[minimum_index]=arr[minimum_index],arr[i] 
    return arr


arr=[4,5,6,1,2,3]
print(in_place_sorting(arr))
