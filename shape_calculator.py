class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def set_width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def set_height(self, value):
        self._height = value
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height) * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        # Returns a string that represents the shape using lines of "*".
        # The number of lines should be equal to the height and the number of "*" in each line should be equal to the width.
        # There should be a new line (\n) at the end of each line.
        # If the width or height is larger than 50, this should return the string: "Too big for picture.".
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        
        oneLine = "*" * self.width
        allLines = [oneLine for _ in range(0, self.height)]

        return "\n".join(allLines)

    def get_amount_inside(self, other):
        # Takes another shape (square or rectangle) as an argument.
        # Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        # For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        
        noFitWidth = self.width // other.width
        noFitHeight = self.height // other.height

        return noFitHeight * noFitWidth

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