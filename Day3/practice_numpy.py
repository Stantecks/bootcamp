import numpy as np


def xa_to_diameter(xa):
    """
    Converts an array of cross-sectional areas to diameters
    with commensurate units.
    """
    # Computes diameter squared and then sqrt
    dia_sq = (xa * 4) / np.pi
    diameter = np.sqrt(dia_sq)

    return diameter
