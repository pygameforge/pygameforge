from vector2 import Vector2

class Line:
    """
    Represents an infinite 2D line defined by a starting position and a direction vector.

    Attributes:
        direction (Vector2): The directional vector of the line (not necessarily normalized).
        start_pos (Vector2): A point on the line (origin).
    """

    def __init__(self, direction: Vector2, start_pos: Vector2) -> None:
        self.direction = direction
        self.start_pos = start_pos

    # --- Collision & Intersection ---

    def detect_collision(self, point: Vector2) -> bool:
        """
        Returns True if the given point lies on the line.
        """
        pass

    def intersect_line(self, other: "Line") -> Vector2 | None:
        """
        Computes the intersection point between this line and another line.
        Returns None if they are parallel or do not intersect.
        """
        pass

    def intersect_segment(self, segment_start: Vector2, segment_end: Vector2) -> Vector2 | None:
        """
        Checks intersection between this infinite line and a finite segment.
        Returns the intersection point or None.
        """
        pass

    def intersect_rect(self, rect) -> list[Vector2]:
        """
        Returns a list of intersection points between the line and a rectangle (pygame Rect-like).
        """
        pass

    # --- Geometric Queries ---

    def point_at(self, t: float) -> Vector2:
        """
        Returns a point along the line at parameter t.
        For example, t=0 -> start_pos, t=1 -> start_pos + direction.
        """
        pass

    def length_to(self, point: Vector2) -> float:
        """
        Returns the shortest distance along the line (signed projection length) to a given point.
        """
        pass

    def closest_point(self, point: Vector2) -> Vector2:
        """
        Returns the closest point on the infinite line to the given point.
        """
        pass

    def distance_to_point(self, point: Vector2) -> float:
        """
        Returns the perpendicular (absolute) distance from the line to the given point.
        """
        pass

    def angle_with(self, other: "Line") -> float:
        """
        Returns the angle in radians between this line and another line.
        """
        pass

    def is_parallel_to(self, other: "Line") -> bool:
        """
        Returns True if both lines are parallel.
        """
        pass

    def projection_of_point(self, point: Vector2) -> float:
        """
        Returns the scalar projection value of the point onto the line direction.
        (Useful for parameterizing positions along the line.)
        """
        pass

    # --- Direction Manipulation ---

    def normalize_direction(self) -> None:
        """
        Normalizes the direction vector in-place.
        """
        pass

    def reversed(self) -> "Line":
        """
        Returns a new line with the direction reversed.
        """
        pass

    # --- Drawing Helpers (Useful for pygameforge) ---

    def to_segment_length(self, length: float) -> tuple[Vector2, Vector2]:
        """
        Returns a finite segment representation of the line starting from start_pos with given length.
        """
        pass

    def to_segment_between(self, t1: float, t2: float) -> tuple[Vector2, Vector2]:
        """
        Returns a finite segment between two parameter values t1 and t2.
        """
        pass

    def draw(self, surface, color, length: float = 1000, width: int = 1) -> None:
        """
        Draws a visual representation of the infinite line as a long segment.
        Length parameter controls how long the line will appear.
        """
        pass

    def draw_segment(self, surface, color, t1: float, t2: float, width: int = 1) -> None:
        """
        Draws a segment of the line between parameter values t1 and t2.
        """
        pass

