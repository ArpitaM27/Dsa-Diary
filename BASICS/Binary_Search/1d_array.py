def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return ("number found at index: "+str(mid))
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return ("number not found")

arr=[1,2,3,4,5,6,7,8,9]
target=int(input("Enter the number to be searched: "))
result=binary_search(arr,target)
print(result)