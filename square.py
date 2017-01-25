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

        if new_length>=0 :
            self.length=new_length
            self.height=new_length
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()



        #self.length = new_length
        #self.height = new_length
        

    def set_height (self, new_height):
        super(Square, self).set_height(new_height)

        if new_height>=0 :
            self.height=new_height
            self.length=new_height
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()


        #self.height = new_height
        #self.length = new_height

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
        
