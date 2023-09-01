n=int(input("enter the number of elements:"))
arr = [int(input("enter the elements:")) for i in range(n)]
ele=int(input("enter the element to be found"))
low =0
high =len(arr)-1
found = 0
while low < high:
    mid = (low + high )//2
    if ele <arr[mid]:
        high = mid-1
    if ele > arr[mid]:
        low = mid+1
    if ele == arr[mid]:
        print("element is found: ")
        found =1
        break
if not (found):
    print(f"'{ele}'does not exists")