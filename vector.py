class Vec2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return (((self.x < other.x) and (self.y < other.y)) or
                ((self.x == other.x) and (self.y < other.y)) or
                ((self.x < other.x) and (self.y == other.y)))

    def __iter__(self):
        for i in [self.x, self.y]:
            yield i

    def __hash__(self):
        return hash((self.x, self.y))
