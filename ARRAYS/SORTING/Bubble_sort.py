def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
print("Enter the number of elements in the array:")
n = int(input())
print("Enter the elements of the array:")
arr = list(map(int, input().split()))
bubble_sort(arr)
print("Sorted array is:", arr)