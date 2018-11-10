def my_map(function, itterable):
    """
    Applies a function to all the items in an input list.
    """
    for element in itterable:
        element = function(element)

    return itterable
