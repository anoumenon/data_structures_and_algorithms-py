def insert_shift_array(l, v):
    '''
    This function will insert a value, v, into the center of a list, l
    '''
    if len(l) % 2 != 0:
        m = 1
    else:
        m = 0

    return(l[:(len(l) // 2) + m] + list(v) + l[(len(l) // 2) + m:])
