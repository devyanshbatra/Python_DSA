def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [6, 5, 3, 1, 8, 7, 2, 4]

bubble_sort(arr)
print( ' '.join(map(str, arr)))
            
            
            