class Vec2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, Vec2D):
            return Vec2D(self.x*scalar, self.y*scalar)

    def __floordiv__(self, value):
        return Vec2D(self.x // value, self.y // value)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __iter__(self):
        for i in [self.x, self.y]:
            yield i