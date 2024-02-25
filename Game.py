import pygame
import random
from Figura import Figura
from Button import Button
from ControllerDLV import ControllerDLV


class Game:
    def __init__(self, display, stateManager):
        self.__display = display
        self.__stateManager = stateManager

        self.__size = 125
        self.__start = 137.5
        self.__map = []
        self.__tiles = []
        self.__rotations = []
        self.check = False
        self.delay = False
        self.menuDelay = True
        self.end = False
        self.facts = ""
        self.rot = 0

        self.I = 0
        self.J = 0

        #Buttons
        self.goHome = pygame.Rect(0,0,200,50)
        self.quit = pygame.Rect(0,0,200,50)

        self.hoverGoHome = False
        self.hoverQuit = False

        self.controller = ControllerDLV()

    def setLevel(self,level:int):
        strlvl = ""
        if level == 1:
            strlvl = "-medio"
            self.__size = 100
            self.__start = 100
        elif level == 2:
            strlvl = "-difficile"
            self.__size = 75
            self.__start = 37.5

        # Get random map
        indexMap = random.randint(0,9)
        with open(f"maps{strlvl}/map{indexMap}.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            row = line.strip().split()
            row = [int(x) for x in row]
            self.__map.append(row)

        print(str(indexMap) + '\n')
        print(self.__map)
        print('\n')

        for i in range(len(self.__map)):
            tilestmp = []
            for j in range(len(self.__map[0])):
                tilestmp.append(Figura(self.__map[i][j], i, j, random.randint(0,3), self.__size))
            self.__tiles.append(tilestmp)
        # print(f"dim({len(self.__tiles)}).\n")
        self.facts = f"dim({len(self.__tiles)}).\n"

    def get_rotation(self,solution):
        cleaned_string = solution[1:-1]
        substrings = cleaned_string.split(", ")
        substrings = [substring.replace(" ", "").strip("'") for substring in substrings]

        rotations = []
        for substring in substrings:
            # print(substring[7])
            rotations.append(substring[7])
        return rotations    
    
    def draw_txt(self, str:str, x:int, y:int):
        self.font = pygame.font.Font(None, 40)
        src = self.font.render(str, True, (249, 246, 242))
        self.__display.blit(src, [x,y])
    
    def draw_game_over(self):
        pygame.draw.rect(self.__display, 'black', (225, 350, 450, 200), 0, 10)
        pygame.draw.rect(self.__display, (235,175,235), (225, 350, 450, 200), 4, 10)
        self.draw_txt('YOU WIN', 390, 400)
        Button.draw_light(self.__display, self.goHome, "HOME", self.hoverGoHome, 340, 480)
        Button.draw_red(self.__display, self.quit, "QUIT", self.hoverQuit, 560, 480)

    def reset(self):
        self.__size = 125
        self.__start = 137.5
        self.__map = []
        self.__tiles = []
        self.__rotations = []
        self.check = False
        self.delay = False
        self.end = False
        self.facts = ""
        self.rot = 0
        self.hoverGoHome = False
        self.hoverQuit = False
        self.menuDelay = True
        self.I = 0
        self.J = 0


    def run(self, events):
        if self.end:
            if self.menuDelay:
                pygame.time.delay(2000)
                self.menuDelay = False
            for event in events:
                if event.type == pygame.MOUSEMOTION:
                    self.hoverGoHome = self.goHome.collidepoint(event.pos)
                    self.hoverQuit = self.quit.collidepoint(event.pos) 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.hoverGoHome:
                        self.reset()
                        self.__stateManager.setState("Home")  
                    elif self.hoverQuit:
                        pygame.quit()
            self.draw_game_over()
            return
        
        self.facts += f"figure({self.__tiles[self.I][self.J].getTipo()},{self.__tiles[self.I][self.J].getRot()},{self.I},{self.J}).\n"
        if self.__rotations is not None and len(self.__rotations) > 0:
            self.__tiles[self.I][self.J].setRot(int(self.__rotations[self.rot]))
            self.__display.blit(self.__tiles[self.I][self.J].image, [self.J*self.__size+self.__start,self.I*self.__size+self.__start])
            self.rot += 1
        else:
            self.__display.blit(self.__tiles[self.I][self.J].image, [self.J*self.__size+self.__start,self.I*self.__size+self.__start])

        self.J += 1
        if self.J == len(self.__tiles[0]):
            self.J = 0
            self.I += 1
            if self.I == len(self.__tiles):
                self.check = True
                self.rot = 0
                self.I = 0

                if self.delay:
                    self.end = True

        if self.check:
            self.controller.set_facts(self.facts)
            self.controller.set_DLV()

            self.__rotations = self.get_rotation(self.controller.getSolution())
            self.facts = f"dim({len(self.__tiles)}).\n"
            self.check = False
            self.delay = True

        if self.delay:
            pygame.time.delay(200)