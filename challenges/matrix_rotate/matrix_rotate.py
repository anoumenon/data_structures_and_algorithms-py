# mat = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# want list of lists, 321 321 321


def matrix_rotate(m):

    # a = list(zip(m))  # [([1, 1, 1],), ([2, 2, 2],), ([3, 3, 3],)]
    # did not mutate...

    # b = list(zip(*m))  # [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
    # flipped horizontally.

    # c = list(zip(m[::-1]))  # [([3, 3, 3],), ([2, 2, 2],), ([1, 1, 1],)]
    # flipped vertically!

    # d = list(zip(*m[::-1]))  # [(3, 2, 1), (3, 2, 1), (3, 2, 1)]
    # theory: flip borh horizontal and vert?

    # result, good rotate, but are tuples not lists!
    # d = list(zip(list(*m[::-1]))) # error, too many args for list.

    # e = (list(elem) for elem in d)
    # <generator object matrix_rotate.<locals>.<genexpr> at 0x7f7deb166ba0>

    # e = [list(elem) for elem in d]
    # make me a list filled with lists, made 1:1 with this list of tuples..
    # [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
    # !!!


    return([list(elem) for elem in (list(zip(*m[::-1])))])

# matrix_rotate(mat)
