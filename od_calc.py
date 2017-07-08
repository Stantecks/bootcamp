def od_to_cells(optical_density):
    """ Calculates cells per mL from optical density """
    return optical_density * 8e8


def cells_plated(optical_density, dil, drop_size):
    """Calculates cells plated from optical density, dilutions,
    and droplet size.
    """
    return (od_to_cells(optical_density) / dil) * (drop_size / 1000)
