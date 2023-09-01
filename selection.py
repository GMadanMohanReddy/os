def selection(arr):
    for i in range(0,len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                min_idx = j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
        print(arr)

n = int(input("enter number of elements:"))
arr=[int(input("enter element of the array:")) for i in range(n)]
selection(arr)