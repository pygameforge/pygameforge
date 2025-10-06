from .vector2 import Vector2
import math
import pygame

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
        difference = point - self.start_pos
        return abs(self.direction.cross(difference)) < 1e-8

    def intersect_line(self, other: "Line") -> Vector2 | None:
        """
        Computes the intersection point between this line and another line.
        Returns None if they are parallel or do not intersect.
        """
        d = self.direction.cross(other.direction)
        if abs(d) < 1e-8:
            return None  # parallel
        t = (other.start_pos - self.start_pos).cross(other.direction) / d
        return self.point_at(t)

    def intersect_segment(self, segment_start: Vector2, segment_end: Vector2) -> Vector2 | None:
        """
        Checks intersection between this infinite line and a finite segment.
        Returns the intersection point or None.
        """
        seg_dir = segment_end - segment_start
        denom = self.direction.cross(seg_dir)
        if abs(denom) < 1e-8:
            return None  # parallel
        t = (segment_start - self.start_pos).cross(seg_dir) / denom
        u = (segment_start - self.start_pos).cross(self.direction) / denom
        if 0 <= u <= 1:
            return self.point_at(t)
        return None

    def intersect_rect(self, rect) -> list[Vector2]:
        """
        Returns a list of intersection points between the line and a rectangle (pygame Rect-like).
        """
        points = []
        rect_points = [
            Vector2(rect.left, rect.top),
            Vector2(rect.right, rect.top),
            Vector2(rect.right, rect.bottom),
            Vector2(rect.left, rect.bottom),
        ]
        for i in range(4):
            p = self.intersect_segment(rect_points[i], rect_points[(i + 1) % 4])
            if p and p not in points:
                points.append(p)
        return points

    # --- Geometric Queries ---

    def point_at(self, t: float) -> Vector2:
        """
        Returns a point along the line at parameter t.
        For example, t=0 -> start_pos, t=1 -> start_pos + direction.
        """
        return self.start_pos + self.direction * t

    def length_to(self, point: Vector2) -> float:
        """
        Returns the shortest distance along the line (signed projection length) to a given point.
        """
        return (point - self.start_pos).dot(self.direction) / self.direction.length_squared()

    def closest_point(self, point: Vector2) -> Vector2:
        """
        Returns the closest point on the infinite line to the given point.
        """
        t = self.length_to(point)
        return self.point_at(t)

    def distance_to_point(self, point: Vector2) -> float:
        """
        Returns the perpendicular (absolute) distance from the line to the given point.
        """
        return abs((point - self.start_pos).cross(self.direction)) / self.direction.length()

    def angle_with(self, other: "Line") -> float:
        """
        Returns the angle in radians between this line and another line.
        """
        dot = self.direction.dot(other.direction)
        det = self.direction.cross(other.direction)
        return math.atan2(det, dot)

    def is_parallel_to(self, other: "Line") -> bool:
        """
        Returns True if both lines are parallel.
        """
        return abs(self.direction.cross(other.direction)) < 1e-8

    def projection_of_point(self, point: Vector2) -> float:
        """
        Returns the scalar projection value of the point onto the line direction.
        (Useful for parameterizing positions along the line.)
        """
        return (point - self.start_pos).dot(self.direction) / self.direction.length_squared()

    # --- Direction Manipulation ---

    def normalize_direction(self) -> None:
        """
        Normalizes the direction vector in-place.
        """
        self.direction = self.direction.normalize()

    def reversed(self) -> "Line":
        """
        Returns a new line with the direction reversed.
        """
        return Line(-self.direction, self.start_pos)

    # --- Drawing Helpers ---

    def to_segment_length(self, length: float) -> tuple[Vector2, Vector2]:
        """
        Returns a finite segment representation of the line starting from start_pos with given length.
        """
        return (self.start_pos, self.start_pos + self.direction.get_normalized() * length)

    def to_segment_between(self, t1: float, t2: float) -> tuple[Vector2, Vector2]:
        """
        Returns a finite segment between two parameter values t1 and t2.
        """
        return (self.point_at(t1), self.point_at(t2))

    def draw(self, surface, color, length: float = 1000, width: int = 1) -> None:
        """
        Draws a visual representation of the infinite line as a long segment.
        Length parameter controls how long the line will appear.
        """
        start, end = self.to_segment_length(length)
        pygame.draw.line(surface, color, start.tuple(), end.tuple(), width)

    def draw_segment(self, surface, color, t1: float, t2: float, width: int = 1) -> None:
        """
        Draws a segment of the line between parameter values t1 and t2.
        """
        start, end = self.to_segment_between(t1, t2)
        pygame.draw.line(surface, color, start.tuple(), end.tuple(), width)
