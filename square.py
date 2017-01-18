from rectangle import Rectangle
class Square (Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

    def set_length (self, new_length):
        super(Square, self).set_length(new_length)

        super(Square, self).set_width(length, width)
        
