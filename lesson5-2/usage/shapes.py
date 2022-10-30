class Circle:

    def __init__(self, radius: float) -> None:
        self.__radius = radius
    
    def __str__(self) -> str:
        return f"The Area of Circle radius='{self.__radius}' equals "
    
    @property
    def radius(self) -> float:
        return self.__radius


class Triangle:

    def __init__(self, height: float, base: float) -> None:
        self.__height = height
        self.__base = base
    
    def __str__(self) -> str:
        return f"The Area of Triangle height='{self.__height}' base={self.__base} equals "
    
    @property
    def height(self) -> float:
        return self.__height
    
    @property
    def base(self) -> float:
        return self.__base


class Rectangle:

    def __init__(self, height: float, width: float) -> None:
        self.__height = height
        self.__width = width
    
    def __str__(self) -> str:
        return f"The Area of Rectangle height='{self.__height}' width={self.__width} equals "
    
    @property
    def height(self) -> float:
        return self.__height
    
    @property
    def width(self) -> float:
        return self.__width