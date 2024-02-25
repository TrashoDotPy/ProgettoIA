import pygame
import time

origine = [[0,1,0],[1,5,1],[0,0,0]]
lineaT = [[0,1,0],[1,0,1],[0,0,0]]
lineaL = [[0,1,0],[1,0,0],[0,0,0]]
lineaD = [[0,1,0],[0,0,0],[0,1,0]]
luce = [[0,1,0],[0,2,0],[0,0,0]]

class Figura:  
    def __init__(self, tipo, x, y, rot, size):
        self.tipo = tipo
        self.row = x
        self.col = y
        self.rot = rot
        self.size = size
        self.assegnaImmagine()
        self.assegnaMatrice(self.tipo)

    def assegnaImmagine(self):
        tmpimg = pygame.image.load(f"batteriaFili/{self.tipo}.png")
        self.image = pygame.transform.scale(tmpimg,(self.size,self.size))
        self.image = pygame.transform.rotate(self.image, self.rot * -90)

    def assegnaMatrice(self, tipo):
        match tipo:
            case 0:
                self.richieste = origine.copy()
            case 1:
                self.richieste = lineaD.copy()
            case 2:
                self.richieste = lineaL.copy()
            case 3:
                self.richieste = lineaT.copy()
            case 4:
                self.richieste = luce.copy()

    def ruotaMatrice(self):
        n = len(self.richieste)

    # Transposizione della matrice
        for i in range(n):
            for j in range(i,n):
                temp = self.richieste [i][j]
                self.richieste[i][j] = self.richieste[j][i]
                self.richieste[j][i] = temp

    # Inversione delle righe
        for i in range (n):
            for j in range (int(n/2)):
                temp = self.richieste [i][j]
                self.richieste[i][j] = self.richieste[i][n-j-1]
                self.richieste[i][n-j-1] = temp
    
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo
        self.assegnaImmagine()
        self.assegnaMatrice()

    def getRow(self):
        return self.row
    
    def setRow(self, row):
        self.row = row

    def getCol(self):
        return self.col
    
    def setCol(self, col):
        self.col = col

    def getRot(self):
        return self.rot
    
    def setRot(self, rot):
        rottmp = rot - self.rot
        self.image = pygame.transform.rotate(self.image, (90 * rottmp)*-1)
        self.rot = rot

    def isAttachedU(self):
        return self.richieste[0][1] == 1

    def isAttachedD(self):
        return self.richieste[2][1] == 1
    
    def isAttachedL(self):
        return self.richieste[1][0] == 1

    def isAttachedR(self):
        return self.richieste[1][2] == 1
    
    def toString(self):
        return f"figure({self.tipo},{self.rot},{self.row},{self.col})"