## Lab 3-11-16

import pygame
from pygame.locals import *
from random import randint

class Character(object):

    def __init__(self, imagefile,charname,surf,pos,scalesize):
        self.SURF = surf
        self.POS = pos
        self.IMAGESURF = pygame.image.load(imagefile)
        self.IMAGESURF = pygame.transform.scale(self.IMAGESURF,(scalesize,scalesize))

        self.HP = (0, 300) # should range from (0 - 300) ## randint: return a random integer(start,stop)
        self.DMG = (0, 100) # should range from (0 - 100)

        self.GameFont = pygame.font.SysFont("Sylfaen", 50)
        # this text has a black background. Can you make it transparent ?. DONE
        self.NAME = self.GameFont.render(charname, True,(255,255,255),None) 
        self.Randomize()
        self.__drawText()
        self.__displayText()
    
 
        

# complete this function
# this function should randomize HP, DMG and should display on the screen
# this function should be called on a button press
    def Randomize(self):
        #pass
        self.HP = randint(0, 300)
        self.DMG = randint(0, 300)
        

## DON'T UNCOMMENT UNLESS YOU WANT IT TO RANDOMLY GENERATE NON-STOP
##        self.HPText = self.GameFont.render('HP : ' +str(self.HPrand), True,(255,255,255),None)
##        self.DMGText = self.GameFont.render('DMG: ' +str(self.DMGrand), True,(255,255,255),None)

    def __displayText(self):
        self.SURF.blit(self.HPText,(self.POS[0]+200,self.POS[1]+50))
        self.SURF.blit(self.DMGText,(self.POS[0]+200,self.POS[1]+150))

        self.SURF.blit(self.NAME,(self.POS[0]+20,self.POS[1]-100))
    

# fix the error in this function, DONE
    def __drawText(self):
        # this text has a black background. Can you make it transparent ?.
        self.HPText = self.GameFont.render('HP : ' +str(self.HP), True,(255,255,255),None)
        self.DMGText = self.GameFont.render('DMG: ' +str(self.DMG), True,(255,255,255),None)
    

# fix the errors in this function, DONE
    def display(self):
        self.Randomize()
        self.__displayText()
        self.SURF.blit(self.IMAGESURF,self.POS)
        


