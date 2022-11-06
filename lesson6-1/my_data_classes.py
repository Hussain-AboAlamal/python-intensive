from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    
    def to_tuple(self) -> tuple:
        return (self.x, self.y)

@dataclass
class Rectangle:
    xy: Point
    width: int
    height: int

    def to_tuple(self) -> tuple[tuple]:
        x1 = self.xy.x + self.width
        y1 = self.xy.y + self.height
        return (self.xy.to_tuple(), (x1, y1))
