from .linked_list import LinkedList

ll_a = LinkedList(['a', 'b', 'c', 'd', 'e'])
ll_b = LinkedList([1, 2, 3, 4, 5])


def merge_lists(a, b):

    # handle if one or both lists are empty
    if a._head is None and b._head is None:
        return('Empty Lists')
    elif a._head is None:
        return b._head
    elif b._head is None:
        return a._head

    # sets segment around zip point
    a_pos = a._head
    b_pos = b._head
    a_cache = a._head._next
    b_cache = b._head._next

    while a_pos is not None and b_pos is not None:

        # handles first step of zip provided two nodes
        a_pos._next = b_pos

        # handles the case where each l.list is one node
        if a_cache is None and b_cache is None:
            return a._head

        # handles the case where a is longer
        if a_cache is not None and b_cache is None:
            b_pos._next = a_cache
            return a._head

        # handles the case where b is longer
        if b_cache is not None and a_cache is None:
            return a._head

        b_pos._next = a_cache

        # moves to the next zip segment provied full segment avaliable
        a_pos = a_cache
        b_pos = b_cache
        a_cache = a_pos._next
        b_cache = b_pos._next
