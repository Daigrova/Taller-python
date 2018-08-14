import pygame
from pygame.locals import *
from GameTools import load_image,iniciar




class Finger(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('CursorRegular.jpg',-1)
        self.clicking = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.clicking:
            self.rect.move_ip(5, 10)

    def click(self,target):
        self.image = load_image('CursorClick.jpg',-1)[0]
        self.clicking = 1
        hitbox = self.rect.inflate(-5,-5)
        return hitbox.colliderect(target.rect)

    def unclick(self):
        self.image = load_image('CursorRegular.jpg',-1)[0]
        self.clicking = 0



class Texto:
    def __init__(self, background):
        self.ownFont = pygame.font.SysFont('Comic Sans MS',30)
        self.textos = ['¿Que quieres?', '¿Que se supone que haces?', 'Ya sueltame', 'Dije que me sueltes']
        self.bg = background
        self.text = self.ownFont.render(self.textos[0], 1, (10, 10,10) )
        posicion = self.text.get_rect(centerx = self.bg.get_width()/2)
        self.bg.blit(self.text,posicion)

    def updateText(self,numero_texto):

        if (numero_texto > 0 and numero_texto < 1):
            numero_texto = 1
        elif (numero_texto >= 1 and numero_texto < 3):
            numero_texto = 2
        elif (numero_texto >= 3):
            numero_texto = 3
        self.bg.fill((250,250,250))
        self.text = self.ownFont.render(self.textos[numero_texto], 1 , (10,10,10))
        posicion = self.text.get_rect(centerx = self.bg.get_width()/2)
        self.bg.blit(self.text,posicion)

    def reset(self):
        self.bg.fill((250,250,250))
        self.text = self.ownFont.render(self.textos[0], 1 , (10,10,10))
        posicion = self.text.get_rect(centerx = self.bg.get_width()/2)
        self.bg.blit(self.text,posicion)        


class Face(pygame.sprite.Sprite):
    def __init__(self,background):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('NormalFace.png',-1) #Inicia el nuevo sprite
        self.clicked = 0
        self.rect.midtop = (320, 240)   #Guarda la posicion inicial
        self.timer = None
        self.clockTime = 0
        self.texto = Texto(background)

    def update(self):
        if self.clicked:
            
            x,y = pygame.mouse.get_pos()
            self.rect.midtop = (x,y-25)
            self.timer.tick()
            self.clockTime += self.timer.get_rawtime()/1000
            if self.clockTime >= 0 and self.clockTime <1:
                self.image = load_image('AngryFace_1.png',-1)[0]
                self.texto.updateText(self.clockTime)
            if self.clockTime >= 1 and self.clockTime <3:
                self.image = load_image('AngryFace_3.png',-1)[0]
                self.texto.updateText(self.clockTime)
            if self.clockTime >= 3 and self.clockTime <5:
                self.image = load_image('AngryFace_5.png',-1)[0]
                self.texto.updateText(self.clockTime)

    def isClicked(self):
        if not self.clicked:
            self.clicked = 1
            self.timer = pygame.time.Clock()


    def unclicked(self):
        self.clicked = 0
        self.clockTime =0 
        self.image = load_image('NormalFace.png',-1)[0]
        self.texto.reset()

    def timeClicked(self):
        return self.clockTime

class Screen:
    def __init__(self):
        iniciar()
        self.screen_x = 920
        self.screen_y = 670
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.sprites = None

    def add_objects_screen(self,*objetos):
        self.sprites = pygame.sprite.RenderPlain(*objetos)

    def screen_update(self,background):
        self.screen.blit(background, (0, 0))
        self.sprites.draw(self.screen)
        self.sprites.update()
        pygame.display.flip()

    def get_size(self):
        return self.screen_x, self.screen_y

class Background:
    def __init__(self, size_x, size_y):
        self.background = pygame.Surface((size_x, size_y))
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

    def get_bg(self):
        return self.background