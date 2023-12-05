def binarysearch(arr, start, end, x):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, start, mid - 1, x)
        else:
            return binarysearch(arr, mid + 1, end, x)
    else:
        return -1
    
def bubblesort_rekursif(x, n):
    if n == 1:
        return

    for i in range(n - 1):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]

    bubblesort_rekursif(x, n - 1)


array = [87, 54, 34, 23, 89, 15, 2, 200, 28, 31]

print("list sebelum di sorting:", array)

bubblesort_rekursif(array, len(array))
print("list setelah di sorting:", array)