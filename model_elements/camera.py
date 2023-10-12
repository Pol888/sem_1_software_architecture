
from .staff.point_3d import Point3D
from .staff.angle3d import Angle3d
from typing import Optional


class Camera():
    def __init__(self, location: Optional[Point3D] = None, angle: Optional[Angle3d] = None):
        self.location: Point3D = location
        self.angle: Angle3d = angle

    @staticmethod
    def rotate(angle3d: Angle3d) -> None:
        pass

    @staticmethod
    def movie(point3d: Point3D) -> None:
        pass
