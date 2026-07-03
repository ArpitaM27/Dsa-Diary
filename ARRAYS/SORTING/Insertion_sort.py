def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

print("Enter the number of elements in the array:")
n = int(input())
print("Enter the elements of the array:")
arr = list(map(int, input().split()))
insertion_sort(arr)
print("Sorted array is:", arr)
