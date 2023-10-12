from poligonal_model import PoligonalModel
from flash import Flash
from camera import Camera
import typing


class Scene:
    def __init__(self, models: list[PoligonalModel, ], flashes: list[Flash, ], cameras: list[Camera, ],
                 id: typing.Optional[int] = None):

        self.id = id
        # ------------------------------------------------------
        if len(models) > 1:
            self.models: list[PoligonalModel, ] = models
        else:
            raise Exception('Количество элементов "models" = 0')
        # -------------------------------------------------------
        self.flashes: list[Flash, ] = flashes
        # --------------------------------------------------------
        if len(cameras) > 1:
            self.cameras: list[Camera, ] = cameras
        else:
            raise Exception('Количество элементов "cameras" = 0')

    def method_1(self, type_1: type) -> type:
        pass

    def method_2(self, type_1: type, type_2: type) -> type:
        pass
