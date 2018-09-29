def selection_sort(arr):
    """
    This sort moves backswards form the end of the arr,
    taking the largest of the vals between it's current position,
    and the start of the arr and swapping them.
    """
    for num in range(len(arr)-1, 0, -1):
        pos_of_max = 0
        for i in range(num + 1):
            if arr[i] > arr[pos_of_max]:
                pos_of_max = i
        arr[i], arr[pos_of_max] = arr[pos_of_max], arr[i]
    return arr
