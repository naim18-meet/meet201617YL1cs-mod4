import turtle

class Rectangle :
    def __init__(self,length,height):
        """
        Initialize new rectangle instance.

        :param length: length of rectangle (horizontal dimension).  Must be >= 0.  Otherwise, set to 0.
        :param length: height of rectangle (vertical dimension).  Must be >= 0.  Otherwise, set to 0.
        """
        if length>=0 :
            self.length=length
        else :
            self.length=0

        if height>=0 :
            self.height=height
        else :
            self.height=0

        self.turtle=turtle.clone() #Make a new turtle object just for this instance so that drawings can be cleared.
        turtle.speed(0) #Make turtle move as fast as possible.
        self.has_been_drawn=False #Keep track of whether shape has been drawn.

    def set_length(self,new_length):
        """
        Change the length of the rectangle.

        :param new_length: length (horizontal dimension) of rectangle.  Must be >= 0.  Otherwise, no change is made.
        """
        if new_length>=0 :
            self.length=new_length
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()

    def set_height(self,new_height):
        """
        Change the height of the rectangle.

        :param new_height: height (vertical dimension) of rectangle.  Must be >= 0.  Otherwise, no change is made.
        """   
        if new_height>=0 :
            self.height=new_height
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()

    def get_area(self):
        """
        Calculate the area of the shape
        """
        return self.length*self.height

    def set_start(self, startx, starty):
        self.start=(startx,stary)
        

    def draw_shape(self):
        """
        Draw the shape, starting at 0,0.

        If any old drawings exist, remove them.
        """
        self.turtle.clear() #Remove old drawings (if they exist)
        self.turtle.penup()
        self.turtle.goto(self.start)
        self.turtle.pendown()
        self.turtle.goto(self.length,0)
        self.turtle.goto(self.length,self.height)
        self.turtle.goto(0,self.height)
        self.turtle.goto(0,0)
        self.turtle.penup()
        self.has_been_drawn=True
