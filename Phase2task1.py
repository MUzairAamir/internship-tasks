# Design a Shape base class with an area() method, and implement Circle, Rectangle, and Triangle subclasses that override it.
class Shape:
  def __init__(self, lenght , width  ):
    self.length =lenght
    self.width = width 
    
  
    
  def area(self):
    area = self.length * self.width
    return area;

class Circle(Shape):
  def __init__(self,radius):
    
    self.radius=radius
  def area(self):
    area = self.radius * self.radius  * 3.14159265
    return area;
class Rectangle(Shape):
  def __init__(self,length,width):
    super().__init__(length,width)
  
  
class Triangle(Shape):
  def __init__(self,length,width):
    super().__init__(length,width)

  def area(self):
    area = (self.length * self.width) / 2
    return area;  
