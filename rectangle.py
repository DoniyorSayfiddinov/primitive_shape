from polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, a,b) -> None:
        super().__init__(a, b)
    def getArea(self):
        return super().getArea()
    def getPerimeter(self):
        return super().getPerimeter()