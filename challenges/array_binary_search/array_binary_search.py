def binary_search(l, v):
    '''
    takes in 2 parameters: a sorted array and the search key
    return the index of the array’s element that is equal to the search key,
    or -1 if the element does not exist.
    '''
    mindex = 0
    middle = len(l) // 2
    maxdex = len(l) - 1

    while mindex != maxdex:
        if v == l[middle]:
            print(middle)
            return(middle)
        if v < l[middle]:
            maxdex = middle
            middle = maxdex // 2
        if v > l[middle]:
            mindex = middle
            middle = maxdex - ((maxdex - middle) // 2)
    print(-1)
