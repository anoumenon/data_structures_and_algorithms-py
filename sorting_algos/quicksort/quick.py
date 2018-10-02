def quick_sort(arr):
    """
    Pure implementation of quick sort algorithm in Python:
    quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    """
    arr_length = len(arr)
    if arr_length <= 1:
        return arr
    else:
        piv = arr[0]
        greater = [element for element in arr[1:] if element > piv]
        lesser = [element for element in arr[1:] if element <= piv]
        return quick_sort(lesser) + [piv] + quick_sort(greater)
