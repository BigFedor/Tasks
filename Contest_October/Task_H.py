def merge_lists(arr1, arr2):
    i = 0
    j = 0
    k = 0
    arr = [0] * (len(arr1) + len(arr2))
    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1
        elif:
            arr[k] = arr2[j]
            j += 1
            k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
    return (arr)