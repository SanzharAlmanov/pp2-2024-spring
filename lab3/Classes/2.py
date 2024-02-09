class Shape:
  def area(self):
    return 0
class Square(Shape):
  def __init__(self, length):
    super().__init__()
    self.length = length
  def area(self):
    return self.length * self.length
square = Square(5)
print(f"The area of the square is: {square.area()}")