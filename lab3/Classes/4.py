class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def move(self, x, y):
    self.x += x
    self.y += y
  def show(self):
    print(f"The coordinates are: {self.x} and {self.y}")
  def dist(self, b):
    res = ((self.x - b.x)**2 + (self.y - b.y)**2)**0.5
    print(f'distance between 2 points is: {res}')
p1 = Point(4, 5)
p2 = Point(1, 3)
p1.show()
p2.move(2, 3)
p2.show()
p1.dist(p2)