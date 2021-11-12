# O(n^2)

arr = list(map(int, input().split(',')))

for i in range(1, len(arr)):
    '''
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
    '''
    key = arr[i]
    j = i
    while j > 0 and key < arr[j-1]:
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = key 


print(arr)