def selection_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
print("Enter the number of elements in the array:")
n=int(input())
print("Enter the elements of the array:")
arr=list(map(int,input().split()))
selection_sort(arr)
print("Sorted array is:",arr)