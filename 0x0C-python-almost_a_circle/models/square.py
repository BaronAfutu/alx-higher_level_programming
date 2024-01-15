#!/usr/bin/python3
"""Define the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square Constructor. Initializes a Square

        Args:
            size (int): Size of the new Square.
            x (int): X coordinate of the new Square.
            y (int): Y coordinate of the new Square.
            id (int): Identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the parameters of the Square.

        Args:
            *args (ints): New attribute values.
                - arg 0 => id
                - arg 1 => size
                - arg 2 => x
                - arg 3 => y
            **kwargs (dict): key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the attributes of the Square as a dictionary."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns the print() and str() output of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,self.width)
