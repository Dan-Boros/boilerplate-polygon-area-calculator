class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self):
        pass
    
    def set_height(self):
        pass
    
    def get_area(self):
        pass
        # : Returns area (width * height)
    
    def get_perimeter(self):
        pass
        # : Returns perimeter (2 * width + 2 * height)
    
    def get_diagonal(self):
        pass
        # : Returns diagonal ((width ** 2 + height ** 2) ** .5)
    
    def get_picture(self):
        pass
        # : Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
    
    def get_amount_inside(self):
        pass
        # : Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)
    
    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def __repr__(self):
        return f"Square(side={self.width})"