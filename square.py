import turtle
from rectangle import Rectangle
class Square (Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

        self.turtle=turtle.clone() 
        turtle.speed(0) 
        self.has_been_drawn=False 
        
    def set_length (self, new_length):
        super(Square, self).set_length(new_length)
        new_length = self.length
        new_height = self.length

    def get_area(self):
    
        return self.length*self.height

    def draw_shape(self):

        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.goto(self.length,0)
        self.turtle.goto(self.length,self.height)
        self.turtle.goto(0,self.height)
        self.turtle.goto(0,0)
        self.turtle.penup()
        self.has_been_drawn=True

        

    #def set_wedth(self, new_width):
    #    super(Square, self).set_width(new_width)
        
