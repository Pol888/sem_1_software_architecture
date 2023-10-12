from in_memory_model.i_model_changed_observer import IModelChangedObserver
from in_memory_model.i_model_changer import IModelChanger
from model_elements.camera import Camera
from model_elements.flash import Flash
from model_elements.poligonal_model import PoligonalModel
from model_elements.scene import Scene


class ModelStore(IModelChanger):
    def __init__(self, changed_observer=None):
        if changed_observer is None:
            self._changed_observers = []
        else:
            self._changed_observers: list[IModelChangedObserver,] = changed_observer

        self.models: list[PoligonalModel, ] = [PoligonalModel(), ]
        self.scans: list[Scene, ] = [Scene([PoligonalModel(), ], [Flash(), ], [Camera()]), ]
        self.flashes: list[Flash, ] = [Flash(), ]
        self.cameras: list[Camera, ] = [Camera(), ]


    def get_scena(self, n: int) -> Scene:
        pass

    def notify_change(self, i_model_changer: IModelChanger):
        pass