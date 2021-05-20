def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
nlist = [14,46,43,27,57,41,45,21,70]
print("Original: ")
print(nlist) 
selection_sort(nlist)
print("Sorted: ")
print(nlist) 