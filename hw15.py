import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add another Vector")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Can only subtract another Vector")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Can only multiply by a scalar")

    def dot_product(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Can only calculate dot product with another Vector")

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Приклад використання
v1 = Vector(2, 3)
v2 = Vector(1, -1)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1.dot_product(v2))
print(abs(v1))
print(v1 == v2)
