from my_shapes import triangle_area, circle_area, rectangle_area

from shapes import Circle, Triangle, Rectangle

if __name__ == "__main__":
    c = Circle(5)
    ca = circle_area(c.radius)
    print(f"{c} {ca}")

    r = Rectangle(4, 5)
    ra = rectangle_area(r.height, r.width)
    print(f"{r} {ra}")

    t = Triangle(4, 8)
    ta = triangle_area(t.height, t.base)
    print(f"{t} {ta}")
