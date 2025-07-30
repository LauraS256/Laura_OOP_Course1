"""
A class for representing a circle
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_cir(self):
        print(f"Circumference of this circle is: {2 * 3.14 * self.radius} units.")

    def display_area(self):
        print(f"The area of the circle is: {3.14 * self.radius ** 2} square units.")

new_circle = Circle(17)

new_circle.display_cir()
new_circle.display_area()