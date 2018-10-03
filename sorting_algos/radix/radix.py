def radix_sort(arr):
    """
    This sort evaluated from the ones digit place up across each number
    as it moved them from bucket to bucket.
    """
    len_arr = len(arr)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[] for i in range(0, 10)]
        for value in arr:
            least_digit = value % modulus
            least_digit /= div
            new_list[int(least_digit)].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_arr:
            return new_list[0]

        arr = []
        for x in new_list:
            for y in x:
                arr.append(y)
