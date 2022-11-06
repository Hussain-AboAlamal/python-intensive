from math import pi

def triangle_area(height: float, base: float) -> float:
    """calculate area of a triangle

    Args:
        height (float): triangle height in any unit
        base (float): triangle base in any unit

    Returns:
        float
    """

    return height * base / 2

def circle_area(radius: float) -> float:
    """calculate area of a circle

    Args:
        radius (float): radius of the circle

    Returns:
        float
    """

    return pi * radius ** 2

def rectangle_area(height: float, width: float) -> float:
    """calculate are of a rectangle

    Args:
        width (float): rectangle width
        height (float): rectangle height

    Returns:
        float: _description_
    """
    
    return width * height
