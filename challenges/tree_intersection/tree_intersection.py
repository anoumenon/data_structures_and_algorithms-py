def tree_intersection(t_a, t_b):
    """
    Return commonaity
    O(n)
    Because what is more efficient than hash tables? foresight.
    """
    report = []
    for val in t_a.contents:
        if val in t_b.contents:
            report.append(val)
    return report
