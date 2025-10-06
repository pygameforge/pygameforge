import math

class Vector2():
    """
    Represents a 2D vector with x and y coordinates.

    This class supports:
        - Vector arithmetic: addition, subtraction, multiplication, division
        - In-place operations: +=, -=, *=, /=
        - Comparison with other Vector2 objects, lists, or tuples
        - Geometric properties: magnitude, normalization, distance, angle
        - Vector operations: dot product and 2D cross product

    Example usage:
        v1 = Vector2(3, 4)
        v2 = Vector2(1, 2)
        v3 = v1 + v2
        distance = v1.distance_to(v2)
        angle = v1.angle_to(v2)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        if isinstance(other, list) or isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        raise TypeError("Can't compare a non array value to a Vector2")
    
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"
    
    def __repr__(self):
        return f"<Vector2 x={self.x}, y={self.y}>"
    
    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        if isinstance(other, list) or isinstance(other, tuple):
            return Vector2(self.x + other[0], self.y + other[1])
        raise TypeError("Can't add a non array value to a Vector2")
    
    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        if isinstance(other, list) or isinstance(other, tuple):
            return Vector2(self.x - other[0], self.y - other[1])
        raise TypeError("Can't subtract a non array value to a Vector2")
    
    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        if isinstance(other, list) or isinstance(other, tuple):
            return Vector2(self.x * other[0], self.y * other[1])
        return Vector2(self.x * other, self.y * other)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        if isinstance(other, list) or isinstance(other, tuple):
            return Vector2(self.x / other[0], self.y / other[1])
        return Vector2(self.x / other, self.y / other)
    
    def __iadd__(self, other):
        if isinstance(other, Vector2):  
            self.x += other.x
            self.y += other.y
            return self
        if isinstance(other, list) or isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
            return self
        raise TypeError("Can't add a non array value to a Vector2")
    
    def __isub__(self, other):
        if isinstance(other, Vector2):  
            self.x -= other.x
            self.y -= other.y
            return self
        if isinstance(other, list) or isinstance(other, tuple):
            self.x -= other[0]
            self.y -= other[1]
            return self
        raise TypeError("Can't subtract a non array value to a Vector2")
        
    def __itruediv__(self, other):
        if isinstance(other, Vector2):  
            self.x /= other.x
            self.y /= other.y
        elif isinstance(other, list) or isinstance(other, tuple):
            self.x /= other[0]
            self.y /= other[1]
        else:
            self.x /= other
            self.y /= other
        
        return self
        
    def __imul__(self, other):
        if isinstance(other, Vector2):  
            self.x *= other.x
            self.y *= other.y
        elif isinstance(other, list) or isinstance(other, tuple):
            self.x *= other[0]
            self.y *= other[1]
        else:
            self.x *= other
            self.y *= other
        
        return self
        
    def __ne__(self, other):
        return not self.__eq__(other=other)
    
    def __pow__(self, value):
        return Vector2(self.x ** value, self.y ** value)
    
    def __rmul__(self, value):
        return Vector2(self.x * value, self.y * value)
        
    def magnitude(self):
        """
        Returns the magnitude (length) of the vector.
        
        This is the Euclidean distance from the origin (0,0) to the vector (x,y).
        """
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self):     
        """
        Returns a new Vector2 with the same direction but magnitude 1.
        
        If the vector has zero length, returns Vector2(0, 0).
        """
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vector2(0, 0)
        return Vector2(self.x / magnitude, self.y / magnitude)

    def normalize(self):
        """
        Normalizes the vector in place.
        
        After this call, the vector will have magnitude 1 and the same direction.
        If the vector has zero length, it remains unchanged (or becomes Vector2(0,0)).
        """
        magnitude = self.magnitude()
        if magnitude == 0:
            self.x = 0
            self.y = 0
        self.x /= magnitude
        self.y /= magnitude

    def distance_to(self, other):
        """
        Returns the Euclidean distance between this vector and another.
        
        'other' can be a Vector2, a list, or a tuple of length 2.
        """
        if isinstance(other, Vector2):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if isinstance(other, list) or isinstance(other, tuple):
            return math.sqrt((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2)
        raise TypeError("Can't get a distance between a 1D value and a Vector2")

    def angle_to(self, other):
        """
        Returns the angle in radians between this vector and another.
        
        'other' can be a Vector2, a list, or a tuple of length 2.
        The result is in the range [0, pi].
        """
        if isinstance(other, Vector2):
            ox, oy = other.x, other.y
        elif isinstance(other, (list, tuple)):
            ox, oy = other[0], other[1]
        else:
            raise TypeError("Can't get an angle between a 1D value and a Vector2")
        
        dot = self.x * ox + self.y * oy
        mag_self = self.magnitude()
        mag_other = math.sqrt(ox**2 + oy**2)
        
        if mag_self == 0 or mag_other == 0:
            return 0.0
        
        cos_theta = max(min(dot / (mag_self * mag_other), 1.0), -1.0)
        return math.acos(cos_theta)

    def dot(self, other):
        """
        Returns the dot (scalar) product of this vector with another Vector2.
        
        Useful for projections and calculating angles between vectors.
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """
        Returns the 2D cross product (as a scalar) of this vector with another Vector2.
        
        The result represents the magnitude of the perpendicular vector in 2D.
        """
        return self.x * other.y - self.y * other.x