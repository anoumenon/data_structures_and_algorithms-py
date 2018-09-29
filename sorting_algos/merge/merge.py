def merge_sort(arr):
    """
    This sort...
    """
    length = len(arr)
    if length > 1:
        mid = length // 2
        l_half = merge_sort(arr[:mid])
        r_half = merge_sort(arr[mid:])
        i = 0
        j = 0
        k = 0
        l_length = len(l_half)
        r_length = len(r_half)
        while i < l_length and j < r_length:
            if l_half[i] < r_half[j]:
                arr[k] = l_half[i]
                i += 1
            else:
                arr[k] = r_half[j]
                j += 1
            k += 1
        while i < l_length:
            arr[k] = l_half[i]
            i += 1
            k += 1
        while j < r_length:
            arr[k] = r_half[j]
            j += 1
            k += 1

    return arr
