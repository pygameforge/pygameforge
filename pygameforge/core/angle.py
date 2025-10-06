import math
from .vector2 import Vector2

class Angle:
    """
    Utility class for angle-related operations and vector rotations.
    Provides static methods for converting, rotating, and manipulating angles.
    """

    # --- Vector Rotation ---
    @staticmethod
    def rotate_vector(vec: Vector2, angle_rad: float) -> Vector2:
        """
        Rotates a Vector2 by a given angle in radians.
        
        Args:
            vec (Vector2): The vector to rotate.
            angle_rad (float): The rotation angle in radians.
        
        Returns:
            Vector2: A new Vector2 rotated by the given angle.
        """
        pass

    # --- Degrees <-> Radians Conversion ---
    @staticmethod
    def deg_to_rad(deg: float) -> float:
        """
        Converts degrees to radians.
        
        Args:
            deg (float): Angle in degrees.
        
        Returns:
            float: Angle in radians.
        """
        pass

    @staticmethod
    def rad_to_deg(rad: float) -> float:
        """
        Converts radians to degrees.
        
        Args:
            rad (float): Angle in radians.
        
        Returns:
            float: Angle in degrees.
        """
        pass

    # --- Angle Difference ---
    @staticmethod
    def angle_diff(a: float, b: float) -> float:
        """
        Returns the smallest difference between two angles in radians.
        
        Args:
            a (float): First angle in radians.
            b (float): Second angle in radians.
        
        Returns:
            float: Minimal signed difference (b - a) in radians.
        """
        pass

    # --- Angle From Vector ---
    @staticmethod
    def angle_from_vector(vec: Vector2) -> float:
        """
        Returns the angle of a vector relative to the X-axis in radians.
        
        Args:
            vec (Vector2): The vector to measure.
        
        Returns:
            float: Angle in radians.
        """
        pass

    # --- Create Vector From Angle ---
    @staticmethod
    def vector_from_angle(angle_rad: float, length: float = 1.0) -> Vector2:
        """
        Creates a Vector2 from an angle and optional length.
        
        Args:
            angle_rad (float): Angle in radians.
            length (float, optional): Vector magnitude. Defaults to 1.0.
        
        Returns:
            Vector2: Vector pointing in the given angle.
        """
        pass

    # --- Angle Interpolation ---
    @staticmethod
    def lerp_angle(a: float, b: float, t: float) -> float:
        """
        Linearly interpolates between two angles, respecting the shortest rotation path.
        
        Args:
            a (float): Start angle in radians.
            b (float): End angle in radians.
            t (float): Interpolation factor [0,1].
        
        Returns:
            float: Interpolated angle in radians.
        """
        pass

    # --- Angle Normalization ---
    @staticmethod
    def normalize_angle(rad: float) -> float:
        """
        Normalizes an angle to the range [-pi, pi].
        
        Args:
            rad (float): Angle in radians.
        
        Returns:
            float: Normalized angle in radians.
        """
        pass

    # --- Angle Between Two Vectors ---
    @staticmethod
    def angle_between_vectors(v1: Vector2, v2: Vector2) -> float:
        """
        Computes the signed angle from vector v1 to v2 in radians.
        
        Args:
            v1 (Vector2): First vector.
            v2 (Vector2): Second vector.
        
        Returns:
            float: Signed angle in radians from v1 to v2.
        """
        pass

    # --- Incremental Rotation ---
    @staticmethod
    def rotate_towards(current: float, target: float, max_delta: float) -> float:
        """
        Rotates `current` angle towards `target` by up to `max_delta` radians.
        
        Args:
            current (float): Current angle in radians.
            target (float): Target angle in radians.
            max_delta (float): Maximum allowed rotation in radians.
        
        Returns:
            float: New angle in radians after rotation.
        """
        pass
