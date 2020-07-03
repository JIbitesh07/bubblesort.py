def bubblesort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[24,21,34,56,78]
bubblesort(arr)
print("sorted array")
for i in range(0,len(arr)):
    print(arr[i])
