# Design a Shape base class with an area() method, and implement Circle, Rectangle, and Triangle subclasses that override it.
class Shape:
  def __init__(self, lenght , width  ):
    self.length =lenght
    self.width = width 
    
  # just a placeholder method to be overridden by subclasses
    
  def area(self):
    area = self.length * self.width
    return area;
# there are two ways to implement the area method in the subclasses,#
#  one is to use the super() method to call the parent class's area method and then modify it as needed,
# # and the other is to completely override the area method in the subclass. In this case,
# # we will override the area method in each subclass to provide the specific implementation for that shape.
class Circle(Shape):
  def __init__(self,radius):
    
    self.radius=radius
  def area(self):
    area = self.radius * self.radius  * 3.14159265
    return area;
class Rectangle(Shape):
  def __init__(self,length,width):
    super().__init__(length,width)
  # simply using the parent class's area method to calculate the area of the rectangle
  
class Triangle(Shape):
  def __init__(self,length,width):
    super().__init__(length,width)

  def area(self):
    area = (self.length * self.width) / 2
    return area;  
