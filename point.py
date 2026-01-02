import math

class Point:
    def __init__(self, x, y=None, polar=False):
        if isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        else:
            r_val = x
            phi_val = y
            if polar:
                self.x = r_val * math.cos(phi_val)
                self.y = r_val * math.sin(phi_val)
            else:
                self.x = x
                self.y = y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dist(self, x_or_point=None, y=None):
        if x_or_point is None:
            return abs(self)
        elif isinstance(x_or_point, Point):
            dx = self.x - x_or_point.x
            dy = self.y - x_or_point.y
            return math.sqrt(dx**2 + dy**2)
        elif isinstance(x_or_point, (int, float)) and isinstance(y, (int, float)):
            dx = self.x - x_or_point
            dy = self.y - y
            return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f"({self.x}, {self.y})"

