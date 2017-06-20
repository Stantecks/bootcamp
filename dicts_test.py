def seq_concat(a, b, **kwargs):
    """Concatenates sequences."""
    seq = a + b

    for key in kwargs:
        seq += kwargs[key]
#  Under the hood the above was a dictionary
    return seq
