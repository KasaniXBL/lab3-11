## Button Class

import pygame
from pygame.locals import *

pygame.init()

class Button(object):

    def __init__(self,height, width, color, textColor, text, surf, position):

        self.SURF = surf
        self.POS = position         ## position of button, set equal to whatever position we pass in (BSPOS,BYPOS)
        self.ButtonColor = color    ## ButtonColor = BCOLOR(0,30,50)
        self.HighLightColor = (color[0] + ((255 - color[0])//3),
                               color[1] + ((255 - color[1])//3),
                               color[2] + ((255 - color[2])//3))

        self.HEIGHT = height
        self.WIDTH = width
        self.Radius = self.HEIGHT//2

        self.TxtColor = textColor
        tHEIGHT = int(self.HEIGHT * .20)
        BUTTONfont = pygame.font.SysFont('broadway', tHEIGHT)
        
        # Set Up Text Surface
        self.TextSurf = BUTTONfont.render(text, True, textColor, None)

        w, h = self.TextSurf.get_size()               ## Gets the dimensions of the surface. Returns width and height.

        self.Xtext_position = (self.WIDTH - w)//2       ## Centers text on the X position
        self.Ytext_position = int((self.HEIGHT - h)//2) ## Centers text on the Y position
        
        # Set Up Button Surface
        self.ButtonSurf = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.ButtonSurf.fill((0,0,0,0))

        self.active = True      ## ON
        self.highlight = False  ## OFF
        
    def rounded_edge(self, color):
        pygame.draw.circle(self.ButtonSurf, color, (self.Radius, self.Radius), self.Radius)
        pygame.draw.circle(self.ButtonSurf, color, (self.WIDTH - self.Radius, self.Radius), self.Radius)
        pygame.draw.rect(self.ButtonSurf, color, Rect((self.Radius, 0), (self.WIDTH - 2 * self.Radius, self.HEIGHT)))

    def buttonText(self):
        # Draw/blit Text onto Button surface
        self.ButtonSurf.blit(self.TextSurf, (self.Xtext_position, self.Ytext_position))
    
    def clicked(self, mouse):
        yesORno = False ## OFF
        P1 = self.POS
        P2 = (P1[0] + self.WIDTH, P1[1] + self.HEIGHT)  ## (XPOSITION + WIDTH (RIGHT or LEFT SIDE OF BOX), YPOSITION + HEIGHT(TOP OR BOTTOM OF BOX))
        yesORno = (self.active and P1[0] <= mouse[0] <= P2[0] and P1[1] <= mouse[1] <= P2[1])   ## (self.active(TURNS yesORno ON) and XPOSITION <= to mouse X location <= P2[0] and YPOSITION <= to mouse Y location <= P2[1]

        return yesORno  ## ON

    def display(self):

        if self.active:                                ## if True do this:
            if self.highlight:                       ## if False do this:
                self.rounded_edge(self.HighLightColor) ## Corner Circles become white
                self.buttonText()                      ## Draw Text onto Button Surface
                self.SURF.blit(self.ButtonSurf, self.POS) ## Draw Button Surface on SURF at this XY position
            else:                                      ## if not False do this
                self.rounded_edge(self.ButtonColor)    ## Corner Circles become this color (0,30,50)
                self.buttonText()                      ## Draw Text onto Button Surface
                self.SURF.blit(self.ButtonSurf, self.POS) ## Draw Button Surface on SURF at this XY position
