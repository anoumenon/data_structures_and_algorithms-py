def merge_lists(a, b):
    '''
    Merge two lists into a new list.
    O(1) space: mutates lists in place.
    '''
    if a._head:
        curr_a = a._head
    else:
        return'first list empty'

    if b._head:
        curr_b = b._head
    else:
        return'second list empty'

    next_a = None
    next_b = None

    return_list = a

    while curr_a and curr_b:

        if curr_a._next:
            next_a = curr_a._next
        if curr_b._next:
            next_b = curr_b._next

        curr_a._next = curr_b
        if next_a:
            curr_b._next = next_a

        curr_a = next_a
        curr_b = next_b

        if next_a and next_a._next:
            next_a = next_a._next
        else:
            next_a = None

        if next_b and next_b._next:
            next_b = next_b._next
        else:
            next_b = None

    return return_list
