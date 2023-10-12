from typing import Optional

from model_elements.staff.angle3d import Angle3d
from model_elements.staff.color import Color
from model_elements.staff.point_3d import Point3D


class Flash():
    def __init__(self, location: Optional[Point3D] = None, angle: Optional[Angle3d] = None,
                 color: Optional[Color] = None, power: float = 0):
        self.location: Point3D = location
        self.angle: Angle3d = angle
        self.color: Color = color
        self.power: float = power

    @staticmethod
    def rotate(angle3d: Angle3d) -> None:
        pass

    @staticmethod
    def movie(point3d: Point3D) -> None:
        pass
