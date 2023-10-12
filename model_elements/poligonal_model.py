from .staff.poligon import Poligon
from .staff.texture import Texture


class PoligonalModel:
    def __init__(self, textures=None):
        if textures is None:
            textures = []

        self.poligons: list[Poligon, ] = [Poligon(), ]

        self.textures: list[Texture, ] = textures
