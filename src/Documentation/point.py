import math

class Point:
  """Representation of a point in a xy-coordinate system.
  Attributes
  ----------
  x : float
      The X coordinate.
  y : float
      The Y coordinate.  
  """
  
  def __init__(self, x, y):
    """Initialization of the point with x and y values."""
    self.x = x 
    self.y = y  
  def __str__(self): 
    return f"( {self.x:> 6.4f} | {self.y:> 6.4f} )"
  def __add__(self, other):
    return Point (self.x+other.x, self.y+other.y)
  def __abs__(self):
    return math.sqrt (pow(self.x,2)+pow(self.y,2))
  def __sub__(self):
    # tbd 
    pass

class Origin(Point):
    def __init__(self):
        super().__init__(0.0, 0.0)

if __name__ == "__main__":
    p1 = Point ( -3, 2)
    p2 = Point ( 6, -6) 
    p3 = p1+p2
    pO = Origin()
    p4 = pO + p3
    print(f"pO {pO}")   
    print(f"p3 {p3}")          # p3 (  3.0000 | -4.0000 )
    print(f"p4 {p4}") 
    print(f"|p3| = {abs(p3)}") # |p3| = 5.0

    print(Point.__doc__)
    help(Point)