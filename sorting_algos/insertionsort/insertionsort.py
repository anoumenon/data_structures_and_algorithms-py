def insertion_sort(arr):
    """
    Always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.
    """
    for index in range(1, len(arr)):

        current_val = arr[index]
        position = index

        while position > 0 and arr[position-1] > current_val:
            arr[position] = arr[position-1]
            position -= 1

        arr[position] = current_val

    return arr
