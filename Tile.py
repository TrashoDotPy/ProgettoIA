import pygame
from Figura import Figura


class Tile(Figura):
    def __init__(self, tipo, x, y, rot):
        self.tipo = tipo
        self.row = x 
        self.col = y
        self.rot = rot
        
        super().assegnaMatrice(tipo)

    
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo
    
    def setRot(self, rot):
        self.rot = rot
        super().image = pygame.transform.rotate(super().image, self.rot * 90)
        if rot > 0:
            for i in range(self.rot):
                super().ruotaMatrice()

    def getRot(self):
        return self.rot
    
    def getRow(self):
        return self.row
    
    def setRow(self, row):
        self.row = row

    def getCol(self):
        return self.col
    
    def setCol(self, col):
        self.col = col
        