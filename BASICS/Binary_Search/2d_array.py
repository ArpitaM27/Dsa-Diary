# Whole matrix is one sorted array
# row = mid // cols
# col = mid % cols

def binary_search_2d(matrix, target):
    
    row=len(matrix)
    col=len(matrix[0])
    low=0
    high=row*col-1
    while low<=high:
        mid=(low+high)//2
        row_index =mid//col
        col_index =mid%col
        if matrix[row_index][col_index]==target:
            return True
        elif matrix[row_index][col_index]<target:
            low=mid+1
        else:
            high=mid-1
    return False

arr=[[1,2,3],[4,5,6],[7,8,9]]
target=int(input("Enter the number to be searched: "))
result=binary_search_2d(arr,target)
print(result)