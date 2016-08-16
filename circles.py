"""
Tools used for creating and mathing circles
"""

import math


class Circle(object):
    """An advanced circle analytics toolkit"""

    # Class variables are shared accross all instances.
    version = '0.1'


    def __init__(self, radius):
        self.radius = radius


    @property
    def radius(self):
        'Radius of the circle'
        return self.diameter / 2.0


    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    def area(self):
        'Perform quadratic on a shape of a uniform'
        p = self.__perimeter()
        r = p / math.pi / 2.0 # doesn't store the radius anywhere
        return math.pi * r ** 2.0


    def perimeter(self):
        return 2.0 * math.pi * self.radius


    __perimeter = perimeter # stores a private copy so subclasses can extend/override perimeter. Name Mangling. Class local reference. Self means you not your children.


    # Static methods do not require an instance to be created and do not need to access self.
    @staticmethod
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


    # Class method used as a contructor.
    @classmethod
    def from_bbd(cls, bbd):
        'Constructs a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2)
        return cls(radius) # cls ensures subclasses can use


class Tire(Circle):
    'Tires are circes with a corrected perimeter'


    # Lack of init bubbles up to Parent (Circle)

    # If parent is called it is `extending`. If the parent is not called it is `overriding`.
    def perimeter(self):
        return Circle.perimeter(self) * 1.25
