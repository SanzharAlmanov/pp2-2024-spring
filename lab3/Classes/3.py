from turtle import Shape


class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width
rect = Rectangle(4, 5)
print(f"The area of the rectangle is: {rect.area()}")